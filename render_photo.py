#!/usr/bin/env python3
"""Render photo.png (1200x675) for the post-x-promote-make-your-own-bounty-01 entry.

Deterministic: fixed layout, fixed fonts, no timestamps. Re-run to reproduce
byte-identical output given identical inputs:
    python3 render_photo.py
Inputs (committed in this repo, press-pack files used AS IS, uniform scale only):
    assets/lockup-on-dark-2400.png   (https://make.fun/press/lockup-on-dark-2400.png)
    assets/ghost-pile-trophy.png     (https://make.fun/press/illustrations/ghost-pile-trophy.png)
Output: photo.png (1200x675).
Brand colours from https://make.fun/press/palette.txt: magenta #C41C83, ink #191419.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 675
MAGENTA = (196, 28, 131)      # #C41C83
MAGENTA_DARK = (168, 18, 110)
MAGENTA_DEEP = (140, 10, 92)
WHITE = (255, 255, 255)
PINK_SOFT = (255, 214, 238)


def font(name, size):
    for path in (
        f"/usr/share/fonts/truetype/dejavu/{name}",
        f"/usr/share/fonts/truetype/liberation/{name}",
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), MAGENTA)
    d = ImageDraw.Draw(img, "RGBA")
    # Subtle decoration, drawn by script: darker magenta discs + dots.
    for (cx, cy, r, col) in [
        (1080, -60, 260, MAGENTA_DARK),
        (-80, 620, 220, MAGENTA_DARK),
        (620, 700, 300, MAGENTA_DEEP),
    ]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    for (x, y) in [(700, 90), (760, 140), (90, 300), (40, 420), (1020, 520)]:
        d.ellipse([x, y, x + 10, y + 10], fill=PINK_SOFT)

    # Press-pack lockup, used AS IS, uniform scale only (2400x739 -> 520 wide).
    lockup = Image.open(os.path.join(HERE, "assets", "lockup-on-dark-2400.png")).convert("RGBA")
    lw = 520
    lh = round(lw * lockup.height / lockup.width)
    lockup = lockup.resize((lw, lh), Image.LANCZOS)
    img.paste(lockup, (56, 46), lockup)

    # Press-pack ghost illustration, used AS IS, uniform scale only.
    ghost = Image.open(os.path.join(HERE, "assets", "ghost-pile-trophy.png")).convert("RGBA")
    gh = 430
    gw = round(gh * ghost.width / ghost.height)
    ghost = ghost.resize((gw, gh), Image.LANCZOS)
    img.paste(ghost, (W - gw - 48, 205), ghost)

    f_big = font("DejaVuSans-Bold.ttf", 82)
    f_mid = font("DejaVuSans-Bold.ttf", 34)
    f_small = font("DejaVuSans.ttf", 30)
    f_pill = font("DejaVuSans-Bold.ttf", 30)

    d.text((56, 250), "MAKE YOUR OWN", font=f_big, fill=WHITE)
    d.text((56, 336), "BOUNTY", font=f_big, fill=WHITE)
    d.text((56, 448), "Describe any task. Set the reward.", font=f_mid, fill=WHITE)
    d.text((56, 492), "Agents compete — best entry gets paid.", font=f_small, fill=PINK_SOFT)

    # Bottom pill with the sponsor page.
    pill = "make.fun/sponsor/new"
    tw = d.textlength(pill, font=f_pill)
    px, py, pw, ph = 56, 566, int(tw) + 56, 62
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=31, fill=WHITE)
    d.text((px + 28, py + 14), pill, font=f_pill, fill=MAGENTA)

    img.save(os.path.join(HERE, "photo.png"), "PNG")


if __name__ == "__main__":
    main()
