# Project briefs

One-page pitches ready to send to a coordinator or capstone instructor. Each lists the problem, deliverables, the data we can provide, the best program, and when to pitch. Adjust the scope to the program's length: a 5-week Black Bear Consulting Corps sprint is not a two-semester capstone.

**Terms for every software project:** code lives in a GitHub repo under an open-source license the students can show in their portfolios, unless the department allows an assignment to the LLC. Paid interns sign an IP assignment in their offer letter. See [hiring-rules.md](https://github.com/wbp318/bottle_recycling_2027/blob/main/internships/hiring-rules.md).

| # | Project | Discipline | Best program | Pitch by |
| --- | --- | --- | --- | --- |
| 1 | Container count and volume dashboard | CS, CIS | UMaine COS 397/497; UMA CIS internship | May–Aug 2027 (capstone); now (UMA) |
| 2 | Computer-vision container classifier | AI, ECE | UMaine ECE capstone; COS capstone | May–Aug 2027 |
| 3 | Bag-drop and commercial pickup route optimizer | CS, operations | COS capstone; USM operations students | May–Aug 2027 |
| 4 | GIS site selection: towns with an open license | GIS, data | Maine Geospatial Institute; UMaine spatial informatics | Jan 2027 (MGI) |
| 5 | Storage and campsite booking and billing | CIS, web | UMA CIS (web track); KVCC | Now for spring |
| 6 | Market and competitor study | Business | Black Bear Consulting Corps | Now (late Oct slot) or summer 2027 |
| 7 | Grant pipeline and first applications | Business, writing | Innovate for Maine; BBCC | Oct–Dec 2026 |
| 8 | Woodlot inventory and management plan | Forestry | UMaine Forest Resources intern or class project | **Now** (forestry recruiting) |
| 9 | Goat pasture and parasite trial | Animal science | Extension, SARE Graduate Grant | Winter 2027 for a spring proposal |
| 10 | Rural redemption economics and EPR | Sustainability, economics | Mitchell Center | Any time |
| 11 | Bag-drop shed or sorting conveyor design | Mechanical engineering | UMaine ME capstone; Advanced Manufacturing Center | May–Aug 2027 |

## 1. Container count and volume dashboard

- **Problem:** We need daily counts by stream (material, deposit tier, size), cash paid out, float balance, and handling fees owed, to reconcile with the cooperative's pickup counts.
- **Deliverables:**
  - A web app for counter staff to log bags and counts
  - A dashboard of volume by day and source (walk-in, bag-drop, route, charity)
  - Float and reimbursement reconciliation
  - CSV export
- **Data:** cooperative stream spec (once registered), sample counts, the plan's unit economics.
- **Stretch:** forecast volume by season to schedule staff.

## 2. Computer-vision container classifier

- **Problem:** Hand sorting is the biggest labor cost. A camera station that classifies containers could speed counting and catch out-of-state or unregistered labels before we pay a deposit on them.
- **Deliverables:**
  - A labeled image dataset collected on site
  - A trained model, for example on a Jetson or Raspberry Pi with a camera
  - A counting-station prototype with a simple interface
  - Accuracy report against hand counts
- **Constraints:** must run offline in a cold building.
- **Compare against:** reverse vending machines. The CCET grant covers at least 25% of commercial equipment ([grants](https://github.com/wbp318/bottle_recycling_2027/blob/main/grants/redemption-center.md)), so the student build is a learning project and a benchmark, not a replacement.

## 3. Bag-drop and commercial pickup route optimizer

- **Problem:** A rural center depends on bag-drop sheds and commercial pickups ([plan](https://github.com/wbp318/bottle_recycling_2027/blob/main/PLAN.md)).
- **Deliverables:**
  - Weekly route planner with stop volumes, truck capacity, and time windows
  - Cost per stop
  - Recommendation on where the next shed should go
- **Data:** account list and addresses (once signed), Maine road network.

## 4. GIS site selection: towns with an open license

- **Problem:** Licenses are capped by town population. We need every town in the target counties ranked by population, existing centers, distance to the nearest center, and residents per center.
- **Deliverables:**
  - A map and ranked table
  - A layer of candidate bag-drop locations
  - A short memo on compelling-need arguments for towns at their cap
- **Data:** DEP licensed-center list (requested), census populations, town boundaries.

## 5. Storage and campsite booking and billing

- **Problem:** Winter boat and RV storage plus up to four campsites need reservations, contracts, deposits, reminders, and lodging-tax records ([ideas](https://github.com/wbp318/bottle_recycling_2027/tree/main/ideas)).
- **Deliverables:**
  - Booking site with availability
  - E-signed storage contracts
  - Payment integration
  - Monthly lodging-tax report
- **Alternative:** evaluate off-the-shelf tools first and recommend build or buy.

## 6. Market and competitor study

- **Problem:** We need real volume estimates.
- **Deliverables:**
  - Inventory of redemption centers within 30 miles: hours, services, reviews
  - Saturday car counts at two incumbents
  - Survey of 20 local bars and restaurants about pickup
  - Pricing for boat and RV storage and campsites nearby
- **Fit:** Black Bear Consulting Corps' 5-week format.

## 7. Grant pipeline and first applications

- **Problem:** We found about 90 programs ([grants](https://github.com/wbp318/bottle_recycling_2027/tree/main/grants)).
- **Deliverables:**
  - A tracker with deadlines and requirements
  - Drafts for the CCET Fund, Northeast Farmers Fund, and SARE Farmer Grant
  - A boilerplate project description and budget template

## 8. Woodlot inventory and management plan

- **Problem:** The woodlot could supply firewood and qualify for WoodsWISE and NRCS forestry cost-share.
- **Deliverables:**
  - Stand map
  - Timber cruise and volume estimates
  - Sustainable annual firewood yield
  - Management plan in a format the Maine Forest Service accepts
  - Trail and campsite layout suggestions
- **Supervision:** a local consulting forester as co-mentor.
- **Timing:** forestry recruiting for summer 2027 is happening **now**.

## 9. Goat pasture and parasite trial

- **Problem:** Rotational grazing and parasite management on a small farm with goats and chickens.
- **Path:** meet faculty through an Extension Small Ruminant Roundtable or pasture walk. A graduate student could apply for a SARE Graduate Grant (up to $30k) with the farm as the site, or the farm could apply for a SARE Farmer Grant.

## 10. Rural redemption economics and EPR

- **Problem:** Maine's handling fee, commingling, and coming packaging EPR change rural redemption economics, and there's little data from small rural centers.
- **Offer:** anonymized volume, cost, and access data from a working center as a thesis or class-project site for the Mitchell Center's materials-management group.

## 11. Bag-drop shed or sorting conveyor design

- **Problem:** A locked, weatherproof bag-drop shed with tagging, or a simple gravity conveyor and bin layout for the sorting floor.
- **Deliverables:** design, bill of materials, a prototype, and a safety review. The Advanced Manufacturing Center can fabricate for a fee.
