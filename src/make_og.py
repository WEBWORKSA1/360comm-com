# Generates assets/img/og.png (1200x630 social share image). Requires Pillow.
import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1200, 630
img = Image.new('RGB', (W, H), '#0b1b3f')
d = ImageDraw.Draw(img)
for y in range(H):  # vertical gradient navy -> blue
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(11 + (29 - 11) * t), int(27 + (78 - 27) * t), int(63 + (216 - 63) * t)))
def font(size, bold=True):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
              '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()
d.text((80, 170), '360Comm', font=font(110), fill='white')
d.text((80, 310), 'Compare business phone, VoIP, video', font=font(42, False), fill='#cfd9f2')
d.text((80, 362), '& contact-center platforms', font=font(42, False), fill='#cfd9f2')
d.rounded_rectangle((80, 450, 640, 530), radius=16, fill='#f97316')
d.text((110, 470), 'Free quotes in 60 seconds  ->', font=font(34), fill='white')
out = os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', 'og.png')
img.save(out, optimize=True)
print('og.png written')
