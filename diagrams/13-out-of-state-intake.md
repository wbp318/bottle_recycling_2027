### Out-of-state container check at intake

Containers bought outside Maine carry a $100 fine per container for the center that accepts them, and returns over 2,500 containers need name, address, and plate.

```mermaid
flowchart TD
    IN([Customer or account brings containers]) --> LBL{Registered Maine<br/>deposit label?}
    LBL -->|No| BACK[Hand back, not redeemable]
    LBL -->|Yes| WHO{Who is returning?}
    WHO -->|Commercial pickup account| ACCT{Signed agreement that<br/>containers were sold in Maine,<br/>volume in its normal range?}
    WHO -->|Bag-drop customer| BAG{Registered account<br/>with address on file?}
    WHO -->|Walk-in| SIZE{More than 2,500<br/>containers at once?}
    ACCT -->|Yes| COUNT
    ACCT -->|No| FLAG
    BAG -->|Yes| SIZE
    BAG -->|No| HOLD[Hold the bag until the<br/>customer registers]
    SIZE -->|No| RED{Red flags?<br/>Pallet loads, repeat bulk,<br/>far-away customer}
    SIZE -->|Yes, nonprofit| RED
    SIZE -->|Yes| LOG[Log name, address,<br/>license plate]
    LOG --> RED
    RED -->|No| COUNT[Count, pay deposit,<br/>sort into streams]
    RED -->|Yes| FLAG[Refuse or escalate to<br/>the manager; note the decision]

    classDef bad fill:#FBEDE6,stroke:#A8401B,color:#1A2622
    classDef good fill:#E4F2EB,stroke:#0C6B4C,color:#1A2622
    class BACK,FLAG,HOLD bad
    class COUNT good
```
