# EOC Node — Priced & Resourced BOM
## 102 Chief Williams Dr, Kathleen, GA (Hub)

| Field | Value |
|-------|--------|
| Node | EOC Kathleen — Hub + Apps |
| Band | 420–450 MHz (standard **ham / 70 cm** radios) |
| Apps | **FreePBX** · **MeshChat** · **Citadel** email |
| Estimate class | Planning / budgetary (±30%) |
| Currency | USD |
| Date | 2026-03-11 |
| Related | `EOC_Node_Configuration.md`, `BOM_Totals.md` |

**Base total = hardware + software hosts only.**  
**Antenna work** and **labor** are **OPTIONAL** add-ons (see §5–§6).

> Licensing note: standard ham radios imply **Part 97** (or other lawful authority). Confirm operators/licenses before transmit; governmental air-gap use may require a separate authorization path.

---

## 1. Base hardware (REQUIRED)

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 2 | Ham 70 cm / 420–450 MHz base or mobile radio | 550 | **1,100** | Standard amateur UHF (e.g. Icom/Yaesu/Kenwood class); one path WR, one Perry — or dual-radio hub |
| 1 | Spare ham UHF radio | 550 | **550** | Hot spare |
| 2 | Power supply 13.8 V / 20–30 A | 120 | **240** | For base radios |
| 2 | Ham Yagi 420–450 MHz (10–12 dBi class) | 120 | **240** | **Antenna hardware only** (install optional) |
| 1 | Ham omni 70 cm (optional fill) | 90 | **90** | Portable / local |
| 1 | Coax (LMR-400/9913), connectors, arrestors kit | 350 | **350** | Materials only |
| 1 | Edge router / firewall (QoS, DHCP) | 250 | **250** | e.g. OpenWrt/OPNsense class mini |
| 1 | Small managed or unmanaged GbE switch | 80 | **80** | Enclave LAN |
| 1 | FreePBX host (mini PC / NUC-class) | 450 | **450** | On-prem Asterisk/FreePBX |
| 1 | MeshChat + Citadel host (mini PC) | 400 | **400** | May share one host w/ FreePBX (−$400 if combined) |
| 1 | UPS (small) | 200 | **200** | |
| 2 | Continuity workstation / laptop | 500 | **1,000** | Softphone, MeshChat, Citadel web |
| 2 | Softphone (software) or cheap SIP ATA | 40 | **80** | FreePBX endpoints |
| 1 | USB/serial audio or radio-IT gateway kit | 200 | **200** | If bridging radio ↔ IP (AllStar/URI-class) as designed |
| 1 | Cables, PDUs, labels, shelves | 150 | **150** | |

**Base hardware subtotal (EOC): $5,380**  
*(If FreePBX + MeshChat + Citadel on **one** mini PC: **$4,980**)*

---

## 2. Base software (REQUIRED)

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | **FreePBX** / Asterisk | 0 | **0** | OSS; support optional |
| 1 | **MeshChat** | 0 | **0** | OSS / community |
| 1 | **Citadel** (email/groupware) | 0 | **0** | OSS |
| 1 | OS media / offline packages | 50 | **50** | Sneaker-net ISO/USB |

**Base software subtotal (EOC): $50**

---

## 3. EOC BASE TOTAL (no antenna work, no labor)

| Category | Amount $ |
|----------|----------:|
| Hardware | 5,380 |
| Software | 50 |
| **EOC BASE TOTAL** | **$5,430** |

---

## 4. Optional — Antenna hardware already in base

Yagis/omni/coax **materials** are in §1.  
The following is **install / structural work only**.

---

## 5. OPTIONAL — Antenna work

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | Mast / tower attach or roof tripod allowance | 1,500 | **1,500** | Height still recommended for path |
| 1 | Antenna crew — mount, aim, weatherseal (lump) | 2,200 | **2,200** | Climb/roof labor |
| 1 | Grounding / polyphaser install labor | 400 | **400** | |
| 1 | Structural / landlord review allowance | 800 | **800** | If required |

**Optional antenna work (EOC): $4,900**

---

## 6. OPTIONAL — Labor / resources

| Role | Hours | Rate $/hr | Extended $ | Tasks |
|------|------:|----------:|-----------:|--------|
| Project coordinator | 16 | 100 | **1,600** | Schedule, docs |
| RF / radio tech | 24 | 95 | **2,280** | Radio program, aim assist |
| Network / FreePBX admin | 32 | 110 | **3,520** | Router, DHCP, FreePBX, MeshChat, Citadel, air gap |
| Field tech | 16 | 85 | **1,360** | Cabling, rack, test |
| Training / handoff | 8 | 90 | **720** | User SOP |

**Optional labor (EOC): $9,480**

---

## 7. Totals — choose package

| Package | Amount $ |
|---------|----------:|
| **A — Base only** (radios, FreePBX, MeshChat, Citadel, LAN) | **$5,430** |
| **B — Base + antenna work** | **$10,330** |
| **C — Base + labor** | **$14,910** |
| **D — Base + antenna work + labor (full)** | **$19,810** |

---

## 8. Application stack (EOC hosts)

| App | Product | Host |
|-----|---------|------|
| VoIP | **FreePBX** | Mini PC @ EOC |
| Chat | **MeshChat** | Mini PC @ EOC (or shared) |
| Email | **Citadel** | Mini PC @ EOC (or shared) |
