"""MerchMe 36-month scenario model. All inputs are assumptions unless noted."""
import json, sys

# ---------- Unit economics (per unit, ZAR) ----------
TEE_PRICE, HOOD_PRICE = 450.0, 699.0
def net(p): return p/1.15
def fee(p): return 0.032*p + 2.0          # PayFast card 3.2% + R2 (sourced)
TEE = dict(net=net(TEE_PRICE), fee=fee(TEE_PRICE), pack=7.0, reserve=8.0)
HOOD = dict(net=net(HOOD_PRICE), fee=fee(HOOD_PRICE), pack=9.0, reserve=12.16)
# blank+print cost by production stage (A outsourced, B hub, C bulk+own DTF)
COGS = {'A': (185.0, 420.0), 'B': (145.0, 380.0), 'C': (125.0, 315.0)}
BASE_EXVAT = (250.0, 480.0)               # recommended published base price (ex VAT)

def pool(item, bp):
    return item['net'] - item['fee'] - item['pack'] - item['reserve'] - bp

def per_unit(stage, split, base_up=0.0):
    """returns (merchme_tee, creator_tee, merchme_hood, creator_hood)"""
    bt, bh = COGS[stage]
    pt, ph = pool(TEE, bt), pool(HOOD, bh)
    if split == '75/25':
        return 0.75*pt, 0.25*pt, 0.75*ph, 0.25*ph
    # base + markup: creator gets net - fee - base; MerchMe gets remainder of pool
    ct = TEE['net'] - TEE['fee'] - BASE_EXVAT[0] - base_up
    ch = HOOD['net'] - HOOD['fee'] - BASE_EXVAT[1] - base_up
    return pt-ct, ct, ph-ch, ch

MIX_TEE = 0.65
UNITS_PER_ORDER = 1.3

SCEN = {
 'Conservative': dict(onb=[(1,3,10/3),(4,7,5),(8,12,15),(13,24,25),(25,36,35)], active=0.15, opm=3),
 'Base':         dict(onb=[(1,3,5),(4,7,8),(8,12,30),(13,24,60),(25,36,90)], active=0.20, opm=4),
 'Upside':       dict(onb=[(1,3,20/3),(4,7,12),(8,12,50),(13,24,100),(25,36,150)], active=0.25, opm=5),
}

def run(name, split='rec', onb_mult=1.0, act_mult=1.0, founders=1.0, opm_mult=1.0, anchor_orders=0.0, base_up=0.0):
    s = SCEN[name]
    cum = 0.0; cash = 0.0; low = 0.0; low_m = 0
    stage = 'A'; hub_on = False; dtf_on = False
    rows = []
    for m in range(1, 37):
        add = 0
        for a,b,r in s['onb']:
            if a <= m <= b: add = r
        cum += add*onb_mult
        if m == 1: act = 0.0
        elif m <= 7: act = 0.5
        else: act = s['active']*act_mult
        active = cum*act
        orders = active*s['opm']*opm_mult + (anchor_orders if m >= 10 else 0.0)
        units = orders*UNITS_PER_ORDER
        # stage triggers based on previous month orders handled at start
        mt, ct, mh, ch = per_unit(stage, split, base_up)
        ut, uh = units*MIX_TEE, units*(1-MIX_TEE)
        net_rev = ut*TEE['net'] + uh*HOOD['net']
        gmv = net_rev*1.15
        mm_gp = ut*mt + uh*mh                      # MerchMe gross profit after creator share
        creator = ut*ct + uh*ch
        pool_tot = mm_gp + creator
        # variable opex
        var = 0.03*net_rev + 2.20*orders + 8.70*active
        # fixed opex
        fx = 0
        fx += founders*(0 if m <= 6 else (40000 if m <= 18 else 70000))
        if m >= 7: fx += 22000                     # creator success manager
        if m >= 10: fx += 15000                    # support / ops
        if orders > 1800: fx += 15000              # second support/ops
        if m >= 4: fx += 12000                     # part-time designer / QC
        if m >= 19 and orders > 800: fx += 30000   # growth & partnerships hire
        # dev
        if m <= 2: fx += 50000                     # phase 0 build R100k
        elif 4 <= m <= 7: fx += 162500             # MVP build R650k over 4 months
        elif m >= 8: fx += (40000 if (m >= 19 and orders > 800) else 20000)
        fx += 4000 if m <= 7 else (8000 if m <= 24 else 12000)   # tech running
        fx += 8000                                 # accounting, legal, insurance, POPIA
        if m <= 2: fx += 40000                     # one-off legal/company setup R80k
        fx += 10000 if m <= 6 else (20000 if m <= 18 else 35000) # creator acquisition
        capex = 0
        if hub_on: fx += 35000
        if dtf_on: fx += 20000
        ebitda = mm_gp - var - fx
        cash += ebitda
        # triggers for next month
        if not hub_on and orders >= 900:
            hub_on = True; stage = 'B'; capex += 100000
        if not dtf_on and orders >= 1800:
            dtf_on = True; stage = 'C'; capex += 200000
        cash -= capex
        if cash < low: low, low_m = cash, m
        rows.append(dict(m=m, cum=cum, active=active, orders=orders, units=units, gmv=gmv, net=net_rev,
                         pool=pool_tot, gp=mm_gp, creator=creator, var=var, fx=fx, capex=capex,
                         ebitda=ebitda, cash=cash, stage=stage))
    # break-even: first month from which ebitda stays >= 0 through m36
    be = None
    for i in range(36):
        if all(r['ebitda'] >= 0 for r in rows[i:]):
            be = rows[i]['m']; break
    return rows, low, low_m, be

def yr(rows, k, y):
    return sum(r[k] for r in rows[(y-1)*12:y*12])

def summary(name, **kw):
    rows, low, low_m, be = run(name, **kw)
    out = dict(name=name)
    for y in (1,2,3):
        out[f'y{y}'] = dict(
            creators_end=round(rows[y*12-1]['cum']),
            active_end=round(rows[y*12-1]['active']),
            orders=round(yr(rows,'orders',y)), units=round(yr(rows,'units',y)),
            gmv=round(yr(rows,'gmv',y)), net=round(yr(rows,'net',y)),
            pool=round(yr(rows,'pool',y)), gp=round(yr(rows,'gp',y)), creator=round(yr(rows,'creator',y)),
            opex=round(yr(rows,'var',y)+yr(rows,'fx',y)), capex=round(yr(rows,'capex',y)),
            ebitda=round(yr(rows,'ebitda',y)))
    out['m36_orders'] = round(rows[35]['orders']); out['m36_ebitda'] = round(rows[35]['ebitda'])
    out['m36_gmv_annualised'] = round(rows[35]['gmv']*12)
    out['peak_burn'] = round(low); out['peak_month'] = low_m; out['breakeven'] = be
    out['cash_m36'] = round(rows[35]['cash'])
    return out, rows

if __name__ == '__main__':
    print('Per-unit (MerchMe tee, creator tee, MerchMe hoodie, creator hoodie)')
    for st in 'ABC':
        for sp in ('75/25','rec'):
            print(st, sp, [round(x,2) for x in per_unit(st, sp)])
    print('pools', {st:(round(pool(TEE,COGS[st][0]),2), round(pool(HOOD,COGS[st][1]),2)) for st in 'ABC'})
    for n in SCEN:
        o,_ = summary(n)
        print(json.dumps(o, indent=1))
