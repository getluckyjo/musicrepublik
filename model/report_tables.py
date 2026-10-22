import merchme_model as M
def fm(x): return f"{x/1e6:.2f}m" if abs(x)>=1e6 else f"{x/1e3:.0f}k"
for n in M.SCEN:
    o, rows = M.summary(n)
    print('==', n, 'rec', 'BE', o['breakeven'], 'peak', fm(o['peak_burn']), 'm', o['peak_month'], 'cash36', fm(o['cash_m36']), 'm36 orders', o['m36_orders'], 'm36 ebitda', fm(o['m36_ebitda']), 'GMV ann', fm(o['m36_gmv_annualised']))
    hub = next((r['m'] for r in rows if r['stage']=='B'), None); dtf = next((r['m'] for r in rows if r['stage']=='C'), None)
    print('   hub from month', hub, 'DTF from month', dtf)
    for y in (1,2,3):
        d=o[f'y{y}']
        print(f"   Y{y}: creators {d['creators_end']} active {d['active_end']} orders {d['orders']} units {d['units']} GMV {fm(d['gmv'])} net {fm(d['net'])} pool {fm(d['pool'])} creator {fm(d['creator'])} GP {fm(d['gp'])} opex {fm(d['opex'])} capex {fm(d['capex'])} EBITDA {fm(d['ebitda'])}")
    o2, _ = M.summary(n, split='75/25')
    print('   75/25 same vol: BE', o2['breakeven'], 'peak', fm(o2['peak_burn']), 'Y3 creator', fm(o2['y3']['creator']), 'Y3 GP', fm(o2['y3']['gp']), 'Y3 EBITDA', fm(o2['y3']['ebitda']))

print('\n== Base sensitivities')
cases = [
 ('75/25, same volumes', dict(split='75/25')),
 ('75/25, onboarding -40%, activity -25%', dict(split='75/25', onb_mult=0.6, act_mult=0.75)),
 ('Founders unpaid to M36', dict(founders=0.0)),
 ('Orders per active creator 5', dict(opm_mult=1.25)),
 ('Active share 25%', dict(act_mult=1.25)),
 ('Orders 5 and active 25%', dict(opm_mult=1.25, act_mult=1.25)),
 ('3 anchor artists, +300 orders/month from M10', dict(anchor_orders=300)),
 ('Base price +R30 ex VAT', dict(base_up=30)),
 ('Anchors + founders unpaid', dict(anchor_orders=300, founders=0.0)),
 ('Orders 4 -> 3 (worse conversion)', dict(opm_mult=0.75)),
]
for label, kw in cases:
    o, rows = M.summary('Base', **kw)
    print(f"  {label}: BE {o['breakeven']} peak {fm(o['peak_burn'])} (m{o['peak_month']}) cash36 {fm(o['cash_m36'])} m36orders {o['m36_orders']} m36EBITDA {fm(o['m36_ebitda'])} Y3 creator {fm(o['y3']['creator'])} Y3 GP {fm(o['y3']['gp'])}")

# break-even volume at stage C, full Y3 team
for split in ('rec','75/25'):
    mt,ct,mh,ch = M.per_unit('C', split)
    blended = 0.65*mt + 0.35*mh
    netu = 0.65*M.TEE['net'] + 0.35*M.HOOD['net']
    var_u = 0.03*netu + 2.2/1.3 + 8.70/(4*1.3)
    fixed = 70000+22000+15000+15000+12000+30000+40000+12000+8000+35000+35000+20000
    u = fixed/(blended-var_u)
    print(split, 'stage C contrib/unit', round(blended,1), 'var/unit', round(var_u,1), 'fixed', fixed, 'BE units', round(u), 'orders', round(u/1.3), '/day', round(u/1.3/30,1))
    mt,ct,mh,ch = M.per_unit('B', split)
    blended = 0.65*mt + 0.35*mh
    fixedB = fixed-15000-20000
    u = fixedB/(blended-var_u)
    print(split, 'stage B contrib/unit', round(blended,1), 'fixed', fixedB, 'BE units', round(u), 'orders', round(u/1.3))
print('net per unit blended', round(0.65*M.TEE['net']+0.35*M.HOOD['net'],2))
