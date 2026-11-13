import sys, os, textwrap
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image, ImageDraw, ImageFont
from articles import ALL

INK=(5,4,9); GOLD=(212,175,55); GOLD_L=(243,229,171); WHITE=(255,255,255); MUTED=(150,147,160)
F="/usr/share/fonts/truetype/dejavu/"
def serif(s): return ImageFont.truetype(F+"DejaVuSerif-Bold.ttf", s)
def sans(s,b=True): return ImageFont.truetype(F+("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), s)

os.makedirs('assets/og', exist_ok=True)
for a in ALL:
    W,H=1200,630
    im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)], fill=(int(5+16*t),int(4+11*t),int(9+28*t)))
    for rad,al in ((560,9),(430,13),(300,17)):
        ov=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(ov).ellipse(
            [W-rad,-rad//2,W+rad//2,rad], fill=GOLD+(al,))
        im=Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB')
    d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,6], fill=GOLD)

    # category chip
    chip=a['cat'].upper(); cf=sans(17); cw=d.textlength(chip,font=cf)
    d.rounded_rectangle([72,74,72+cw+38,74+40], radius=20, outline=GOLD, width=2)
    d.text((72+19,84), chip, font=cf, fill=GOLD)

    # headline — wrap by measured pixel width, shrink until it fits 4 lines
    MAXW = W - 72 - 96   # left margin + right gutter clear of the glow
    def wrap_px(text, f):
        out, cur = [], ""
        for word in text.split():
            trial = (cur + " " + word).strip()
            if d.textlength(trial, font=f) <= MAXW:
                cur = trial
            else:
                if cur: out.append(cur)
                cur = word
        if cur: out.append(cur)
        return out
    for size in (54,50,46,42,38,34):
        f = serif(size)
        lines = wrap_px(a['h1'], f)
        if len(lines) <= 4 and all(d.textlength(l, font=f) <= MAXW for l in lines):
            break
    lines = lines[:4]
    y=170
    for ln in lines:
        d.text((72,y), ln, font=f, fill=WHITE); y+=int(size*1.30)

    d.line([(72,y+22),(212,y+22)], fill=GOLD, width=3)
    d.text((72,y+50), f"{a['mins']} min read", font=sans(19,False), fill=MUTED)

    bf=sans(22); d.text((72,H-70), "BUILDTEK  EVENTS", font=bf, fill=WHITE)
    d.text((72+d.textlength("BUILDTEK  EVENTS",font=bf)+22, H-68), "buildtek.in", font=sans(19,False), fill=GOLD)

    p=f"assets/og/{a['slug']}.jpg"
    im.save(p,'JPEG',quality=86,optimize=True,progressive=True)
print(f"generated {len(ALL)} article OG cards")
