# 420–450 MHz RF Mesh Network Architecture
## Houston County EMA Continuity Links — VoIP, Chat, Email

| Field | Value |
|-------|--------|
| Sites | EOC (Kathleen), Emory Hospital Warner Robins, Emory Hospital Perry |
| Band | **420–450 MHz** (licensed / authorized UHF; coordinate exact channels) |
| Topology | Hub-and-spoke RF mesh with optional cross-link |
| Apps | VoIP, Chat, Email |
| Version | 1.1 |
| Date | 2026-03-11 |

---

## 1. Mission

Provide resilient, county-controlled IP connectivity among:

1. **EOC** — 102 Chief Williams Dr, Kathleen, GA 31047  
2. **Emory Hospital Warner Robins** — 1601 Watson Blvd, Warner Robins, GA 31093  
3. **Emory Hospital Perry** — 1120 Morningside Dr, Perry, GA 31069  

for **voice (VoIP)**, **chat**, and **email** when commercial networks are degraded or unavailable.

---

## 2. Design Principles

1. **EOC is the hub** — Kathleen sits between the hospitals; applications terminate/relay at the EOC.  
2. **Directional RF on long hops** — Yagi (or sector) links for EOC↔hospital; not omni-to-omni for primary paths.  
3. **Mesh for resilience** — fixed nodes can relay; optional WR↔Perry backup; portables may join via EOC omni.  
4. **Bandwidth discipline** — 420–450 MHz UHF is capacity-limited; QoS protects voice; email is store-and-forward.  
5. **RF is transport only** — SIP, chat, and mail are standard IP apps behind routers/VPN.  
6. **Licensed / authorized operation** — FCC (or federal) authorization in **420–450 MHz**, EIRP limits, and coordination are mandatory.

---

## 3. High-Level Architecture

```
                    ┌─────────────────────────────────────┐
                    │     EOC Kathleen (HUB + APPS)        │
                    │  SIP PBX · Chat · Mail Relay · NMS  │
                    │  Edge Router (QoS/VPN) · UPS/Gen    │
                    │  420–450 MHz Mesh Node              │
                    │  Yagi→WR | Yagi→Perry | Omni fill   │
                    └──────────────┬──────────────────────┘
                                   │
                 ┌─────────────────┼─────────────────┐
                 │ ~8–10 mi        │                 │ ~7–9 mi
                 ▼                 │                 ▼
    ┌────────────────────┐        │      ┌────────────────────┐
    │ Emory Warner Robins│        │      │   Emory Perry      │
    │ Mesh Node + Router │◄───────┴─────►│ Mesh Node + Router │
    │ Yagi → EOC         │  optional     │ Yagi → EOC         │
    │ Softphone / Chat   │  backup hop   │ Softphone / Chat   │
    └────────────────────┘  ~15–20 mi    └────────────────────┘
```

### Logical layers

| Layer | Function |
|-------|----------|
| **L0 Site** | Mast, grounding, power, weatherproofing |
| **L1 RF Mesh** | 420–450 MHz IP mesh radios, antennas |
| **L2/L3 Transport** | Bridged or routed mesh; site subnets |
| **L4 Security** | Site-to-site VPN, firewall |
| **L5 Apps** | SIP VoIP, chat, email |
| **L6 Ops** | Monitoring, spares, SOP, training |

---

## 4. RF Mesh Topology

### 4.1 Primary paths (always up)

| Link | Distance (approx.) | Mode | Role |
|------|--------------------|------|------|
| EOC ↔ Emory WR | 8–10 mi | Directed mesh / PTP-style | Primary |
| EOC ↔ Emory Perry | 7–9 mi | Directed mesh / PTP-style | Primary |

### 4.2 Secondary path (optional)

| Link | Distance (approx.) | Mode | Role |
|------|--------------------|------|------|
| Emory WR ↔ Emory Perry | 15–20 mi | Directed | Failover / relay if EOC RF fails |

### 4.3 Tactical extension

| Link | Mode | Role |
|------|------|------|
| EOC omni ↔ portable UHF nodes | Mesh client | Parking lot / field chat & limited voice |

### 4.4 Mesh behavior

- **Infrastructure mesh:** three fixed nodes form the core.  
- **Hub preference:** traffic defaults via EOC (shortest admin path to apps).  
- **Self-healing:** if EOC↔WR fails and WR↔Perry + EOC↔Perry exist, WR may reach EOC via Perry (higher latency — voice secondary).  
- **No consumer Wi-Fi mesh** on the inter-facility hops.

---

## 5. RF Parameters

### 5.1 Band and licensing

- **Operating band:** **420–450 MHz** only (tune/order radios and antennas for this range).  
- **Planning center frequency:** **435 MHz** (mid-band) for link-budget and antenna VSWR checks; final channels per authorization.  
- **Prefer:** spectrally efficient UHF IP/mesh radios certified for **420–450 MHz** (wider channel or MIMO UHF) over single 12.5 kHz FM if multi-call VoIP is required.  
- **Authorization:** obtain lawful authority before transmit — this segment includes **federal** and **amateur (70 cm)** allocations; Houston County must use channels it is eligible to hold (e.g., federal/NTIA assignment, appropriate FCC license, or other approved sharing). Document **call sign / agency ID, exact frequencies, bandwidth, max EIRP**.  
- **Do not** operate on amateur spectrum under Part 97 for this governmental mesh unless a separate, lawful amateur-aux plan is explicitly approved (out of scope for hospital/EOC continuity).

### 5.2 Radio plant (per fixed site)

| Item | Specification |
|------|----------------|
| Radio | Outdoor **420–450 MHz** IP mesh / fixed wireless router (authorized service) |
| TX power | Up to **5 W (37 dBm)** subject to authorization |
| Duplex | As supported (TDD mesh typical) |
| Interfaces | Ethernet to site router; PoE or DC |
| Environmental | IP67-class outdoor or radio in NEMA enclosure |

### 5.3 Antennas and height AGL

| Site | Antenna | Gain | Height AGL | Aim |
|------|---------|------|------------|-----|
| **EOC Kathleen** | 2× Yagi (or 1–2 sectors) | 10–12 dBi | **100–150 ft** (min 80 ft) | Toward WR; toward Perry |
| **EOC Kathleen** | Collinear omni (optional) | 5–8 dBi | Below / clear of Yagis | Local portables |
| **Emory WR** | 1× Yagi | 10–14 dBi | **60–100 ft** (roof + 20–40 ft mast) | Toward EOC |
| **Emory Perry** | 1× Yagi | 10–14 dBi | **60–100 ft** (roof + 20–40 ft mast) | Toward EOC |

- Polarization: **vertical**, matched end-to-end.  
- Feedline: **½″ or ⅞″ hardline**; minimize length.  
- Protect: bulkhead polyphasers, bonded ground, drip loops.

### 5.4 Link budget summary (planning)

Assumes 5 W, ~11–12 dBi Yagis tuned for **420–450 MHz**, ~4.5 dB total line/misc loss, planning frequency **435 MHz**.

| Link | Clear LOS Prx | Light trees (−10 dB) | Moderate (−20 dB) | Multi-svc VoIP viable? |
|------|---------------|----------------------|-------------------|-------------------------|
| EOC–WR | ~−53 dBm | ~−63 dBm | ~−73 dBm | Yes if clutter ≤ ~20 dB |
| EOC–Perry | ~−52 dBm | ~−62 dBm | ~−72 dBm | Yes if clutter ≤ ~20 dB |
| WR–Perry | ~−59 dBm | ~−69 dBm | ~−79 dBm | Backup / degraded only |

**Target fade margin:** ≥ 20 dB for multi-service VoIP.

---

## 6. IP Network Architecture

### 6.1 Addressing (example — replace with county standard)

| Site | LAN subnet | RF/mesh transfer |
|------|------------|------------------|
| EOC | 10.40.0.0/24 | 10.40.10.0/28 |
| Emory WR | 10.40.1.0/24 | 10.40.10.0/28 |
| Emory Perry | 10.40.2.0/24 | 10.40.10.0/28 |

- Mesh cloud: single L2 broadcast domain **or** routed (/30 or OSPF/BGP-lite per vendor).  
- **Recommended:** **routed** sites + VPN overlays (cleaner QoS and failure domains).

### 6.2 Site edge kit (all three)

1. 420–450 MHz mesh radio  
2. Ethernet to **firewall/router** with QoS  
3. Managed PoE switch (small)  
4. UPS (EOC: UPS + generator preferred)  
5. Time sync (NTP from EOC)

### 6.3 Security

- **IPsec or WireGuard** site-to-site (hospital ↔ EOC).  
- No open management on RF SSID/mesh without auth.  
- Separate **ops** and **user** VLANs where practical.  
- Hospital traffic subject to **HIPAA** controls (encryption in transit, access logging).  
- Do not bridge raw hospital EHR LANs onto the mesh — only designated continuity endpoints.

---

## 7. Application Architecture

### 7.1 Placement

| Application | Primary host | Hospital clients |
|-------------|--------------|------------------|
| **SIP PBX / registrar** | EOC | Softphones or ATAs on continuity VLAN |
| **Chat server** | EOC | Desktop/mobile clients on continuity VLAN |
| **Email** | EOC mail relay / webmail | MUA or webmail via VPN |
| **DNS / NTP** | EOC | Point hospitals at EOC |

### 7.2 VoIP

- Codec: **Opus 16–24 kbps** or **G.729**.  
- Concurrent calls: design for **2–4** across the mesh.  
- QoS: DSCP **EF** for RTP; prioritize SIP signaling.  
- Media: prefer **hospital phone ↔ EOC PBX** (one RF hop). Avoid phone-to-phone hairpin across two RF hops when possible.  
- Survivability: EOC PBX on UPS/gen; optional FXO/FXS to radio patch only if required by SOP.

### 7.3 Chat

- Lightweight self-hosted stack (e.g. Mattermost / Matrix / XMPP).  
- Disable rich media / large file transfer on RF SSID.  
- Keep presence refresh conservative.

### 7.4 Email

- **Store-and-forward** at EOC.  
- Size limits (e.g. 1–5 MB); strip/block large attachments on RF path.  
- Queue and send when voice load is low; never starve RTP.  
- Optional: webmail only (less chatty than sync IMAP).

### 7.5 QoS policy (edge routers)

| Priority | Traffic | Treatment |
|----------|---------|-----------|
| 1 | SIP + RTP | Highest / EF / reserved bandwidth |
| 2 | Chat | Assured forwarding |
| 3 | VPN/control / NMS | Assured |
| 4 | Email | Best effort / rate-limited |
| 5 | Bulk / other | Lowest / blocked on RF |

---

## 8. Capacity Model

| Service | Budget each | Aggregate planning |
|---------|-------------|--------------------|
| VoIP (×3 calls) | ~24–40 kbps up/down each | ~100–150 kbps |
| Chat | ~5–20 kbps | ~20 kbps |
| Email | Bursty | Cap **50–100 kbps** when calls active |
| Overhead (VPN, mesh, IP) | — | +20–40% |

**Minimum useful RF throughput:** ~**300–500 kbps** stable bidirectional per spoke for comfortable multi-service; **~100–150 kbps** absolute floor for 1 call + chat.

If licensed channel only supports tens of kbps: **1 VoIP + chat**; email off-peak only.

---

## 9. Physical Architecture per Site

### 9.1 EOC Kathleen (hub)

- Mast/tower **100–150 ft AGL**  
- 2× Yagi (WR + Perry) + optional omni  
- Mesh node, core router/firewall, SIP + chat + mail, NMS  
- UPS + generator circuit  
- Spares: 1 radio, 1 Yagi, injectors, cables  

### 9.2 Emory WR & Emory Perry (spokes)

- Roof + mast **60–100 ft AGL** total  
- 1× Yagi to EOC (optional 2nd Yagi toward other hospital for backup)  
- Mesh node, edge router, UPS  
- Continuity workstation(s): softphone + chat + webmail  
- Biomed/Facilities-approved mount and grounding  

---

## 10. Operations

### 10.1 Monitoring

- SNMP/ICMP from EOC NMS to radios and routers  
- Alert: RF link down, high latency/jitter, UPS on battery  
- Weekly test call WR→EOC and Perry→EOC  

### 10.2 Acceptance tests

1. RSSI/SNR vs link-budget prediction  
2. iperf or equivalent throughput floor  
3. Three concurrent G.729/Opus calls + chat — MOS/jitter check  
4. Email send while calls active — voice must hold  
5. Failover: disable EOC↔WR; confirm backup path behavior (if built)  

### 10.3 SOP

- Who may use continuity phones/chat  
- Call priority during incidents  
- Attachment policy on email  
- Outage escalation to radio tech / IT  

---

## 11. Bill of Materials (logical)

| Qty | Item |
|-----|------|
| 3 | **420–450 MHz** outdoor mesh/IP radios (fixed) |
| 1 | Spare radio (420–450 MHz) |
| 4–5 | Yagi antennas 10–14 dBi, **420–450 MHz** (incl. spare) |
| 1 | Omni 5–8 dBi, **420–450 MHz** (EOC optional) |
| 3 | Edge firewall/routers with QoS |
| 3 | UPS systems (EOC sized for gen transfer) |
| Lot | Hardline, grounding, polyphasers, NEMA, masts |
| 1 | SIP PBX + chat server + mail relay (EOC VMs/appliances) |
| Lot | Softphones/ATAs for continuity positions |
| 1 | NMS / logging |

*Exact vendor SKUs depend on certification for **420–450 MHz**, lawful channel assignment, and channel width available to Houston County.*

---

## 12. Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| Insufficient mast height / trees | High jitter, lost calls | Meet AGL targets; path survey; county tower |
| Narrow channel only | Cannot multi-call | Efficient codecs; limit calls; seek wider authorization |
| Hospital RF/EMI restrictions | Delay install | Early Biomed engagement |
| License / EIRP cap | Lower margin | Higher antennas/gain; lower data rate modes |
| No eligible **420–450 MHz** channels | Cannot transmit legally | Confirm federal/FCC eligibility before procurement |
| Mesh relay path | Latency hurts VoIP | Prefer hub paths; relay = chat/backup voice |
| Security/HIPAA | Compliance failure | VPN, endpoint control, no raw LAN bridge |

---

## 13. Phased Deployment

| Phase | Scope | Outcome |
|-------|--------|---------|
| **A** | Path survey + temporary mast test EOC↔WR and EOC↔Perry | Go/no-go on heights |
| **B** | Permanent RF + routers + SIP/chat at EOC; 1 client each hospital | VoIP + chat live |
| **C** | Email relay + QoS hardening + monitoring | Full app set |
| **D** | Optional WR↔Perry Yagis + portable omni kit | Failover + tactical |

---

## 14. Architecture Decision Record

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Band | **420–450 MHz** authorized UHF | Range/foliage; fixed design band; county/federal control |
| Topology | EOC hub mesh | Geography; app centralization |
| Antennas | Yagi primary | Link budget at 7–10 mi |
| Apps host | EOC | One RF hop to services |
| Email | Store-and-forward | Protect VoIP |
| 5.8/CBRS | Out of scope here | Alternate if broadband added later |

---

## 15. Success Criteria

- Stable EOC↔WR and EOC↔Perry RF with ≥ **20 dB** planning margin class after survey.  
- **≥ 2** concurrent narrowband VoIP calls hub-spoke with acceptable MOS.  
- Chat usable during those calls.  
- Email delivers via EOC queue without dropping calls.  
- Documented SOP and weekly test completed.

---

*End of architecture — 420–450 MHz RF Mesh (3-site).*
