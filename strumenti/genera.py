"""Genera la pagina pubblica di LumiShelf (docs/index.html) e il README.md dai dati in dati/.

Uso: python strumenti/genera.py [--schermate CARTELLA_PNG]
Con --schermate converte le catture del collaudo in docs/img/*.webp (larghezza 540 px).
"""
import argparse, collections, datetime, html, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "strumenti"))
from schermate import GRUPPI, EROE  # noqa: E402

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
SIMBOLI = {"telefono": "📱", "emulatore": "🧪", "ereditata": "📦", "limiti": "⚠️", "programma": "🗓️", "rinviata": "⏸️", "decidere": "💭"}


def data_lunga(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {MESI[d.month - 1]} {d.year}"


def mb(n):
    return f"{round(n / 1048576)} MB" if n else ""


def e(s):
    return html.escape(str(s), quote=True)


def carica():
    j = lambda n: json.loads((ROOT / "dati" / n).read_text(encoding="utf-8"))
    return j("app.json"), j("funzioni.json"), j("versioni.json")


def schermate(src):
    from PIL import Image
    out = ROOT / "docs" / "img"
    out.mkdir(parents=True, exist_ok=True)
    nomi = {n for _, items in GRUPPI for n, _ in items} | set(EROE)
    for n in sorted(nomi):
        p = pathlib.Path(src) / f"{n}.png"
        if not p.is_file():
            print("manca la schermata", p, file=sys.stderr)
            continue
        im = Image.open(p).convert("RGB")
        w = 540
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(out / f"{n}.webp", "WEBP", quality=82, method=6)


def presenti():
    d = ROOT / "docs" / "img"
    return {p.stem for p in d.glob("*.webp")} if d.is_dir() else set()


def pagina(app, cat, versioni):
    stati = cat["stati"]; funzioni = cat["funzioni"]
    nome_stato = {s["id"]: s["nome"] for s in stati}
    conta = collections.Counter(f["stato"] for f in funzioni)
    tot = len(funzioni)
    repo = f"https://github.com/{app['repo']}"
    tag = f"v{app['versione']}"
    apk_url = f"{repo}/releases/download/{tag}/{app['apk_nome']}"
    imgs = presenti()
    col = app["collaudo"]

    # Barra e legenda
    barra = "".join(f'<span class="seg s-{s["id"]}" style="flex:{conta[s["id"]]}" title="{e(s["nome"])}: {conta[s["id"]]}"></span>' for s in stati if conta[s["id"]])
    legenda = "".join(
        f'<li><button type="button" class="chip s-{s["id"]}" data-stato="{s["id"]}" aria-pressed="false"><i aria-hidden="true"></i>'
        f'<span class="chip-nome">{e(s["nome"])}</span><span class="chip-n">{conta[s["id"]]}</span></button>'
        f'<p class="chip-desc">{e(s["spiegazione"])}</p></li>' for s in stati)

    aree = list(dict.fromkeys(f["area"] for f in funzioni))
    opzioni = "".join(f'<option value="{e(a)}">{e(a)}</option>' for a in aree)
    gruppi = []
    for a in aree:
        righe = []
        for f in (x for x in funzioni if x["area"] == a):
            q = " ".join([f["nome"], f["descrizione"], f["nota"], nome_stato[f["stato"]], a]).lower()
            dal = f'<span class="dal">dalla {e(f["dal"])}</span>' if f["dal"] else ""
            nota = f'<p class="nota">{e(f["nota"])}</p>' if f["nota"] else ""
            righe.append(
                f'<li class="f" data-stato="{f["stato"]}" data-area="{e(a)}" data-q="{e(q)}">'
                f'<div class="f-testo"><h4>{e(f["nome"])}</h4><p>{e(f["descrizione"])}</p>{nota}</div>'
                f'<div class="f-meta"><span class="pill s-{f["stato"]}"><i aria-hidden="true"></i>{e(nome_stato[f["stato"]])}</span>{dal}</div></li>')
        gruppi.append(f'<section class="area" data-area="{e(a)}"><h3>{e(a)} <span class="area-n">{len(righe)}</span></h3><ul class="righe">{"".join(righe)}</ul></section>')

    galleria = []
    for titolo, items in GRUPPI:
        figs = "".join(
            f'<figure><img src="img/{n}.webp" alt="LumiShelf, schermata: {e(c)}" width="540" height="1140" loading="lazy" decoding="async"><figcaption>{e(c)}</figcaption></figure>'
            for n, c in items if n in imgs)
        if figs:
            galleria.append(f'<div class="gal"><h3>{e(titolo)}</h3><div class="striscia" tabindex="0" aria-label="{e(titolo)}: scorri per vedere tutte le schermate">{figs}</div></div>')

    eroe = "".join(
        f'<img class="tel t{i}" src="img/{n}.webp" alt="{e(a)}" width="540" height="1140" fetchpriority="{"high" if i == 1 else "auto"}">'
        for i, (n, a) in enumerate(zip(EROE, ["La Home di LumiShelf", "Un libro EPUB aperto nel lettore", "La pagina di una serie manga"])) if n in imgs)

    vers = []
    for i, v in enumerate(versioni):
        punti = "".join(f"<li>{e(p)}</li>" for p in v["punti"])
        corrente = ' <span class="corrente">questa versione</span>' if i == 0 else ""
        vers.append(f'<li class="ver"><div class="ver-testa"><h3>{e(v["versione"])}{corrente}</h3><p class="ver-data"><time datetime="{v["data"]}">{data_lunga(v["data"])}</time></p></div>'
                    f'<div><p class="ver-titolo">{e(v["titolo"])}</p><ul>{punti}</ul></div></li>')

    collaudo = ""
    if col.get("jvm"):
        collaudo = (f'<p class="collaudo">Collaudo della {e(app["versione"])}, {data_lunga(col["data"])}: {e(col["jvm"])} test sul codice superati; '
                    f'{e(col["android_note"])} test Android superati su un emulatore con lo schermo del Note 10 Plus e {e(col["android_compatto"])} su un telefono compatto da 360 dp. '
                    f'L’APK pubblicato è quello collaudato.</p>')

    descr = (f"App Android gratuita per leggere e organizzare PDF, libri EPUB, manga e fumetti (CBZ, CBR) e documenti Office. "
             f"Senza account: i file restano sul telefono. Scarica l’APK {app['versione']}.")
    verifica = f'<meta name="google-site-verification" content="{e(app["google_verifica"])}">\n' if app.get("google_verifica") else ""
    sost = {
        "VERSIONE": e(app["versione"]), "CODICE": str(app["codice"]), "DATA": data_lunga(app["data"]), "DATA_ISO": app["data"],
        "APK_URL": apk_url, "APK_MB": mb(app["apk_bytes"]) or "circa 68 MB", "APK_NOME": e(app["apk_nome"]),
        "APK_SHA": e(app["apk_sha256"] or "disponibile nella pagina della versione"), "CERT_SHA": e(app["cert_sha256"]),
        "PACCHETTO": e(app["pacchetto"]), "ETICHETTA": e(app["etichetta"]), "MIN_ANDROID": e(app["min_android"]), "MIN_SDK": str(app["min_sdk"]),
        "TARGET_ANDROID": e(app["target_android"]), "TARGET_SDK": str(app["target_sdk"]),
        "REPO": repo, "RELEASE_URL": f"{repo}/releases/tag/{tag}", "RELEASES": f"{repo}/releases", "ISSUES": f"{repo}/issues",
        "PAGINA": app["pagina"], "TOT": str(tot), "TELEFONO_N": str(conta["telefono"]), "EMULATORE_N": str(conta["emulatore"]),
        "BARRA": barra, "LEGENDA": legenda, "OPZIONI": opzioni, "GRUPPI": "".join(gruppi), "GALLERIA": "".join(galleria),
        "EROE": eroe, "VERSIONI": "".join(vers), "COLLAUDO": collaudo,
        "DESCRIZIONE": e(descr), "VERIFICA": verifica, "JSONLD": jsonld(app, funzioni, descr, apk_url),
    }
    t = (ROOT / "strumenti" / "modello.html").read_text(encoding="utf-8")
    for k, v in sost.items():
        t = t.replace("{{" + k + "}}", v)
    assert "{{" not in t, t[t.index("{{"):t.index("{{") + 40]
    return t


def jsonld(app, funzioni, descr, apk_url):
    pagina = app["pagina"]
    dati = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "LumiShelf",
        "description": descr,
        "url": pagina,
        "image": pagina + "img/anteprima.png",
        "screenshot": [pagina + f"img/{n}.webp" for n in EROE],
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": f"Android {app['min_android']} o successivo",
        "softwareVersion": app["versione"],
        "datePublished": app["data"],
        "downloadUrl": apk_url,
        "fileSize": mb(app["apk_bytes"]),
        "inLanguage": "it",
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "featureList": [f["nome"] for f in funzioni if f["stato"] in ("telefono", "emulatore")],
        "author": {"@type": "Organization", "name": "LumiShelf", "url": f"https://github.com/{app['repo']}"},
    }
    return json.dumps(dati, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def sitemap(app):
    from schermate import GRUPPI as G
    imgs = [n for _, items in G for n, _ in items]
    righe = "".join(f"\n    <image:image><image:loc>{app['pagina']}img/{n}.webp</image:loc></image:image>" for n in imgs if (ROOT / "docs" / "img" / f"{n}.webp").is_file())
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            f'  <url>\n    <loc>{app["pagina"]}</loc>\n    <lastmod>{app["data"]}</lastmod>{righe}\n  </url>\n</urlset>\n')


def radice(app):
    """Sito lumishelf.github.io: rinvio alla pagina, robots.txt, 404, chiave IndexNow, favicon (da risorse.py)."""
    d = ROOT / "radice"; d.mkdir(exist_ok=True)
    p = app["pagina"]
    verifica = f'<meta name="google-site-verification" content="{e(app["google_verifica"])}">\n' if app.get("google_verifica") else ""
    testa = ('<!doctype html>\n<html lang="it">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
             '{titolo}<link rel="icon" href="/favicon.ico" sizes="48x48">\n<link rel="icon" href="/icona-192.png" type="image/png" sizes="192x192">\n'
             '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<meta name="theme-color" content="#070E1C">\n' + verifica)
    stile = ('<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#070E1C;color:#F3F4F7;'
             'font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:24px;text-align:center}a{color:#E8B86D}</style>\n')
    (d / "index.html").write_text(
        testa.format(titolo="<title>LumiShelf – lettore PDF, EPUB e manga per Android</title>\n"
                     '<meta name="description" content="LumiShelf, app Android gratuita per leggere e organizzare PDF, EPUB, manga e documenti.">\n'
                     f'<link rel="canonical" href="{p}">\n<meta http-equiv="refresh" content="0; url={p}">\n')
        + stile + f'</head>\n<body>\n<p>La pagina di LumiShelf è <a href="{p}">{p}</a></p>\n</body>\n</html>\n', encoding="utf-8")
    (d / "404.html").write_text(
        testa.format(titolo='<title>Pagina non trovata · LumiShelf</title>\n<meta name="robots" content="noindex">\n')
        + stile + f'</head>\n<body>\n<p>Questa pagina non esiste. LumiShelf è qui: <a href="{p}">{p}</a></p>\n</body>\n</html>\n', encoding="utf-8")
    (d / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {p}sitemap.xml\n", encoding="utf-8")
    (d / f"{app['indexnow_key']}.txt").write_text(app["indexnow_key"], encoding="utf-8")
    (d / ".nojekyll").write_text("", encoding="utf-8")
    (d / "README.md").write_text(f"# lumishelf.github.io\n\nRinvio alla pagina di LumiShelf: {p}\n", encoding="utf-8")


def readme(app, cat, versioni):
    stati = cat["stati"]; funzioni = cat["funzioni"]
    nome_stato = {s["id"]: s["nome"] for s in stati}
    conta = collections.Counter(f["stato"] for f in funzioni)
    repo = f"https://github.com/{app['repo']}"
    tag = f"v{app['versione']}"
    apk_url = f"{repo}/releases/download/{tag}/{app['apk_nome']}"
    col = app["collaudo"]
    r = [f"# LumiShelf", "", f"[![LumiShelf: lettore PDF, EPUB e manga per Android]({'docs/img/anteprima.png'})]({app['pagina']})", "",
         "Libreria e lettore di documenti per Android: PDF, EPUB, manga e fumetti, documenti Office e testo, organizzati in un unico posto. Nessun account: i file restano sul telefono.", "",
         f"**[Scarica la {app['versione']}]({apk_url})** (APK, {mb(app['apk_bytes']) or 'circa 68 MB'}, Android {app['min_android']} o successivo) · [Pagina del progetto]({app['pagina']}) · [Tutte le versioni]({repo}/releases)", "",
         "## Stato delle funzioni", "",
         f"{len(funzioni)} funzioni in tutto. Ogni funzione passa per tre gradini: implementata, collaudata con test automatici su emulatore, provata sul telefono di riferimento (Samsung Galaxy Note 10 Plus).", ""]
    r += ["| Stato | Funzioni | Significato |", "| --- | ---: | --- |"]
    r += [f"| {SIMBOLI[s['id']]} {s['nome']} | {conta[s['id']]} | {s['spiegazione']} |" for s in stati]
    if col.get("jvm"):
        r += ["", f"Collaudo della {app['versione']} ({data_lunga(col['data'])}): {col['jvm']} test sul codice; {col['android_note']} test Android su emulatore tipo Note 10 Plus e {col['android_compatto']} su telefono compatto da 360 dp."]
    for a in dict.fromkeys(f["area"] for f in funzioni):
        r += ["", f"### {a}", "", "| Funzione | Stato | Dalla | Descrizione |", "| --- | --- | --- | --- |"]
        for f in (x for x in funzioni if x["area"] == a):
            desc = f["descrizione"] + (f" *{f['nota']}*" if f["nota"] else "")
            r.append(f"| **{f['nome']}** | {SIMBOLI[f['stato']]} {nome_stato[f['stato']]} | {f['dal'] or '—'} | {desc.replace('|', '/')} |")
    r += ["", "## Installazione", "",
          f"1. Dal telefono scarica `{app['apk_nome']}` dalla [pagina della versione]({repo}/releases/tag/{tag}).",
          "2. Apri il file dalle notifiche o da Download. La prima volta Android chiede di consentire l'installazione di app dal browser: consenti solo per questa occasione, se preferisci.",
          "3. Tocca **Installa** (o **Aggiorna** se hai già LumiShelf). Una versione nuova si installa sopra la precedente: libreria, progressi e raccolte restano.",
          "4. Per le versioni successive: in LumiShelf apri **Impostazioni › Informazioni › Controlla aggiornamenti**.", "",
          f"Sul telefono l'app si chiama «{app['etichetta']}» (pacchetto `{app['pacchetto']}`): è la versione su cui si sviluppa la nuova interfaccia.", "",
          "Verifica facoltativa del file:", "",
          f"- SHA-256 dell'APK: `{app['apk_sha256'] or 'nella pagina della versione'}`",
          f"- SHA-256 del certificato di firma: `{app['cert_sha256']}`", "",
          "## Dati dell'app", "",
          "| | |", "| --- | --- |",
          f"| Versione | {app['versione']} (codice {app['codice']}), pubblicata il {data_lunga(app['data'])} |",
          f"| Android | da {app['min_android']} (API {app['min_sdk']}), compilata per Android {app['target_android']} (API {app['target_sdk']}) |",
          "| Lingua | Italiano |",
          "| Formati | PDF, EPUB, CBZ, CBR, CB7, ZIP, RAR, 7Z, JPG, PNG, WebP, BMP, DOCX, XLS, XLSX, XLSM, XLTX, XLTM, TXT, LOG, XML, JSON, CSV, Markdown, HTML, YAML, INI, Properties, DICOM; DOC, ODT e RTF con un'app esterna |",
          "| Dati | Catalogo, progressi, raccolte e metadati in database sul telefono. Backup in un file JSON quando lo chiedi |",
          "| Rete | Solo per la sincronizzazione sulla rete locale e per il controllo aggiornamenti, quando lo chiedi. Nessun account, nessun tracciamento |",
          "| Codice sorgente | Non pubblicato in questo repository |", "",
          "## Versioni", ""]
    for v in versioni:
        r += [f"### {v['versione']} · {data_lunga(v['data'])}", "", f"**{v['titolo']}**", ""] + [f"- {p}" for p in v["punti"]] + [""]
    r += ["---", "", f"Questa pagina è generata da `strumenti/genera.py` a partire dai file in `dati/`. Segnalazioni e idee: [Issues]({repo}/issues)."]
    return "\n".join(r) + "\n"


def note_versione(app, versioni):
    v = versioni[0]
    righe = [f"## {v['titolo']}", ""] + [f"- {p}" for p in v["punti"]] + ["",
             "### Installazione",
             f"Scarica `{app['apk_nome']}` dal telefono, aprilo e tocca **Installa** o **Aggiorna**: libreria, progressi e raccolte restano.",
             f"Sul telefono l'app si chiama «{app['etichetta']}» (`{app['pacchetto']}`). Android {app['min_android']} o successivo.", "",
             "### Verifica",
             f"- SHA-256 dell'APK: `{app['apk_sha256']}`",
             f"- SHA-256 del certificato: `{app['cert_sha256']}`", "",
             f"Funzioni e stato di ogni funzione: {app['pagina']}"]
    return "\n".join(righe) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--schermate"); a = ap.parse_args()
    app, cat, versioni = carica()
    if a.schermate:
        schermate(a.schermate)
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "index.html").write_text(pagina(app, cat, versioni), encoding="utf-8")
    (ROOT / "docs" / ".nojekyll").write_text("", encoding="utf-8")
    (ROOT / "docs" / "sitemap.xml").write_text(sitemap(app), encoding="utf-8")
    radice(app)
    (ROOT / "README.md").write_text(readme(app, cat, versioni), encoding="utf-8")
    (ROOT / "dati" / "note_versione.md").write_text(note_versione(app, versioni), encoding="utf-8")
    print("pagina, README e note generati")
