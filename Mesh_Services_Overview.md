# How the Mesh and Its Services Work
## Houston County Air-Gapped RF Continuity Network

| Field | Value |
|-------|--------|
| Sites | EOC Kathleen · Emory Warner Robins · Emory Perry |
| RF | 420–450 MHz (ham / 70 cm) |
| Apps | FreePBX · MeshChat · Citadel |
| Isolation | Air-gapped enclave (no Internet / no production LAN) |
| Detail docs | [Architecture](420-450MHz_RF_Mesh_Architecture.md) · [EOC Config](EOC_Node_Configuration.md) · [Hospital Config](Hospital_Node_Configuration.md) · [BOM Totals](BOM_Totals.md) |

---

## 1. What this system is

A **private three-site data network** that carries **voice, chat, and email** between the Emergency Operations Center and two hospitals when normal phones/Internet are down or must not be used.

It is **not** the public telephone network, hospital EHR, or the Internet. It is a standalone **enclave** linked only by radio.

```text
┌──────────────────┐     RF 420–450 MHz     ┌──────────────────┐
│ Emory Warner     │◄──────────────────────►│                  │
│ Robins           │                        │  EOC Kathleen    │
│  Phones + PCs    │                        │  FreePBX         │
└──────────────────┘                        │  MeshChat        │
                                            │  Citadel         │
┌──────────────────┐     RF 420–450 MHz     │  Hub radios      │
│ Emory Perry      │◄──────────────────────►│                  │
│  Phones + PCs    │                        └──────────────────┘
└──────────────────┘
```

---

## 2. Big picture: layers

| Layer | What it does |
|-------|----------------|
| **People & handsets** | Talk on SIP desk phones; use PCs for chat/mail |
| **Enclave LAN** | Small isolated switch/subnet at each building |
| **Edge router** | DHCP, firewall, QoS; **no** Internet route |
| **Ham UHF radios** | Carry IP (or radio–IP gateway) between sites |
| **EOC servers** | Host FreePBX, MeshChat, and Citadel |

Hospitals are **clients**. The EOC is the **hub and application host**.

---

## 3. The enclave LAN (per site)

Each site has its own **enclave LAN**: a closed local network that only mesh devices join.

| Site | Example subnet | Gateway (edge router) |
|------|----------------|------------------------|
| EOC | `10.40.0.0/24` | `10.40.0.1` |
| Emory WR | `10.40.1.0/24` | `10.40.1.1` |
| Emory Perry | `10.40.2.0/24` | `10.40.2.1` |

**On the enclave:** SIP phones, continuity PCs, router, radio/gateway, UPS (optional).  
**Not on the enclave:** hospital EHR, guest Wi‑Fi, office Internet PCs.

Phones and PCs usually get addresses by **DHCP from that site’s edge router**. Servers at the EOC use **static** IPs.

---

## 4. How RF connects the sites

1. Each site has **ham 420–450 MHz** radio(s) and a **Yagi** aimed along the path (EOC aims at both hospitals; hospitals aim at Kathleen).  
2. Radios (and optional radio–IP gateways) present an Ethernet path into the enclave switch/router.  
3. Edge routers **route** between the local subnet and the EOC subnet over that RF path.  
4. There is **no** path to the public Internet, cellular data, or hospital production LAN.

Optional later: a direct WR↔Perry backup radio hop if the EOC radio path fails.

---

## 5. How the services work

All three services run on **Linux mini PC(s) at the EOC**. Hospital users reach them over RF.

### 5.1 Voice — FreePBX + SIP desk phones

| Piece | Role |
|-------|------|
| **FreePBX** @ EOC (`10.40.0.10`) | Phone system (SIP registrar / call routing) |
| **SIP desk phones** | 2 at EOC, 2 at WR, 2 at Perry (6 total) |

**Call flow (hospital → EOC):**

```text
User dials on SIP phone
    → Phone has enclave IP (DHCP)
    → SIP signaling to FreePBX at EOC over RF
    → FreePBX rings target extension (e.g. EOC 1001)
    → RTP audio between phones (via FreePBX path)
```

**Example extensions**

| Site | Extensions |
|------|------------|
| EOC | 1001, 1002 |
| Emory WR | 2001, 2002 |
| Emory Perry | 3001, 3002 |

Voice is prioritized with **QoS** so chat/email do not starve calls. Codecs stay small (e.g. G.729/Opus) because ham UHF capacity is limited.

### 5.2 Chat — MeshChat

| Piece | Role |
|-------|------|
| **MeshChat** @ EOC (`10.40.0.11`) | Message server |
| Browser / client on continuity PC | User types messages |

**Flow:** PC on hospital enclave → RF → MeshChat at EOC → other users’ clients.  
No Internet federation; keep file transfers small.

### 5.3 Email — Citadel

| Piece | Role |
|-------|------|
| **Citadel** @ EOC (`10.40.0.12`) | Internal mail / groupware |
| Webmail (or client) on continuity PC | Read/send enclave mail |

**Flow:** User sends mail inside the island → stored/forwarded at EOC Citadel → recipients on the mesh.  
**No** outbound SMTP to the public Internet. Large attachments are limited so voice stays usable.

---

## 6. What happens in a typical incident

1. Operators power enclave gear (UPS/generator as available).  
2. Radios link EOC ↔ hospitals.  
3. Phones register to FreePBX; PCs open MeshChat and Citadel.  
4. Coordination uses **phone first**, chat second, email for longer notes.  
5. Nothing depends on Verizon/AT&T, hospital WAN, or cloud PBX.

---

## 7. Air gap (why it stays isolated)

| Rule | Meaning |
|------|---------|
| No Internet default route | Routers cannot reach the public web |
| No EHR/core trunk | Enclave switch not uplinked to clinical LAN |
| Apps only at EOC | No cloud FreePBX / Slack / Gmail |
| Offline updates | Patches via sneaker-net media only |
| Dedicated endpoints | Phones/PCs used only on the mesh |

DNS and time also come from the **EOC** (`10.40.0.13` example), not from public DNS/NTP.

---

## 8. Who does what

| Location | Provides | Does not provide |
|----------|----------|------------------|
| **EOC** | Radios, FreePBX, MeshChat, Citadel, DNS/NTP, 2 phones, ops PCs | — |
| **Each hospital** | Radio, enclave LAN, edge router (DHCP), 2 SIP phones, MeshChat/Citadel PCs | App servers |

---

## 9. Capacity mindset

Ham UHF is **narrow** compared with microwave or fiber. The design assumes:

- A few compressed VoIP calls  
- Light MeshChat  
- Small Citadel messages  

Email yields to voice under load (QoS + size limits).

---

## 10. One-page service map

```text
                    EOC Kathleen
         ┌─────────────────────────────────┐
         │  FreePBX 10.40.0.10             │
         │  MeshChat 10.40.0.11            │
         │  Citadel 10.40.0.12             │
         │  DNS/NTP 10.40.0.13             │
         │  SIP phones 1001 / 1002         │
         │  Edge router + ham radios       │
         └────────────┬────────────────────┘
                      │ RF 420–450 MHz
         ┌────────────┴────────────┐
         ▼                         ▼
 Emory Warner Robins          Emory Perry
 10.40.1.0/24                 10.40.2.0/24
 SIP 2001 / 2002              SIP 3001 / 3002
 Chat/Mail PCs                Chat/Mail PCs
 Router DHCP + radio          Router DHCP + radio
```

---

## 11. Related documents

| Doc | Purpose |
|-----|---------|
| [420-450MHz_RF_Mesh_Architecture.md](420-450MHz_RF_Mesh_Architecture.md) | Full architecture |
| [EOC_Node_Configuration.md](EOC_Node_Configuration.md) | How to build/configure the hub |
| [Hospital_Node_Configuration.md](Hospital_Node_Configuration.md) | How to build/configure spokes |
| [EOC_Node_BOM.md](EOC_Node_BOM.md) / hospital BOMs | Priced gear + resource links |
| [BOM_Totals.md](BOM_Totals.md) | Program cost roll-up |

---

*Overview — air-gapped ham RF mesh with FreePBX, MeshChat, and Citadel*
