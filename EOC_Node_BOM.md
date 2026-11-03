# EOC Node — Priced & Resourced BOM
## 102 Chief Williams Dr, Kathleen, GA (Hub)

| Field | Value |
|-------|--------|
| Node | EOC Kathleen — Hub + Apps |
| Band | 420–450 MHz air-gapped mesh |
| Estimate class | Planning / budgetary (±30%) |
| Currency | USD |
| Date | 2026-03-11 |
| Related | `EOC_Node_Configuration.md`, `420-450MHz_RF_Mesh_Architecture.md` |

Prices are **street/catalog planning figures**, not vendor quotes. Labor is **loaded** (wages + burden).

---

## 1. Hardware & materials

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | Tower / mast system (100–150 ft AGL class) | 18,000 | **18,000** | New or lease space on existing; site-dependent |
| 2 | Yagi antenna 10–12 dBi (420–450 MHz) | 350 | **700** | Aim WR & Perry |
| 1 | Omni collinear 5–8 dBi (optional) | 400 | **400** | Portable fill |
| 1 | 420–450 MHz outdoor mesh IP radio | 4,500 | **4,500** | Authorized UHF IP/mesh class |
| 1 | Hardline, connectors, polyphasers, grounding kit | 2,800 | **2,800** | ½″/⅞″ plant |
| 1 | Edge router / firewall (QoS, DHCP) | 1,800 | **1,800** | No Internet WAN |
| 1 | Managed PoE switch (8–24 port) | 450 | **450** | Enclave only |
| 1 | PoE / DC power plant | 350 | **350** | Radio power |
| 1 | SIP PBX appliance or server | 2,200 | **2,200** | On-prem VoIP |
| 1 | Chat + internal mail host (server/VM host) | 1,800 | **1,800** | May be one box w/ PBX at lower cost |
| 1 | Local DNS/NTP/NMS (may share host) | 400 | **400** | Incremental if shared ≈ $0–400 |
| 1 | UPS (rack/tower, enclave runtime) | 1,200 | **1,200** | |
| 1 | Generator transfer / circuit work allowance | 3,500 | **3,500** | If circuit exists, reduce |
| 2 | Continuity workstations | 900 | **1,800** | Softphone/chat/mail |
| 2 | Softphone licenses / ATA | 120 | **240** | |
| 1 | NEMA / ice bridge / cable entry kit | 900 | **900** | |
| 1 | Spares held at EOC (radio PSU, injectors) | 600 | **600** | Site stock |

**Hardware subtotal (EOC): $41,640**

---

## 2. Software & licenses (enclave)

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | PBX software / support (Year 1) | 800 | **800** | Or included w/ appliance |
| 1 | Chat server license / support (Year 1) | 500 | **500** | OSS ≈ $0 + support |
| 1 | Internal mail / webmail (Year 1) | 400 | **400** | |
| 1 | Frequency authorization / coordination fees | 1,500 | **1,500** | Highly variable |

**Software / auth subtotal (EOC): $3,200**

---

## 3. Resources (labor)

| Role | Hours | Rate $/hr | Extended $ | Tasks |
|------|------:|----------:|-----------:|--------|
| Project manager | 40 | 140 | **5,600** | Schedule, hospital coordination |
| RF engineer | 48 | 160 | **7,680** | Path, antenna, radio config |
| Network engineer | 56 | 150 | **8,400** | Router, DHCP, QoS, air gap, DNS/NTP |
| Tower / mast crew | 64 | 180 | **11,520** | Climb/install (or contractor lump) |
| Systems admin (apps) | 40 | 130 | **5,200** | PBX, chat, mail build |
| Field tech | 32 | 95 | **3,040** | Cabling, grounding, test assist |
| Documentation / training | 16 | 110 | **1,760** | As-builts, SOP handoff |

**Labor subtotal (EOC): $43,200**

---

## 4. Travel / misc

| Item | Extended $ |
|------|-----------:|
| Contingency materials (5% of hardware) | **2,082** |
| Permits / structural review allowance | **2,500** |

**Misc subtotal (EOC): $4,582**

---

## 5. EOC node total

| Category | Amount $ |
|----------|----------:|
| Hardware & materials | 41,640 |
| Software & authorization | 3,200 |
| Labor / resources | 43,200 |
| Misc / contingency | 4,582 |
| **EOC NODE TOTAL** | **$92,622** |

**Budget band:** ~**$65k–$120k** (mast reuse vs new tower dominates).

---

## 6. Resource roster (who)

| Resource | Count | Source |
|----------|------:|--------|
| Project manager | 1 | County IT / EMA or contractor |
| RF engineer | 1 | Radio vendor or consultant |
| Network engineer | 1 | County IT / contractor |
| Tower crew | 2–3 | Licensed contractor |
| Systems admin | 1 | EMA / IT |
| Field tech | 1–2 | EMA / contractor |
