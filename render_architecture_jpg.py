from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1600, 1100
img = Image.new("RGB", (W, H), "#F7F5F0")
d = ImageDraw.Draw(img)


def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


f_title = font(28, True)
f_sub = font(16, False)
f_site = font(18, True)
f_body = font(14, False)
f_small = font(12, False)
f_label = font(13, True)

EOC = "#1F4E6E"
WR = "#2F6F4E"
PR = "#6B3E1F"
RF = "#3D5A80"
MUTED = "#64748B"
BOX_BG = "#FFFFFF"
APP = "#0F766E"
EDGE = "#475569"


def rounded_rect(xy, fill, outline, width=2, radius=12):
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text_center(x, y, text, fnt, fill="#0F172A"):
    bbox = d.textbbox((0, 0), text, font=fnt)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((x - tw / 2, y - th / 2), text, font=fnt, fill=fill)


def bullet_block(x, y, lines, fnt, fill="#1E293B", line_h=20):
    for i, line in enumerate(lines):
        d.text((x, y + i * line_h), line, font=fnt, fill=fill)


d.text(
    (48, 28),
    "Houston County 420-450 MHz RF Mesh — Component Architecture (AIR-GAPPED)",
    font=f_title,
    fill="#0F172A",
)
d.text(
    (48, 68),
    "EOC Kathleen (Hub)  ·  Emory Hospital Warner Robins  ·  Emory Hospital Perry   |   VoIP · Chat · Email (enclave only)",
    font=f_sub,
    fill=MUTED,
)

rounded_rect((48, 100, 1550, 148), "#FEF2F2", "#B91C1C", 2, 8)
d.text(
    (64, 112),
    "AIR GAP: No Internet / cloud / cellular / prod-LAN bridge     Band 420-450 MHz     Primary Yagi links     Optional WR<->Perry backup",
    font=f_body,
    fill="#7F1D1D",
)

# EOC hub
rounded_rect((480, 180, 1120, 470), BOX_BG, EOC, 3, 14)
d.rectangle((480, 180, 1120, 220), fill=EOC)
text_center(800, 200, "EOC Kathleen — HUB + APPS (AIR-GAPPED)", f_site, "#FFFFFF")

rounded_rect((500, 240, 760, 340), "#ECFDF5", APP, 2, 10)
d.text((515, 250), "Applications (on-prem)", font=f_label, fill=APP)
bullet_block(515, 275, ["• FreePBX + 2 SIP phones", "• MeshChat", "• Citadel mail"], f_small)

rounded_rect((780, 240, 1100, 340), "#F1F5F9", EDGE, 2, 10)
d.text((795, 250), "Edge / Ops", font=f_label, fill=EDGE)
bullet_block(
    795,
    275,
    ["• Router/FW (QoS, no Internet)", "• Local NMS / NTP / DNS", "• UPS + Generator"],
    f_small,
)

rounded_rect((500, 355, 760, 450), "#EFF6FF", RF, 2, 10)
d.text((515, 365), "RF Mesh Node", font=f_label, fill=RF)
bullet_block(515, 390, ["• 420-450 MHz IP mesh radio", "• PoE / DC plant"], f_small)

rounded_rect((780, 355, 1100, 450), "#FFF7ED", "#9A3412", 2, 10)
d.text((795, 365), "Antennas (100-150 ft AGL)", font=f_label, fill="#9A3412")
bullet_block(
    795,
    390,
    [
        "• Yagi -> Emory WR (10-12 dBi)",
        "• Yagi -> Emory Perry (10-12 dBi)",
        "• Omni fill (optional 5-8 dBi)",
    ],
    f_small,
)

# Warner Robins
rounded_rect((60, 560, 520, 900), BOX_BG, WR, 3, 14)
d.rectangle((60, 560, 520, 600), fill=WR)
text_center(290, 580, "Emory Hospital Warner Robins", f_site, "#FFFFFF")

rounded_rect((80, 620, 500, 700), "#EFF6FF", RF, 2, 10)
d.text((95, 630), "RF + Antenna", font=f_label, fill=RF)
bullet_block(
    95,
    655,
    ["• 420-450 MHz mesh radio", "• Yagi -> EOC (10-14 dBi) @ 60-100 ft AGL"],
    f_small,
)

rounded_rect((80, 715, 500, 790), "#F1F5F9", EDGE, 2, 10)
d.text((95, 725), "Edge", font=f_label, fill=EDGE)
bullet_block(95, 750, ["• Router/FW (QoS, enclave only)", "• UPS"], f_small)

rounded_rect((80, 805, 500, 880), "#ECFDF5", APP, 2, 10)
d.text((95, 815), "Endpoints", font=f_label, fill=APP)
bullet_block(95, 840, ["• 2x SIP VoIP desk phones", "• MeshChat + Citadel PCs"], f_small)

# Perry
rounded_rect((1080, 560, 1540, 900), BOX_BG, PR, 3, 14)
d.rectangle((1080, 560, 1540, 600), fill=PR)
text_center(1310, 580, "Emory Hospital Perry", f_site, "#FFFFFF")

rounded_rect((1100, 620, 1520, 700), "#EFF6FF", RF, 2, 10)
d.text((1115, 630), "RF + Antenna", font=f_label, fill=RF)
bullet_block(
    1115,
    655,
    ["• 420-450 MHz mesh radio", "• Yagi -> EOC (10-14 dBi) @ 60-100 ft AGL"],
    f_small,
)

rounded_rect((1100, 715, 1520, 790), "#F1F5F9", EDGE, 2, 10)
d.text((1115, 725), "Edge", font=f_label, fill=EDGE)
bullet_block(1115, 750, ["• Router/FW (QoS, enclave only)", "• UPS"], f_small)

rounded_rect((1100, 805, 1520, 880), "#ECFDF5", APP, 2, 10)
d.text((1115, 815), "Endpoints", font=f_label, fill=APP)
bullet_block(1115, 840, ["• 2x SIP VoIP desk phones", "• MeshChat + Citadel PCs"], f_small)

# Primary RF links
d.line([(700, 470), (290, 560)], fill=RF, width=4)
d.line([(900, 470), (1310, 560)], fill=RF, width=4)

# Optional backup dashed
for x in range(520, 1080, 16):
    d.line([(x, 730), (min(x + 8, 1080), 730)], fill="#94A3B8", width=3)

text_center(495, 500, "Primary RF  ~8-10 mi", f_small, RF)
text_center(1105, 500, "Primary RF  ~7-9 mi", f_small, RF)
text_center(800, 710, "Optional backup RF  ~15-20 mi", f_small, MUTED)

# Layer legend
rounded_rect((60, 930, 1540, 1055), BOX_BG, "#94A3B8", 2, 12)
d.text((80, 945), "Component Stack (each site)", font=f_label, fill="#0F172A")
layers = [
    (80, "L5 Apps", "SIP · Chat · Email"),
    (320, "L4 Security", "FW · no Internet"),
    (560, "L2/L3 IP", "Enclave routed · QoS"),
    (800, "L1 RF Mesh", "420-450 MHz radio"),
    (1040, "L0 Physical", "Mast · Hardline · Ground"),
    (1280, "Traffic QoS", "1 VoIP  2 Chat  3 Email"),
]
for x, title, desc in layers:
    rounded_rect((x, 980, x + 220, 1035), "#F8FAFC", "#CBD5E1", 1, 8)
    d.text((x + 12, 990), title, font=f_label, fill="#0F172A")
    d.text((x + 12, 1010), desc, font=f_small, fill=MUTED)

out = Path(r"C:\Users\dell\Mesh_Design\RF_Mesh_Component_Architecture.jpg")
img.save(out, "JPEG", quality=92, optimize=True)
print(f"Wrote {out} ({out.stat().st_size} bytes)")
