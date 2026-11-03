# EOC Node Configuration Instructions
## 102 Chief Williams Dr, Kathleen, GA — Air-Gapped Hub

| Field | Value |
|-------|--------|
| Role | Hub + application host |
| Band | 420–450 MHz (**standard ham / 70 cm** radios) |
| Apps | **FreePBX** · **MeshChat** · **Citadel** |
| LAN subnet (example) | `10.40.0.0/24` |
| Mesh transfer (example) | `10.40.10.0/28` |
| Isolation | **Air-gapped** — no Internet / no production-LAN bridge |
| Related doc | `420-450MHz_RF_Mesh_Architecture.md`, `EOC_Node_BOM.md` |

---

## 1. Purpose

Configure the EOC as the **central node** of the three-site RF mesh so that:

- Emory Warner Robins and Emory Perry can reach **FreePBX**, **MeshChat**, and **Citadel** hosted here  
- IP addressing, DNS, and NTP for the enclave are served from the EOC  
- The node **never** gains a path to the public Internet or county/hospital production networks  

---

## 2. Equipment to configure (EOC)

| Item | Function |
|------|----------|
| Mast + 2× ham Yagi (+ optional omni) | RF paths to WR and Perry (install optional per BOM) |
| Standard ham 420–450 MHz radios | UHF links (Part 97 / authorized operators) |
| Coax, arrestors, ground | RF plant |
| Edge router / firewall | Routing, DHCP, QoS, air gap |
| Small GbE switch | Enclave LAN |
| FreePBX host (mini PC) | VoIP server |
| MeshChat + Citadel host (or shared mini PC) | Chat & email |
| Local DNS / NTP (may share app host) | Name & time |
| UPS | Power survivability |
| Continuity workstations | Softphone, MeshChat, Citadel clients |

---

## 3. Pre-configuration checklist

- [ ] Lawful RF authority for **420–450 MHz** (typically **Part 97** ham licenses / club or other authorization)  
- [ ] Mast height target **100–150 ft AGL** if antenna work is performed; Yagis aimed at WR and Perry  
- [ ] No WAN/ISP/cellular modem cable present on enclave switch or router  
- [ ] IP address plan approved (see §4)  
- [ ] UPS tested  
- [ ] Offline media for **FreePBX**, **MeshChat**, **Citadel**, router firmware  

---

## 4. IP address plan (EOC example)

| Device | Address | Method |
|--------|---------|--------|
| Edge router LAN gateway | `10.40.0.1/24` | Static |
| Mesh radio (LAN side) | `10.40.0.2/24` | Static |
| FreePBX | `10.40.0.10/24` | Static |
| MeshChat | `10.40.0.11/24` | Static |
| Citadel (or shared w/ MeshChat) | `10.40.0.12/24` | Static |
| DNS / NTP / NMS | `10.40.0.13/24` | Static (or same as app host) |
| Mesh link toward WR | `10.40.10.1/30` (example) | Static |
| Mesh link toward Perry | `10.40.10.5/30` (example) | Static |
| Workstations / softphones | `10.40.0.50–10.40.0.200` | **DHCP** |

**DHCP pool on EOC router:** `10.40.0.50`–`10.40.0.200`  
**Exclude from pool:** `10.40.0.1`–`10.40.0.49` (static gear)

Gateway for all EOC LAN devices: `10.40.0.1`  
DNS for all enclave clients: `10.40.0.13` (EOC local)  
NTP: `10.40.0.13` (EOC local — **no** public NTP)

---

## 5. Configuration sequence

### Step 1 — Physical & RF plant

1. Mount Yagi toward Emory WR; mount Yagi toward Emory Perry; optional omni for portables.  
2. Install hardline, polyphasers, and single-point ground.  
3. Mount outdoor mesh radio; connect feedlines; weatherproof.  
4. Run Ethernet from radio to enclave switch/router (PoE/DC as required).  
5. Confirm antenna AGL and azimuth log entries.

### Step 2 — Edge router / firewall (air gap)

1. Set LAN interface: `10.40.0.1/24`.  
2. Set mesh/WAN-facing interfaces to hospital link subnets (e.g. `10.40.10.1/30`, `10.40.10.5/30`) — these are **RF peers only**, not Internet.  
3. **Do not** configure a default route to any ISP, cellular, or enterprise edge.  
4. Add routes (or dynamic routing) **only** to:  
   - `10.40.1.0/24` via WR mesh peer  
   - `10.40.2.0/24` via Perry mesh peer  
5. Enable **DHCP server** on LAN with pool `10.40.0.50–200`; options:  
   - Router/gateway = `10.40.0.1`  
   - DNS = `10.40.0.13`  
   - NTP = `10.40.0.13` (if supported)  
6. Firewall policy:  
   - Allow enclave LAN ↔ hospital subnets for SIP, RTP, chat, mail, DNS, NTP, NMS  
   - **Deny** any traffic toward unknown/public ranges  
   - Deny bridging to any non-enclave interface  
7. QoS (egress toward RF):  
   - Priority 1: SIP + RTP (EF)  
   - Priority 2: Chat  
   - Priority 3: Control / NMS  
   - Priority 4: Email (rate-limited)  

### Step 3 — Ham UHF radios

1. Program authorized **420–450 MHz** frequencies (planning center **435 MHz** if not yet assigned).  
2. Match tones/modes with hospital radios; document simplex or linked design.  
3. If using a radio–IP gateway (URI/AllStar-class), set Ethernet toward enclave switch; radio mgmt IP `10.40.0.2/24`, gateway `10.40.0.1` as applicable.  
4. Aim/align Yagis (if antenna work performed); record signal reports.  
5. Secure mic/control access; only licensed/authorized operators transmit.  
6. Verify end-to-end path to hospital nodes after spokes are online.

### Step 4 — Local DNS & NTP

1. Install/configure DNS on `10.40.0.13` with internal zone (example):  
   - `pbx.mesh.local` → `10.40.0.10` (**FreePBX**)  
   - `chat.mesh.local` → `10.40.0.11` (**MeshChat**)  
   - `mail.mesh.local` → `10.40.0.12` (**Citadel**)  
2. Configure NTP as **local stratum** (or GPS-disciplined clock with **no** Internet IP path).  
3. Point EOC workstations at this DNS/NTP.

### Step 5 — FreePBX (VoIP)

1. Install **FreePBX** on `10.40.0.10` (no cloud trunk, no Internet registration).  
2. Create extensions for EOC and both hospitals.  
3. Codecs: prefer **Opus 16–24 kbps**, **G.729**, or ulaw only if bandwidth allows.  
4. Bind SIP to enclave IP only.  
5. Allow SIP/RTP only from `10.40.0.0/24`, `10.40.1.0/24`, `10.40.2.0/24`.  
6. Test EOC softphone registration to FreePBX on LAN before RF tests.

### Step 6 — MeshChat

1. Install **MeshChat** on `10.40.0.11` (or shared host).  
2. Disable external federation / Internet features; limit file transfer size.  
3. Create accounts for EOC and hospital continuity users.  
4. Publish host via internal DNS only (`chat.mesh.local`).

### Step 7 — Citadel email

1. Install **Citadel** on `10.40.0.12` (or shared host with MeshChat).  
2. Create enclave-only mailboxes / rooms.  
3. **Disable** outbound Internet SMTP.  
4. Set attachment size limits (e.g. 1–5 MB).  
5. Prefer Citadel web access for lower RF chatter than sync clients.

### Step 8 — EOC continuity workstations

1. Connect to enclave switch only.  
2. Obtain DHCP address from EOC router **or** assign static in workstation range.  
3. Softphone → register to FreePBX at `pbx.mesh.local` / `10.40.0.10`.  
4. Open **MeshChat** → `chat.mesh.local`.  
5. Open **Citadel** → `mail.mesh.local`.  
6. Confirm DNS is EOC-local only.

### Step 9 — NMS / monitoring

1. Monitor router, radios, FreePBX, UPS via enclave IPs.  
2. Alert on RF link down, high jitter, UPS on battery.  
3. No cloud telemetry agents.

---

## 6. Air-gap verification (EOC)

- [ ] `show ip route` / equivalent: **no** default via Internet  
- [ ] No cellular/satellite modem on enclave switch  
- [ ] Traceroute to `8.8.8.8` or public DNS **fails**  
- [ ] Hospital production LAN not reachable from enclave  
- [ ] FreePBX / MeshChat / Citadel resolve only on `.mesh.local` / EOC DNS  
- [ ] Patches applied from offline media only  

---

## 7. Acceptance tests (EOC-led)

1. EOC softphone registers to **FreePBX**.  
2. Reach hospital peer IPs / radios when spokes are up.  
3. Place VoIP call EOC ↔ WR and EOC ↔ Perry; check audio quality.  
4. **MeshChat** message EOC ↔ each hospital.  
5. Send **Citadel** mail while a call is active — voice remains usable.  
6. Confirm Citadel cannot send to public Internet.  

---

## 8. Configuration record (fill in)

| Item | Value |
|------|--------|
| Date / tech | |
| Radio model / serial | |
| Authorized frequencies | |
| Yagi az/el WR | |
| Yagi az/el Perry | |
| RSSI/SNR WR link | |
| RSSI/SNR Perry link | |
| Router firmware | |
| FreePBX version | |
| MeshChat / Citadel versions | |
| Sign-off | |

---

*EOC hub configuration — air-gapped 420–450 MHz RF mesh*
