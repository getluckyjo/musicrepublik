# Kickoff run-sheet: Stations 0–5, tailored to Julien

About **90 minutes**. One station at a time. Show each one working before moving
on. He does four things: click settings, approve pop-ups, answer questions,
look at what we built. Nothing else.

| | Station | Time | Leaves with |
|---|---|---|---|
| 0 | What are you building? | 10 min | His priority, in his words |
| 1 | Switch on your tools | 15 min | One connector live and used on real data |
| 2 | Teach Claude your business | 20 min | `julien-voice` skill uploaded and tested |
| 3 | Ship something real | 30 min | A live link, and one change made while he watches |
| 4 | Set up your project | 10 min | Two Projects with his brand in them |
| 5 | Your first week | 5 min | Three specific things to try |

If time runs short, protect **2 and 3**. They need nothing external and carry
the session.

---

## Station 0: What are you building? (10 min)

We know the businesses, so don't ask him to explain them. Play it back and ask:

> "Music Republik for promotion and advisory, MerchHaus for merch and corporate
> apparel, both about five months old. Have I got that right?"

Then the two questions:
1. **Which of the two needs the most help in the next three months?**
2. **What's the one thing you'd love to get off your plate?**

Listen for these, because they decide Stations 1 and 3:
- "Admin and email" → Gmail
- "Never sure where the cash is across both companies" → Xero, dashboard
- "Need more corporate clients" → MerchHaus one-pager
- "Pitching a government or an emerging-market promoter" → pitch site
- "Forecasting merch orders" → small tool

## Station 1: Switch on your tools (15 min)

⚠️ **Check first:** is julien@musicrepublik.com on Google Workspace? If he's on
Microsoft 365, the Gmail, Calendar and Drive connectors won't see his work
account. Go to Xero, or fall back to Calendar on a personal Google account.

**Default pick: Gmail** (two businesses' enquiries landing in one inbox).
**Switch to Xero** if Station 0 was about the numbers. For an accountant it
will probably land harder.

Demo prompts, all run on his real data straight after connecting:
- Gmail: *"Who emailed me in the last two weeks about a tour, merch or corporate
  apparel and hasn't had a reply? Draft a one-line follow-up for each."*
- Xero: *"What's the cash position, and who owes us money and for how long?"*
  If he has both companies in Xero, run it for both.
- Calendar: *"What does show week look like, and where are the free 90-minute blocks?"*

Say out loud: reading is free and doing gets asked about; he can revoke access
any time; and emails from strangers are treated as information, not instructions.

## Station 2: Teach Claude your business (20 min)

Draft is ready: [`setup/julien-voice/SKILL.md`](../../setup/julien-voice/SKILL.md).
The business sections and the personal-register voice are done. **Only ask what's missing:**

- **Q4:** Who do you write to most: agents, corporates, promoters, suppliers, your team?
- **Q5:** What's your sign-off?
- **Q6:** Anything that makes you cringe in your own writing?
- **Q7:** Do you write in Afrikaans as well? Do you mix languages?
- **Q8, the one that matters:** paste one real email to an agent or client, and one WhatsApp.
- **Check:** "Commercial conclusions — not opinions" and the other site lines.
  Are those yours or the web agency's?

Fill the TODOs, delete what's still empty, then install it the easy way: **new
chat → "create a skill for me" → paste the text.** Test immediately on something
real he has to write this week.

## Station 3: Ship something real (30 min)

He already has a good Music Republik site, so **don't build another one.** Offer
what fits his Station 0 answer:

**A. MerchHaus one-pager (my pick).** He has nothing live for MerchHaus, and
corporate apparel buyers need a link. Customer-facing, so **Vercel**.
- *Who opens it:* corporate marketing and procurement (apparel and
  activations), promoters, and international merch companies. *Action:*
  email or WhatsApp.
- *Three things:* the full operation from range plan to on-site retail; the
  track record with the biggest tours to reach SA; corporate apparel done to
  tour standard.
- *Numbers to lead with:* 15+ years · 30–35 arena and stadium tours · show-day
  teams up to 50 · Metallica, U2, Rihanna, Elton John… (confirm he can name them).
  Keep the 24.6% IRR off it: that's an investor number, not a client one.
- *Feel:* ask him.

**B. Merch forecast tool.** Attendance × conversion × spend per head →
units by product and size, stock float, staffing, margin after venue commission and
royalties. His spreadsheet logic as something he can use on a phone at a
settlement. Internal, so build it as an **artifact**. Use his numbers only, never ours.

**C. Pitch site for one advisory prospect.** For example a tourism authority or
an emerging-market promoter. Use it if Station 0 surfaces a live deal.

**D. Dashboard across both businesses.** Cash, pipeline, upcoming shows. An
**artifact**, live off Xero. Best fit if he lit up at the Xero demo.

Ask for his brand as an upload: logo, show photos, colours. For anything
Music Republik, the colours are already captured (`#0F0F0F`, gold `#CAB06D`,
`#F0ECE0`, Archivo Narrow headings). Then **change one thing and redeploy while
he watches.** Don't skip it.

Vercel free tier is meant for non-commercial use, so tell him straight that a
business site may need a paid plan, and get an explicit yes before any domain.
MerchHaus domain: check .co.za availability, and note that merchhaus.com is
taken by a US company.

## Station 4: Set up your project (10 min)

Drafts: [`setup/project-instructions.md`](../../setup/project-instructions.md).
Two Projects, Music Republik and MerchHaus. Put the brand assets from Station 3
in the right one. Start a chat inside and show him it already knows.

**Layer 2** (Claude Code on the web → GitHub → Vercel): offer it in one line
only if he shipped A or C and will keep changing it. A clean "not yet" is fine.

## Station 5: Your first week (5 min)

Recap in four lines, then **three things to try**. Drafts below; rewrite them
from what he actually said:

1. *"Draft follow-ups to every agent, promoter or corporate who emailed in the
   last fortnight and hasn't heard back from me."*
2. *"Here's last tour's merch report. Build me a forecast for [next show] and
   tell me where I'm being optimistic."*
3. *"Turn [this week's show or deal] into a LinkedIn post in my voice."* The
   blog has been quiet since May; his posts are his best marketing.

Close by booking the next session before he leaves, and agree the one thing
he'll bring to it. Update [`progress.md`](../../progress.md) the same day.
