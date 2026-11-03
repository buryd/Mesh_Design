# Emory Warner Robins Node — Priced & Resourced BOM
## 1601 Watson Blvd, Warner Robins, GA (Spoke)

| Field | Value |
|-------|--------|
| Node | Emory Hospital Warner Robins |
| Band | 420–450 MHz air-gapped mesh |
| Enclave subnet (example) | `10.40.1.0/24` |
| Estimate class | Planning / budgetary (±30%) |
| Currency | USD |
| Date | 2026-03-11 |
| Related | `Hospital_Node_Configuration.md` |

Prices are **planning figures**, not quotes. Labor is **loaded**. Optional WR↔Perry backup gear is **excluded** here (listed as option).

---

## 1. Hardware & materials

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | Roof mast (+20–40 ft; total 60–100 ft AGL) | 4,500 | **4,500** | Incl. mounts; hospital approval |
| 1 | Yagi antenna 10–14 dBi (420–450 MHz) | 400 | **400** | Aimed at EOC |
| 1 | 420–450 MHz outdoor mesh IP radio | 4,500 | **4,500** | Spoke node |
| 1 | Hardline + polyphaser + grounding kit | 1,800 | **1,800** | Roof to closet |
| 1 | Edge router / firewall (QoS, DHCP) | 1,500 | **1,500** | Enclave gateway |
| 1 | Small managed PoE switch | 350 | **350** | Enclave VLAN only |
| 1 | PoE / DC injector plant | 250 | **250** | |
| 1 | UPS | 800 | **800** | |
| 2 | Softphone or ATA | 120 | **240** | VoIP endpoints |
| 2 | Continuity PC / thin client | 750 | **1,500** | Chat + webmail |
| 1 | NEMA / roof penetration / weather kit | 700 | **700** | |
| 1 | Labels, patch cords, PDU odds | 200 | **200** | |

**Hardware subtotal (WR): $16,740**

### Optional (not in site total)

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | 2nd Yagi toward Perry | 400 | 400 | Backup hop |
| 1 | 2nd mesh radio | 4,500 | 4,500 | Backup hop |

**Optional backup add-on: $4,900** (exclude unless Phase D)

---

## 2. Software & licenses

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 2 | Softphone licenses (Year 1) | 50 | **100** | If not free/bundle |
| 1 | Hospital escort / Biomed coordination fee allowance | 1,000 | **1,000** | Internal or billed |

**Software / site fees subtotal (WR): $1,100**

---

## 3. Resources (labor)

| Role | Hours | Rate $/hr | Extended $ | Tasks |
|------|------:|----------:|-----------:|--------|
| Project coordinator | 16 | 140 | **2,240** | Access, schedule w/ hospital |
| RF engineer | 24 | 160 | **3,840** | Align, radio config, SNR |
| Network engineer | 24 | 150 | **3,600** | Router, DHCP, QoS, air gap |
| Roof / mast installer | 32 | 170 | **5,440** | Mast, coax, ground |
| Field tech | 24 | 95 | **2,280** | Closet, endpoints, test |
| Hospital Biomed/Facilities escort | 16 | 120 | **1,920** | Required access |
| Training (continuity users) | 8 | 110 | **880** | Phone/chat/mail SOP |

**Labor subtotal (WR): $20,200**

---

## 4. Travel / misc

| Item | Extended $ |
|------|-----------:|
| Contingency (5% of hardware) | **837** |
| Structural / roof engineering letter allowance | **2,000** |

**Misc subtotal (WR): $2,837**

---

## 5. Warner Robins node total

| Category | Amount $ |
|----------|----------:|
| Hardware & materials | 16,740 |
| Software & site fees | 1,100 |
| Labor / resources | 20,200 |
| Misc / contingency | 2,837 |
| **WR NODE TOTAL** | **$40,877** |

**Budget band:** ~**$30k–$55k** (roof engineering and mast drive variance).  
**With optional Perry backup path:** ~**$45,777**

---

## 6. Resource roster (who)

| Resource | Count | Source |
|----------|------:|--------|
| Project coordinator | 1 | EMA / contractor |
| RF engineer | 1 | Shared w/ EOC project |
| Network engineer | 1 | Shared w/ EOC project |
| Roof/mast crew | 2 | Contractor |
| Field tech | 1 | Contractor / EMA |
| Biomed / Facilities escort | 1 | Hospital |
| End-user trainer | 1 | EMA |
