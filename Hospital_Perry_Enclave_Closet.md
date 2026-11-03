# Emory Perry — Enclave Closet / Rack
## What’s inside and how each piece works

| Field | Value |
|-------|--------|
| Site | Emory Hospital Perry — 1120 Morningside Dr |
| Subnet | `10.40.2.0/24` (example) |
| Role | Spoke closet — **clients only** (no app servers) |
| FreePBX extensions | **3001**, **3002** |
| Related | [Perry Wiring](Hospital_Perry_Wiring_Diagram.md) · [Hospital Config](Hospital_Node_Configuration.md) · [Overview](Mesh_Services_Overview.md) |

---

## 1. Closet layout

```text
[UPS]
   └── PoE GbE Switch ──┬── Edge router (10.40.2.1)
                        ├── Radio / radio–IP gateway
                        ├── SIP phones 3001, 3002
                        └── Continuity PCs (MeshChat + Citadel)
```

Roof: Yagi aimed at EOC, coax, arrestor, ham radio — see [Hospital_Perry_Wiring_Diagram.md](Hospital_Perry_Wiring_Diagram.md).

**Not in this closet:** FreePBX, MeshChat server, Citadel server (those stay at EOC).

---

## 2. Equipment in this closet

| Equipment | What it does | How it works here |
|-----------|----------------|-------------------|
| **UPS** | Backup power | Powers switch, router, radio PSU; phones via PoE |
| **PoE GbE switch** | Enclave LAN hub | Phones, PCs, router, radio/gateway only; **not** trunked to EHR |
| **Edge router / firewall** | Gateway, DHCP, QoS, air gap | `10.40.2.1`; DHCP for phones/PCs; default path to EOC `10.40.0.0/24` over RF; **no** Internet |
| **Radio–IP gateway** *(if used)* | Ham RF ↔ Ethernet | Links closet IP network to Kathleen over 420–450 MHz |
| **Radio PSU** | Powers ham radio | Often in closet even if radio is on the roof |
| **SIP phones 3001, 3002** | Hospital voice | DHCP from this router; SIP server = FreePBX `10.40.0.10` at EOC |
| **Continuity PCs** | Chat / email clients | Reach MeshChat `.11` and Citadel `.12` at EOC over RF |

---

## 3. How each service uses this closet

| Service | Path through closet |
|---------|---------------------|
| **Voice** | Phone → switch → router → radio/gateway → RF → FreePBX @ EOC → far phone |
| **Chat** | PC → switch → router → RF → MeshChat @ EOC |
| **Email** | PC → switch → router → RF → Citadel @ EOC |
| **DHCP** | Edge router assigns `10.40.2.50–200` |
| **DNS / NTP** | Queried at EOC `10.40.0.13` via RF |

---

## 4. Air-gap rules for this closet

- No cable to hospital core / EHR / guest Wi‑Fi  
- No ISP or cellular modem  
- Label ports **MESH ENCLAVE — NOT EHR**  
- Facilities/Biomed approve roof and power only; apps stay off clinical LAN  

---

*Perry enclave closet — spoke*
