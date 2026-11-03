# EOC Kathleen — Enclave Closet / Rack
## What’s inside and how each piece works

| Field | Value |
|-------|--------|
| Site | EOC — 102 Chief Williams Dr, Kathleen |
| Subnet | `10.40.0.0/24` (example) |
| Role | Hub closet — LAN + **application servers** |
| Related | [EOC Wiring](EOC_Wiring_Diagram.md) · [EOC Config](EOC_Node_Configuration.md) · [Overview](Mesh_Services_Overview.md) |

---

## 1. Closet layout

```text
[UPS]
   └── PoE GbE Switch ──┬── Edge router (10.40.0.1)
                        ├── Radio / radio–IP gateway(s)
                        ├── FreePBX mini PC (10.40.0.10)
                        ├── MeshChat / Citadel host (.11 / .12)
                        ├── DNS / NTP (.13, may share host)
                        ├── SIP phones 1001, 1002
                        └── Continuity PCs
```

Outdoor: Yagis, coax, arrestors, ham radios (RF) — see [EOC_Wiring_Diagram.md](EOC_Wiring_Diagram.md).

---

## 2. Equipment in this closet

| Equipment | What it does | How it works here |
|-----------|----------------|-------------------|
| **UPS** | Backup power | Feeds switch, router, mini PCs, radio PSUs; phones often via PoE |
| **PoE GbE switch** | Enclave LAN hub | All enclave Ethernet lands here; PoE to SIP phones; **no** Internet/EHR uplink |
| **Edge router / firewall** | Gateway, DHCP, QoS, air gap | `10.40.0.1`; DHCP for phones/PCs; routes only to WR/Perry over RF; blocks Internet |
| **Radio–IP gateway** *(if used)* | Ham RF ↔ Ethernet | Presents RF path as IP toward hospital routers |
| **Radio PSU(s)** | Power for ham radios | 13.8 V supplies; radios may be mast-mounted with Ethernet into closet |
| **FreePBX mini PC** | VoIP server | Linux host; all six site phones register here (`pbx.mesh.local`) |
| **MeshChat / Citadel host** | Chat + email | Linux host (or shared with FreePBX); internal only |
| **DNS / NTP** | Names and time | Enclave resolution/time; no public DNS/NTP |
| **SIP phones 1001, 1002** | EOC voice | DHCP → register to FreePBX on same LAN or via switch |
| **Continuity PCs** | Ops clients | MeshChat + Citadel; optional softphone spare |

---

## 3. How a call works from this closet

1. Local phone (1001) or hospital phone signals FreePBX on the switch.  
2. FreePBX routes the call.  
3. If far end is a hospital, edge router sends SIP/RTP toward the radio/gateway → RF → hospital closet.  
4. QoS on the router keeps voice ahead of chat/mail.

---

## 4. Air-gap rules for this closet

- No ISP modem, cellular modem, or county Internet firewall in this rack  
- No patch to non-enclave building LAN  
- App updates only via offline media  

---

*EOC enclave closet — hub*
