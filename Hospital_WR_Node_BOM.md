# Emory Warner Robins Node — Priced & Resourced BOM
## 1601 Watson Blvd, Warner Robins, GA (Spoke)

| Field | Value |
|-------|--------|
| Node | Emory Hospital Warner Robins |
| Band | 420–450 MHz (**ham / 70 cm** radios) |
| Apps (clients) | **SIP VoIP phones** · MeshChat · Citadel |
| Enclave subnet (example) | `10.40.1.0/24` |
| Estimate class | Planning / budgetary (±30%) |
| Currency | USD |
| Date | 2026-03-11 |

**Base = gear only.** **Antenna work** and **labor** are **OPTIONAL**.

---

## 1. Base hardware (REQUIRED)

| Qty | Item | Unit $ | Extended $ | Notes |
|----:|------|-------:|-----------:|-------|
| 1 | Ham 70 cm / 420–450 MHz mobile or base radio | 550 | **550** | Standard amateur UHF |
| 1 | Power supply 13.8 V (if base) | 120 | **120** | Omit if vehicle/mobile PSU not needed |
| 1 | Ham Yagi 420–450 MHz (10–14 dBi class) | 130 | **130** | Materials; aim EOC |
| 1 | Coax, connectors, arrestor kit | 220 | **220** | Materials only |
| 1 | Edge router / firewall (QoS, DHCP) | 250 | **250** | Enclave gateway |
| 1 | Small PoE GbE switch (or + injectors) | 100 | **100** | Enclave + phones |
| 1 | Radio–IP interface kit (if used) | 200 | **200** | Match EOC design |
| 1 | UPS (small) | 150 | **150** | |
| 2 | **SIP VoIP desk phones** (PoE) | 100 | **200** | FreePBX ext **2001, 2002** |
| 2 | Continuity PC / thin client | 450 | **900** | MeshChat + Citadel |
| 1 | Patch cords, labels, shelf | 80 | **80** | |

**Base hardware subtotal (WR): $2,900**

### Optional RF backup to Perry (not in base)

| Qty | Item | Extended $ |
|----:|------|-----------:|
| 1 | Extra ham UHF radio + Yagi materials | **680** |

---

## 2. Base software (REQUIRED)

| Qty | Item | Extended $ | Notes |
|----:|------|-----------:|-------|
| — | FreePBX / MeshChat / Citadel **clients** | **0** | Servers at EOC only |
| 1 | Offline browser/client install media | **25** | |

**Base software subtotal (WR): $25**

---

## 3. WR BASE TOTAL (no antenna work, no labor)

| Category | Amount $ |
|----------|----------:|
| Hardware | 2,900 |
| Software | 25 |
| **WR BASE TOTAL** | **$2,925** |

---

## 4. OPTIONAL — Antenna work

| Qty | Item | Extended $ | Notes |
|----:|------|-----------:|-------|
| 1 | Roof mast / tripod allowance | **1,200** | Height still recommended |
| 1 | Antenna mount, aim, weatherseal labor | **1,800** | Roof crew |
| 1 | Grounding install labor | **300** | |
| 1 | Hospital roof / Biomed review allowance | **750** | |

**Optional antenna work (WR): $4,050**

---

## 5. OPTIONAL — Labor / resources

| Role | Hours | Rate $/hr | Extended $ | Tasks |
|------|------:|----------:|-----------:|--------|
| Project coordinator | 8 | 100 | **800** | Access, schedule |
| RF / radio tech | 12 | 95 | **1,140** | Program, align assist |
| Network admin | 12 | 110 | **1,320** | Router, DHCP, air gap, clients |
| Field tech | 12 | 85 | **1,020** | Closet, phones, PCs |
| Hospital escort | 8 | 100 | **800** | Facilities/Biomed |
| User training | 4 | 90 | **360** | FreePBX / MeshChat / Citadel |

**Optional labor (WR): $5,440**

---

## 6. Totals — choose package

| Package | Amount $ |
|---------|----------:|
| **A — Base only** | **$2,925** |
| **B — Base + antenna work** | **$6,975** |
| **C — Base + labor** | **$8,365** |
| **D — Base + antenna work + labor (full)** | **$12,415** |
