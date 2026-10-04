### How a rural site reaches enough volume

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
