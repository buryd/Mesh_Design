# Hospital Node Configuration Instructions
## Emory Warner Robins & Emory Perry — Air-Gapped Spokes

| Field | Value |
|-------|--------|
| Role | Spoke / client node |
| Band | 420–450 MHz (**standard ham / 70 cm** radios) |
| Hub apps | **FreePBX** · **MeshChat** · **Citadel** at EOC |
| Hub | EOC Kathleen (`10.40.0.0/24`) |
| Isolation | **Air-gapped** — no Internet / no EHR or production-LAN bridge |
| Related docs | `420-450MHz_RF_Mesh_Architecture.md`, `EOC_Node_Configuration.md`, hospital BOMs |

Use this procedure at **both** hospital sites. Only the **subnet, aiming azimuth, and site name** change.

---

## 1. Purpose

Configure each hospital so that:

- Continuity **FreePBX softphones, MeshChat, and Citadel** clients join a **hospital enclave subnet**  
- That subnet reaches **EOC-hosted FreePBX / MeshChat / Citadel** over the RF mesh  
- The hospital node **never** bridges into EHR/clinical LAN, guest Wi‑Fi, or the Internet  

Hospitals **do not** host FreePBX, MeshChat, or Citadel servers — they host **clients only**.

---

## 2. Site identity

| Site | Address | Enclave LAN (example) | Mesh peer (example) |
|------|---------|------------------------|---------------------|
| **Emory Hospital Warner Robins** | 1601 Watson Blvd, Warner Robins, GA 31093 | `10.40.1.0/24` | `10.40.10.2/30` (pairs with EOC `10.40.10.1`) |
| **Emory Hospital Perry** | 1120 Morningside Dr, Perry, GA 31069 | `10.40.2.0/24` | `10.40.10.6/30` (pairs with EOC `10.40.10.5`) |

**Antenna aim:** Yagi toward **EOC — 102 Chief Williams Dr, Kathleen**  
**Height:** roof + mast → **60–100 ft AGL** total  

---

## 3. Equipment to configure (each hospital)

| Item | Function |
|------|----------|
| Roof mast (optional BOM) | Antenna height |
| Ham Yagi 420–450 MHz | Directed link to EOC |
| Standard ham 70 cm radio | UHF link to EOC |
| Coax, arrestor, ground | RF plant |
| Edge router / firewall | Gateway, **DHCP**, QoS, air gap |
| Small GbE switch | Enclave VLAN only |
| UPS | Power |
| Softphones / ATAs | **FreePBX** clients |
| PCs / thin clients | **MeshChat** + **Citadel** |
| Optional 2nd ham radio + Yagi | Only if WR↔Perry backup path is built |

---

## 4. Pre-configuration checklist

- [ ] Facilities / Biomed approval for roof mast and RF install  
- [ ] Confirmed **no** trunk/patch into EHR or hospital Internet edge  
- [ ] Ham / authorized frequencies match EOC channel plan (Part 97 or other)  
- [ ] EOC hub already configured (or coordinated cutover window)  
- [ ] IP plan for this site filled (§5)  
- [ ] Continuity room/locations identified for phones and PCs  

---

## 5. IP address plan (per hospital)

### 5.1 Emory Warner Robins (`10.40.1.0/24`)

| Device | Address | Method |
|--------|---------|--------|
| Edge router LAN gateway | `10.40.1.1/24` | Static |
| Mesh radio (LAN side) | `10.40.1.2/24` | Static |
| Mesh link to EOC | `10.40.10.2/30` | Static |
| Softphones / ATAs / PCs | `10.40.1.50`–`10.40.1.200` | **DHCP from edge router** |

### 5.2 Emory Perry (`10.40.2.0/24`)

| Device | Address | Method |
|--------|---------|--------|
| Edge router LAN gateway | `10.40.2.1/24` | Static |
| Mesh radio (LAN side) | `10.40.2.2/24` | Static |
| Mesh link to EOC | `10.40.10.6/30` | Static |
| Softphones / ATAs / PCs | `10.40.2.50`–`10.40.2.200` | **DHCP from edge router** |

**DHCP options (both sites):**  
- Gateway = site `.1`  
- DNS = **`10.40.0.13`** (EOC local — via RF)  
- NTP = **`10.40.0.13`** (EOC local)  

**Do not** point DNS/NTP at hospital enterprise or public resolvers.

---

## 6. Configuration sequence

### Step 1 — Physical & RF plant

1. Install roof mast; mount **Yagi aimed at Kathleen EOC**.  
2. Install hardline, polyphaser, bond to building ground.  
3. Mount mesh radio; connect coax and Ethernet to enclave closet.  
4. Keep all enclave cabling on **dedicated** switch/ports — label **MESH ENCLAVE ONLY**.  
5. Record AGL, azimuth, and photos for the path survey file.

### Step 2 — Edge router / firewall (air gap)

1. Set LAN:  
   - WR: `10.40.1.1/24`  
   - Perry: `10.40.2.1/24`  
2. Set mesh-facing interface to the /30 peer address for this site.  
3. **No default route to the Internet.**  
4. Add route to EOC services:  
   - Destination `10.40.0.0/24` via EOC mesh peer  
5. (Optional) Add route to other hospital only if backup WR↔Perry RF path exists.  
6. Enable **DHCP server** on LAN:  
   - WR pool `10.40.1.50–200`  
   - Perry pool `10.40.2.50–200`  
   - DNS/NTP options → `10.40.0.13`  
7. Firewall:  
   - Allow enclave clients → EOC PBX / chat / mail / DNS / NTP  
   - Allow return traffic  
   - **Deny** all interfaces connected to hospital production/EHR/guest  
   - Deny public Internet ranges  
8. QoS toward RF: VoIP (SIP/RTP) > chat > control > email (rate-limit).

### Step 3 — Ham UHF radio

1. Match EOC **420–450 MHz** frequency/mode plan.  
2. If using radio–IP gateway, set Ethernet IP to site `.2` (WR `10.40.1.2` / Perry `10.40.2.2`).  
3. Align Yagi to EOC (if antenna work performed); record signal.  
4. Only licensed/authorized operators transmit.  
5. Confirm reachability to EOC gateway `10.40.0.1` and FreePBX `10.40.0.10`.

### Step 4 — Enclave switch

1. Create/use VLAN dedicated to mesh continuity.  
2. Connect: router LAN, radio/gateway Ethernet, phones, PCs, UPS mgmt (optional).  
3. **Do not** uplink this VLAN to hospital core / EHR.  
4. Label ports clearly.

### Step 5 — FreePBX phones / ATAs

1. Connect phone to enclave switch.  
2. Phone obtains IP by **DHCP from hospital edge router** (or rare static in client range).  
3. Set SIP server to **FreePBX**: `pbx.mesh.local` or `10.40.0.10`.  
4. Enter extension/credentials issued by EOC.  
5. Codec preference: Opus or G.729.  
6. Verify registration **through RF** to EOC FreePBX (not to any hospital PBX).

### Step 6 — MeshChat & Citadel clients

1. Connect PC to enclave switch only (or enclave-only NIC).  
2. Confirm DHCP address on hospital enclave subnet.  
3. **MeshChat** → `chat.mesh.local` / `10.40.0.11`.  
4. **Citadel** → `mail.mesh.local` / `10.40.0.12`.  
5. Confirm DNS queries go to `10.40.0.13` (EOC).  
6. Disable OS auto-update to Internet; use offline patch SOP.

### Step 7 — Optional WR↔Perry backup (Phase D)

Only if authorized:

1. Add second Yagi aimed at the other hospital.  
2. Add second radio or dual-link config.  
3. Add router route for the other hospital subnet via that backup peer.  
4. Prefer EOC hub for voice; use backup for failover/chat as designed.

---

## 7. What the hospital node does **not** run

| Service | Where it runs |
|---------|----------------|
| FreePBX | **EOC only** |
| MeshChat | **EOC only** |
| Citadel | **EOC only** |
| Authoritative DNS / NTP | **EOC only** |

Hospital gear = **clients + edge router + ham radio + switch + UPS**.

---

## 8. Air-gap verification (each hospital)

- [ ] No cable from enclave switch to EHR/core/Internet edge  
- [ ] Router has **no** Internet default route  
- [ ] DHCP issues only enclave addresses  
- [ ] Phone DNS = EOC `10.40.0.13`  
- [ ] Cannot browse public websites from enclave PC  
- [ ] Cannot reach hospital clinical subnets from enclave PC  
- [ ] Softphone registers to EOC **FreePBX** only  

---

## 9. Acceptance tests (per hospital)

1. Ping EOC gateway `10.40.0.1` and FreePBX `10.40.0.10`.  
2. Softphone registers; call EOC continuity phone.  
3. Second call while **MeshChat** message sent — voice stays usable.  
4. Send **Citadel** mail to EOC mailbox; confirm delivery; confirm **no** Internet send.  
5. Fail RF briefly — document recovery when link returns.  
6. Log signal reports and leave copy at EOC and hospital.

---

## 10. Site configuration record (fill in)

| Item | Warner Robins | Perry |
|------|---------------|-------|
| Date / tech | | |
| Radio model / serial | | |
| Antenna AGL (ft) | | |
| Azimuth to EOC (°) | | |
| RSSI / SNR to EOC | | |
| Router LAN IP | `10.40.1.1` | `10.40.2.1` |
| DHCP pool | `10.40.1.50–200` | `10.40.2.50–200` |
| Extensions / users tested | | |
| Air-gap checks passed (Y/N) | | |
| Sign-off | | |

---

## 11. Quick reference — DHCP for a hospital VoIP phone

```text
Phone → Enclave switch → Hospital edge router (DHCP)
                              ↓
                     IP from 10.40.x.50–200
                     GW  = 10.40.x.1
                     DNS = 10.40.0.13 (EOC)
                              ↓
                     SIP register → 10.40.0.10 (FreePBX @ EOC) via ham UHF / IP path
```

---

*Hospital spoke configuration — air-gapped ham 420–450 MHz · FreePBX / MeshChat / Citadel*
