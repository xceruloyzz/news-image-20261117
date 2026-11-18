#!/usr/bin/env python3
"""Generate entry.png: a one-image front page summing up the world news of
Tuesday 17 November 2026.

All news content is hardcoded below from reporting published on the day
(BBC, Reuters, AP, The Guardian, WFP/IOM, Japan Times). The renderer is
fully deterministic: fixed canvas, fixed fonts, no randomness, no clock,
no network. Run it to rebuild entry.png byte-for-byte:

    python3 tools/generate_frontpage.py
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 20)
RED = (178, 24, 32)
NAVY = (16, 42, 84)
STEEL = (70, 96, 128)
GOLD = (196, 138, 20)
GREEN = (22, 92, 60)
TEAL = (10, 102, 116)
GREY = (84, 84, 88)
LIGHT = (233, 226, 208)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading=1.18):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def panel(draw, box, kicker, kicker_color, headline, body, head_size=31):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(255, 255, 252), outline=(190, 182, 160), width=2)
    draw.rectangle([x0, y0, x0 + 10, y1], fill=kicker_color)
    draw.text((x0 + 24, y0 + 12), kicker, font=font(SANS_B, 19), fill=kicker_color)
    y = text_block(draw, (x0 + 24, y0 + 40), headline, font(SANS_B, head_size),
                   INK, x1 - x0 - 44, leading=1.12)
    # Auto-fit the body: shrink the font until the wrapped text fits the box.
    size = 22
    while size > 15:
        fnt = font(SANS, size)
        lines = wrap(draw, body, fnt, x1 - x0 - 44)
        if y + 8 + len(lines) * int(size * 1.22) <= y1 - 8:
            break
        size -= 1
    text_block(draw, (x0 + 24, y + 8), body, font(SANS, size), (40, 40, 44),
               x1 - x0 - 44, leading=1.22)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 104], fill=INK)
    d.text((36, 26), "THE WORLD TODAY", font=font(SERIF_B, 46), fill=(255, 255, 255))
    d.rectangle([716, 22, 988, 82], fill=RED)
    tag = "ONE DAY - ONE IMAGE"
    tw = d.textlength(tag, font=font(SANS_B, 19))
    d.text((716 + (272 - tw) / 2, 40), tag, font=font(SANS_B, 19), fill=(255, 255, 255))
    d.rectangle([0, 104, W, 164], fill=RED)
    date_txt = "TUESDAY  -  17 NOVEMBER 2026"
    tw = d.textlength(date_txt, font=font(SANS_B, 40))
    d.text(((W - tw) / 2, 114), date_txt, font=font(SANS_B, 40), fill=(255, 255, 255))

    # ---- Lead story -----------------------------------------------------
    lead = [28, 178, 996, 452]
    d.rectangle(lead, fill=(255, 255, 252), outline=(190, 182, 160), width=2)
    d.rectangle([28, 178, 38, 452], fill=RED)
    d.text((54, 190), "LEAD STORY  -  EUROPE AT WAR", font=font(SANS_B, 20), fill=RED)
    y = text_block(d, (54, 218), "UKRAINE BLOWS OPEN THE CRIMEA BRIDGE",
                   font(SANS_B, 43), INK, 590, leading=1.1)
    text_block(d, (54, y + 10),
               "A span of the Kerch road bridge collapses into the sea in "
               "what President Zelenskyy calls an \"unprecedented "
               "operation\". In reply, Russian missiles close Kyiv's "
               "bridges over the Dnipro.",
               font(SANS, 23), (40, 40, 44), 590, leading=1.25)
    # Lead illustration: a bridge deck with a broken span over the sea.
    ix0, iy0, ix1, iy1 = 668, 218, 972, 420
    d.rectangle([ix0, iy0, ix1, iy1], fill=(196, 216, 232))
    d.rectangle([ix0, iy0 + 128, ix1, iy1], fill=NAVY)
    for wx in range(ix0 + 12, ix1 - 30, 52):  # waves
        d.arc([wx, iy0 + 152, wx + 34, iy0 + 176], 0, 180, fill=(140, 180, 215), width=3)
    d.rectangle([ix0, iy0 + 84, ix0 + 118, iy0 + 98], fill=STEEL)       # left deck
    d.rectangle([ix1 - 118, iy0 + 84, ix1, iy0 + 98], fill=STEEL)      # right deck
    d.line([ix0 + 118, iy0 + 98, ix0 + 168, iy0 + 140], fill=STEEL, width=7)  # fallen span
    d.line([ix1 - 118, iy0 + 98, ix1 - 162, iy0 + 132], fill=STEEL, width=7)
    d.rectangle([ix0 + 40, iy0 + 40, ix0 + 54, iy0 + 84], fill=STEEL)  # pylon
    d.rectangle([ix1 - 54, iy0 + 40, ix1 - 40, iy0 + 84], fill=STEEL)
    cx, cy = (ix0 + ix1) // 2, iy0 + 66                                # blast star
    for dx, dy in [(0, -26), (19, -19), (26, 0), (19, 19), (0, 26),
                   (-19, 19), (-26, 0), (-19, -19)]:
        d.line([cx, cy, cx + dx, cy + dy], fill=(232, 116, 12), width=5)
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(245, 166, 35))
    d.text((ix0 + 10, iy1 - 28), "KERCH BRIDGE, CRIMEA",
           font=font(SANS_B, 17), fill=(255, 255, 255))

    # ---- Four main stories ----------------------------------------------
    panel(d, [28, 466, 502, 700], "MIDDLE EAST", RED,
          "TANKERS HIT IN THE STRAIT OF HORMUZ",
          "Tehran's Guards say two tankers struck mines in the strait. "
          "Bahrain stops Iranian drones aimed at a US radar; a third "
          "US carrier reaches the region.")
    panel(d, [522, 466, 996, 700], "GAZA", TEAL,
          "WINTER EMERGENCY GRIPS GAZA",
          "1.7 million displaced and 1.4 million facing acute hunger "
          "as winter rains flood camps. WFP and IOM warn aid is "
          "running short.")
    panel(d, [28, 714, 502, 900], "ASIA - DIPLOMACY", NAVY,
          "TRUMP LANDS IN MANILA",
          "ASEAN opens a three-day Asia trip ending in China, with Xi "
          "and Putin talks ahead. Washington curbs China's access to "
          "US AI chips.", head_size=30)
    panel(d, [522, 714, 996, 900], "CLIMATE - COP31", GREEN,
          "CLIMATE TALKS ENTER DECISIVE DAYS",
          "In Antalya a first draft deal is on the table: rows over "
          "quitting fossil fuels and money for poorer nations. "
          "Deadline: 20 Nov.", head_size=30)

    # ---- Bottom ticker strip --------------------------------------------
    d.rectangle([0, 914, W, 968], fill=NAVY)
    ticker = ("JAPAN JETS SCRAMBLE OVER RUSSIAN AIRCRAFT  |  "
              "OIL $92.76  |  "
              "VULCAN FAILURE LOSES 40 SATELLITES")
    tsize = 18
    while tsize > 12 and d.textlength(ticker, font=font(SANS_B, tsize)) > 984:
        tsize -= 1
    tw = d.textlength(ticker, font=font(SANS_B, tsize))
    d.text(((W - tw) / 2, 932), ticker, font=font(SANS_B, tsize), fill=(255, 255, 255))
    d.rectangle([0, 968, W, H], fill=INK)
    foot = "All stories reported on Tuesday 17 November 2026  -  Sources: BBC, Reuters, AP, The Guardian, WFP"
    tw = d.textlength(foot, font=font(SANS, 19))
    d.text(((W - tw) / 2, 984), foot, font=font(SANS, 19), fill=(235, 230, 215))

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
