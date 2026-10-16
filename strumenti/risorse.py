"""Crea le risorse per motori di ricerca e condivisione: icone (PNG, ICO) e immagine di anteprima 1200x630.

Uso: python strumenti/risorse.py   (richiede Playwright con Chromium e Pillow)
Scrive in docs/img/ (pagina) e in radice/ (sito lumishelf.github.io).
"""
import asyncio, pathlib, io
from PIL import Image
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"; RADICE = ROOT / "radice"
ICONA = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64' width='512' height='512'>
<rect width='64' height='64' rx='14' fill='#070E1C'/>
<path d='M12 18c7-3 14-3 20 2 6-5 13-5 20-2v28c-7-3-14-3-20 2-6-5-13-5-20-2z' fill='none' stroke='#E8B86D' stroke-width='3.5' stroke-linejoin='round'/>
<path d='M32 20v28' stroke='#E8B86D' stroke-width='3.5'/></svg>"""

SCHEDA = """<!doctype html><html><head><meta charset='utf-8'><style>
@font-face{font-family:L;src:url(file://%(docs)s/fonts/literata-latin.woff2)}
@font-face{font-family:I;src:url(file://%(docs)s/fonts/instrument-sans-latin.woff2)}
*{margin:0;box-sizing:border-box}
body{width:1200px;height:630px;background:#070E1C;color:#F3F4F7;font-family:I,sans-serif;position:relative;overflow:hidden}
.lume{position:absolute;inset:-200px -100px auto 420px;height:760px;background:radial-gradient(45%% 50%% at 55%% 30%%,rgba(232,184,109,.32),rgba(232,184,109,.08) 45%%,transparent 70%%)}
.testo{position:absolute;left:72px;top:150px;width:520px}
h1{font-family:L,serif;font-weight:560;font-size:104px;letter-spacing:-.03em;line-height:.95}
p{font-family:L,serif;font-size:30px;line-height:1.35;color:#D7DDE7;margin-top:26px}
.pic{font-size:22px;color:#E8B86D;margin-top:30px;font-family:I,sans-serif}
.scaffale{position:absolute;right:56px;bottom:86px;width:520px;display:grid;grid-template-columns:30fr 35fr 30fr;gap:4%%;align-items:end;padding:0 3%%}
.scaffale img{width:100%%;aspect-ratio:540/1140;object-fit:cover;object-position:top;border-radius:20px;border:5px solid #1A2436;box-shadow:0 26px 40px -20px #000}
.scaffale img:nth-child(3){rotate:-4deg;transform-origin:0 100%%}
.mensola{position:absolute;right:46px;width:540px;bottom:70px;height:16px;border-radius:3px 3px 8px 8px;background:linear-gradient(180deg,#5A452B,#3A2D1D 22%%,#241B12);box-shadow:inset 0 1.5px 0 rgba(240,199,132,.75),0 22px 36px -14px #000}
</style></head><body><div class='lume'></div>
<div class='testo'><h1>LumiShelf</h1><p>Lettore di PDF, EPUB, manga e documenti per Android</p><p class='pic'>Gratis e senza account<br>lumishelf.github.io/LumiShelf</p></div>
<div class='scaffale'><img src='file://%(docs)s/img/06_home_con_dati.webp'><img src='file://%(docs)s/img/10_epub_reale.webp'><img src='file://%(docs)s/img/route_manga_serie.webp'></div>
<div class='mensola'></div></body></html>"""

async def main():
    RADICE.mkdir(exist_ok=True); (DOCS / "img").mkdir(parents=True, exist_ok=True)
    tmp = ROOT / "strumenti" / "_scheda.html"
    tmp.write_text(SCHEDA % {"docs": str(DOCS)}, encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 512, "height": 512})
        await pg.set_content("<html><body style='margin:0;background:transparent'>" + ICONA + "</body></html>")
        png = await pg.locator("svg").screenshot(omit_background=True)
        pg2 = await b.new_page(viewport={"width": 1200, "height": 630})
        await pg2.goto("file://" + str(tmp)); await pg2.wait_for_timeout(800)
        await pg2.screenshot(path=str(DOCS / "img" / "anteprima.png"))
        await b.close()
    tmp.unlink()
    big = Image.open(io.BytesIO(png)).convert("RGBA")
    for size, name in [(192, "icona-192.png"), (48, "icona-48.png"), (180, "apple-touch-icon.png")]:
        im = big.resize((size, size), Image.LANCZOS)
        if name == "apple-touch-icon.png":  # iOS vuole un'icona piena, senza trasparenza
            bg = Image.new("RGBA", im.size, "#070E1C"); bg.alpha_composite(im); im = bg.convert("RGB")
        im.save(DOCS / "img" / name); im.save(RADICE / name)
    big.save(RADICE / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    im = Image.open(DOCS / "img" / "anteprima.png").convert("RGB"); im.save(DOCS / "img" / "anteprima.png", optimize=True)
    print("risorse create")

asyncio.run(main())
