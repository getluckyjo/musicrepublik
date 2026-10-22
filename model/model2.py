"""MerchMe 36-month scenario model v2. Every input is an assumption unless noted as sourced."""
TEE_PRICE, HOOD_PRICE = 450.0, 699.0
def net(p): return p/1.15
def fee(p): return 0.032*p + 2.0   # PayFast card 3.2% + R2 ex VAT (sourced)
TEE = dict(net=net(TEE_PRICE), fee=fee(TEE_PRICE), pack=7.0, reserve=8.0)
HOOD = dict(net=net(HOOD_PRICE), fee=fee(HOOD_PRICE), pack=9.0, reserve=12.16)
COGS = {'A': (185.0, 420.0), 'B': (145.0, 380.0), 'C': (125.0, 315.0)}  # blank+print
BASE = (250.0, 480.0)   # recommended published base price ex VAT (tee, hoodie)
MIX_TEE, UPO = 0.65, 1.3

def pool(it, bp): return it['net'] - it['fee'] - it['pack'] - it['reserve'] - bp
def per_unit(stage, split, base_up=0.0):
    bt, bh = COGS[stage]; pt, ph = pool(TEE, bt), pool(HOOD, bh)
    if split == '75/25': return 0.75*pt, 0.25*pt, 0.75*ph, 0.25*ph
    if split == '60/40': return 0.40*pt, 0.60*pt, 0.40*ph, 0.60*ph   # creator 60%
    ct = TEE['net'] - TEE['fee'] - BASE[0] - base_up
    ch = HOOD['net'] - HOOD['fee'] - BASE[1] - base_up
    return pt-ct, ct, ph-ch, ch

SCEN = {
 'Conservative': dict(onb=[(1,3,10/3),(4,7,5),(8,12,15),(13,24,25),(25,36,35)], active=0.15, opm=3),
 'Base':         dict(onb=[(1,3,5),(4,7,8),(8,12,30),(13,24,60),(25,36,90)], active=0.20, opm=4),
 'Upside':       dict(onb=[(1,3,20/3),(4,7,12),(8,12,50),(13,24,100),(25,36,150)], active=0.25, opm=5),
}
HUB_T, HUB_FX, HUB_CAP = 500, 25000, 80000
DTF_T, DTF_FX, DTF_CAP = 1800, 30000, 200000

def founders_cost(m, plan):
    if plan == 'lean': return 0 if m <= 12 else (40000 if m <= 24 else 70000)
    return 0 if m <= 6 else (40000 if m <= 18 else 70000)   # 'full'

def run(name, split='rec', onb_mult=1.0, act_mult=1.0, opm_mult=1.0, anchor=0.0, base_up=0.0,
        plan='lean', founder_mult=1.0, mvp=650000):
    s = SCEN[name]; cum=0.0; cash=0.0; low=0.0; lowm=0
    stage='A'; hub=False; dtf=False; rows=[]
    for m in range(1,37):
        add = next((r for a,b,r in s['onb'] if a<=m<=b), 0)
        cum += add*onb_mult
        act = 0.0 if m==1 else (0.5 if m<=7 else s['active']*act_mult)
        active = cum*act
        orders = active*s['opm']*opm_mult + (anchor if m>=10 else 0)
        units = orders*UPO
        mt,ct,mh,ch = per_unit(stage, split, base_up)
        ut, uh = units*MIX_TEE, units*(1-MIX_TEE)
        netrev = ut*TEE['net'] + uh*HOOD['net']; gmv = netrev*1.15
        gp = ut*mt + uh*mh; cr = ut*ct + uh*ch
        var = 0.03*netrev + 2.20*orders + 8.70*active
        fx = founders_cost(m, plan)*founder_mult
        if plan == 'lean':
            if m >= 8: fx += 22000
        else:
            if m >= 7: fx += 22000
        if m >= 10: fx += 15000
        if orders > DTF_T: fx += 15000
        if m >= 4: fx += 12000
        if m >= 19 and orders > 800: fx += 30000
        if m <= 2: fx += 50000
        elif 4 <= m <= 7: fx += mvp/4
        elif m >= 8:
            fx += (35000 if m >= 19 else 20000) if plan=='lean' else (40000 if (m>=19 and orders>800) else 20000)
        fx += 4000 if m <= 7 else (8000 if m <= 24 else 12000)
        fx += 8000
        if m <= 2: fx += 40000
        fx += 10000 if m <= 6 else (20000 if m <= 18 else 35000)
        if hub: fx += HUB_FX if plan=='lean' else 45000
        if dtf: fx += DTF_FX
        eb = gp - var - fx
        capex = 0
        if not hub and orders >= (HUB_T if plan=='lean' else 900):
            hub=True; stage='B'; capex += (HUB_CAP if plan=='lean' else 120000)
        if not dtf and orders >= DTF_T:
            dtf=True; stage='C'; capex += DTF_CAP
        cash += eb - capex
        if cash < low: low, lowm = cash, m
        rows.append(dict(m=m,cum=cum,active=active,orders=orders,units=units,gmv=gmv,net=netrev,
                         pool=gp+cr,gp=gp,creator=cr,opex=var+fx,capex=capex,ebitda=eb,cash=cash,stage=stage))
    be=None
    for i in range(36):
        if all(r['ebitda']>=0 for r in rows[i:]): be=i+1; break
    return rows, low, lowm, be

def ysum(rows,k,y): return sum(r[k] for r in rows[(y-1)*12:y*12])
def fm(x): return f"R{x/1e6:.2f}m" if abs(x)>=1e6 else f"R{x/1e3:.0f}k"

if __name__ == '__main__':
    for st in 'ABC':
        print(st, {sp:[round(v,2) for v in per_unit(st,sp)] for sp in ('75/25','rec','60/40')}, 'pool', round(pool(TEE,COGS[st][0]),2), round(pool(HOOD,COGS[st][1]),2))
    for n in SCEN:
        rows, low, lowm, be = run(n)
        hubm = next((r['m'] for r in rows if r['stage']!='A'), None); dtfm = next((r['m'] for r in rows if r['stage']=='C'), None)
        print(f"\n== {n} (rec, lean): BE m{be} peak {fm(low)} at m{lowm}; cash m36 {fm(rows[35]['cash'])}; m36 orders {rows[35]['orders']:.0f}/mo; m36 EBITDA {fm(rows[35]['ebitda'])}; m36 GMV annualised {fm(rows[35]['gmv']*12)}; hub m{hubm} dtf m{dtfm}")
        for y in (1,2,3):
            print(f"  Y{y}: creators {rows[y*12-1]['cum']:.0f}, active {rows[y*12-1]['active']:.0f}, orders {ysum(rows,'orders',y):,.0f}, units {ysum(rows,'units',y):,.0f}, GMV {fm(ysum(rows,'gmv',y))}, net {fm(ysum(rows,'net',y))}, pool {fm(ysum(rows,'pool',y))}, creator {fm(ysum(rows,'creator',y))}, GP {fm(ysum(rows,'gp',y))}, opex {fm(ysum(rows,'opex',y))}, capex {fm(ysum(rows,'capex',y))}, EBITDA {fm(ysum(rows,'ebitda',y))}")
        for sp in ('75/25',):
            r2, l2, lm2, b2 = run(n, split=sp)
            print(f"  [{sp} same volumes] BE m{b2} peak {fm(l2)}; Y3 creator {fm(ysum(r2,'creator',3))} GP {fm(ysum(r2,'gp',3))} EBITDA {fm(ysum(r2,'ebitda',3))}; 36m creator total {fm(sum(r['creator'] for r in r2))}")
        print(f"  36m creator total (rec) {fm(sum(r['creator'] for r in rows))}; 36m GMV {fm(sum(r['gmv'] for r in rows))}; 36m GP {fm(sum(r['gp'] for r in rows))}; 36m opex {fm(sum(r['opex'] for r in rows))}")
    print('\n== Base sensitivities (rec, lean unless stated)')
    cases = [
     ('Recommended split (reference)', dict()),
     ('75/25 split, same volumes', dict(split='75/25')),
     ('75/25 split, onboarding -40% and activity -25%', dict(split='75/25', onb_mult=0.6, act_mult=0.75)),
     ('60/40 profit share (creator 60%)', dict(split='60/40')),
     ('Fully staffed plan (founders paid from M7, R45k hub at 900 orders)', dict(plan='full')),
     ('Founders unpaid for all 36 months', dict(founder_mult=0.0)),
     ('Orders per active creator 3 instead of 4', dict(opm_mult=0.75)),
     ('Orders per active creator 5 instead of 4', dict(opm_mult=1.25)),
     ('Active share 25% instead of 20%', dict(act_mult=1.25)),
     ('Orders 5 and active share 25%', dict(opm_mult=1.25, act_mult=1.25)),
     ('Three anchor artists adding 300 orders/month from M10', dict(anchor=300)),
     ('Base price +R30 ex VAT (creator earns R30 less)', dict(base_up=30)),
     ('MVP build R400k instead of R650k', dict(mvp=400000)),
    ]
    for label, kw in cases:
        name = 'Base'
        rows, low, lowm, be = run(name, **kw)
        print(f"  {label}: BE {('m'+str(be)) if be else 'not by m36'}; peak funding {fm(low)} (m{lowm}); m36 EBITDA {fm(rows[35]['ebitda'])}/mo; m36 orders {rows[35]['orders']:.0f}")
    # break-even volumes
    netu = 0.65*TEE['net'] + 0.35*HOOD['net']
    var_u = 0.03*netu + 2.2/UPO + 8.70/(4*UPO)
    fixedC = 70000+22000+15000+15000+12000+30000+35000+12000+8000+35000+HUB_FX+DTF_FX
    fixedB = fixedC-15000-DTF_FX
    for sp in ('rec','75/25','60/40'):
        for st, fxx in (('B',fixedB),('C',fixedC)):
            mt,ct,mh,ch = per_unit(st, sp); bl = 0.65*mt+0.35*mh
            u = fxx/(bl-var_u)
            print(f"  BE volume {sp} stage {st}: contrib {bl:.1f}/unit, var {var_u:.1f}, fixed {fxx}, units {u:,.0f}/mo, orders {u/UPO:,.0f}/mo ({u/UPO/30:.0f}/day), GMV ann {fm(u*netu*1.15*12)}")
    print('blended net/unit', round(netu,2), 'blended GMV/unit', round(netu*1.15,2))
