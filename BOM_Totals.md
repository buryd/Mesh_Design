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

Detail: [EOC BOM](EOC_Node_BOM.md) · [WR BOM](Hospital_WR_Node_BOM.md) · [Perry BOM](Hospital_Perry_Node_BOM.md)

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

| App | Product | License $ | Where | Resource |
|-----|---------|----------:|-------|----------|
| VoIP server | **FreePBX** | 0 | EOC Linux mini PC | [freepbx.org](https://www.freepbx.org/) |
| VoIP handsets | SIP desk phones ×6 | ~600 | 2 per site | [Grandstream IP phones](https://www.grandstream.com/products/ip-voices-telephony/ip-phones) (example) |
| Chat | **MeshChat** | 0 | EOC server | [GitHub kn6plv/meshchat](https://github.com/kn6plv/meshchat) |
| Email | **Citadel** | 0 | EOC server | [citadel.org](https://www.citadel.org/) |
| Spare | Optional softphone | 0 | Continuity PC | [Linphone](https://www.linphone.org/) |

---

## 6. Resource hyperlinks (master)

### Software
| Resource | URL |
|----------|-----|
| FreePBX | https://www.freepbx.org/ |
| FreePBX downloads | https://www.freepbx.org/downloads/ |
| FreePBX wiki | https://wiki.freepbx.org/ |
| MeshChat packages | https://github.com/kn6plv/meshchat |
| MeshChat / AREDN install notes | https://www.arednmesh.org/content/meshchat-installation-help |
| Citadel | https://www.citadel.org/ |
| Citadel download | https://www.citadel.org/download.html |
| Debian | https://www.debian.org/download |
| Ubuntu Server | https://ubuntu.com/download/server |
| Linphone (optional softphone) | https://www.linphone.org/ |

### Hardware / RF / network (examples)
| Resource | URL |
|----------|-----|
| OPNsense | https://opnsense.org/ |
| OpenWrt | https://openwrt.org/ |
| Ham Radio Outlet | https://www.hamradio.com/ |
| DX Engineering | https://www.dxengineering.com/ |
| Grandstream SIP phones | https://www.grandstream.com/products/ip-voices-telephony/ip-phones |
| FCC Part 97 | https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97 |

### Project documents
| Doc | Link |
|-----|------|
| Architecture | [420-450MHz_RF_Mesh_Architecture.md](420-450MHz_RF_Mesh_Architecture.md) |
| EOC configuration | [EOC_Node_Configuration.md](EOC_Node_Configuration.md) |
| Hospital configuration | [Hospital_Node_Configuration.md](Hospital_Node_Configuration.md) |
| EOC BOM | [EOC_Node_BOM.md](EOC_Node_BOM.md) |
| WR BOM | [Hospital_WR_Node_BOM.md](Hospital_WR_Node_BOM.md) |
| Perry BOM | [Hospital_Perry_Node_BOM.md](Hospital_Perry_Node_BOM.md) |

---

## 7. Notes

1. Antenna **materials** stay in **base**; antenna **install/mast labor** is optional.  
2. Labor section is fully optional.  
3. Desk phones are **in base** (required), not optional.  
4. Confirm **Part 97** (or other) authority before RF transmit on 420–450 MHz.  
5. Prefer G.729/Opus on phones for RF; keep Citadel attachments small.  
6. Vendor links are **examples** for sourcing — not sole-source requirements.  
