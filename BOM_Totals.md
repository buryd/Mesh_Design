# RF Mesh BOM Totals — All Nodes
## Ham 420–450 MHz · FreePBX · MeshChat · Citadel

| Field | Value |
|-------|--------|
| Radios | Standard **ham / 70 cm** (420–450 MHz) |
| VoIP | **FreePBX** (EOC) |
| Chat | **MeshChat** (EOC) |
| Email | **Citadel** (EOC) |
| Antenna work | **Optional** |
| Labor | **Optional** |
| Estimate class | Planning / budgetary (±30%) |
| Currency | USD |
| Date | 2026-03-11 |

Detail: `EOC_Node_BOM.md`, `Hospital_WR_Node_BOM.md`, `Hospital_Perry_Node_BOM.md`

---

## 1. Base totals by node (REQUIRED gear only)

| Node | Base hardware + software $ |
|------|---------------------------:|
| EOC Kathleen | **5,430** |
| Emory Warner Robins | **2,765** |
| Emory Perry | **2,765** |
| **PROGRAM BASE TOTAL** | **$10,960** |

---

## 2. Optional add-ons by node

| Node | Antenna work $ | Labor $ | Antenna + labor $ |
|------|----------------:|--------:|------------------:|
| EOC | 4,900 | 9,480 | 14,380 |
| Emory WR | 4,050 | 5,440 | 9,490 |
| Emory Perry | 4,050 | 5,440 | 9,490 |
| **Optional sum** | **13,000** | **20,360** | **33,360** |

---

## 3. Program packages (pick one)

| Package | What it includes | **Program total $** |
|---------|------------------|--------------------:|
| **A — Base only** | Ham radios, routers, FreePBX, MeshChat, Citadel, client PCs; **no** antenna install, **no** paid labor | **$10,960** |
| **B — Base + all antenna work** | A + mast/aim/ground labor at 3 sites | **$23,960** |
| **C — Base + all labor** | A + engineering/admin/training labor; antenna work excluded | **$31,320** |
| **D — Full** | Base + antenna work + labor at all nodes | **$44,320** |

### Grand total (recommended reporting lines)

| | Amount $ |
|--|----------:|
| **Minimum (Package A)** | **$10,960** |
| **Full optional (Package D)** | **$44,320** |
| Planning band on D (±30%) | **~$31,000 – $58,000** |

---

## 4. Application stack (cost)

| App | Product | License $ | Where |
|-----|---------|----------:|-------|
| VoIP | **FreePBX** | 0 | EOC server |
| Chat | **MeshChat** | 0 | EOC server |
| Email | **Citadel** | 0 | EOC server |
| Clients | Softphone / browser | 0–80 | Each site |

---

## 5. Notes

1. Antenna **materials** (Yagi, coax) stay in **base**; antenna **install/mast labor** is optional.  
2. Labor section is fully optional (volunteer / in-house can choose Package A or B).  
3. Ham radios are far cheaper than commercial Part 90 IP mesh gear; throughput for FreePBX/MeshChat/Citadel remains **narrow** — keep codecs low and email small.  
4. Confirm **Part 97** (or other) authority before RF transmit on 420–450 MHz.  
5. Optional WR↔Perry second radio pair ≈ **+$680 materials per end** (not in totals above).  
