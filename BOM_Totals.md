# RF Mesh BOM Totals — All Nodes
## Ham 420–450 MHz · FreePBX · SIP Phones · MeshChat · Citadel

| Field | Value |
|-------|--------|
| Radios | Standard **ham / 70 cm** (420–450 MHz) |
| VoIP | **FreePBX** (EOC) + **6 SIP desk phones** (2 per site) |
| Chat | **MeshChat** (EOC) |
| Email | **Citadel** (EOC) |
| Antenna work | **Optional** |
| Labor | **Optional** |
| Estimate class | Planning / budgetary (±30%) |
| Currency | USD |
| Date | 2026-03-11 |

Detail: `EOC_Node_BOM.md`, `Hospital_WR_Node_BOM.md`, `Hospital_Perry_Node_BOM.md`

---

## 1. VoIP phone roll-up

| Site | SIP desk phones | FreePBX extensions | Unit ~$ | Extended $ |
|------|----------------:|--------------------|--------:|-----------:|
| EOC | 2 | 1001, 1002 | 100 | 200 |
| Emory WR | 2 | 2001, 2002 | 100 | 200 |
| Emory Perry | 2 | 3001, 3002 | 100 | 200 |
| **Total** | **6** | — | — | **$600** |

All phones: PoE → enclave switch → DHCP from site edge router → register to FreePBX `10.40.0.10`.

---

## 2. Base totals by node (REQUIRED gear only)

| Node | Base hardware + software $ |
|------|---------------------------:|
| EOC Kathleen | **5,510** |
| Emory Warner Robins | **2,925** |
| Emory Perry | **2,925** |
| **PROGRAM BASE TOTAL** | **$11,360** |

---

## 3. Optional add-ons by node

| Node | Antenna work $ | Labor $ | Antenna + labor $ |
|------|----------------:|--------:|------------------:|
| EOC | 4,900 | 9,480 | 14,380 |
| Emory WR | 4,050 | 5,440 | 9,490 |
| Emory Perry | 4,050 | 5,440 | 9,490 |
| **Optional sum** | **13,000** | **20,360** | **33,360** |

---

## 4. Program packages (pick one)

| Package | What it includes | **Program total $** |
|---------|------------------|--------------------:|
| **A — Base only** | Ham radios, routers, FreePBX, **6 SIP phones**, MeshChat, Citadel, PCs; no antenna install, no paid labor | **$11,360** |
| **B — Base + all antenna work** | A + mast/aim/ground labor at 3 sites | **$24,360** |
| **C — Base + all labor** | A + engineering/admin/training labor; antenna work excluded | **$31,720** |
| **D — Full** | Base + antenna work + labor at all nodes | **$44,720** |

### Grand total (recommended reporting lines)

| | Amount $ |
|--|----------:|
| **Minimum (Package A)** | **$11,360** |
| **Full optional (Package D)** | **$44,720** |
| Planning band on D (±30%) | **~$31,000 – $58,000** |

---

## 5. Application stack (cost)

| App | Product | License $ | Where |
|-----|---------|----------:|-------|
| VoIP server | **FreePBX** | 0 | EOC server |
| VoIP handsets | SIP desk phones ×6 | ~600 | 2 per site |
| Chat | **MeshChat** | 0 | EOC server |
| Email | **Citadel** | 0 | EOC server |
| Spare | Optional softphone | 0 | Continuity PC |

---

## 6. Notes

1. Antenna **materials** stay in **base**; antenna **install/mast labor** is optional.  
2. Labor section is fully optional.  
3. Desk phones are **in base** (required), not optional.  
4. Confirm **Part 97** (or other) authority before RF transmit on 420–450 MHz.  
5. Prefer G.729/Opus on phones for RF; keep Citadel attachments small.  
