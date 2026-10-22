# South African Print-on-Demand Supply Chain and Fulfilment Options for MerchMe

*Research date: 22 October 2026. All prices are in ZAR unless stated. "incl. VAT" and "excl. VAT" are stated where the source says so; "VAT basis not stated" means the source did not say. Where a page has no visible date, it is marked "undated (page live Oct 2026)". SA VAT is 15%.*

## 1. Local POD / print partners that can print single units on demand (API, white-label, drop-ship)

### Takeaway
South Africa has several no-minimum, white-label POD printers: TeePrint (Johannesburg), OTC Printing (Western Cape), T-POD and Lucani (Cape Town), Hopper SA (Durban) and Brandly. None of them publicly offers a real order API. Integration is by email, store URL, manual upload, or one small unproven Shopify app (In.It Dropship). The global platforms do not print apparel locally: Gelato lists South Africa as a production country but leaves it off its apparel production list, so a Gelato tee ordered for an SA fan is made abroad and shipped in. MerchMe will therefore have to build its own order routing to local partners, or co-develop an integration with one of them.

### Cited Findings
**Local SA POD / drop-ship printers**
- **TeePrint (Boksburg, Johannesburg).** Calls itself a "T-shirt Drop shipping Supplier and marketplace" and the backend for many SA drop-ship brands. Methods: DTG, DTF, vinyl, sublimation and screen. Products: tees, hoodies, bags, caps, jackets, tanks; it can also source baby grows, key rings, mugs, overalls and stickers. No joining fee and no minimum order. Print area up to 35 x 45 cm. The site says "We will print and ship your order within 10 working days", and its FAQ says "We dispatch all orders within 7–10 days" with faster turnaround on request. White-label is available: no TeePrint mention on the package, plus neck labels, custom boxes, pack-ins, tee-bags and hang tags. Full payment is required upfront "as each item is bespoke". It has **no native integration or API**: Shopify and WooCommerce stores link through a TeePrint store URL, or orders are emailed to admin@teeprint.co.za. Sublimation orders have an MOQ. No public per-unit prices were found. — [TeePrint seller page](https://teeprint.co.za/start-selling-shirts/) (page modified June 2025, live Oct 2026)
- **OTC Printing (Western Cape).** Offers POD with "no minimum orders". Average turnaround is "5–7 working days but we strive to get your orders out within 1–3 days". Uses DTG and transfer printing; the page says "No cheap, screen printed plastisol prints". Orders arrive as automated emails, and artwork is sent via Google Drive or WeTransfer. Ships with Aramex at "R100 for up to 12 tees" or with The Courier Guy/PUDO, with no mark-up on courier fees. White-label: each garment goes in a clear sealed bag with a washing-instruction sticker, and the seller's own stickers or inserts can be added. Payment is upfront at first, moving to weekly invoicing once the relationship is established. Products: men's, ladies' and kids' tees, racerback tanks, hoodies, sweatshirts, 11oz and two-tone mugs, 6-panel and trucker caps, visors, baby onesies, wooden coasters, magnets, tote bags. The price list is available by email only. — [OTC Printing POD page](https://www.otcprinting.co.za/print-on-demand/) (modified Sept 2025, live Oct 2026)
- **T-POD (Cape Town).** Tees (unisex, women's, kids', recycled) with front, back, sleeve and inside-collar printing. No stated minimum and no monthly subscription; fulfilment and shipping are charged per order. A locally made 280gsm 60/40 cotton-poly hoodie is listed at **R450** (VAT basis not stated; ask what printing is included). Ships within SA, to wider Africa and internationally via Pargo/Tunl. Offers an online designer and cart ordering, with no stated external-store API. — [Vaybel supplier profile of T-POD](https://vaybel.com/suppliers/t-pod) (sources checked 14 Oct 2026)
- **Lucani (Cape Town).** DTF and embroidery, no minimum order, "Production in 3 to 5 business days" from design approval, delivery anywhere in SA. Store integration "depend[s] on your e-commerce platform… Contact Lucani". — [Lucani POD page](https://lucani.co.za/collections/print-on-demand-clothing-south-africa-how-it-works/) (live Oct 2026)
- **Hopper SA (Durban).** DTF and embroidery on tees, hoodies, golf shirts and jackets, including customer-supplied garments, with no minimum. **Pic-a-Tee** decorates caps, beanies, polos, jackets, hoodies and babywear, with embroidery and no quantity minimum. — [Vaybel similar-suppliers list](https://vaybel.com/suppliers/t-pod) (Oct 2026)
- **Brandly.** A "print-on-demand for product brands" service: "Choose from 10,000+ products. We add your branding, build your online store and fulfil eligible orders". It has a dedicated "Creator merch" offer. Plans: Entry R999 once-off plus R150/month; Basic R3,500 plus R150/month; Pro R6,000 plus R200/month (VAT basis not stated). "Product eligibility, minimum quantities and branding methods vary by product." Packaging, labels and tags are available. — [Brandly homepage](https://brandly.co.za/) (live Oct 2026)
- **In.It Dropship.** A "Shopify app for South African merchants of printed apparel" built by a Johannesburg developer. It is free to install, forwards Shopify orders automatically and charges only when an order is fulfilled. Fees are shown in **US dollars**, and the app had **no public reviews in October 2026**. — [Insaka, "Print on Demand in South Africa: Local vs International", 21 Oct 2026](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)
- Insaka says the local POD market "is smaller and changes often". Local printers "often [have] manual or basic" store integration, while international platforms have "polished Shopify apps". It adds that "many South African DTF and screen printing businesses will fulfil single orders for online sellers if you ask". — [Insaka, 21 Oct 2026](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)
- Insaka's illustrative SA POD tee economics (described as "illustrative, not quotes", Oct 2026): sale price R449; blank plus printing R200; local courier R70; payment fees about R19 (Payfast 3.2% + R2 excl. VAT); marketing R90; profit R70, about 16% of the sale price. — [Insaka, 21 Oct 2026](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)

**Global platforms and South Africa**
- **Gelato** says it has "over 140 production hubs in 32 countries" and **lists South Africa** among its production countries. "Over 85% of orders are produced in the same country where they are delivered." — [Gelato Help: Where do you print locally?](https://support.gelato.com/en/articles/8996076-where-do-you-print-locally) (live Oct 2026)
- **However, Gelato's apparel production list does not include South Africa.** It names Australia, Brazil, Canada, Czech Republic, France, Germany, Italy, New Zealand, Poland, Portugal, Sweden, the Netherlands, the UK and the US. — [Gelato Help: Where is my apparel order printed?](https://support.gelato.com/en/articles/8996105-where-is-my-apparel-clothing-order-printed) (live Oct 2026)
- Insaka: "Printful, Printify and Gelato… None of them confirms South African production on its public delivery pages." Printful lists a **US$12.49 worldwide rate for a single T-shirt** and warns that customs fees may apply. — [Insaka, 21 Oct 2026](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options). This partly conflicts with Gelato's help centre, which does list SA as a production country (likely for non-apparel items; see Gaps).
- A 2023 Shopify Community user reported that Gelato had "POD Partners located locally" in SA. — [Shopify Community thread, Aug 2023 (older, flag)](https://community.shopify.com/t/which-is-the-best-print-on-demand-app-for-south-africa/145857)
- Printful's own country selector lists Australia, Brazil, Canada, France, Germany, Italy, Japan, Latvia, New Zealand, Republic of Korea, Spain, UK and USA. South Africa is not among them. — [Printful homepage](https://www.printful.com/) (Oct 2026)
- Printful notes that Gelato uses local printing companies rather than its own facilities, so "print quality and shipping costs can vary by partner, and orders are assigned automatically with limited seller control". This comes from a competitor. — [Printful vs Gelato](https://www.printful.com/printful-vs-gelato)
- Prodigi has a "Print on demand dropshipping South Africa" landing page; only the snippet was reviewed. — [Prodigi SA page](https://www.prodigi.com/markets/south-africa-print-on-demand/)

**DTF transfer bureaus (B2B transfers MerchMe could press itself)**
- **Blank Media (Edenvale, Johannesburg):** 560mm gang sheets "from R189/m incl. VAT", same-day service, nationwide delivery. — [Blank Media](https://blankmedia.co.za/e-store/dtf-printing-south-africa/). A Facebook promotion shows R169/m for 560 x 1000mm. — [Blank Media Facebook post (undated)](https://www.facebook.com/blankmediasa/posts/-premium-dtf-prints-only-r169-per-meter560mm-x-1000mm-edenvale-johannesburg-fast/1500678992067794/)
- **DTFXpress (Cape Town):** half gang sheet (550 x 500mm) R150; full sheet (550 x 1000mm) from R220; 550 x 1500mm R330; 550 x 3000mm R660; dispatch "within 24 Hours"; no setup fee. VAT basis not stated. — [DTFXpress price guide](https://dtfxpress.co.za/dtf-printing-prices-south-africa/) (modified 6 Apr 2026)
- **DTF PRO / dtfprinting.co.za (Cape Town):** "Prices include VAT". A Facebook group post lists A4 R60, A3 R85, 290 x 1000mm R165, with a minimum of 1m x 55cm for sheets. — [DTF PRO](https://dtfprinting.co.za/); [Facebook group post (undated)](https://www.facebook.com/groups/809010695886067/posts/25434188129608315/)
- A TikTok print-shop rate card lists pocket print R50, A4 R100, A3 R150 (these appear to be printed-on-garment branding prices; whether the garment is included is not stated). — [TikTok @mmn_statement_creatives (2026)](https://www.tiktok.com/@mmn_statement_creatives/video/7696583058819927317)

### Inferences
- No SA partner found offers a documented REST API with webhooks, catalogue sync and status callbacks, as Printful or Gelato do. MerchMe's MVP should assume **email/CSV/portal order hand-off plus manual tracking-number capture**, or fund a partner to build an API. This is a key technology risk to raise with the tech researcher.
- Turnaround spans 1–3 days (OTC best case, DTFXpress transfers in 24h) to 7–10 working days (TeePrint). Add 1–4 courier days and fans should expect **about 4–14 business days** door to door. The faster end requires a partner that holds blanks in stock.
- Insaka's R200 "blank and printing" figure, the T-POD hoodie at R450 and the transfer prices together suggest an outsourced single-unit tee costs roughly **R150–R250** before shipping (this is my synthesis, not a quote). That leaves thin margins under a 75/25 creator split unless retail prices sit around R400–R500 or above.
- Gelato is useful to MerchMe for the **diaspora** (UK, US and EU apparel hubs), not for SA fans buying apparel.
- To spread risk, MerchMe should run a dual-region partner panel: one partner in Gauteng (TeePrint, or a Johannesburg DTF bureau plus press) and one in the Western Cape (OTC, Lucani, T-POD), with KZN (Hopper SA) as a later addition.

### Gaps
- Per-unit POD price lists for TeePrint, OTC, Lucani and Hopper are not public; OTC sends its PDF only by email. Quotes are needed.
- Which Gelato product categories (posters, cards, mugs?) are actually produced in SA. The help centre confirms an SA hub but not its catalogue.
- Independent quality reviews (wash tests, defect rates) of any SA POD partner. Only testimonials on the suppliers' own sites were found.
- "Merch Hub" and Printulu POD offers were not verified in this research.

## 2. Print technologies, single-unit costs, in-house set-up cost, throughput, break-even and power reliability

### Takeaway
DTF is the default technology for SA single-unit POD. Transfers cost about R30–R60 for an A4 print on a gang sheet (R60 as a single print), and an entry A3 DTF set-up costs about **R34k–R100k**, with a 600mm industrial line at about R100k–R280k (2025–26 prices). DTG equipment (Epson F-series) has no published rand price and costs about US$5k–US$17k abroad. Screen printing suits only batch drops. Load-shedding risk is currently low: as at 4 Sept 2026 there had been 476 consecutive days without load-shedding, with residual localised "load reduction". Backup power is still prudent at roughly R22k–R35k for a 5kVA inverter, with batteries extra.

### Cited Findings
**Technology choice**
- Lucani: "DTF printing is the most common method for print-on-demand because it requires no setup screens, supports full-colour artwork, and produces durable prints on individual items." — [Lucani](https://lucani.co.za/collections/print-on-demand-clothing-south-africa-how-it-works/)
- TeePrint offers DTG and DTF for drop-shippers "so, no need to order a large quantity"; sublimation orders have an MOQ and a longer turnaround. — [TeePrint](https://teeprint.co.za/start-selling-shirts/)
- DTFXpress says DTF works on "cotton, polyester, and blends" and resists fading, cracking and peeling. — [DTFXpress](https://dtfxpress.co.za/dtf-printing-prices-south-africa/)

**Outsourced per-print prices (DTF transfers, before pressing)**
- A4 R60, A3 R85 (Cape Town, incl. VAT per the site). — [Facebook group post](https://www.facebook.com/groups/809010695886067/posts/25434188129608315/); [DTF PRO](https://dtfprinting.co.za/)
- Gang sheets cost R169–R189 per metre (560mm wide, incl. VAT; Johannesburg) — [Blank Media](https://blankmedia.co.za/e-store/dtf-printing-south-africa/) — or R220 per 550 x 1000mm sheet (Cape Town, Apr 2026) — [DTFXpress](https://dtfxpress.co.za/dtf-printing-prices-south-africa/)

**In-house DTF equipment (SA prices)**
- Winnerjet's SA price guide (published Dec 2025, updated Jan 2026, from a Chinese vendor): entry A3 desktop about R20,000–R45,000; A3 plus auto shaker and curing oven about R39,000–R99,900; industrial 600mm roll-to-roll about R100,000–R280,000+. Consumables: DTF ink R332–R390 per kg; powder R299 per kg; film 35cm x 100m R1,431.75; A3 curing oven about R3,334. — [Winnerjet](https://www.winnerjet.com/revealing-the-price-of-dtf-printers-in-southern-africa/)
- Bizinbox (Facebook, 25 Jan 2026): A3 DTF printer only R34,000; A3 printer plus oven about R39,000. — [Facebook post](https://www.facebook.com/bizinbox/posts/new-30cm-dtf-printer-desktop-ovenperfect-for-starting-your-own-dtf-printing-or-t/1372750484899257/)
- SourcePrinting: A3 mini DTF compact printer R54,000; oven R4,000. — [SourcePrinting](https://sourceprinting.co.za/product/a3-dtf-compact-printer-new-printer-alert/)
- MaxLaser: 600mm DTF printer R280,200 incl. VAT; automatic shaker and oven on finance from about R4,681–R5,019 per month. — [MaxLaser](https://www.maxlaser.co.za/dtf-printers)
- A Facebook reseller lists an "A3 DTF Starter + Shaker Package" at R99,900. — [Facebook post (undated)](https://www.facebook.com/61550936473597/posts/looking-for-uv-printer-or-dtf-printer-speak-to-us-delivery-and-training-a3-dtf-a/122322956900031215/)
- Winnerjet warns that very cheap imported machines "lack local support" and that downtime losses outweigh hardware savings. It recommends white-ink circulation and RIP software. This is vendor advice. — [Winnerjet](https://www.winnerjet.com/revealing-the-price-of-dtf-printers-in-southern-africa/)

**DTG equipment (no SA rand pricing found)**
- Epson SureColor F2270 hybrid DTG/DTF: US$12,995, or US$16,899 as a pretreat bundle (US reseller). — [Heat Press Nation](https://heatpressnation.com/collections/epson-f2270-direct-to-garment-printers)
- Epson SC-F1000 (A4 DTG/DTF hybrid): €4,990 incl. EU VAT. — [2Stamp (EU)](https://www.2stamp.com/en/printers/566-dtg-printer-epson-scf1000.html)
- Sign Africa reported in April 2025 that Epson had released its first DTF printer (only the snippet was reviewed). — [Sign Africa, 24 Apr 2025](https://www.signafrica.com/epson-releases-its-first-dtf-printer/)

**Throughput**
- An entry XP600-head DTF printer "fits shops doing fewer than 20–30 transfers a day"; i1600/i3200 heads suit higher volume. — [A Good Printer blog (2026)](https://www.agoodprinter.com/blog/dtf-printhead-comparison-xp600-i1600-i3200.html)
- An A3 DTF printer (33cm width) prints about **0.9 m²/hour at 8 passes** (720 x 1440 dpi). — [DTF Station guide](https://dtfstation.com/blog/a3-dtf-printers-high-quality-printing-for-your-business/)

**Power reliability**
- As at 4 Sept 2026, Eskom said South Africa had "recorded 476 consecutive days, or about 16 months, without loadshedding since 16 May 2025". Year-to-date EAF (energy availability factor) was 67.79%, the highest since 2020, and 6,220MW sat in cold reserve. — [Eskom media statement, 4 Sept 2026](https://www.eskom.co.za/eskom-fully-meets-2026-winter-demand-eaf-remains-at-its-highest-level-since-2020-67-79-and-diesel-expenditure-declines-by-r4-84-billion-or-81-64-to-deliver-energy-security/)
- Eskom's Winter 2026 Outlook (published 22 April 2026, covering 1 April to 31 August) projected no load-shedding. — [Eskom](https://www.eskom.co.za/stable-power-system-performance-reinforced-by-operational-and-cost-efficiencies-winter-outlook-projecting-no-loadshedding/)
- Localised "load reduction" in areas with illegal connections still affects **6.5% of Eskom customers**. Seven provinces are now free of it; Gauteng (40.4% of its target feeders cleared) and KZN remain affected. Eskom targets national eradication by **March 2027**. — [Eskom, 4 Sept 2026](https://www.eskom.co.za/eskom-fully-meets-2026-winter-demand-eaf-remains-at-its-highest-level-since-2020-67-79-and-diesel-expenditure-declines-by-r4-84-billion-or-81-64-to-deliver-energy-security/)
- Backup power prices: "R22K to R35K for a 5kva inverter; R30K to R45K for an 8kva inverter" (undated) — [Versofy Energy](https://www.versofy.energy/blog/solar-power-with-battery-backup-price-and-performance); a Felicity inverter or kit listed at R22,500 — [Invert Solar](https://invertsolar.co.za/) (live Oct 2026)

### Inferences
- **Transfer cost per print (my calculation):** a 550 x 1000mm sheet holds about 6 A4 or 3 A3 prints. At R169–R220 per sheet, that works out to about R28–R37 per A4 and R56–R73 per A3 on a bureau gang sheet. A single A4 print costs R60.
- **In-house consumables (rough):** film at R1,431.75 for 100m of 35cm-wide film is about R14 per running metre, or about R4–R5 of film per A4 print. Ink and powder per print were not sourced. A plausible all-in consumable cost of about R8–R15 per A4 print still needs vendor confirmation.
- **Break-even versus a bureau (rough):** saving about R20–R45 per print, an R40k–R100k A3 kit pays back after roughly **1,000–5,000 prints**, before labour, rent, maintenance and printhead replacement. At 20–30 prints a day (the XP600 ceiling), that is about 2–8 months. In-house printing becomes attractive at roughly **30+ orders a day** sustained. Below that, outsourcing (or buying bureau transfers and pressing in-house) is lower risk.
- **Hybrid path:** (1) launch fully outsourced with 2–3 POD partners; (2) at roughly 10–30 orders a day, hold blank inventory, buy gang-sheet transfers from a bureau, and press and pack in a small MerchMe hub, which needs only a heat press and packing staff and gives control over QC and branding; (3) at roughly 50+ orders a day, buy a 600mm i3200-head DTF line (R100k–R280k).
- Screen printing should be reserved for creator "drops" with known pre-order quantities.
- Load-shedding is currently a low operational risk. A 5kVA inverter plus battery is a reasonable insurance line item (roughly R40k+ including battery; battery cost not sourced) for a press-and-pack hub, especially in Gauteng or KZN where localised load reduction persists.

### Gaps
- No SA rand price was found for Epson F1000/F2270 or Brother GTX DTG printers. Contact the local Epson distributor.
- Heat press prices in SA, their power draw (kW), and total power consumption of a DTF line (curing oven plus shaker) were not found, so backup sizing is unverified.
- Ink and powder consumption per m² and actual labour cost per print were not found. Staffing benchmarks (operators per shift, units per operator per day) for SA print shops were not found, nor was a 2026 national minimum wage source.
- Solar and battery cost for a full small-factory backup was not sourced.

## 3. Blank garments: suppliers, costs, quality tiers, inventory and import duties

### Takeaway
Local wholesale blanks are cheap at the promo tier: Barron cotton tees cost about R46–R65 excl. VAT and plain hoodies about R165–R300. Heavyweight streetwear blanks (240–300gsm) exist from small local makers, but their prices were not found. Imported finished clothing pays about **45% customs duty plus 15% import VAT** (HS 61/62, including 6109 T-shirts), which strongly favours local blanks and local production. Fabric duty (about 22% per one US-government source) is much lower, which supports local cut-make-trim (CMT).

### Cited Findings
**Blank suppliers and prices**
- Barron Promo Cotton T-Shirt: R46.48–R65.08 excl. VAT (S–2XL), plain colours. — [Brandability](https://www.brandability.co.za/buy/barron-promo-cotton-t-shirt) (undated, page live Oct 2026)
- Barron Clothing direct: T-shirts "From R31.45 ZAR"; Barron polyester tee R86.39 on sale (regular R95.98). — [Barron Clothing T-shirts](https://www.barronclothing.com/collections/t-shirts) (Oct 2026)
- Barron Long Fit T-Shirt (2XL–5XL): R79.51–R104.99, minimum order value R1,000. — [Probrand Group](https://probrandgroup.africa/product/barron-long-fit-t-shirt/)
- 180g Barron Crew Neck T-Shirt listed at "R 19.99 | R 24.99". This looks unusually low; check whether it is a sale, excl. VAT, or bulk-tier pricing. — [Supply Shop](https://supplyshop.co.za/products/180g-barron-crew-neck-t-shirt)
- Barron BRT Performance Hoodie: R394.55 on sale (regular R543.98). — [Barron Clothing](https://www.barronclothing.com/products/brt318)
- Plain unisex 300gsm "heavyweight" poly-cotton (50/50) hoodies "From R165.22 Each excl VAT", or R299 each incl. VAT. — [T-Shirts South Africa](https://tshirtssouthafrica.com/unisex-hoodies/)
- Premium men's hoodies at R210 each incl. VAT. — [Hoodies South Africa](https://hoodiessouthafrica.com/)
- Plain hoodies, Durban: R199 each (sizes listed include kids 2–3 to 13–14). — [T-Shirts Durban](https://tshirtsdurban.com/plain-hoodies-durban/)
- Just Brand wholesales blank hoodies, including Barron lines. — [Just Brand](https://www.justbrand.co.za/collections/high-quality-blank-hoodies-wholesale)
- Plaintshirts.co.za lists 98 non-sublimated blanks with fabric-weight pricing for "print-ready orders across South Africa". — [Plain T-Shirts](https://plaintshirts.co.za/)
- Poly Nation describes itself as a manufacturer of "top-quality t-shirts, hoodies, sweaters and jackets" wholesale blanks. — [Poly Nation](https://polynation.co.za/wholesale-blank-t-shirts-and-hoodies/)
- **Heavyweight streetwear tier:** "EBEN SUPPLY BOX FIT BLANK TEES. 240gsm 100% cotton… Made in Cape Town" (no price shown). — [Eben Studios Instagram (undated)](https://www.instagram.com/p/C3ziZedoluL/)
- T-POD's locally manufactured hoodie: 280gsm 60/40, listed at R450 (printed retail, not a blank price). — [Vaybel/T-POD](https://vaybel.com/suppliers/t-pod)
- An OTC Printing customer testimonial praises "soft 100% combed cotton shirts" and high gsm. — [OTC Printing](https://www.otcprinting.co.za/print-on-demand/)

**Import duties**
- "South Africa applies 45% import duty on most clothing and textile products under HS chapters 61 and 62". The table lists **6109 T-shirts at 45%**. VAT is 15% on the "ATV (FOB + 10% uplift for non-SACU origin + non-rebated duty)", and ITAC permits apply to rebate provisions. — [JLog HS 61–62 guide (updated Mar 2026; page modified 27 Sept 2026)](https://jlog.co.za/clothing-textiles-hs-61-62-6/)
- **Conflicting source:** the US International Trade Administration's country guide says "The end rate for apparel is 40 percent, yarns 15 percent; fabrics 22 percent; finished goods 30 percent; and fibers, 7.5 percent." This likely reflects bound or phase-down "end rates" rather than current applied rates. — [trade.gov SA Import Tariffs](https://www.trade.gov/country-commercial-guides/south-africa-import-tariffs)
- Twyg: "South Africa has a 45% tariff on imported clothing". — [Twyg explainer](https://twyg.co.za/what-global-tariff-war-means-for-fashion/)
- Reuters (June 2024): Mr Price CEO says that from 1 July, parcels below R500 "will now be taxed at exactly the same rate of 45% plus VAT that we would pay". — [Reuters, 13 Jun 2024 (older)](https://www.reuters.com/business/retail-consumer/s-africas-tax-change-level-playing-field-clothing-retailers-mr-price-ceo-says-2024-06-13/)
- Webber Wentzel: until 2024, the de minimis rule let parcels of R500 or less pay a 20% flat duty without VAT. From 1 Sept 2024, VAT was added to the 20% flat rate, with restructuring by 1 Nov 2024. Local retailers "pay up to 45% customs duty on imports and 15% import VAT". The article also describes the R-CTFL 2030 Master Plan's aims to "boost local production… and substitute imports". — [Webber Wentzel, 19 Sept 2024 (older)](https://www.webberwentzel.com/News/Pages/sars-increases-customs-duties-for-online-retail-orders-what-you-need-to-know.aspx)
- Insaka (Oct 2026), citing Daily Maverick: SARS has charged 15% VAT on top of the 20% flat duty on low-value parcels since Sept 2024. — [Insaka](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)

### Inferences
- With 45% duty plus VAT on imported finished garments, importing printed POD apparel from Printful or Gelato abroad is uncompetitive for SA fans. Local blanks plus local decoration is the only viable model.
- **Cost tiers for planning (VAT basis per source):** promo tee about R45–R65 excl. VAT (Barron); mid/long-fit tee about R80–R105; plain hoodie about R165–R300; branded performance hoodie about R395–R545. A premium heavyweight tee from a local maker is probably R100–R200+ (inference only; no price found).
- **Inventory implications:** a POD hub must stock size × colour × style combinations. For example, 5 sizes × 3 colours × 2 garments is 30 SKUs at perhaps 10–30 units each, or roughly 300–900 blanks (R15k–R60k of stock at R50–R65 per tee; hoodies cost more). Limiting the catalogue to black, white and one seasonal colour keeps this manageable.
- Duty on fabric is lower than on finished clothing (one source says 22% versus 40–45%), so a later **local CMT heavyweight blank** (own label, 240–280gsm) could be a differentiator for creators. Rates need verification on the SARS tariff book.

### Gaps
- Amrod blank prices (dealer-only pricing), Gildan/Crest SA distributor pricing, and caps, beanies and totes blank pricing were not found.
- Local CMT minimums and costs per unit for a custom heavyweight tee were not found.
- No Proudly SA or local-cotton-specific blank supplier was verified.
- The SARS Schedule 1 tariff book was not directly accessed. The 45% figure comes from a clearing agent and secondary sources; it conflicts with the ITA's "40% end rate".

## 4. Fulfilment and couriers: rates, speeds, coverage, COD and returns

### Takeaway
SA parcel delivery is cheap and fast for a 0.3–1kg tee parcel. The Courier Guy (TCG) locker-to-locker network (formerly PUDO) costs **R59–R69** from 1 Sept 2026, or R79–R89 to the door, taking 1–4 days. Paxi costs R59.95 but takes 7–9 days on its economy service. Pargo costs about R75–R140 and has 4,000+ pickup points with better township and rural reach. Economy door-to-door starts around R89–R95. Bob Go aggregates the main couriers on a pay-as-you-go basis from about R72. Outlying-area door surcharges of R100–R150 make pickup points essential for township and rural fans.

### Cited Findings
**The Courier Guy Lockers (formerly PUDO)**
- **Prices from 1 Sept 2026, all incl. VAT:**
  - Locker-to-locker: XS (60x17x8cm, 2kg) R59; S (60x41x8, 5kg) R69; M (10kg) R79; L (15kg) R109; XL (20kg) R149.
  - Locker-to-door: R79, R89, R119, R176, R239, excluding a monthly fuel surcharge. Door-to-locker costs the same.
  - Kiosks: locker-to-kiosk R69–R169; kiosk-to-door R93–R280.
  - Delivery takes 1–2 business days between main centres and 2–4 to regional areas. Recipients have 36 hours to collect.
  - PUDO was rebranded as TCG "Lockers" in June 2025. A Shopify app (The Courier Guy Locker) exists.
  - — [Insaka PUDO prices, updated Oct 2026](https://www.insaka.co.za/blog/pudo)
- The 1 Sept 2026 increase is corroborated by an Instagram post listing Small R69, Medium R79, Large R109 and XL R149. — [Instagram post](https://www.instagram.com/p/Dahfv-SuJWd/?hl=en)
- **Pre-September 2026 prices (older):** locker-to-locker R49 (2kg), R59 (5kg), R69 (10kg), R89 (15kg), R119 (20kg); locker-to-door for 5kg R83.94. — [CTNews, 31 Aug 2026, citing MyBroadband 30 Aug](https://ctnews.co.za/cheapest-ways-to-send-a-parcel-from-cape-town-courier-lockers-paxi-and-pargo-compared/)
- **Locker network size (conflicting):** "over 1,400 lockers and over 200 kiosks" (TCG FAQ, as cited by Insaka) versus "2,300+ lockers and 220+ kiosks… adding approximately three new locations a day" (MyBroadband, July 2026, via CTNews). — [Insaka](https://www.insaka.co.za/blog/pudo); [CTNews](https://ctnews.co.za/cheapest-ways-to-send-a-parcel-from-cape-town-courier-lockers-paxi-and-pargo-compared/)

**Paxi (PEP)**
- Small economy bag (5kg) R59.95, 7–9 business days; small speed R109.95, 3–5 days; large economy (10kg) R109.95; store-to-home R119.95 (5kg) or R149.95 (10kg), 3–5 days. More than 2,800 points (PEP, Tekkie Town, Shoe City). Has a portal for small businesses. — [CTNews, 31 Aug 2026](https://ctnews.co.za/cheapest-ways-to-send-a-parcel-from-cape-town-courier-lockers-paxi-and-pargo-compared/)
- DeliverAI describes Paxi as "designed for the township and rural market". — [DeliverAI Paxi (Oct 2026)](https://deliverai.co.za/couriers/paxi)

**Pargo**
- More than 4,000 pickup points; about R75–R140; 2–5 business days. Shopify and WooCommerce integrations and an API. Markets itself for "informal settlements and outlying areas" where addresses are hard to service. — [CTNews, 31 Aug 2026](https://ctnews.co.za/cheapest-ways-to-send-a-parcel-from-cape-town-courier-lockers-paxi-and-pargo-compared/); [Pargo](https://pargo.co.za/)

**Door-to-door benchmarks (DeliverAI SA Courier Price Index, June 2026)**
- TCG economy door-to-door from R89 (2–4 days); Fastway from R95 (2–3 days); DPD Laser next-day from R145; TCG same-day metro from R140; Pargo from R79; PUDO from R60; Paxi from R59.95.
- 2kg parcel, Johannesburg to Cape Town: economy R85–R135, next-day R140–R210. Johannesburg to Durban: R75–R110 economy, R120–R170 overnight.
- Couriers bill on the greater of actual weight and volumetric weight (L x W x H ÷ 5,000).
- — [Growth Pulse Media, 19 Aug 2026](https://www.growthpulsemedia.co.za/courier-costs-for-ecommerce-south-africa/)
- **Township and rural surcharge:** "Door-to-door delivery to townships and rural addresses attracts a surcharge of R100–R150 per parcel above the standard rate", per TechCentral citing Pargo's CEO. Pickup points can cut cost "by up to 80%" in those areas. — [Growth Pulse Media](https://www.growthpulsemedia.co.za/courier-costs-for-ecommerce-south-africa/) citing [TechCentral](https://techcentral.co.za/couriers-more-risky-township-deliveries/248097/)

**Bob Go (aggregator)**
- Connects Shopify and WooCommerce to The Courier Guy, RAM, Fastway, SkyNet, Internet Express, Pargo, WumDrop and Bob Box lockers. Pay-as-you-go costs R0/month with "shipment rates start from R72". Paid plans cost R249–R1,999/month excl. VAT and add discounted rates, branded tracking, checkout rates and bulk labels. Aggregators are claimed to save 15–25% (an industry benchmark claim). — [Growth Pulse Media, Aug 2026](https://www.growthpulsemedia.co.za/courier-costs-for-ecommerce-south-africa/); [Bob Go pricing](https://www.bobgo.co.za/pricing)
- The Bob Go homepage shows example comparisons such as "Local overnight flyer… R64". — [Bob Go](https://www.bobgo.co.za/)

**Other couriers and benchmarks**
- **Aramex:** OTC Printing ships POD orders with Aramex at "R100 for up to 12 tees". — [OTC Printing](https://www.otcprinting.co.za/print-on-demand/)
- **SA Post Office:** has shrunk from about 2,500 branches to about 657 per MyBroadband, and consumer confidence is damaged. — [CTNews, Aug 2026](https://ctnews.co.za/cheapest-ways-to-send-a-parcel-from-cape-town-courier-lockers-paxi-and-pargo-compared/)
- **Checkout behaviour:** SA cart abandonment is about 75% (Statista via Netcash), and "67.3% of SA online purchases [are] driven by free delivery availability". Recommended free-shipping thresholds are R500–R800 for fashion. — [Growth Pulse Media](https://www.growthpulsemedia.co.za/courier-costs-for-ecommerce-south-africa/)
- **3PL rates:** "South African e-commerce brands typically pay R150–R250 per 5 kg domestically, and 40–60% less than retail courier rates by using a 3PL" (snippet only). — [JLog](https://jlog.co.za/ecommerce-shipping-checklist-south-africa/)

### Inferences
- A single tee (about 0.25–0.4kg packed flat in a poly mailer) fits the TCG **XS (R59) or S (R69)** locker size. A hoodie probably needs S or M (R69–R79). This makes **R59–R79 locker delivery** the default low-cost option for MerchMe, offering R79–R119 door delivery alongside it.
- To reach township and rural fans, MerchMe should offer **Pargo and Paxi pickup** at checkout. Paxi is the cheapest for non-urgent orders and its PEP footprint is strong in lower-income areas.
- Bob Go (or direct TCG + Pargo APIs) can supply live rates, waybills and tracking to the MerchMe app, so a courier layer can be integrated without bespoke contracts at launch.
- **Returns:** because TCG prices door-to-locker the same as locker-to-door, a reverse label for a size exchange costs about R59–R89 each way. Budget about R120–R180 per exchange round trip, plus reprint cost if the item is personalised.

### Gaps
- **Cash-on-delivery** availability for TCG, Pargo, Paxi and Aramex was not found in this research. COD appears uncommon in SA parcel networks, but this is unverified.
- Independent reliability data (on-time %, loss/damage rates) for each courier was not found.
- Official Aramex/Fastway 2026 rate cards and current Courier Guy door-to-door rate tables were not directly accessed; the figures above are aggregator and benchmark data.
- Pargo's own 2026 rate card was not accessed; the R75–R140 range comes from MyBroadband via CTNews.

## 5. Packaging, quality control, misprint/return rates and the Consumer Protection Act

### Takeaway
SA POD partners offer white-label packaging (sealed bags, neck labels, branded boxes, inserts). Personalised print-to-order goods are excluded from ECTA's 7-day no-reason cooling-off right. However, the CPA's six-month implied warranty for defective goods still applies, and the platform as seller carries consumer liability even when the printer makes the item. No reliable data on misprint or return rates was found.

### Cited Findings
**Packaging and white-labelling**
- OTC Printing: white-labelled, "no sign of our company for POD orders". Each clothing item goes in a clear sealed bag with a washing-instruction sticker; seller stickers or inserts are optional. — [OTC Printing](https://www.otcprinting.co.za/print-on-demand/)
- TeePrint: "There is no mention of TeePrint on the package or the product". Neck labels, custom packing, personal notes, custom boxes, pack-ins, tee-bags and hang tags are available. Garments go "through several quality checks". — [TeePrint](https://teeprint.co.za/start-selling-shirts/)
- Brandly offers packaging, labels and tags ("Brand finish"). — [Brandly](https://brandly.co.za/)
- Lucani: each garment is "printed using DTF, DTG, or another digital method, then inspected". — [Lucani](https://lucani.co.za/collections/print-on-demand-clothing-south-africa-how-it-works/)

**Consumer law**
- **ECTA s44** gives online consumers a 7-day cooling-off right to cancel. — [Michalsons](https://www.michalsons.com/blog/consumer-protection-in-electronic-transactions-ect-v-cpa/2631); [SEESA](https://www.seesa.co.za/blog/online-transactions/)
- **ECTA s42(2)** excludes goods that "are made to the consumer's specifications" or "are clearly personalised" from the cooling-off right. — [Consumer Goods and Services Ombud Advisory Note 10: E-Commerce (2021, via SAFLII)](https://www3.saflii.org/za/cases/ZACGSO/2021/10.html); [MJK Inc on ECTA](https://mjkinc.co.za/software-technology-law/ecta-electronic-contracts)
- **CPA s56** (implied warranty): "within six months after the delivery of goods, a consumer may return the goods to the supplier without penalty and at the supplier's risk and expense" if they fail the quality standards. — [Eastern Cape DEDEAT (Facebook post quoting the CPA)](https://www.facebook.com/ECDEDEAT/posts/warranty-informationconsumer-protection-act-is-the-general-legislative-instrumen/3854384064686686/); [JustAnswer SA law Q&A](https://www.justanswer.com/south-africa-law/4us4k-reference-new-consumer-protection-act-thursday.html). Both are secondary sources.
- Insaka: "your customer's consumer rights apply to you as the seller, even though the printer handles the product. Agree in writing how your provider handles misprints, defects and returns." It also advises publishing a size chart for every garment to reduce exchanges, and putting honest total lead times on product pages. — [Insaka, 21 Oct 2026](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)
- TeePrint requires full upfront payment "as each item is bespoke, and cannot be resold". This shows that SA printers treat POD items as non-returnable stock. — [TeePrint](https://teeprint.co.za/start-selling-shirts/)
- Insaka recommends caps and tote bags for beginners because they "avoid sizing returns". — [Insaka](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)

### Inferences
- **MerchMe returns policy:**
  - Defective or misprinted items: free replacement or refund within 6 months (CPA s56). The cost is recovered from the print partner under a written SLA.
  - Change-of-mind on a creator design: arguably excluded from ECTA cooling-off as "made to specification / personalised". Counsel should confirm, because a standard catalogue design printed on demand is not obviously "personalised" in the way a custom name print is.
  - Size exchanges: offer a goodwill exchange (fan pays courier) as a customer-experience choice, backed by strong size charts and fit notes.
- **Partner SLA terms:** reprint SLA (for example, 48–72h), pre-dispatch photo QC, wash-durability standard (for example, 30+ washes for DTF), and partner liability for misprints.
- MerchMe should own the packaging spec (branded mailer, thank-you card from the creator, size/care sticker). Partners already accept seller inserts and stickers, so this is feasible without an own warehouse.

### Gaps
- **Typical POD misprint, defect and return rates** (SA or global): no reliable source was found. Searches returned only market-size reports.
- **CPA s20** (return of goods not examined before delivery) and its interplay with ECTA s42 for online apparel was not verified. A legal review is needed.
- Costs of custom poly mailers, branded boxes and hang tags in SA were not found.

## 6. Ability to expand to other products locally (caps, beanies, totes, posters, phone cases, stickers, mugs)

### Takeaway
SA POD partners already cover the main merch categories beyond tees. OTC (mugs, caps, visors, totes, coasters, magnets, onesies), TeePrint (caps, bags, mugs, key rings, stickers, baby grows), Pic-a-Tee (caps and beanies with no-minimum embroidery), Hopper SA (embroidery) and Brandly (headwear, drinkware, bags, tech and stationery) between them cover caps, mugs, totes, stickers and key rings. Posters, art prints and phone cases are less clearly covered by the apparel shops. Sublimation items may carry MOQs.

### Cited Findings
- OTC Printing POD catalogue: men's, ladies' and kids' tees, racerback tanks, hoodies, sweatshirts, 11oz and two-tone mugs, 6-panel active caps, washed trucker caps, visors, baby onesies, wooden coasters, rectangle magnets, natural tote bags. — [OTC Printing](https://www.otcprinting.co.za/print-on-demand/)
- TeePrint: T-shirts, hoodies, bags, caps, jackets, tanks; "We can source baby grows, caps, key rings, mugs, overalls, bags, stickers and much more". "Sublimation orders have a MOQ, and a longer turn around time." — [TeePrint](https://teeprint.co.za/start-selling-shirts/)
- Pic-a-Tee decorates "caps, beanies, polos, jackets, hoodies and babywear, with embroidery available without a quantity minimum". Hopper SA (Durban) offers DTF and embroidery with no minimum. — [Vaybel listings](https://vaybel.com/suppliers/t-pod)
- Brandly categories: Apparel 478 products, Headwear 209, Drinkware 90, Bags 757, Gifting 206, Stationery 59, Technology 186, Workwear 325 (14 categories). "Product eligibility, minimum quantities and branding methods vary by product." — [Brandly](https://brandly.co.za/)
- Lucani offers DTF printing and embroidery. — [Lucani](https://lucani.co.za/collections/print-on-demand-clothing-south-africa-how-it-works/)
- Insaka's suggested starter POD range for SA: tees and hoodies, caps and tote bags, mugs and drinkware, art prints and posters. — [Insaka](https://www.insaka.co.za/blog/print-on-demand-in-south-africa-local-vs-international-options)
- Gelato lists South Africa as a production-hub country (which products are made there is unconfirmed; Gelato's core catalogue includes wall art, posters, cards and mugs). — [Gelato Help](https://support.gelato.com/en/articles/8996076-where-do-you-print-locally)
- Prodigi markets POD dropshipping for South Africa (only the snippet was reviewed). — [Prodigi](https://www.prodigi.com/markets/south-africa-print-on-demand/)

### Inferences
- **Phase 1 catalogue:** tee, hoodie, cap (embroidered or DTF), tote and 11oz mug. All are available no-minimum from at least two SA partners.
- **Phase 2:** beanies (embroidery), stickers, posters and art prints. Posters may route via Gelato's SA hub or Prodigi if confirmed; otherwise use local digital print shops.
- Phone cases need sublimation or UV printing and many device SKUs, so they fit poorly with local POD partners. They are better served via a global partner or deferred.
- An in-house DTF line also decorates caps (with a cap press), totes and hoodies. Mugs require a separate sublimation set-up, which is a reason to keep mugs outsourced.

### Gaps
- No pricing was found for SA POD caps, beanies, totes, mugs, stickers or posters.
- No SA POD source for phone cases or posters with a drop-ship model was verified; the Gelato SA hub's product list and the Prodigi SA page were not confirmed.

## 7. Cross-border: SADC neighbours and the global diaspora

### Takeaway
SA-based fulfilment can serve the SACU neighbours (Namibia, Botswana, Lesotho, eSwatini). They form a single customs territory with SA and pay no internal customs duty, although buyers face destination VAT and customs paperwork. Pargo has expanded pickup points to all four countries (date unknown), and some SA POD shops already ship to wider Africa via Pargo/Tunl. For UK, US and EU diaspora fans, shipping from SA is costly and slow. A global POD partner with local apparel hubs (Gelato UK/US/EU, Printful UK/US/EU) is the practical route, using the same artwork.

### Cited Findings
- The SACU bloc (Botswana, Eswatini, Lesotho, Namibia) is a "single customs territory with South Africa, so goods move between them without internal customs duty once cleared". It is recommended as the first cross-border market. Destination import VAT is charged to the buyer by default, and must be disclosed at checkout to avoid refused parcels. Commercial exporters generally need a SARS exporter code. — [Growth Pulse Media, 17 May 2026](https://www.growthpulsemedia.co.za/cross-border-ecommerce-south-africa/)
- JLog: VAT calculation uses "FOB + 10% uplift for non-SACU origin", which confirms SACU-specific treatment in SA customs valuation. — [JLog](https://jlog.co.za/clothing-textiles-hs-61-62-6/)
- Pargo "expanded their network of parcel pick-up points to Namibia, Botswana, Lesotho and Swaziland". The article is undated, so it may be old. — [Pargo media coverage](https://pargo.co.za/media-coverage/pargo-launches-cross-border-delivery-service-to-other-african-countries/)
- T-POD delivers to "South Africa, wider Africa and international delivery through Pargo/Tunl; exact overseas countries unspecified." — [Vaybel/T-POD](https://vaybel.com/suppliers/t-pod)
- Road freight to Namibia or Botswana costs about R3,500–R12,000 per pallet, which is relevant for bulk drops to a regional partner. — [JLog international shipping](https://jlog.co.za/international-shipping-from-south-africa/)
- **Gelato for the diaspora:** apparel is produced in the UK and US (all print areas, including inner and outer labels and sleeves) and across the EU. Over 85% of orders are produced in-country and it delivers to more than 200 countries. — [Gelato apparel production](https://support.gelato.com/en/articles/8996105-where-is-my-apparel-clothing-order-printed); [Gelato local production](https://support.gelato.com/en/articles/8996076-where-do-you-print-locally)
- Gelato's base cost for a classic unisex tee is about US$9–US$11 (US$7.50 on Gelato+), versus Printful at about US$11.50–US$13. — [Syncost Gelato review (2026)](https://www.syncost.com/blogs/gelato-print-on-demand-review)
- Printful has fulfilment presence in the UK, USA, Spain, Latvia, France, Germany, Italy, Canada, Brazil, Australia, NZ, Japan and Korea. — [Printful](https://www.printful.com/)
- Growth Pulse Media warns that international courier cost is "the variable that most often turns a profitable-looking order into a loss", and that cross-border from SA should start in low-friction markets. — [Growth Pulse Media](https://www.growthpulsemedia.co.za/cross-border-ecommerce-south-africa/)

### Inferences
- MerchMe could route orders automatically by fan location:
  - **SA addresses** go to local partners.
  - **SACU addresses** go to the same SA partner, shipped via Pargo cross-border or a regional courier, with the destination VAT shown at checkout.
  - **UK, US, EU and AU addresses** go to the Gelato (or Printful) API.
- This keeps one creator design library, but blank styles will differ by region, so product pages need region-specific mockups and size charts.
- Gelato and Printful have full APIs, which makes the diaspora channel technically easier to integrate than the SA channel.
- Gelato and Printful price in USD, so the creator split for diaspora orders should be calculated in USD and converted. FX volatility is a margin risk.

### Gaps
- Actual per-parcel courier rates from SA to Windhoek, Gaborone, Maseru and Mbabane, and current Pargo cross-border availability, were not found.
- Import VAT rates and any small-parcel thresholds in Namibia, Botswana, Lesotho and eSwatini were not verified.
- Gelato and Printful delivery times and costs to UK and US fans for specific products were not quoted (only base tee costs).
- Which SADC countries beyond SACU (Zimbabwe, Mozambique, Zambia) are realistically serviceable was not researched.
