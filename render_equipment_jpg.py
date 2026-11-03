from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1800, 1250
img = Image.new("RGB", (W, H), "#F7F5F0")
d = ImageDraw.Draw(img)


def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


f_title = font(26, True)
f_sub = font(15, False)
f_head = font(15, True)
f_body = font(13, False)
f_small = font(11, False)
f_qty = font(12, True)

EOC = "#1F4E6E"
WR = "#2F6F4E"
PR = "#6B3E1F"
SHR = "#4C1D95"
MUTED = "#64748B"
BOX = "#FFFFFF"


def round_box(xy, fill, outline, w=2, r=12):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=w)


def header_bar(x1, y1, x2, y2, color, title):
    round_box((x1, y1, x2, y2), BOX, color, 3, 12)
    d.rectangle((x1, y1, x2, y1 + 36), fill=color)
    bbox = d.textbbox((0, 0), title, font=f_head)
    tw = bbox[2] - bbox[0]
    d.text(((x1 + x2) / 2 - tw / 2, y1 + 9), title, font=f_head, fill="#FFFFFF")


def equip_rows(x, y, width, rows, accent):
    yy = y
    for qty, name, note in rows:
        round_box((x, yy, x + width, yy + 48), "#F8FAFC", "#CBD5E1", 1, 8)
        round_box((x + 6, yy + 8, x + 42, yy + 40), accent, accent, 1, 6)
        qb = d.textbbox((0, 0), str(qty), font=f_qty)
        qw = qb[2] - qb[0]
        d.text((x + 24 - qw / 2, yy + 14), str(qty), font=f_qty, fill="#FFFFFF")
        d.text((x + 52, yy + 6), name, font=f_body, fill="#0F172A")
        d.text((x + 52, yy + 26), note, font=f_small, fill=MUTED)
        yy += 54
    return yy


d.text(
    (36, 20),
    "420-450 MHz RF Mesh — Equipment Pieces (AIR-GAPPED)",
    font=f_title,
    fill="#0F172A",
)
d.text(
    (36, 54),
    "Air-gapped enclave: no Internet/cloud/prod-LAN gear  |  Qty = planning quantities  |  Band: 420-450 MHz",
    font=f_sub,
    fill=MUTED,
)

col_w = 560
gap = 24
x1, x2, x3 = 36, 36 + col_w + gap, 36 + 2 * (col_w + gap)
top, bottom = 95, 980

# EOC
header_bar(x1, top, x1 + col_w, bottom, EOC, "EOC Kathleen (Hub)")
equip_rows(
    x1 + 12,
    top + 50,
    col_w - 24,
    [
        (1, "Tower / mast system", "100-150 ft AGL, bonded ground"),
        (2, "Yagi antennas 10-12 dBi", "420-450 MHz toward WR & Perry"),
        (1, "Omni collinear 5-8 dBi", "Optional portable / local fill"),
        (1, "420-450 MHz mesh IP radio", "Hub RF node"),
        (1, "Hardline + polyphasers", "1/2 in or 7/8 in feedline plant"),
        (1, "Router / firewall", "QoS; NO Internet WAN route"),
        (1, "PoE / DC power plant", "Powers outdoor radio"),
        (1, "Managed PoE switch", "Enclave VLAN only"),
        (1, "SIP PBX server/appliance", "On-prem VoIP (no cloud)"),
        (1, "Chat + internal mail host", "Enclave apps at EOC"),
        (1, "Local NMS / NTP / DNS", "No public time/DNS"),
        (1, "UPS + generator circuit", "Hub power survivability"),
        (2, "Continuity workstations", "Softphone, chat, webmail"),
        (1, "NEMA / cable entry kit", "Weatherproof I/O"),
    ],
    EOC,
)

# WR
header_bar(x2, top, x2 + col_w, bottom, WR, "Emory Hospital Warner Robins")
equip_rows(
    x2 + 12,
    top + 50,
    col_w - 24,
    [
        (1, "Roof mast", "+20-40 ft; total 60-100 ft AGL"),
        (1, "Yagi antenna 10-14 dBi", "420-450 MHz aimed at EOC"),
        (1, "420-450 MHz mesh IP radio", "Spoke RF node"),
        (1, "Hardline + polyphaser", "Roof to telecom closet"),
        (1, "Grounding kit", "Bond to building ground"),
        (1, "Router / firewall", "QoS; enclave only (no WAN)"),
        (1, "PoE / DC injector", "Radio power"),
        (1, "Small PoE switch", "Enclave VLAN (not EHR)"),
        (1, "UPS", "Spoke survivability"),
        (2, "Softphone or ATA", "Mesh-only VoIP"),
        (2, "PCs / thin clients", "Enclave chat + mail"),
        (1, "NEMA / mount hardware", "Hospital roof approved"),
        (1, "Optional 2nd Yagi", "Only if WR-Perry backup built"),
        (1, "Optional 2nd mesh radio", "Dedicated backup path"),
    ],
    WR,
)

# Perry
header_bar(x3, top, x3 + col_w, bottom, PR, "Emory Hospital Perry")
equip_rows(
    x3 + 12,
    top + 50,
    col_w - 24,
    [
        (1, "Roof mast", "+20-40 ft; total 60-100 ft AGL"),
        (1, "Yagi antenna 10-14 dBi", "420-450 MHz aimed at EOC"),
        (1, "420-450 MHz mesh IP radio", "Spoke RF node"),
        (1, "Hardline + polyphaser", "Roof to telecom closet"),
        (1, "Grounding kit", "Bond to building ground"),
        (1, "Router / firewall", "QoS; enclave only (no WAN)"),
        (1, "PoE / DC injector", "Radio power"),
        (1, "Small PoE switch", "Enclave VLAN (not EHR)"),
        (1, "UPS", "Spoke survivability"),
        (2, "Softphone or ATA", "Mesh-only VoIP"),
        (2, "PCs / thin clients", "Enclave chat + mail"),
        (1, "NEMA / mount hardware", "Hospital roof approved"),
        (1, "Optional 2nd Yagi", "Only if WR-Perry backup built"),
        (1, "Optional 2nd mesh radio", "Dedicated backup path"),
    ],
    PR,
)

# Shared strip
round_box((36, 1000, 1764, 1215), BOX, SHR, 3, 12)
d.rectangle((36, 1000, 1764, 1036), fill=SHR)
d.text((52, 1008), "Shared Spares & Common Kits (pool for all sites)", font=f_head, fill="#FFFFFF")

shared = [
    (1, "Spare mesh radio", "420-450 MHz"),
    (1, "Spare Yagi", "10-14 dBi"),
    (2, "Spare PoE / PSU", "Field swap"),
    (2, "Portable mesh kits", "Tactical / parking"),
    (1, "Alignment / test kit", "Install & maint"),
    (1, "Freq authorization file", "License / agency ID"),
    (1, "Offline patch media kit", "Sneaker-net updates"),
    (1, "Air-gap audit checklist", "No WAN / no EHR bridge"),
]
sx = 52
for qty, name, note in shared:
    round_box((sx, 1055, sx + 200, 1185), "#F5F3FF", "#C4B5FD", 1, 8)
    round_box((sx + 70, 1068, sx + 130, 1100), SHR, SHR, 1, 6)
    qb = d.textbbox((0, 0), str(qty), font=f_qty)
    qw = qb[2] - qb[0]
    d.text((sx + 100 - qw / 2, 1074), str(qty), font=f_qty, fill="#FFFFFF")
    # wrap name
    d.text((sx + 12, 1115), name, font=f_body, fill="#0F172A")
    d.text((sx + 12, 1145), note, font=f_small, fill=MUTED)
    sx += 212

out = Path(r"C:\Users\dell\Mesh_Design\RF_Mesh_Equipment_List.jpg")
img.save(out, "JPEG", quality=92, optimize=True)
print(f"Wrote {out} ({out.stat().st_size} bytes)")
