# MerchMe (South Africa): technology build options and legal, regulatory, IP and tax requirements

Research date: 22 October 2026. Every fact below carries its source and date where known. Items marked **[CHANGED since 2024]** differ from what a 2024-era plan would assume. None of this is legal or tax advice. Items marked **[CONFIRM: lawyer/accountant]** need professional sign-off before launch.

Business model assumed: creators upload designs, MerchMe auto-generates a branded mobile shop per creator, fans buy, a print-on-demand (POD) partner prints and ships, and MerchMe pays the creator 25% of profit and keeps 75%.

---

## T1. Build vs buy: which commerce platform suits a creator-per-storefront marketplace?

### Takeaway
No off-the-shelf SaaS marketplace fits SA well. Shopify Payments, Stripe Connect and Sharetribe's default payments are not natively available to SA merchants. The practical choices are:
- **(a) Fastest MVP:** WooCommerce plus a multi-vendor plugin (Dokan/WCFM), using a SA gateway with split payments.
- **(b) Scalable build:** open-source Medusa plus Mercur, or a custom Next.js and Supabase stack, with a Paystack or PayFast split-payment integration.

Shopify is viable only for a single-store MVP where MerchMe is the seller and pays creator royalties outside the checkout.

### Cited Findings
- **Shopify plans (ZA pricing page, Oct 2026, billed in USD):**
  - Basic: US$25/mo (US$22/mo annual).
  - Grow: US$65/mo (US$58 annual).
  - Advanced: US$399/mo (US$359 annual).
  - Plus: from US$2,300/mo.
  - Extra fee when using a third-party payment provider: 2% (Basic), 1% (Grow), 0.6% (Advanced), 0.2% (Plus).
  - Shopify says "Shopify Payments is available only in certain countries" — [Shopify ZA pricing](https://www.shopify.com/za/pricing)
- Shopify Payments is not offered in SA, so merchants must connect gateways such as PayFast or PayGate and pay Shopify's extra transaction fee. Shopify bills in USD, so rand cost moves with the exchange rate. The source is a competitor with commercial bias — [Shopstar vs Shopify](https://www.shopstar.co.za/post/shopstar-vs-shopify-south-africa); also [Netcash Shopify pricing guide](https://netcash.co.za/blog/shopify-pricing-everything-you-need-to-know-about-plans-and-pricing/)
- **WooCommerce + Dokan (vendor's own July 2026 comparison):**
  - Free tier, then Starter US$149/yr (1 site), Professional US$249/yr, Business US$499/yr, Enterprise US$999/yr.
  - Capterra lists lifetime options, e.g. Starter US$596.
  - Dokan has a Paystack module.
  - Sources: [Dokan blog](https://dokan.co/blog/513197/best-woocommerce-multi-vendor-plugins/); [Capterra](https://www.capterra.co.za/software/168004/dokan-multivendor-marketplace); [Dokan Paystack module](https://dokan.co/wordpress/modules/paystack-module/)
- **WCFM:** core plugin free; WCFM Ultimate roughly US$49–59/yr for 2 sites, lifetime about US$199, add-ons extra. Figures conflict across listings — [TrustRadius](https://tr-web.dev.trustradius.com/products/wcfm-marketplace/pricing); [G2](https://g2.com/products/wcfm-marketplace/pricing)
- **Medusa + Mercur:**
  - Mercur is an MIT-licensed, open-source marketplace layer on Medusa.
  - It includes vendor onboarding, multi-vendor catalogues, commissions, automated payouts and a vendor panel.
  - It is self-hostable with "no percentage of GMV", and also deploys to Medusa Cloud — [Mercur GitHub](https://github.com/mercurjs/mercur); [Medusa marketplace page](https://medusajs.com/marketplace)
  - Mercur 2.0's Medusa Cloud setup uses Stripe as "customer payments + Mercur payout provider" (env vars `STRIPE_API_KEY`, `STRIPE_PAYOUT_WEBHOOK_SECRET`) — [Medusa blog: Mercur 2.0 on Cloud](https://medusajs.com/blog/get-started-with-mercur-2-0-on-cloud)
- **Vendure / Medusa / Saleor (secondary sources, quality mixed):**
  - One comparison says Vendure suits multi-vendor marketplaces but needs more upfront planning than Medusa.
  - Medusa is modular but heavy customisation can become hard to maintain — [PowerGate: Medusa vs Vendure](https://powergatesoftware.com/tech-blog/medusajs-vs-vendure/)
  - Saleor is GraphQL-first on Python/Django with multi-channel and multi-warehouse support; native multi-vendor support not confirmed — [PkgPulse 2026](https://www.pkgpulse.com/guides/medusa-vs-saleor-vs-vendure-headless-ecommerce-2026)
- **Sharetribe [CHANGED since 2024]:**
  - Now two plans: Build US$39/mo (testing) and Live US$259/mo (US$199/mo annual), plus Hold US$49/mo.
  - Every plan includes 1 million usage credits per month.
  - Usage-based billing takes effect for existing customers on 1 December 2026 — [Sharetribe pricing help](https://www.sharetribe.com/help/en/articles/17105170-sharetribe-pricing-plans-and-usage-based-fees); [Sharetribe docs: usage-based pricing](https://www.sharetribe.com/docs/introduction/pricing/)
  - A third party claims a 2% transaction fee; this is not confirmed on official pages — [Roobykon](https://roobykon.com/?p=15222)
- **Custom-stack hosting:**
  - Supabase Pro is about US$25 per organisation per month and includes a US$10 compute credit. A growing app is about US$36/mo (third-party, verified July/Aug 2026) — [MakerKit Supabase pricing](https://makerkit.dev/blog/saas/supabase-pricing)
  - Vercel Pro is a US$20/mo platform fee with 1 deploying seat and US$20 usage credit; extra seats and overage cost more. Hobby is non-commercial only — [Vercel docs](https://vercel.com/docs/plans/pro-plan/switching); [MakerKit Vercel cost](https://makerkit.dev/blog/saas/vercel-cost)

### Inferences
- **Creator-per-storefront on Shopify** means either one Shopify store per creator (US$25+/mo each plus the 2% third-party fee, which kills unit economics at scale) or one store with a multi-vendor app. Neither gives native split payouts in SA. Shopify suits only a "MerchMe sells everything, pays royalties by EFT monthly" MVP.
- **Mercur's default payout rail is Stripe**, which is not directly available in SA (see T3). A Medusa/Mercur build therefore needs a custom payout provider (Paystack subaccounts or PayFast split). This is likely 2–4 weeks of extra engineering (estimate, not sourced).
- **Recommended phasing:**
  - **Phase 0 (2–6 weeks):** WooCommerce + Dokan/WCFM, or a single Shopify store with collections per creator, to prove demand.
  - **Phase 1 (3–5 months):** custom Next.js + Supabase/Postgres, or Medusa + Mercur. Each creator gets a subdomain or path (e.g. `creator.merchme.co.za` or `merchme.co.za/creator`) with a shared catalogue, auto-generated mockups and SA split payments.
- **Custom subdomains** are trivial on Vercel or Cloudflare with a wildcard DNS record. Path-based URLs are simpler for SEO and SSL.

### Gaps
- Shopify Collective availability outside the US/Canada and pricing of Shopify multi-vendor apps (Webkul, Shipturtle) were not researched.
- Medusa Cloud and Saleor Cloud prices were not retrieved.
- Sharetribe's support for non-Stripe (SA) payment gateways was not confirmed.
- I found no sourced current USD/ZAR rate for October 2026. One 2025/26 guide implied about R18.4/USD (US$25 ≈ R460). Recompute at today's rate.

---

## T2. Product mock-up generation, design-upload editors and AI tools

### Takeaway
Mock-up APIs are cheap; a credit-based API like Dynamic Mockups costs tens of US$/month at MVP scale. Printful's free mock-up generator is tied to Printful's own catalogue, which isn't printed in SA. A full web-to-print editor such as Customer's Canvas costs four figures a month. For an MVP, use a simple upload-and-place UI (e.g. an open-source canvas library) plus a mock-up API.

### Cited Findings
- **Dynamic Mockups:**
  - Current pricing page: Free tier of 50 credits; Pro US$15/mo billed annually or US$19 monthly (3,600 credits/yr).
  - Free accounts include watermarked API access — [Dynamic Mockups pricing](https://dynamicmockups.com/pricing/)
  - Older pages list an API plan at US$49/mo at US$0.089/image with a 1,000-image API trial. Enterprise is annual with a 100k-image minimum. Sources conflict by date — [Dynamic Mockups help](https://help.dynamicmockups.com/en/articles/13251205-what-is-dynamic-mockups); [Dynamic Mockups pricing archive](https://dynamicmockups.com/?p=3752)
- **Printful mock-up generator API:**
  - Asynchronous: create a task, then poll.
  - General Printful API limit is 120 calls/min, with lower limits on mock-up endpoints.
  - No separate API price found; free for Printful products. Third-party sources — [Jentic: Printful API](https://jentic.com/apis/printful); [Dynamic Mockups FAQ on rate limits](https://dynamicmockups.com/?p=58403)
  - A 2020 report says mock-up access was limited if the account had no orders in 30 days (may be outdated) — [Shopify app reviews](https://apps.shopify.com/reviews/633877)
- **Zakeke** (product customiser): paid plans from US$29.90/mo; Enterprise by quote. Source is a competitor's blog — [Dynamic Mockups: product customisation software](https://dynamicmockups.com/tools/best-photo-product-customization-software/)
- **Customer's Canvas** (Aurigma web-to-print editor): starts at about US$1,000/mo, priced by quote, often with setup fees — [Krowdbase](https://www.krowdbase.com/software/customer-s-canvas); [Capterra](https://www.capterra.com/p/173237/Customer-s-Canvas/); [ZoftwareHub](https://zoftwarehub.com/en-ae/products/customer-s-canvas/reviews)
- **Placeit:** from US$14.95/mo (Capterra) — [Capterra Placeit pricing](https://www.capterra.com/p/228818/Placeit/pricing/)
- **Mediamodifier:** Pro from about US$14–25/mo (sources conflict); offers an API but rates are not published — [Mediamodifier blog](https://mediamodifier.com/blog/placeit-alternatives); [Toolradar comparison](https://toolradar.com/compare/mediamodifier-vs-smartmockups)

### Inferences
- **MVP:** creators upload a transparent PNG; a canvas library positions it within a print-area template per product; then call a mock-up API (Dynamic Mockups) or render mock-ups in-house with pre-shot blank-product photos and displacement maps.
  - Mock-up cost at 20 products × 100 creators = 2,000 images. That is roughly within a Pro-tier credit pack per year, or about US$180 at US$0.089/image.
- **Print files:** whatever the POD partner needs (typically 300 dpi PNG at print-area size) must be generated server-side from the same placement data. This is a core build item.
- **Skip at MVP:** a full customiser (Zakeke, Customer's Canvas) is unnecessary, because fans don't customise; creators place designs once.

### Gaps
- Fabric.js and Konva licence and maturity were not verified in this session; both are widely used open-source canvas libraries.
- Smartmockups (now part of Canva) has no public API; this was not verified.
- AI-assisted design tools (e.g. text-to-image for creators, background removal, upscaling) were not researched. Costs and IP terms of AI outputs remain open.

---

## T3. Payments in SA for a marketplace with split payouts

### Takeaway
Stripe is not directly available. South Africa is listed as "Extended network" and routed to Paystack. The two SA gateways with documented split or marketplace features are:
- **Paystack:** subaccounts and split groups; 2.9% + R1 local cards, 2% EFT, ex VAT.
- **PayFast:** Split Payments; 3.2% + R2 cards, 2% instant EFT, ex VAT; custom integration only; one split per payment.

Peach Payments and Stitch offer payouts APIs for disbursing to creators from a float. Yoco and Ozow are good checkout rails but have no documented split feature.

### Cited Findings
- **Stripe [CONFIRMED Oct 2026]:** Stripe's global availability page lists South Africa as "Extended network", linking to paystack.com/stripe/south-africa. This means no direct Stripe account for SA entities — [Stripe global](https://stripe.com/global)
  - Paystack (a Stripe company) launched in SA in 2021 — [TechCrunch 2021](https://techcrunch.com/2021/05/06/paystack-expands-to-south-africa-seven-months-after-stripe-acquisition)
- **Paystack SA fees:** local cards 2.9% + R1.00 (VAT exclusive); EFT 2%; international cards 3.1% + R1.00 — [Paystack support: transaction pricing](https://support.paystack.com/en/articles/2130306)
  - A 2026 comparison says Paystack waives the R1 on payments under R10 and pays out 2 working days after payment — [Zande 2026 comparison](https://www.zande.io/blog/paystack-vs-payfast-vs-yoco)
- **Paystack splits:** "Transaction Splits" split money between multiple bank accounts called subaccounts, as flat or percentage shares. Multi-party splits use a split group and split code; leftover after flat amounts settles to the main account — [Paystack support: transaction splits](https://support.paystack.com/en/articles/2132802)
- **PayFast fees (fees page modified 7 Aug 2026):**
  - Credit/cheque card: 3.2% + R2.00.
  - Instant EFT and Capitec Pay: 2.0% (min R2.00).
  - SnapScan: 3.5% + R2.00. Zapper and SCode: 4.5% + R5.00. Mobicred: 3.2%.
  - Payout fee R8.70 ex VAT; immediate payout 0.8% ex VAT (min R14.00).
  - No setup or monthly fees; fees shown ex VAT — [PayFast fees](https://payfast.io/fees/)
- **PayFast Split Payments:**
  - Splits part of an online payment with a third party, as a fixed amount, a percentage or both.
  - One primary account can link to unlimited secondary accounts, but each buyer payment is split only once.
  - A platform can be the secondary account for many merchants.
  - Available only through custom integration — [PayFast blog: Split Payments](https://payfast.io/?p=6563); [CMARIX guide](https://www.cmarix.com/blog/build-marketplace-payment-solution-with-payfast-split-payments/)
- **Peach Payments:**
  - Growth plan 2.95% + R1.50 per transaction (ex VAT), no setup or monthly fees, weekly settlement on Thursdays; Bulk Payouts feature — [Peach fees page, modified 25 Jun 2026](https://www.peachpayments.com/fees/); [SME South Africa](https://smesouthafrica.co.za/?p=50578)
  - Real-time clearance payouts for all SA merchants, funded from settlement balance or EFT, via API or dashboard. Recipients typically get funds in about 90 seconds. Beneficiary bank-account verification included. Per-payout price not published — [ITNewsAfrica](https://www.itnewsafrica.com/africa-by-region/southern-africa-africa-by-region/south-africa-peach-payments-announces-real-time-clearance-payouts/)
- **Yoco online:**
  - 2.55–2.95% (ex VAT); no monthly or setup fees — [Yoco online payments, updated 5 Oct 2026](https://www.yoco.com/za/online-payment/)
  - Checkout API is a hosted redirect flow — [Yoco developer docs](https://developer.yoco.com/docs/checkout-api)
  - No subscriptions or recurring billing — [StoreKit Yoco guide](https://storekit.com/docs/guides/payments/yoco.md)
  - No split or marketplace feature mentioned.
- **Ozow (pay-by-bank / instant EFT):**
  - Tiers from 2.5% (up to R499,999.99 monthly value) down to 1.5% (over R10m/month); refunds R5.00–R8.50 each.
  - No setup or monthly fees. The enterprise threshold differs across Ozow pages (R1m vs R1.5m/month) — [Ozow SMS pricing](https://sms.ozow.com/pricing/); [Ozow pricing](https://ozow.com/pricing)
- **Stitch:**
  - Payouts API for one-off or bulk disbursements from a float, over SDV, RTC or RPP rails, 24/7/365.
  - Real-time bank account verification; marketed for marketplace collections plus withdrawals.
  - Pricing not public — [Stitch payouts](https://stitch.money/payouts); [Stitch marketplaces](https://stitch.money/e-hailing-and-marketplaces); [TechCabal 2022](https://techcabal.com/2022/07/04/stitch-launches-stitch-payouts-in-south-africa/)
- **PayPal (SA):**
  - Usable mainly for receiving international payments. Withdrawals go to SA banks via FNB, each needing a Balance of Payments code and reported to SARB. Takes 3–5 business days — [FNB PayPal](https://fnb.co.za/forex/payments/paypal.html); [Wise ZA](https://wise.com/za/blog/receiving-money-with-paypal)
  - Conversion fees 3–4% — [Wise ZA](https://wise.com/za/blog/receiving-money-with-paypal)

### Inferences
- **Worked fee example on a R450 T-shirt** (calculations from the cited rates, ex VAT; add 15% VAT on fees for a non-VAT-vendor's true cost):

  | Rail | Fee | Notes |
  |---|---|---|
  | Paystack card | R14.05 | |
  | Paystack EFT | R9.00 | |
  | PayFast card | R16.40 | |
  | PayFast instant EFT | R9.00 | |
  | Yoco | R11.48–R13.28 | |
  | Ozow | R11.25 | |
  | Shopify extra fee (Basic) | +R9.00 | on top of the gateway fee |

- **Split vs batch payouts:** PayFast's "one split per payment" fits a one-creator-per-storefront model, since every order belongs to one creator. Paystack split groups also work.
  - A split at checkout pays the creator before returns or chargebacks are known, and before the actual POD cost is final. So "25% of profit" must be a fixed, pre-computed amount per SKU.
  - Alternative: hold funds and pay monthly via Peach or Stitch payouts, net of refunds. That is better for a profit share, but raises the payments-regulation question in L5.
- **KYC on creators:** using gateway subaccounts or secondary accounts means each creator must pass the gateway's onboarding/KYC (ID, bank account verification). That adds friction for small creators. Batch payouts from MerchMe's own account need only bank verification, but put MerchMe in the money flow.
- **Recommended stack:**
  - Paystack, for cards, EFT and splits on one API, with Stripe-backed reliability.
  - Optionally PayFast or Ozow for instant-EFT coverage.
  - Peach or Stitch payouts for monthly creator payouts if a principal model is used.

### Gaps
- No official Paystack SA payout/transfer fee or settlement schedule was retrieved; the 2-day figure is third-party.
- PayFast split-payment specifics are unconfirmed: who bears the fee, and whether the secondary party must hold its own PayFast account.
- Peach per-payout fee and Stitch pricing are not published.
- Gateways' exact KYC requirements for subaccounts were not retrieved.

---

## T4. Social integration: Instagram/Facebook Shops, TikTok Shop, link-in-bio, WhatsApp

### Takeaway
SA merchants cannot run organic Facebook or Instagram Shops or product tags; Meta ended Shops for SA on 10 August 2023. Catalogue sync and product-tagged ads still work. TikTok Shop is not live in SA as of October 2026 on the evidence found. The realistic channel is a link-in-bio or link-sticker to the creator's mobile shop, plus WhatsApp catalogues and payment links.

### Cited Findings
- **Meta Shops:** "As of 10 August 2023, Facebook (Meta) no longer supports the Facebook and Instagram Shops feature for South Africa."
  - SA merchants can still connect accounts, sync the product catalogue and advertise.
  - They can tag products in Instagram advertising, but not in organic posts — [Netcash Shop help, modified Nov 2024](https://shop.netcash.co.za/blog/docs/sales-channels/facebook-and-instagram/tagging-products-on-instagram/)
- Meta's 2023 list of 21 markets keeping Shops without checkout did not include SA — [TechCrunch](https://techcrunch.com/?p=2534880)
- Meta says Instagram shopping tags appear only in countries where the catalogue has pricing information; no country list was retrieved — [Meta developers: localized catalog](https://developers.facebook.com/documentation/ads-commerce/catalog/localized-catalog-ig)
- **[CHANGED since 2024]** A merchant blog (Aug 2026, lower-quality source) reports Meta phased out native in-app checkout across most regions from June 2025, routing shoppers to brands' own sites — [Whatmore](https://www.whatmore.ai/blog/why-meta-s-instagram-product-tagging-update-matters-and-why-you-still-need-your-own-shoppable-video-storefront/)
- **Instagram links:** since April 2023, all accounts (including creator and business) can add up to 5 links in bio. Only the first shows; links open in the in-app browser — [TechCrunch 2023](https://techcrunch.com/2023/04/18/instagram-takes-on-linktree-and-others-with-support-for-up-to-5-links-in-bio/); [Search Engine Land](https://searchengineland.com/instagram-now-allows-up-to-5-links-in-bio-395742)
- **TikTok Shop:**
  - 2026 country lists (about 25 live markets as of Feb 2026, across SE Asia, North America, Europe and the Middle East) contain no African market — [PhotonPay 2026](https://www.photonpay.com/hk/blog/article/tiktok-shop-available-countries); [TT Calculator](https://ttcalculator.net/blog/tiktok-shop-expansion-2026/)
  - EU expansion to Austria, Belgium, the Netherlands and Poland from 15 June 2026 — [Global Dating Insights](https://www.globaldatinginsights.com/featured/tiktok-expands-tiktok-shop-to-four-new-eu-countries/)
- **TikTok in SA, 1 Oct 2026:** TikTok launched "TikTok One Creator Marketplace" in SA, for brand-creator paid collaborations. The Creator Rewards Programme is "again not available in South Africa". The article does not mention TikTok Shop — [Business Day, 1 Oct 2026](https://www.businessday.co.za/companies/2026-10-01-tiktok-hopeful-about-new-monetisation-platform-for-local-creators-and-influencers/)
- **TikTok bio link:** a clickable website link requires 1,000+ followers or a Registered Business Account. Sources conflict on whether business accounts also need 1,000 followers. Mobile app only — [Stan Store 2026 guide](https://stan.store/blog/tiktok-link-bio-requirements-2026-guide/); [Captions.ai Apr 2025](https://www.captions.ai/blog-post/how-to-add-link-to-tiktok-bio)
- **WhatsApp:**
  - Catalogues can be set up by SA businesses — [SME South Africa](https://smesouthafrica.co.za/setting-up-whatsapp-business-catalogues/)
  - No evidence of native WhatsApp in-chat payments in SA in 2026.
  - Third-party route: Peach Payments partnered with Sukhiba (Oct 2024) for WhatsApp catalogues with card, EFT and BNPL payments — [Daba Finance](https://dabafinance.com/en/news/peach-payments-partners-sukhiba-to-offer-whatsapp-based-sales-channel)

### Inferences
- **Product requirement:** each creator shop must be mobile-first and fast-loading in the Instagram/TikTok in-app browsers (no login wall, guest checkout, Apple Pay/Google Pay or Capitec Pay/instant EFT). Most traffic will come from bio links, Story link stickers and Reels captions, not native shopping surfaces.
- **Paid tagging:** MerchMe could sync a Meta catalogue to run product-tagged ads per creator. This is a paid, MerchMe-run channel, not organic.
- **TikTok risk:** creators under 1,000 followers on personal TikTok accounts may not get a clickable link. This affects the long-tail creator segment.

### Gaps
- TikTok Shop SA status was not found on an official TikTok source; absence is inferred from 2026 country lists.
- TikTok "Showcase" availability in SA was not researched.
- Meta's official current product-tagging country list was not retrieved.
- Instagram Story link sticker availability was not re-verified; it was believed available to all accounts since 2021, but not sourced here.

---

## T5. Order routing to POD partners, courier APIs and analytics

### Takeaway
SA courier integration is straightforward through aggregators. Bob Go (ex-uAfrica) connects The Courier Guy, Pargo, RAM, Skynet and others plus Bob Box lockers. The Courier Guy has a documented REST API on the Shiplogic platform, including locker/pickup-point endpoints. POD routing will be a custom webhook/API integration whose shape depends on the chosen SA printer.

### Cited Findings
- **Bob Go:** shipping and order-management platform, formerly uAfrica. Connects to more than 10 courier partners including The Courier Guy, Pargo, RAM, SkyNet and Internet Express.
  - Offers Bob Box locker/counter pickup at checkout.
  - Pay-as-you-go with no base subscription; shipments billed per booking — [Bob Go Shopify app](https://apps.shopify.com/bobgo?locale=es)
  - Its WordPress plugin advertises an open API and calls `api.bobgo.co.za/v2/order-fulfillments` — [Bob Go WordPress plugin](https://wordpress.org/plugins/bobgo-shipping/)
- **The Courier Guy Locker API (PDF, Aug 2025):**
  - `GET` pickup-points with locker/counter filter, lat/lng search within 20 km, or a bounding box.
  - Rates endpoint accepts a pickup-point ID as collection or delivery point — [TCG Locker API docs](https://thecourierguy.co.za/wp-content/uploads/2025/08/The-Courier-Guy-Locker-API-docs.pdf)
- The Shiplogic REST API (used by TCG) covers rate quotes, shipments, label PDFs, cancellation, tracking and webhooks. This comes from an unofficial SDK — [Shiplogic PHP SDK](https://root.packagist.org/packages/sonnenglas/shiplogic-php-sdk)
  - TCG provides sandbox and production credentials on request — [AfterShip/Postmen](https://support.postmen.com/en/article/get-credentials-to-access-the-courier-guy-shipping-api-8cz9mw)
- **PUDO:** a Shopify app offers live quotes and waybills; one reviewer reports API-key setup issues — [PUDO Shopify app](https://apps.shopify.com/pudo-1)
- **Printful API:** general rate limit 120 calls/min; 429 on exceed. Printful is an international POD and not a SA printer — [Jentic: Printful API](https://jentic.com/apis/printful)

### Inferences
- **Order flow:**
  1. The order is paid (gateway webhook).
  2. MerchMe creates a POD job: print file URL, SKU, size/colour and ship-to, via the printer's API, email/CSV or a simple printer portal if they have no API.
  3. The printer marks the job printed.
  4. MerchMe or the printer books a courier via Bob Go/Shiplogic.
  5. A tracking webhook updates the fan and creator dashboards.
- **SA printers:** many have no API, so plan to build a lightweight "printer portal" (job queue, print-file download, status buttons) as part of the MVP.
- **Creator analytics:** a per-creator dashboard (orders, revenue, profit share, payouts) plus UTM-tagged share links per channel (IG bio, IG Story, TikTok bio, WhatsApp). Optionally a Meta Pixel/Conversions API and TikTok Pixel on the shop domain, with POPIA-compliant cookie consent.

### Gaps
- Pargo API and official PUDO API docs were not retrieved.
- Courier rate cards were not retrieved.
- SA POD partners' API capabilities are not covered here (another workstream covers SA print/fulfilment).
- TikTok/Meta pixel and attribution API limits were not researched.

---

## T6. MVP cost and timeline benchmarks, SA developer rates, running costs

### Takeaway
SA contract developer rates cluster around R400–R650/hour for common stacks. Global marketplace MVP benchmarks are US$15k–80k (about R270k–R1.4m at about R18/USD) over 10–20 weeks with an agency. A no-code or plugin MVP is US$5k–20k. Monthly platform running costs for a custom stack start below US$100/month before payment fees and staff.

### Cited Findings
- **Indeed SA job-posting averages:**
  - Full-stack developer: about R584/hour (range R200–R900, 18 postings).
  - Python: about R621/hour.
  - .NET: about R432/hour — [Indeed ZA](https://za.indeed.com/cmp/Communicate-Recruitment/salaries/Full-Stack-Developer)
- Payscale: senior software engineer average base about R484.54/hour (2026; employee pay, may understate contract rates) — [Payscale](https://www.payscale.com/research/ZA/Job=Sr._Software_Engineer_%2F_Developer_%2F_Programmer/Hourly_Rate/5d9413ac/UNIX)
- WageIndicator: SA software developers R24,050–R78,949/month (2025) — [WageIndicator](https://acc.wageindicator.org/en-za/work-in-south-africa/role-and-pay/software-developers)
- Index.dev: African freelance developers US$20–55/hour (2025, not SA-specific) — [Index.dev](https://index.dev/blog/freelance-developer-rates-by-country)
- OfferZen ran its 6th "State of the Developer Nation" survey in 2025; no rate figures were retrieved — [OfferZen blog](https://www.offerzen.com/blog/hiring-tips-and-insights)
- Apptunix (vendor): SA app development R50,000 to R1,500,000+ — [Apptunix](https://apptunix.com/blog/mobile-app-development-cost-in-south-africa)
- **Global marketplace MVP benchmarks (2026):**
  - LowCode Agency: specialist team US$30k–80k; specialist agency US$50k–120k over 10–20 weeks; no-code setup US$5k–20k — [LowCode Agency](https://www.lowcode.agency/blog/marketplace-mvp-development-cost)
  - Creole Studios: basic marketplace MVP US$25k–50k — [Creole Studios](https://www.creolestudios.com/?p=36559)
  - Solguruz: simple MVP US$15k–40k — [Solguruz](https://solguruz.com/blog/mvp-development-cost)
- **Running-cost components (see T1/T2):** Supabase Pro about US$25–36/mo; Vercel Pro US$20/mo plus usage; Dynamic Mockups Pro US$15–19/mo; Sharetribe Live US$199–259/mo; Shopify Basic US$25/mo per store; Dokan US$149–999/yr.

### Inferences
- **Option A, plugin/no-code MVP** (WooCommerce + Dokan/WCFM + Paystack/PayFast + Bob Go, or a single Shopify store):
  - About 3–6 weeks.
  - About R60k–R200k at R400–R600/hour (150–330 hours), plus a design theme.
  - Running cost about R1k–R3k/month for hosting and plugins (estimate, not sourced).
  - Works for 10–50 pilot creators. Per-creator branding and auto-generated shops are limited.
- **Option B, custom MVP** (Next.js + Supabase + Paystack splits + mock-up API + printer portal + Bob Go + creator dashboard):
  - About 12–16 weeks with 2 developers plus a part-time designer.
  - About 1,000–1,300 hours × R500–R600/hour ≈ R500k–R780k.
  - Platform running cost about US$70–150/month (≈ R1.3k–R2.7k at R18/USD) before payment fees, email/SMS and support.
  - Consistent with the US$30k–50k global benchmarks.
- **Ongoing costs to budget:** a maintenance retainer (about 20–40 hours/month), Information Officer/POPIA compliance, accounting (VAT/turnover tax), and IP moderation labour. Moderation is likely the largest hidden operating cost.

### Gaps
- No SA-specific agency rate card or rand-denominated marketplace MVP quote was found.
- OfferZen 2025 freelance figures were not retrieved.
- WooCommerce hosting costs in SA were not sourced.

---

## L1. Consumer law: CPA (Act 68 of 2008) and ECTA (Act 25 of 2002)

### Takeaway
Fans get:
- A 7-day no-reason cooling-off under ECTA s44.
- A 6-month implied warranty for defective goods under CPA s55–56.
- Strict product liability across the supply chain under CPA s61.

The ECTA exemption for goods "made to the consumer's specifications" or "clearly personalised" (s42(2)(f)) probably does not cover catalogue POD merch, because the creator, not the fan, specifies the design. It would cover items the fan personalises (e.g. adds a name). **[CONFIRM: lawyer]**

### Cited Findings
- **ECTA s42(2)** (statute text): section 44 does not apply where the goods "(i) are made to the consumer's specifications; (ii) are clearly personalised; (iii) by reason of their nature cannot be returned; or (iv) are likely to deteriorate or expire rapidly". It also excludes auctions, financial services, newspapers/books and others — [ECTA, gov.za](https://www.gov.za/sites/default/files/gcis_document/201409/a25-02.pdf)
- **ECTA s43(2)–(3):** before the order is placed, the supplier must let the consumer review the entire transaction, correct mistakes and withdraw. If s43(1) or (2) is not complied with, the consumer may cancel within 14 days of receiving the goods — [ECTA, gov.za](https://www.gov.za/sites/default/files/gcis_document/201409/a25-02.pdf)
  - s43(1) requires a long list of website disclosures: supplier identity and legal status, physical address and contacts, registration number, description and full price including transport and taxes, payment method, delivery time, return/refund policy, privacy and security policies, cooling-off rights and more. The full list is in the Act; verbatim s43(1) text was not retrieved this session.
- **ECTA s44:** the consumer may cancel within 7 days of receiving goods without reason or penalty. The only permitted charge is the direct cost of returning the goods. The refund is due within 30 days of cancellation — [Evetech summary](https://evezone.evetech.co.za/quick-bytes/7-day-cooling-off-rule-online-tech-orders-sa); [MJK Inc](https://mjkinc.co.za/compliance/consumer-protection-act/cooling-off-and-cancellation)
- **ECTA s46** (performance): the order must be executed within 30 days unless otherwise agreed; otherwise the consumer may cancel on 7 days' notice. This is from the Act — [ECTA, gov.za](https://www.gov.za/sites/default/files/gcis_document/201409/a25-02.pdf). Verbatim text was not retrieved this session; confirm.
- **CPA s55/s56:** goods must be of good quality, free of defects, safe and reasonably suitable for purpose. The consumer may return defective goods within 6 months for repair, replacement or refund — [BusinessTech](https://businesstech.co.za/news/black-friday/533814/8-laws-you-should-know-before-buying-anything-during-black-friday-in-south-africa-including-returns-and-refunds/); [Van Deventers](https://vandeventers.law/legal-articles/entryid/2076/is-a-refund-always-possible-consumer-protection)
- **CPA s16:** a 5-business-day cooling-off for agreements resulting from direct marketing, by written notice. It does not apply where ECTA s44 applies — [BusinessTech](https://businesstech.co.za/news/black-friday/533814/8-laws-you-should-know-before-buying-anything-during-black-friday-in-south-africa-including-returns-and-refunds/)
- **CPA s61:** producers, importers, distributors and retailers are strictly, jointly and severally liable for harm caused by unsafe or defective goods or inadequate warnings, without proof of negligence. Distributors and retailers have a s61(4)(c) defence where it was unreasonable to expect them to discover the hazard — [Pieterse v Organic Synthesis [2024] ZAGPPHC 1142](https://lawlibrary.org.za/akn/za-gp/judgment/zagpphc/2024/1142/eng@2024-11-14); [Mondaq "Strictly speaking"](https://www.mondaq.com/southafrica/product-liability-safety/172162/strictly-speaking)

### Inferences
- **Who is the supplier:** if MerchMe is the seller of record (principal model), MerchMe is the "supplier" under both Acts and owns returns, warranty and product liability. The creator is a licensor. The POD partner is a producer jointly liable under s61. MerchMe should take back-to-back warranties and indemnities from the printer.
- **Cooling-off returns:**
  - Assume ECTA s44 applies to standard catalogue merch. Budget for change-of-mind returns; the fan pays only the direct return cost.
  - Returned POD items usually can't be resold, so price in a returns allowance.
  - Only rely on s42(2)(f) for genuinely personalised items, such as fan-added names, and disclose this clearly before checkout.
- **Checkout compliance:** build s43 disclosures into the site footer/T&Cs and an order-review step (review, correct, withdraw). Non-compliance extends the cancellation right to 14 days.
- **Fulfilment SLA:** keep POD and shipping within 30 days (s46). Show realistic production times.

### Gaps
- No SA case or Consumer Commission guidance was found on whether POD/catalogue-customised goods are "made to the consumer's specifications".
- Whether a platform operator (as distinct from the seller) falls within CPA s61 is unresolved in the sources.
- The CPA s20 (return of goods) interaction was not separately researched.

---

## L2. POPIA (Act 4 of 2013): fan and creator data, Information Officer, cross-border transfers

### Takeaway
MerchMe must:
- Register its Information Officer (by default the CEO/MD) with the Information Regulator via eServices before processing.
- Get opt-in consent for electronic direct marketing. **[CHANGED since 2024]** The 2025 Regulations amendments confirm that opt-out is not consent.
- Have a s72 basis (usually binding operator agreements) for storing data on foreign cloud services (Supabase, Vercel, Meta/TikTok pixels).
- Take care with fans under 18.

### Cited Findings
- **s55 Information Officer:** public and private bodies must register their Information Officers (and deputies) with the Regulator before they take up duties, via the Regulator's eServices portal — [Michalsons: Information Officer](https://www.michalsons.com/blog/information-officer/12231); [Michalsons: how to register](https://www.michalsons.com/blog/faq-items/how-do-i-register-my-information-officer-with-the-regulator)
  - Michalsons says failure to register is not itself a criminal offence but carries "severe consequences".
  - In a 2026 enforcement action, the Regulator ordered Central Johannesburg TVET College to register an IO and deputy within 31 days — [Michalsons enforcement note](https://www.michalsons.com/blog/central-johannesburg-tvet-college-enforcement-action-popia-breaches/82050)
- **Penalties:** the Regulator warned (2021) that non-compliance with certain provisions can lead to administrative fines up to R10 million and/or imprisonment up to 10 years — [SAnews](https://www.sanews.gov.za/index.ph%70/node/51130)
- **s69 direct marketing:** unsolicited electronic direct marketing (email, SMS, WhatsApp) requires prior consent, or an existing customer under specific conditions; data subjects may object at any time — [Covington, Global Policy Watch, Dec 2024](https://www.globalpolicywatch.com/2024/12/long-awaited-popia-guidance-on-direct-marketing-published-by-south-africas-information-regulator/); [Information Regulator guidance note](https://inforegulator.org.za/wp-content/uploads/2020/07/GUIDANCE-NOTE-ON-DIRECT-MARKETING-IN-TERMS-OF-THE-PROTECTION-OF-PERSONAL-INFORMATION-ACT-4-OF-2013-POPIA.pdf)
- **[CHANGED since 2024]** Amended POPIA Regulations (from 17 April 2025): "For the purposes of direct marketing through unsolicited electronic communications, opt-out shall not constitute consent as referred to in section 69 (2) of the Act." — [MJK Inc: 2025 amendments](https://mjkinc.co.za/popia/regulations-2025-amendments); [Information Regulator: amended regulations PDF](https://inforegulator.org.za/wp-content/uploads/2025/04/POPIA-2021-Regulations-FINAL-21-Jan-2025.pdf)
- **s72 cross-border transfers:** personal information may not be sent to a foreign third party unless the recipient is subject to adequate protection (law, binding corporate rules or binding agreement), the data subject consents, the transfer is necessary for a contract, or another ground applies.
  - Foreign cloud hosts are typically "operators" needing s19–21 security and operator contracts.
  - Transfers of children's information may need the Regulator's prior authorisation — [CMS](https://cms.law/en/zaf/legal-updates/Managing-cross-border-data-transfers); [Michalsons: transfers outside SA](https://www.michalsons.com/focus-areas/privacy-and-data-protection/transfers-of-personal-information-outside-south-africa); [MJK Inc: cross-border agreement](https://mjkinc.co.za/agreements/cross-border-data-transfer-agreement)

### Inferences
- **Data MerchMe will hold:**
  - Fans: name, address, phone, email, order history, pixel/cookie data.
  - Creators: ID number for KYC, bank details, tax number, address.
  - Creator bank and ID data is higher-risk; restrict access and encrypt.
- **Practical checklist:**
  1. Register the IO and a deputy.
  2. Publish a privacy notice (s18) and PAIA manual.
  3. Use opt-in checkboxes at checkout for marketing from MerchMe and, separately, from the creator. Sharing fan data with creators for their own marketing is a separate purpose and needs its own consent.
  4. Sign operator agreements/DPAs with Supabase, Vercel, Paystack/PayFast, Bob Go, the POD partner, and email/SMS providers.
  5. Choose an EU or SA region for hosting where possible.
  6. Get cookie/pixel consent.
  7. Have a breach-notification process (s22).
  8. Set a policy for under-18 fans, e.g. require 18+ to create accounts or obtain guardian consent.

### Gaps
- Exact current POPIA penalty provisions were not checked against the Act.
- The Information Regulator's position on whether every private body must register, and the current eServices process, was not verified on inforegulator.org.za this session.
- s22 breach notification and the new e-portal breach-reporting requirements (2025) were not researched.

---

## L3. IP: copyright, trade marks, likeness, takedowns and creator contracts

### Takeaway
The biggest legal risk is creators uploading designs that infringe third-party copyright or trade marks (band logos, sports/club badges, cartoon characters, celebrity photos, sampled imagery). Physical counterfeit merch can trigger criminal liability under the Counterfeit Goods Act. MerchMe very likely cannot rely on ECTA's hosting safe harbour, because:
- (a) the safe harbour requires membership of a recognised industry representative body and adoption of its code; and
- (b) MerchMe itself reproduces and sells the physical goods.

SA has no fair-use defence yet. The Copyright Amendment Bill is still not law after the Constitutional Court's 2026 ruling.

### Cited Findings
- **ECTA s72** (statute text): "The limitations on liability established by this Chapter apply to a service provider only if— (a) the service provider is a member of the representative body referred to in section 71; and (b) the service provider has adopted and implemented the official code of conduct of that representative body." — [ECTA, gov.za](https://www.gov.za/sites/default/files/gcis_document/201409/a25-02.pdf)
  - Only those service providers that belong to a recognised IRB get the protection — [Obiter article](https://obiter.mandela.ac.za/article/download/12231/17215/73096)
  - ISPA is a recognised IRB. A member that doesn't act on a take-down notice loses the ECTA liability limitations for that content — [ISPA statement on take-downs](https://ispa.org.za/press-releases/covid-19-shines-spotlight-on-website-take-downs/); [Michalsons: take-down notices, updated Dec 2022](https://www.michalsons.com/blog/take-down-notice-take-down-procedure/2745)
- **ECTA s75 hosting:** a service provider must act expeditiously to remove or disable infringing content on notice, or it loses immunity for hosted content — [Ellipsis](https://www.ellipsis.co.za/isp-issues/limitation-of-liability-for-isp-activites/)
- **ECTA s77 take-down notice formalities:**
  - In writing and signed.
  - Complainant's full name and contact details.
  - Identify the right infringed and the material concerned.
  - State the remedial action required.
  - Good-faith statement that the information is true.
  - A person who knowingly and materially misrepresents facts is liable for damages for wrongful take-down — [Michalsons](https://www.michalsons.com/blog/take-down-notice-take-down-procedure/2745)
  - Copyright and trade-mark claims are the leading category of ISPA take-downs — [ISPA](https://ispa.org.za/?p=5682)
- **ECTA s78:** no general obligation to monitor — [ISPA ECTA Amendment Bill submission](https://ispa.org.za/wp-content/uploads/2012/06/ISPA_Submission_ECTA_Amendment_Bill_20121207.pdf)
- **[CHANGED since 2024] Copyright Amendment Bill:**
  - The Constitutional Court ruled on the President's referral of the Copyright Amendment Bill [B13F-2017] and Performers' Protection Amendment Bill [B24F-2016]: Ex parte President... [2026] ZACC 26, 26 June 2026 per one summary.
  - Only proposed s12D(1)–(5) (educational/academic reproduction) were held unconstitutional, as arbitrary deprivation of property.
  - Parliament must replace only those provisions, with the Portfolio Committee limiting its review to them — [Acts Online, 9 Jul 2026](https://acts.co.za/news/blog/2026/07/concourt-ruling-copyright-performers-protection-bills); [Knowledge Gov](https://knowledgegov.org/?p=6547); [GoLegal](https://www.golegal.co.za/constitutional-court-copyright/)
  - One summary says most provisions, including fair use, were found constitutional — [IIPLA](https://iipla.org/news/south-africa-s-constitutional-court-ruling-on-copyright-bill-signals-ongoing-reform-challenges)
  - Commentators agree neither bill can be enacted in its current form. Summaries conflict on how much was upheld — [GoLegal](https://www.golegal.co.za/court-copyright-amendment-bill/)
- **Counterfeit Goods Act 37 of 1997:**
  - Lets owners of registered trade marks, copyright and Merchandise Marks Act marks act against counterfeits.
  - Inspectors may enter, search and seize. Possessing, or publicly displaying for trade, counterfeit goods is an offence.
  - Customs can seize suspect imports on the IP owner's application — [World Trademark Review](https://www.worldtrademarkreview.com/global-guide/anti-counterfeiting-and-online-brand-enforcement/2019/article/procedures-and-strategies-anti-counterfeiting-south-africa); [Acts Online](https://www.acts.co.za/counterfeit_goods_act__1997)
  - Enforcement is active: a 2026 Johannesburg CBD raid seized more than 1,700 counterfeit Springbok items worth R1.5m — [Briefly](https://briefly.co.za/people/252202-saps-seizes-1700-fake-springbok-items-worth-r15-million-joburg-cbd-raid/)
  - Clubs such as Kaizer Chiefs act through trade-mark lawyers — [Kaizer Chiefs](https://kaizerchiefs.com/news/chiefs-marketing-acts-on-counterfeits)
- **Personality / image rights:**
  - Grütter v Lombard (SCA) recognised a person's identity/image as a protectable aspect of personality.
  - Wells v Atoll Media (WCHC 2009) held that using a person's image for commercial gain without consent infringes the right to identity — [SAFLII PER 2011](https://www.saflii.org/za/journals/PER/2011/47.html); [SciELO SA](https://scielo.org.za/scielo.php?script=sci_arttext&pid=S1727-37812011000200009)

### Inferences
- **Safe harbour:** MerchMe is not a classic ISP. Even if it joined ISPA, the s75 hosting protection covers hosting information, not manufacturing and selling physical goods bearing infringing artwork. Treat MerchMe as directly exposed as seller/reproducer. **[CONFIRM: IP attorney, e.g. Adams & Adams, Spoor & Fisher, ENSafrica]**
- **No fair use:** the Copyright Act 98 of 1978 (fair dealing only) remains operative until the amendment bill is re-passed and signed. Fan art, parody and "inspired by" designs of copyrighted characters are not safe.
- **Mitigations:**
  1. **Creator terms:**
     - Creator warrants they own or have licensed all elements, and that no third-party marks, logos, likenesses or samples are used without written permission.
     - Creator indemnifies MerchMe; profit share withheld or clawed back on valid claims.
     - Non-exclusive, worldwide, royalty-bearing licence to MerchMe to reproduce on listed products and in marketing, terminable on notice, with a sell-off period.
     - Creator keeps ownership.
  2. **Pre-publication moderation:** banned-content list (sports/club badges, brands, cartoon characters, celebrity images, other artists' album art), reverse-image or AI similarity checks, manual review for new creators.
  3. **Public IP complaints process:** mirror s77 formalities, take down within 24–48 hours, counter-notice, repeat-infringer termination, and hold payouts on disputed SKUs.
  4. Consider IP/media liability insurance.
  5. **Help creators protect their own work:** copyright arises automatically. Encourage creators to keep dated source files. Offer trade-mark registration guidance (CIPC) for their brand names/logos.
- **Musicians:** album artwork, label logos and photos by third-party photographers are often owned by labels or photographers, not the artist. Require proof of rights for these.

### Gaps
- Trade Marks Act 194 of 1993 specifics (s34 infringement, well-known marks) were not retrieved this session.
- Whether the Copyright Act's moral rights (s20) can be waived by contract in SA was not verified.
- The definition of "service provider" in ECTA s70, and whether e-commerce platforms can join ISPA, were not confirmed.
- No SA case on POD platform liability for user-uploaded designs was found.

---

## L4. Tax: VAT, principal vs agent, creator payouts, non-residents, company structure, turnover tax

### Takeaway
**[CHANGED since 2024]** From 1 April 2026:
- The compulsory VAT registration threshold rose from R1m to R2.3m of taxable supplies per 12 months.
- The voluntary threshold rose from R50k to R120k.
- The turnover-tax ceiling also rose to R2.3m.
- SARS is administering the new thresholds although the amendments were not yet promulgated when its FAQ was issued.

The VAT rate stays 15%. MerchMe's VAT position depends on whether it is principal (seller of goods, paying creators a royalty) or agent (selling on creators' behalf under s54). A 75% platform share points strongly to principal treatment.

### Cited Findings
- **SARS Budget 2026 FAQ (published 20 Mar 2026, updated 12 Aug 2026):**
  - Compulsory VAT registration when taxable supplies exceed "R2.3 million per annum (increased from R1 million)".
  - Voluntary registration above "R120 000 per annum (increased from R50 000)".
  - Effective 1 April 2026.
  - "Although the amendments have not yet been promulgated, the Minister of Finance announced these amendments to be effective from 1 April 2026. SARS is therefore administering new VAT registration applications on the increased threshold with effect from 1 April 2026." — [SARS Budget 2026 FAQ](https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/)
- Businesses below the new threshold may apply to deregister, but deregistration can trigger deemed output tax — [Cliffe Dekker Hofmeyr, 19 Mar 2026](https://www.cliffedekkerhofmeyr.com/en/news/publications/2026/South-Africa/Tax-Exchange-Control/tax-and-exchange-control-alert-19-march-VAT-threshold-increased-Should-SMEs-remain-registered)
- The R1m threshold had been unchanged since 2009; the VAT rate remains 15% — [Daily Investor](https://dailyinvestor.com/finance/121587/big-vat-win-for-south-african-businesses/); [Forvis Mazars](https://www.forvismazars.com/za/en/services/tax/tax-insights/why-small-businesses-are-breathing-again)
- **Turnover tax (SARS FAQ):** "The threshold for Turnover Tax will also increase to R2.3 million from 1 April 2026." 2026/27 rates:

  | Turnover band | Tax |
  |---|---|
  | R0–R600,000 | 0% |
  | R600,001–R950,000 | 1% above R600k |
  | R950,001–R1.4m | R3,500 + 2% above R950k |
  | Above R1.4m | R12,500 + 3% above R1.4m |

  — [SARS Budget 2026 FAQ](https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/)
- **Small business corporation (gross income ≤ R20m), years ending 1 Apr 2026–31 Mar 2027:**

  | Taxable income | Tax |
  |---|---|
  | R0–R99,000 | 0% |
  | R99,001–R365,000 | 7% above R99k |
  | R365,001–R550,000 | R18,620 + 21% |
  | R550,001+ | R57,470 + 27% |

  — [SARS Budget 2026 FAQ](https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/)
- **Provisional tax (SARS FAQ):** "You are a provisional taxpayer if you earn income that is not remuneration (e.g. … business income …)". Exempt only if no business is carried on and taxable income is under the R99,000 threshold (or other narrow conditions). Underestimation penalty 20%; late payment 10% — [SARS Budget 2026 FAQ](https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/)
- **VAT s54 agency:** a supply by an agent on behalf of a principal is deemed made by the principal, not the agent — [Van Deventers](https://vandeventers.law/legal-articles/entryid/1211/section-54-of-the-vat-act-south-africa-explained); [Tax Faculty](https://taxfaculty.ac.za/news/read/vat-agency-and-principals-2)
  - s54(2B) intermediary rules apply mainly to electronic services and were amended from 1 April 2025 — [Deloitte](https://www.deloitte.com/za/en/services/tax/analysis/vat-principles-for-principals-clarity-needed-to-enhance-compliance.html); [RSM](https://www.rsm.global/southafrica/node/1170)
  - No SA source applies s54 to a physical-goods marketplace. In Kenya's Sendy case, a "platform only" argument failed at the Tribunal (on appeal) — [Mondaq](https://webiis08.mondaq.com/southafrica/tax-authorities/1711902/kenya-%7c-commissioner-of-domestic-taxes-vs-sendy-limited)
- **Independent contractors:** amounts paid to someone carrying on an independent trade are not "remuneration", so the payer has no duty to withhold employees' tax (PAYE). SARS applies statutory and common-law tests — [SARS Interpretation Note 17 summary, GoLegal](https://www.golegal.co.za/?p=27318)
  - Contractors must register as provisional taxpayers and file ITR12 — [TaxTim](https://www.taxtim.com/za/answers/tax-liability-for-an-independent-contractor); figures on that page may be outdated.
- **Withholding tax on royalties (non-resident creators):**
  - 15% on royalties paid on or after 1 January 2015.
  - "Royalty" includes payments for the use of, or right to use, intellectual property as defined in s23I.
  - The SA payer withholds; the foreign person is liable.
  - Treaty relief requires the foreign creator to give a WTRD declaration; without one, 15% applies.
  - Interpretation Note 116 covers ss49A–49H — [SARS: withholding tax on royalties](https://www.sars.gov.za/types-of-tax/withholding-tax-on-royalties/); [SARS IN116](https://www.sars.gov.za/intr-in-2021-03-in-116-withholding-tax-on-royalties)

### Inferences
- **Principal model (recommended):**
  - MerchMe sells the merch to fans; its turnover is the full retail price.
  - Once retail sales exceed R2.3m in any 12 months (about R192k/month), VAT registration is compulsory. Registering voluntarily from R120k lets it claim input VAT on POD and courier costs from VAT-registered suppliers.
  - The creator's 25% is a royalty/licence fee for using the design. Creators earning under R2.3m don't register for VAT; if a creator is a VAT vendor, MerchMe pays VAT on top and claims it back if registered.
- **Agent model:**
  - Each creator would be the seller, and VAT on goods sits with each creator, mostly non-registered.
  - MerchMe's VAT supply would be its commission, but a 75% commission plus MerchMe controlling pricing, printing and fulfilment makes this characterisation fragile. It also puts CPA "supplier" duties on each creator.
  - **[CONFIRM: tax advisor]**
- **Creator payouts:**
  - No PAYE on royalty payouts to independent creators.
  - Creators must declare the income and will often be provisional taxpayers.
  - MerchMe should collect each creator's tax number, issue monthly statements and send year-end earnings summaries for creators' own returns.
- **Non-resident creators** (e.g. a Namibian or UK artist): withhold 15% royalty WHT unless a WTRD supports a treaty rate. File WTR01 returns. Also consider exchange-control/BoP reporting via the bank for foreign payouts.
- **Company structure:**
  - Pty Ltd (CIPC) is the default for investors and liability.
  - At a profitable early stage, a qualifying small business corporation pays 0–27% graduated rates.
  - Turnover tax (up to R2.3m turnover) may suit year 1 if eligible. Turnover tax is generally incompatible with flexibility for a growth startup; check the eligibility rules (shareholder types, investment income, professional services).

### Gaps
- Final enactment status of the R2.3m threshold (Taxation Laws Amendment) as of October 2026 was not confirmed beyond SARS administering it.
- IT3(a) or other third-party reporting duty for royalty payouts to SA residents was not found. The IT3(a) is designed for remuneration, which royalties are not; confirm with an accountant.
- Whether a 25%-of-profit design payment is legally a "royalty" (s23I includes designs and copyright) rather than a service fee is assumed, not confirmed.
- Turnover tax eligibility conditions and CIPC registration costs were not researched in this session.

---

## L5. Financial regulation: does collecting fan payments and paying creators require SARB/PASA authorisation?

### Takeaway
Under current rules (SARB Directive 1 of 2007), a business that regularly accepts payments from multiple payers on behalf of a beneficiary, or disburses to multiple parties on a client's behalf, must register as a Third-Party Payment Provider (TPPP) with PASA through a sponsoring bank. There is no PASA fee and it takes about 21 working days.

**[CHANGED since 2024]** SARB is replacing this with an activity-based Authorisation Framework. The third draft was published 21 May 2026, comments closed 15 June 2026, and finalisation was targeted for Q3 2026. Its authorisation triggers are linked to transaction volumes.

MerchMe can largely avoid TPPP status by either:
- (a) being the principal seller and paying creators royalties from its own revenue; or
- (b) using a licensed gateway's split product, so funds flow directly from the gateway to the creator's account.

**[CONFIRM: payments lawyer]**

### Cited Findings
- **PASA TPPP rule:** you must register with PASA through a sponsoring bank if you "accept payments from multiple parties for your client, or disburse payments to multiple parties for your client". Registration is compulsory for services under SARB Directive 1 of 2007.
  - The sponsoring bank submits the application; no PASA fee; 21 working days after complete documents.
  - Page published Jul 2024, modified Nov 2025 — [PASA TPPP registration](https://authorisation.pasa.org.za/so-and-tppp/tppp-registration)
- **SARB draft framework (first draft, 3 March 2025):** the Draft Directive on payment activities plus a Prudential Authority Exemption Notice cover authorisation, governance, prudential, fit-and-proper, client-fund safeguarding, data protection and reporting requirements for banks and non-banks. Persons conducting TPPP activities "will be exempt from several significant requirements" — [Bowmans, 17 Mar 2025](https://bowmanslaw.com/insights/the-south-african-reserve-bank-has-recently-published-a-draft-activity-based-authorisation-framework-for-participants-banks-and-non-banks-in-the-national-payment-system/); [SARB draft PDF](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/consultation-documents/2025-comment-documentation/Draft%20Authorisation%20Framework%20-%203%20March%202025%20-%20sent%20to%20industry.pdf)
- **Third draft (Webber Wentzel, 21 May 2026):**
  - Comments due 15 June 2026; SARB indicated final publication in Q3 2026.
  - Proportionate approach, with "the trigger to apply for authorisation being linked to transaction volumes over specific periods".
  - Domestic activities only; cross-border excluded.
  - Definitions: a TPPP provides "third-party payment" services, meaning acceptance of money "as a regular feature of business from any other person, for the purpose of making payment on behalf of that other person to a third party to whom that payment is due".
  - A "payer service provider" accepts money from a payer to pay multiple beneficiaries.
  - "Money remittance" includes funds "received on behalf of, and made available to, the payee" — [Webber Wentzel](https://www.webberwentzel.com/News/Pages/south-africas-payments-regulatory-framework-third-draft-of-authorisation-framework-published-for-comment.aspx); [Polity, 22 May 2026](https://www.polity.org.za/article/south-africas-payments-regulatory-framework-third-draft-of-authorisation-framework-published-for-comment-2026-05-22)

### Inferences
- **Principal model:** fans pay MerchMe for MerchMe's own goods; MerchMe later pays creators a contractual royalty from its own funds. That is a payment of MerchMe's own debt, not a payment "on behalf of" fans to creators. It should fall outside TPPP and money-remittance definitions. This is the cleanest structure.
- **Agent/marketplace model with MerchMe holding funds:** collecting fans' money "on behalf of" creators (beneficiaries) and then remitting it looks like a beneficiary-side TPPP, or "money remittance" under the new framework. That would need PASA registration via a sponsoring bank now, and possibly SARB authorisation once the final framework and its volume thresholds apply.
- **Gateway split products** (Paystack subaccounts, PayFast split): the regulated gateway receives and settles directly to each creator's account. MerchMe never holds creators' money, which reduces MerchMe's exposure. The trade-off is creator KYC friction.
- **FICA:** a merch retailer is not an "accountable institution" under FICA. However, gateways will apply FICA/KYC to MerchMe and to any creator subaccounts. Unverified; confirm.
- **Action:** before launch, get a short opinion from a payments lawyer (e.g. Webber Wentzel, Bowmans, ENSafrica fintech teams) on the chosen flow, and check whether the SARB framework has been finalised since Q3 2026.

### Gaps
- Whether the SARB Authorisation Framework was published in final form by October 2026 is unknown; no final version was found.
- The volume thresholds in the third draft were not retrieved.
- FICA accountable-institution status was not verified against Schedule 1 of FICA.

---

## L6. Advertising and influencer disclosures (ARB Code)

### Takeaway
The ARB's Social Media Code is **Appendix K** of the Code of Advertising Practice (not Appendix J), in force since 2019. It requires clear and prominent disclosure of any material connection (payment, free product, discount, loan of goods) between an influencer and a brand. Brand and influencer can both be in breach. The CPA s41 also prohibits deceptive omission of material facts.

### Cited Findings
- **ARB Appendix K:** any material connection must be clearly and prominently disclosed. Clause 3 is the disclosure duty; clause 4 covers goods or services given for coverage even without a formal agreement — [MJK Inc influencer agreement](https://mjkinc.co.za/agreements/influencer-agreement); [Advantage magazine](https://advantagemagazine.co.za/influencer-marketing-south-africa/)
- **IAB SA Influencer Marketing Disclosure Toolkit (2026):**
  - Paid social must be "obviously identifiable", with an identifier inside the post content.
  - Free products, discounts, event invites or exclusive access count as connections.
  - If the influencer fails to disclose and the brand didn't exercise adequate oversight, both may breach the Code — [IAB SA toolkit 2026](https://iabsa.net/wp-content/uploads/2022/03/Influencer-Marketing-Disclosure-Tool-Kit-2026-1.pdf)
- **Castle Lager ruling (2026 commentary):** a branded post on a personal X account without "#ad"/"#sponsored" was considered. A commercial relationship can't be compartmentalised by moving branded content to a "personal" account — [Polity, 26 Aug 2026](https://www.polity.org.za/article/when-is-a-personal-post-actually-an-advertisement-2026-08-26); [Bizcommunity](https://www.bizcommunity.com/article/when-is-a-personal-post-actually-an-advertisement-742722a)
- **CPA s41:** failure to disclose a material fact can amount to deception — [Bizcommunity](https://www.bizcommunity.com/article/when-is-a-personal-post-actually-an-advertisement-742722a)

### Inferences
- **Own-merch posts:** a creator promoting their own merch has an obvious commercial interest. A clear "my merch / shop link" is low risk, but best practice is a visible tag (e.g. "#ad" or "my store") because MerchMe earns from the sale.
- **Disclosure required:** where MerchMe pays creators, gives free samples, runs referral bonuses, or has creators promote other creators' products or MerchMe itself, disclosure is required. MerchMe, as the "brand", should include a disclosure clause in creator terms and monitor compliance, since the brand can be jointly in breach.
- **Further rules for MerchMe's own ads:** these must comply with the ARB Code generally, including truthful pricing, delivery and "limited edition" claims. They must also comply with CPA s29–s41 on marketing and with POPIA s69 for electronic marketing.

### Gaps
- The Appendix K text was not read directly; the claim that it requires a written influencer contract is unconfirmed.
- ARB jurisdiction over non-members was not researched. The *Bliss Brands* litigation on this point exists but was not verified this session. It is relevant to how binding ARB rulings are on non-member creators.
