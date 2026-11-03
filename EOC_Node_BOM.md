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
| Related | [EOC Node Configuration](EOC_Node_Configuration.md) · [BOM Totals](BOM_Totals.md) · [Architecture](420-450MHz_RF_Mesh_Architecture.md) |

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
| 1 | Small PoE GbE switch (or switch + injectors) | 120 | **120** | Powers SIP phones |
| 1 | FreePBX host (mini PC / NUC-class) | 450 | **450** | On-prem Asterisk/FreePBX |
| 1 | MeshChat + Citadel host (mini PC) | 400 | **400** | May share one host w/ FreePBX (−$400 if combined) |
| 1 | UPS (small) | 200 | **200** | |
| 2 | **SIP VoIP desk phones** (PoE) | 100 | **200** | FreePBX ext **1001, 1002** |
| 2 | Continuity workstation / laptop | 500 | **1,000** | MeshChat, Citadel; optional softphone spare |
| 1 | USB/serial audio or radio-IT gateway kit | 200 | **200** | If bridging radio ↔ IP (AllStar/URI-class) as designed |
| 1 | Cables, PDUs, labels, shelves | 150 | **150** | |

**Base hardware subtotal (EOC): $5,460**  
*(If FreePBX + MeshChat + Citadel on **one** mini PC: **$5,060**)*

---

## 2. Base software (REQUIRED)

| Qty | Item | Unit $ | Extended $ | Resource |
|----:|------|-------:|-----------:|----------|
| 1 | **FreePBX** / Asterisk | 0 | **0** | [freepbx.org](https://www.freepbx.org/) · [Downloads](https://www.freepbx.org/downloads/) |
| 1 | **MeshChat** | 0 | **0** | [MeshChat (kn6plv)](https://github.com/kn6plv/meshchat) · [AREDN notes](https://www.arednmesh.org/content/meshchat-installation-help) |
| 1 | **Citadel** (email/groupware) | 0 | **0** | [citadel.org](https://www.citadel.org/) · [Download](https://www.citadel.org/download.html) |
| 1 | Linux OS (Debian/Ubuntu) offline media | 50 | **50** | [Debian](https://www.debian.org/download) · [Ubuntu Server](https://ubuntu.com/download/server) |

**Base software subtotal (EOC): $50**

---

## 3. EOC BASE TOTAL (no antenna work, no labor)

| Category | Amount $ |
|----------|----------:|
| Hardware | 5,460 |
| Software | 50 |
| **EOC BASE TOTAL** | **$5,510** |

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
| **A — Base only** (radios, FreePBX, phones, MeshChat, Citadel, LAN) | **$5,510** |
| **B — Base + antenna work** | **$10,410** |
| **C — Base + labor** | **$14,990** |
| **D — Base + antenna work + labor (full)** | **$19,890** |

---

## 8. Application stack (EOC hosts)

| App | Product | Host / endpoint | Resource |
|-----|---------|-----------------|----------|
| VoIP server | **FreePBX** | Mini PC @ EOC (Linux) | [FreePBX](https://www.freepbx.org/) |
| VoIP handsets | SIP desk phones ×2 | Ext 1001, 1002 | [Grandstream IP phones](https://www.grandstream.com/products/ip-voices-telephony/ip-phones) (example) |
| Chat | **MeshChat** | Mini PC @ EOC (or shared) | [MeshChat GitHub](https://github.com/kn6plv/meshchat) |
| Email | **Citadel** | Mini PC @ EOC (or shared) | [Citadel](https://www.citadel.org/) |

---

## 9. Resource hyperlinks

### Software & OS
| Resource | URL |
|----------|-----|
| FreePBX home | https://www.freepbx.org/ |
| FreePBX downloads | https://www.freepbx.org/downloads/ |
| FreePBX wiki / docs | https://wiki.freepbx.org/ |
| MeshChat (current packages) | https://github.com/kn6plv/meshchat |
| MeshChat install help (AREDN) | https://www.arednmesh.org/content/meshchat-installation-help |
| Citadel home | https://www.citadel.org/ |
| Citadel download | https://www.citadel.org/download.html |
| Debian ISO | https://www.debian.org/download |
| Ubuntu Server | https://ubuntu.com/download/server |

### Networking & RF (examples)
| Resource | URL |
|----------|-----|
| OPNsense (edge firewall example) | https://opnsense.org/ |
| OpenWrt | https://openwrt.org/ |
| Ham Radio Outlet (radios/antennas) | https://www.hamradio.com/ |
| DX Engineering (coax/antennas) | https://www.dxengineering.com/ |
| Grandstream IP phones (SIP example) | https://www.grandstream.com/products/ip-voices-telephony/ip-phones |
| FCC Part 97 (amateur radio) | https://www.ecfr.gov/current/title-47/chapter-I/subchapter-D/part-97 |

### Project docs
| Doc | Link |
|-----|------|
| Architecture | [420-450MHz_RF_Mesh_Architecture.md](420-450MHz_RF_Mesh_Architecture.md) |
| EOC configuration | [EOC_Node_Configuration.md](EOC_Node_Configuration.md) |
| Hospital configuration | [Hospital_Node_Configuration.md](Hospital_Node_Configuration.md) |
| Program totals | [BOM_Totals.md](BOM_Totals.md) |
| WR BOM | [Hospital_WR_Node_BOM.md](Hospital_WR_Node_BOM.md) |
| Perry BOM | [Hospital_Perry_Node_BOM.md](Hospital_Perry_Node_BOM.md) |
