# Internships and university projects

How to bring students and faculty from Maine's public universities and community colleges into the project, in forestry, agriculture, sustainability, AI, computing, engineering, and business. Researched October 2026.

| Page | Covers |
| --- | --- |
| [forestry-ag-environment.md](https://github.com/wbp318/bottle_recycling_2027/blob/main/internships/forestry-ag-environment.md) | Forest Resources, Extension, animal science, Mitchell Center, SARE graduate grants, GIS internships |
| [tech-and-business.md](https://github.com/wbp318/bottle_recycling_2027/blob/main/internships/tech-and-business.md) | CS and engineering capstones, UMA CIS, Black Bear Consulting Corps, Innovate for Maine, USM, community colleges |
| [project-briefs.md](https://github.com/wbp318/bottle_recycling_2027/blob/main/internships/project-briefs.md) | Eleven ready-to-send project pitches |
| [hiring-rules.md](https://github.com/wbp318/bottle_recycling_2027/blob/main/internships/hiring-rules.md) | Minimum wage, unpaid internship test, payroll, I-9, workers' comp, remote supervision, IP |

## The short version

1. **Free options exist:**
   - [Black Bear Consulting Corps](https://umaine.edu/innovation/black-bear-consulting-corps/): student teams for 5 weeks, free under 50 employees
   - UMaine computer science capstones (likely free)
   - Class projects
   - Extension pasture walks
   - Hosting a graduate student's SARE-funded research
2. **Paid interns are the norm for real work.** Maine minimum wage is $15.10/hr. Counting, firewood, storage, and production code need pay.
3. **A few programs cover wages:**
   - Maine Geospatial Institute pays $19/hr from state and UMS funds.
   - USM's Career Exploration pays $19.50/hr; ask who covers it.
   - Innovate for Maine is a state-funded fellowship.

   There's no standing state intern subsidy.
4. **UMA in Augusta is likely the closest campus**, and its CIS degree **requires** an internship. Its online-first program suits a remote supervisor.
5. **Act now on forestry:** UMaine forestry interviews for summer 2027 run until mid-November 2026.
6. **The redemption center is research material.** The Mitchell Center studies packaging EPR, and a working rural center is a rare data source.

## Which program for which project

```mermaid
flowchart LR
    subgraph PROJ["Our projects"]
        P1[Count dashboard]
        P2[Computer-vision classifier]
        P3[Route optimizer]
        P4[GIS site selection]
        P5[Booking and billing]
        P6[Market study]
        P7[Grant applications]
        P8[Woodlot plan]
        P9[Goat pasture trial]
        P10[Redemption and EPR research]
        P11[Bag-drop or conveyor design]
    end

    subgraph PROG["Programs"]
        COS[UMaine CS capstone<br/>COS 397/497]
        ECE[UMaine ECE capstone]
        ME[UMaine ME capstone<br/>and Advanced Mfg Center]
        UMA[UMA CIS internship]
        MGI[Maine Geospatial Institute<br/>$19/hr]
        BBCC[Black Bear Consulting Corps<br/>free]
        IFM[Innovate for Maine]
        SFR[UMaine Forest Resources]
        EXT[Extension and<br/>SARE Graduate Grant]
        MIT[Mitchell Center]
    end

    P1 --> COS
    P1 --> UMA
    P2 --> ECE
    P2 --> COS
    P3 --> COS
    P4 --> MGI
    P5 --> UMA
    P6 --> BBCC
    P7 --> IFM
    P7 --> BBCC
    P8 --> SFR
    P9 --> EXT
    P10 --> MIT
    P11 --> ME
```

## Recruiting calendar

```mermaid
gantt
    title Student recruiting and project timing
    dateFormat YYYY-MM-DD
    axisFormat %b %Y

    section Now
    Forestry interns, offers by mid-Nov         :crit, 2026-10-05, 2026-11-15
    BBCC late-October slot (ask)                :crit, 2026-10-05, 2026-10-25
    UMA CIS spring interns (email Dube)         :2026-10-05, 2026-12-15
    Extension and Mitchell Center intros        :2026-10-05, 2026-12-31
    Innovate for Maine hosting inquiry          :2026-10-15, 2026-12-31

    section Winter
    Post summer roles on CareerLink and boards  :2026-11-01, 2027-02-28
    Maine Geospatial Institute openings         :2027-01-05, 2027-02-28
    Innovate for Maine company application      :crit, 2027-01-05, 2027-02-08
    Ag and animal science summer interns        :2027-01-15, 2027-03-31

    section Spring
    SARE graduate proposals with faculty        :2027-02-01, 2027-04-30
    Spring semester (UMA, USM interns)          :2027-01-20, 2027-05-07

    section Summer and fall
    Summer internships                          :2027-05-24, 2027-08-15
    Pitch fall 2027 capstones (COS, ECE, ME)    :crit, 2027-05-01, 2027-08-15
    BBCC fall 2027 application                  :2027-06-01, 2027-08-06
    Fall capstones begin                        :milestone, 2027-08-30, 0d
```

## Costs at a glance

How each route compares in cost to us against what we get. This is a qualitative placement.

```mermaid
quadrantChart
    title Cost to us against value to the project
    x-axis Costs more --> Costs less
    y-axis Less useful --> More useful
    quadrant-1 Do first
    quadrant-2 Worth paying for
    quadrant-3 Skip
    quadrant-4 Nice to have
    Black Bear Corps: [0.84, 0.7]
    CS capstone: [0.85, 0.85]
    ECE capstone: [0.6, 0.78]
    UMA CIS intern: [0.5, 0.8]
    Forestry intern: [0.38, 0.64]
    Geospatial intern: [0.8, 0.6]
    SARE grad research: [0.8, 0.55]
    Extension walk: [0.86, 0.38]
    Innovate for Maine fellow: [0.3, 0.75]
    Ag summer intern: [0.36, 0.44]
    Community college hire: [0.3, 0.32]
```

## Start here

These are tracked as issues [#23](https://github.com/wbp318/bottle_recycling_2027/issues/23) to [#27](https://github.com/wbp318/bottle_recycling_2027/issues/27).

1. Email Eric McPherson (UMaine Forest Resources) about a summer 2027 woodlot intern or class project. Interviews end mid-November.
2. Ask the Foster Center about the late-October Black Bear Consulting Corps slot for the market study, and about hosting an Innovate for Maine fellow in 2027.
3. Email Matthew Dube (UMA CIS) about a spring 2027 intern for the count dashboard.
4. Introduce the farm to the county Extension office and the Mitchell Center.
5. Set up a free employer account on UMaine CareerLink.
6. Keep a GitHub issue per student project so remote supervision is documented.
