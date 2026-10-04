# bottle_recycling_2027

[![CI](https://github.com/wbp318/bottle_recycling_2027/actions/workflows/ci.yml/badge.svg)](https://github.com/wbp318/bottle_recycling_2027/actions/workflows/ci.yml)

Planning repo for a licensed beverage container redemption center in Maine, targeting a 2027 opening.

## What this is

Maine pays licensed redemption centers a per-container handling fee, set in statute and indexed to inflation, on top of refunding the customer's deposit. That fee is the entire margin of the business. This repo holds the plan, the numbers behind it, and the working documents we use to get from idea to a DEP license.

## The plan

Open `maine-redemption-plan.html` in a browser, or read the published version:

https://claude.ai/code/artifact/4e2bd70e-2a05-4e02-8523-a8b3e40098a2

It covers:

- **The rules.** Deposit tiers, who may take returns, the handling fee, licensing, unclaimed deposits, and out-of-state container penalties.
- **How the cash moves.** Customer deposit out of our float, sort into cooperative streams, agent pickup, reimbursement of deposit plus fee.
- **Unit economics** at 2, 4, and 8 million containers a year, with labor, rent, overhead, and float. Planning assumptions are labeled as such.
- **Site ranking.** Lewiston-Auburn, Bangor, the Augusta-Waterville corridor, and the Midcoast, and why the New Hampshire line and Portland are the wrong places.
- **A farm candidate site.** A Maine partner's farm south of Orono: per-town license caps, bag-drop and pickup routes to make up for low density, and economics with no rent.
- **Diagrams** of the money flow, sorting, licensing decisions, partner structure, and timeline are [below](#diagrams).
- **Partner roles** for a Maine operator and an out-of-state funder.
- **A 90-day launch checklist**, starting with the DEP information request.

## Key facts

| Item | Maine |
| --- | --- |
| Deposit | 5¢ standard, 15¢ wine and liquor over 50 mL |
| Handling fee to operator | 6¢ per container as of Sept 2023, indexed from Jan 2025 |
| License | $100 per year, Maine DEP |
| License cap | 1 center in towns of 5,000 or less; 2, 3, or 5 in larger towns |
| To be licensed | LLC in good standing, deed or lease, one dealer agreement, public notice |
| 2025 redemption rate | 69% |
| Out-of-state containers | $100 fine each; ID and plate recorded above 2,500 |

## Diagrams

GitHub renders these. Dollar figures are the plan's planning assumptions, not quotes. Issue numbers refer to this repo's open questions.

### 1. How the money moves

The deposit passes through. The handling fee is the only thing the center keeps.

```mermaid
sequenceDiagram
    autonumber
    actor C as Customer
    participant RC as Redemption center
    participant F as Deposit float (LLC bank line)
    participant A as Cooperative pickup agent
    participant CO as Commingling cooperative
    participant D as Beverage distributors

    D->>C: Sells beverage with 5¢ or 15¢ deposit built into the price
    C->>RC: Brings empty containers
    RC->>RC: Counts containers, rejects out-of-state and unregistered labels
    RC->>F: Draws cash for the refund
    F-->>C: Pays 5¢ per standard container, 15¢ per wine or liquor bottle over 50 mL
    RC->>RC: Sorts into cooperative streams (material, deposit tier, size)
    A->>RC: Scheduled pickup, counts or weighs the sorted material
    A->>CO: Reports counts by stream
    D->>CO: Fund deposits plus handling fees
    CO-->>F: Reimburses deposit (pass-through, 2 to 4 weeks later)
    CO-->>RC: Pays handling fee, 6¢ per container indexed to inflation
    Note over RC,CO: Margin = handling fee only. Scrap belongs to the cooperative.
    Note over F: Float tied up about 2 to 4 weeks of deposits:<br/>about $10k at 2.5M containers per year
```

### 2. What happens to a container inside the center

```mermaid
flowchart TD
    IN([Bag or case arrives]) --> SRC{Where from?}
    SRC -->|Walk-in customer| CTR[Counter count]
    SRC -->|Bag-drop shed in a nearby town| TAG[Tagged bag, customer paid later<br/>by check, app, or account credit]
    SRC -->|Commercial pickup route<br/>bars, restaurants, campgrounds, fairs| RTE[Route intake, account credited]
    SRC -->|Charity drive| CH[Count credited to the nonprofit]
    TAG --> CTR
    RTE --> CTR
    CH --> CTR

    CTR --> CHK{Valid Maine container?}
    CHK -->|Label not registered in Maine| REJ[Reject, return to customer]
    CHK -->|Out-of-state container| OOS[Reject. $100 fine per container risk.<br/>Record ID and plate above 2,500]
    CHK -->|Yes| PAY[Pay deposit out of the float]

    PAY --> MAT{Material}
    MAT --> AL[Aluminum]
    MAT --> PET[PET plastic]
    MAT --> GL[Glass]
    MAT --> OT[Other approved materials]

    AL --> TIER{Deposit tier}
    PET --> TIER
    GL --> TIER
    OT --> TIER
    TIER -->|5¢| SZ5{Size class}
    TIER -->|15¢ wine and liquor| SZ15{Size class}
    SZ5 --> BIN5[Stream bins per cooperative spec]
    SZ15 --> BIN15[Stream bins per cooperative spec]
    BIN5 --> STG[(Staging: bags or bulk bins)]
    BIN15 --> STG
    STG --> PICK[Cooperative agent pickup]
    PICK --> REIMB[Deposit plus 6¢ fee reimbursed]

    classDef bad fill:#FBEDE6,stroke:#A8401B,color:#1A2622
    classDef good fill:#E4F2EB,stroke:#0C6B4C,color:#1A2622
    class REJ,OOS bad
    class REIMB good
```

### 3. Can the farm be licensed? (issue #1)

Licenses are capped by the town the building sits in (38 M.R.S. §3113(3); 06-096 CMR ch. 426). The partner's county of domicile does not decide this.

```mermaid
flowchart TD
    START([Get farm street address and town]) --> POP{Town population<br/>at the latest census}
    POP -->|5,000 or less| C1{Town already has<br/>1 center?}
    POP -->|5,001 to 20,000| C2{Town already has<br/>2 centers?}
    POP -->|20,001 to 30,000| C3{Town already has<br/>3 centers?}
    POP -->|Over 30,000| C5{Town already has<br/>5 centers?}

    C1 -->|No| OPEN[License slot open]
    C2 -->|No| OPEN
    C3 -->|No| OPEN
    C5 -->|No| OPEN
    C1 -->|Yes| CN{Can we prove<br/>compelling public need?}
    C2 -->|Yes| CN
    C3 -->|Yes| CN
    C5 -->|Yes| CN

    CN -->|Ask the DEP regional contact<br/>what evidence counts, issue #10| EV[Gather evidence:<br/>distance to nearest center,<br/>population served, letters from dealers]
    EV --> CNY{DEP accepts?}
    CNY -->|Yes| OPEN
    CNY -->|No| ALT

    OPEN --> BLD{Usable building on the farm?<br/>issue #2}
    BLD -->|Yes, fit-out about $15k to $40k| GO([Go: farm is the licensed center])
    BLD -->|No, new building about $60k to $100k| CMP{Cheaper than renting<br/>a town storefront? issue #3}
    CMP -->|Yes| GO
    CMP -->|No| ALT

    ALT([Fallback: license a storefront in the<br/>nearest town with an open slot,<br/>keep the farm as a bag-drop or not at all])

    classDef go fill:#E4F2EB,stroke:#0C6B4C,color:#1A2622
    classDef stop fill:#FBEDE6,stroke:#A8401B,color:#1A2622
    class GO,OPEN go
    class ALT stop
```

### 4. From idea to license: the DEP path

```mermaid
flowchart LR
    subgraph ENT["Entity (issue #9)"]
        direction TB
        N1[Pick an LLC name,<br/>check availability] --> N2[File Certificate of Formation<br/>$175, paper, 40 to 55 business days]
        N2 --> N3[EIN and bank account]
        N3 --> N4[Good-standing certificate]
    end

    subgraph SITE["Site (issues #1 to #4)"]
        direction TB
        S1[Town, address, open license slot] --> S2[Zoning and code<br/>enforcement OK]
        S2 --> S3[Lease from the landowner<br/>to the LLC, 3 to 5 years]
    end

    subgraph DEAL["Dealers (issue #5)"]
        direction TB
        D1[At least one signed<br/>dealer agreement]
        D2[Optional: member dealer agreement<br/>with a 5,000+ sq ft store]
    end

    subgraph NOTICE["Public notice (issue #12), within 30 days before filing"]
        direction TB
        P1[Publish Notice of Intent<br/>in the local newspaper]
        P2[Mail notice to landowners<br/>within 1,000 ft and across the road]
        P3[Send notice to the<br/>chief municipal officer]
    end

    N4 --> APP
    S3 -->|Title, right, or interest| APP
    D1 --> APP
    D2 -.-> APP
    P1 --> APP
    P2 --> APP
    P3 --> APP

    APP[File Initial Application<br/>plus $100 fee] --> ACC[DEP accepts as complete]
    ACC --> HR{Hearing requested within<br/>20 days of acceptance?}
    HR -->|No| REV[DEP review]
    HR -->|Yes, at Commissioner's discretion| HRG[Public hearing] --> REV
    REV --> LIC([License issued to the LLC])
    LIC --> COOP[Register with the cooperative<br/>for pickup]
    LIC --> REN[Renew every year, $100]
```

### 5. Who holds what

The license, lease, and bank line sit with the LLC, not with either person.

```mermaid
flowchart TB
    MP["Maine partner<br/>member and manager<br/>registered agent"]
    FP["Funding partner<br/>member, out of state"]
    LLC{{"Redemption LLC<br/>(Maine)"}}
    FARM[("Farm property<br/>owned by the Maine partner")]

    MP -->|"Sweat: counter, sorting, routes,<br/>local accounts"| LLC
    FP -->|"Cash: deposit float as a member loan,<br/>buildout as capital"| LLC
    FP -->|"Books, cooperative reporting,<br/>DEP filings, marketing"| LLC
    FARM -->|"Lease, about $500/mo"| LLC

    LLC --> LIC[DEP license]
    LLC --> BANK[Bank account and float line]
    LLC --> COOPR[Cooperative registration]
    LLC --> ACCTS[Dealer agreements and<br/>commercial accounts]
    LLC --> INS[Insurance policies]

    LLC -->|"1. Wages or guaranteed payment"| MP
    LLC -->|"2. Rent"| FARM
    LLC -->|"3. Loan interest and principal"| FP
    LLC -->|"4. Profit split by ownership %<br/>(open term, issue #8)"| MP
    LLC -->|"4. Profit split by ownership %"| FP
```

### 6. How a rural site reaches enough volume

Maine redeems about 850 million containers a year across about 1.4 million people, roughly 600 per resident. Catching a third of local returns, 2 million containers a year needs about 10,000 people within reach. One small town is not enough, so volume has to be brought in (issue #6).

```mermaid
flowchart LR
    subgraph TOWN["Farm's own town"]
        W[Walk-in customers<br/>Saturday mornings matter most]
    end
    subgraph NEAR["Neighboring towns"]
        B1[Bag-drop shed #1<br/>at a store]
        B2[Bag-drop shed #2]
    end
    subgraph COMM["Commercial pickup route"]
        R1[Bars and restaurants]
        R2[Campgrounds, summer]
        R3[Fairs and events]
    end
    subgraph BIG["Member dealer"]
        G[Grocery store 5,000+ sq ft<br/>hands its redemption duty to us]
    end
    CHAR[Charity drives]

    W --> FLOOR
    B1 -->|farm truck| FLOOR
    B2 -->|farm truck| FLOOR
    R1 -->|farm truck| FLOOR
    R2 -->|farm truck| FLOOR
    R3 -->|farm truck| FLOOR
    G --> FLOOR
    CHAR --> FLOOR

    FLOOR[["Farm sorting floor<br/>(the licensed center)"]] --> COOP[Cooperative pickup]
    COOP --> CASH[6¢ per container]
```

### 7. Where the money goes at a farm site, 2.5 million containers a year

$150,000 in handling fees at 6¢.

```mermaid
pie showData
    title Farm site at 2.5M containers per year ($)
    "Counter, route, management labor" : 50000
    "Operating profit before owner pay" : 44750
    "Sorting labor" : 21250
    "Insurance, heat, bags, license, bank" : 20000
    "Route fuel and vehicle wear" : 8000
    "Lease paid to the farm" : 6000
```

### 8. Profit by site and volume

Operating profit before owner pay and tax, from the two tables in the plan. A farm site with a usable building beats a rented town site because there is no rent.

```mermaid
xychart-beta
    title "Operating profit by scenario ($ thousands)"
    x-axis ["Town 2M", "Town 4M", "Town 8M", "Farm 1.5M", "Farm 2.5M", "Farm 4M"]
    y-axis "Profit ($k)" 0 --> 200
    bar [10, 68, 192, 11, 45, 92]
```

### 9. Site ranking at a glance

A qualitative read of section 3 of the plan, not measured data.

```mermaid
quadrantChart
    title Where to put a center
    x-axis Low household density --> High household density
    y-axis Well served already --> Coverage gap
    quadrant-1 Best bets
    quadrant-2 Gap but thin volume
    quadrant-3 Avoid
    quadrant-4 Crowded
    Lewiston-Auburn: [0.78, 0.55]
    Bangor-Brewer: [0.62, 0.6]
    Augusta-Waterville: [0.52, 0.74]
    Midcoast: [0.32, 0.7]
    Partner farm: [0.15, 0.62]
    Greater Portland: [0.95, 0.12]
    NH state line: [0.35, 0.08]
```

### 10. License lifecycle

```mermaid
stateDiagram-v2
    [*] --> Planning
    Planning --> NoticePublished: LLC formed, lease signed,<br/>dealer agreement signed
    NoticePublished --> Filed: Within 30 days of notice,<br/>application plus $100
    Filed --> Incomplete: Missing attachments
    Incomplete --> Filed: Resubmit
    Filed --> Accepted: Deemed complete
    Accepted --> HearingWindow: 20 days to request a hearing
    HearingWindow --> Hearing: Requested and granted
    HearingWindow --> Review: None requested
    Hearing --> Review
    Review --> Denied: Cap reached, no compelling need
    Review --> Licensed
    Denied --> Planning: New site or new town
    Licensed --> Operating: Cooperative pickup registered
    Operating --> Renewal: Every year, $100
    Renewal --> Operating: Renewals are exempt from the town cap
    Operating --> Transfer: Sale or move,<br/>separate DEP transfer application
    Transfer --> Operating
    Operating --> [*]: Close
```

### 11. Timeline to opening

A target schedule starting October 2026. Dates move once issue #1 is answered.

```mermaid
gantt
    title Path to a 2027 opening
    dateFormat YYYY-MM-DD
    axisFormat %b %Y

    section Answers from the Maine partner
    Town, address, license check (#1)        :crit, a1, 2026-10-05, 14d
    Buildings and winter access (#2)         :a2, 2026-10-05, 14d
    Time commitment and hours (#7)           :a3, 2026-10-05, 14d

    section DEP
    Confirm rules and data with DEP (#10)    :crit, d1, after a1, 21d
    Zoning and deed check (#4)               :d2, after a1, 21d

    section Business setup
    Agree on operating terms (#8)            :b1, after d1, 21d
    Attorney drafts agreement and lease      :b2, after b1, 30d
    File LLC, 40 to 55 business days (#9)    :crit, b3, after b1, 77d
    Insurance quotes and CPA (#11)           :b4, after b1, 30d

    section Site and volume
    Buildout quotes (#3)                     :s1, after a2, 30d
    Buildout                                 :s2, after b3, 45d
    Dealer agreements (#5)                   :s3, after d1, 60d
    Bag-drop sites and route accounts (#6)   :s4, after d1, 90d

    section License
    Public notice, within 30 days of filing (#12) :crit, l1, after b3, 14d
    File application                          :milestone, crit, l2, after l1, 0d
    DEP review and hearing window             :l3, after l1, 45d
    Opening day                               :milestone, l4, after l3, 0d
```

### 12. How the open questions depend on each other

```mermaid
flowchart TD
    I1["#1 Town, address,<br/>open license?"]
    I2["#2 Buildings and<br/>winter access"]
    I3["#3 Buildout quotes"]
    I4["#4 Zoning and deed"]
    I5["#5 Dealer agreements"]
    I6["#6 Bag-drops and routes"]
    I7["#7 Partner hours"]
    I8["#8 Operating terms"]
    I9["#9 Form the LLC"]
    I10["#10 Confirm rules with DEP"]
    I11["#11 Insurance and tax"]
    I12["#12 Public notice"]
    FILE(["File DEP application"])

    I1 --> I10
    I1 --> I4
    I1 --> I12
    I2 --> I3
    I10 --> I5
    I10 --> I6
    I3 --> I8
    I7 --> I8
    I8 --> I9
    I8 --> I11
    I9 --> FILE
    I4 --> FILE
    I5 --> FILE
    I12 --> FILE
    I11 --> FILE

    classDef first fill:#E4F2EB,stroke:#0C6B4C,color:#1A2622
    class I1 first
```

## Status

- [x] Confirm the legal model and fee structure
- [x] Draft the plan and site ranking
- [x] Pull the 2026 DEP initial application and map its requirements
- [ ] Get the Maine partner's town and site address; check for an open license there
- [ ] Request current license list and 2026 fee figure from Maine DEP
- [ ] Visit two incumbent centers and count volume
- [ ] Form the LLC and line up the deposit float
- [ ] Sign first commercial pickup accounts
- [ ] File the Redemption Center License Initial Application

## Repo layout

```
maine-redemption-plan.html   the plan, self-contained, opens in any browser
README.md                    this file
.github/workflows/ci.yml     CI: renders every Mermaid diagram, checks the plan HTML, blocks private files, reports dead links
.github/scripts/             helper scripts the CI runs
.gitattributes               Linguist overrides so every file type shows in the language bar
.gitignore                   keeps correspondence drafts and partner documents (private/) out of the repo
```

## Sources

- [Maine DEP, Beverage Container Redemption Program](https://www.maine.gov/dep/sustainability/bottlebill/index.html)
- [Bottle Bill Resource Guide, Maine](https://www.bottlebill.org/maine/)
- [Waste Dive, Maine raises handling fee to 6¢](https://www.wastedive.com/news/maine-governor-bottle-bill-handling-fee-poland-spring/649775/)
- [Maine Public, redemption center closures and modernization](https://www.mainepublic.org/business-and-economy/2023-03-29/as-redemption-centers-close-maine-seeks-to-modernize-its-bottle-deposit-law)
- [NRCM, how Maine modernized the bottle bill](https://www.nrcm.org/blog/how-maine-modernized-bottle-bill/)
- [NCSL, state beverage container deposit laws](https://www.ncsl.org/environment-and-natural-resources/state-beverage-container-deposit-laws)

## A note on how this started

A Parish Brewing label reads "OK+ 10¢ MI" on its deposit line. Oklahoma has never had a bottle deposit law. The label text was typed before 2011 and never fixed: it still lists Delaware, which repealed its deposit that year, and Oregon at 5¢, which moved to 10¢ in 2017. The label is not the law. The statutes above are.
