# EOC Node Configuration Instructions
## 102 Chief Williams Dr, Kathleen, GA — Air-Gapped Hub

| Field | Value |
|-------|--------|
| Role | Hub + application host |
| Band | 420–450 MHz |
| LAN subnet (example) | `10.40.0.0/24` |
| Mesh transfer (example) | `10.40.10.0/28` |
| Isolation | **Air-gapped** — no Internet / no production-LAN bridge |
| Related doc | `420-450MHz_RF_Mesh_Architecture.md` |

---

## 1. Purpose

Configure the EOC as the **central node** of the three-site RF mesh so that:

- Emory Warner Robins and Emory Perry can reach **VoIP, chat, and email** hosted here  
- IP addressing, DNS, and NTP for the enclave are served from the EOC  
- The node **never** gains a path to the public Internet or county/hospital production networks  

---

## 2. Equipment to configure (EOC)

| Item | Function |
|------|----------|
| Tower/mast + 2× Yagi (+ optional omni) | RF paths to WR and Perry |
| 420–450 MHz mesh IP radio | Wireless IP transport |
| Hardline, polyphasers, ground | RF plant |
| Edge router / firewall | Routing, DHCP, QoS, air gap |
| Managed PoE switch | Enclave LAN |
| SIP PBX host | VoIP server |
| Chat + internal mail host | Chat & email servers |
| Local DNS / NTP (may share app host) | Name & time |
| UPS + generator circuit | Power survivability |
| Continuity workstations | Local clients |

---

## 3. Pre-configuration checklist

- [ ] Part 90 / agency frequency authorization for **420–450 MHz** on hand  
- [ ] Mast height target **100–150 ft AGL**; Yagis aimed at WR and Perry  
- [ ] No WAN/ISP/cellular modem cable present on enclave switch or router  
- [ ] IP address plan approved (see §4)  
- [ ] UPS/generator tested  
- [ ] Offline software media for PBX, chat, mail, router firmware  

---

## 4. IP address plan (EOC example)

| Device | Address | Method |
|--------|---------|--------|
| Edge router LAN gateway | `10.40.0.1/24` | Static |
| Mesh radio (LAN side) | `10.40.0.2/24` | Static |
| SIP PBX | `10.40.0.10/24` | Static |
| Chat server | `10.40.0.11/24` | Static |
| Mail host (or shared w/ chat) | `10.40.0.12/24` | Static |
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

### Step 3 — Mesh radio

1. Set radio to authorized **420–450 MHz** channel(s); planning center **435 MHz** if unused for final assign.  
2. Configure node ID / mesh ID shared with hospital radios.  
3. Set Ethernet IP `10.40.0.2/24`, gateway `10.40.0.1` (or vendor bridge mode per design).  
4. Aim/align Yagis; record RSSI/SNR.  
5. Lock admin password; disable open join / guest modes.  
6. Verify Layer-3 reachability to hospital radio peers after hospitals are online.

### Step 4 — Local DNS & NTP

1. Install/configure DNS on `10.40.0.13` with internal zone (example):  
   - `pbx.mesh.local` → `10.40.0.10`  
   - `chat.mesh.local` → `10.40.0.11`  
   - `mail.mesh.local` → `10.40.0.12`  
2. Configure NTP as **local stratum** (or GPS-disciplined clock with **no** Internet IP path).  
3. Point EOC workstations at this DNS/NTP.

### Step 5 — SIP PBX (VoIP)

1. Install on-prem PBX on `10.40.0.10` (no cloud trunk, no Internet registration).  
2. Create extensions for EOC and both hospitals.  
3. Codecs: prefer **Opus 16–24 kbps** or **G.729**.  
4. Bind SIP to enclave IP only.  
5. Allow SIP/RTP only from `10.40.0.0/24`, `10.40.1.0/24`, `10.40.2.0/24`.  
6. Test EOC softphone registration to PBX on LAN before RF tests.

### Step 6 — Chat server

1. Install on-prem chat on `10.40.0.11`.  
2. Disable federation, external auth, and file uploads larger than policy allows.  
3. Create accounts for EOC and hospital continuity users.  
4. Publish URL/host via internal DNS only.

### Step 7 — Internal email

1. Install internal mail/webmail on `10.40.0.12` (or shared host).  
2. Create enclave-only mailboxes.  
3. **Disable** outbound Internet SMTP/IMAP.  
4. Set attachment size limits (e.g. 1–5 MB); queue/defer under voice load if tooling allows.  
5. Prefer webmail for low chatty traffic on RF.

### Step 8 — EOC continuity workstations

1. Connect to enclave switch only.  
2. Obtain DHCP address from EOC router **or** assign static in workstation range.  
3. Install softphone → register to `pbx.mesh.local` / `10.40.0.10`.  
4. Install chat client → `chat.mesh.local`.  
5. Open webmail → `mail.mesh.local`.  
6. Confirm DNS is EOC-local only.

### Step 9 — NMS / monitoring

1. Monitor router, radio, PBX, UPS via enclave IPs.  
2. Alert on RF link down, high jitter, UPS on battery.  
3. No cloud telemetry agents.

---

## 6. Air-gap verification (EOC)

- [ ] `show ip route` / equivalent: **no** default via Internet  
- [ ] No cellular/satellite modem on enclave switch  
- [ ] Traceroute to `8.8.8.8` or public DNS **fails**  
- [ ] Hospital production LAN not reachable from enclave  
- [ ] PBX/chat/mail resolve only on `.mesh.local` / EOC DNS  
- [ ] Patches applied from offline media only  

---

## 7. Acceptance tests (EOC-led)

1. EOC softphone registers to PBX.  
2. Ping hospital mesh peer IPs when spokes are up.  
3. Place VoIP call EOC ↔ WR and EOC ↔ Perry; check MOS/jitter.  
4. Chat message EOC ↔ each hospital.  
5. Send internal email while a call is active — voice remains usable.  
6. Confirm email cannot leave to public Internet.  

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
| PBX version | |
| Chat/mail versions | |
| Sign-off | |

---

*EOC hub configuration — air-gapped 420–450 MHz RF mesh*
