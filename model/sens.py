import merchme_model as M
import copy

def run_case(name, split='rec', onb=1.0, act=1.0, opm=1.0, founders=1.0, base_up=0.0):
    # temporarily patch
    s0 = copy.deepcopy(M.SCEN[name]); b0 = M.BASE_EXVAT
    M.SCEN[name]['opm'] = s0['opm']*opm
    M.BASE_EXVAT = (b0[0]+base_up, b0[1]+base_up)
    rows, low, lm, be = M.run(name, split=split, onb_mult=onb, act_mult=act, founders=True)
    # founder scaling: recompute ebitda adjusting founder cost
    cash=0; low2=0; lm2=0; eb=[]
    for r in rows:
        m=r['m']; fcost = 0 if m<=6 else (40000 if m<=18 else 70000)
        e = r['ebitda'] + fcost*(1-founders)
        eb.append(e); cash += e - r['capex']
        if cash<low2: low2, lm2 = cash, m
    be2=None
    for i in range(36):
        if all(x>=0 for x in eb[i:]): be2=i+1; break
    M.SCEN[name]=s0; M.BASE_EXVAT=b0
    y3 = dict(orders=round(sum(r['orders'] for r in rows[24:])), gmv=round(sum(r['gmv'] for r in rows[24:])),
              gp=round(sum(r['gp'] for r in rows[24:])), creator=round(sum(r['creator'] for r in rows[24:])),
              ebitda=round(sum(eb[24:])))
    return dict(be=be2, peak=round(low2), peak_m=lm2, m36_eb=round(eb[35]), m36_orders=round(rows[35]['orders']), y3=y3, cash36=round(cash))

cases = [
 ('Base, recommended split', dict()),
 ('Base, 75/25 same volumes', dict(split='75/25')),
 ('Base, 75/25 with onboarding -40% & activity -25%', dict(split='75/25', onb=0.6, act=0.75)),
 ('Base, founders unpaid', dict(founders=0.0)),
 ('Base, founders half pay', dict(founders=0.5)),
 ('Base, orders per active creator 5 (not 4)', dict(opm=1.25)),
 ('Base, active share 25% (not 20%)', dict(act=1.25)),
 ('Base, orders 5 + active 25%', dict(opm=1.25, act=1.25)),
 ('Base, base price +R30 ex VAT', dict(base_up=30)),
 ('Base, orders 5 + founders half pay', dict(opm=1.25, founders=0.5)),
 ('Conservative, recommended', dict()),
 ('Conservative, 75/25 same volumes', dict(split='75/25')),
 ('Upside, recommended', dict()),
 ('Upside, 75/25 same volumes', dict(split='75/25')),
 ('Upside, 75/25 onboarding -40% activity -25%', dict(split='75/25', onb=0.6, act=0.75)),
]
for label, kw in cases:
    name = label.split(',')[0]
    print(label, run_case(name, **kw))
