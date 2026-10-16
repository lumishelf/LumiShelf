# LumiShelf

Libreria e lettore di documenti per Android: PDF, EPUB, manga e fumetti, documenti Office e testo, organizzati in un unico posto. Nessun account: i file restano sul telefono.

**[Scarica la 1.19.3](https://github.com/lumishelf/LumiShelf/releases/download/v1.19.3/LumiShelf_1.19.3.apk)** (APK, 68 MB, Android 8.0 o successivo) · [Pagina del progetto](https://lumishelf.github.io/LumiShelf/) · [Tutte le versioni](https://github.com/lumishelf/LumiShelf/releases)

## Stato delle funzioni

67 funzioni in tutto. Ogni funzione passa per tre gradini: implementata, collaudata con test automatici su emulatore, provata sul telefono di riferimento (Samsung Galaxy Note 10 Plus).

| Stato | Funzioni | Significato |
| --- | ---: | --- |
| 📱 Provata sul telefono | 14 | Funziona nell'uso reale su Samsung Galaxy Note 10 Plus (riscontro sulla 1.18.6). |
| 🧪 Collaudata su emulatore | 28 | Test automatici superati su due emulatori (tipo Note 10 Plus e telefono compatto); manca la prova sul telefono. |
| 📦 Presente, da ricollaudare | 7 | Funzione già presente nelle versioni precedenti e mantenuta; non ancora ricollaudata nelle versioni recenti. |
| ⚠️ Disponibile con limiti | 6 | Utilizzabile, con limiti scritti nella descrizione. |
| 🗓️ In programma | 5 | Prevista nei prossimi lavori. |
| ⏸️ Rinviata | 1 | Rimandata per scelta. |
| 💭 Da decidere | 6 | Idea possibile, non ancora approvata. |

Collaudo della 1.19.3 (16 ottobre 2026): 293 test sul codice; 17 test Android su emulatore tipo Note 10 Plus e 17 su telefono compatto da 360 dp.

### Avvio e accessi

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Benvenuto e schede informative** | 📱 Provata sul telefono | 1.18.6 | Benvenuto illustrato e cinque schede da toccare: Libreria, Lettori, Editor, Ricerca e Smart Library, Backup e privacy. Si possono saltare. |
| **Scelta dell'accesso ai file** | 📱 Provata sul telefono | 1.18.5 | Cartelle scelte con Android (SAF) oppure scansione totale della memoria, con le garanzie sulla privacy spiegate prima di scegliere. |
| **Primo caricamento della libreria** | 📱 Provata sul telefono | 1.18.5 | Scansione con contatori reali (documenti trovati, file esaminati, cartelle), interruzione e riprova; la Home si apre a caricamento finito. |
| **Riapertura rapida** | 📱 Provata sul telefono | 1.18.5 | Dopo la configurazione l'app apre direttamente la Home, senza introduzione; con cataloghi molto grandi compare un caricamento neutro. |
| **Rivedi l'introduzione e Ripeti configurazione** | 🧪 Collaudata su emulatore | 1.18.5 | Da Impostazioni › Informazioni, senza perdere catalogo, progressi e raccolte. |

### Home e Libreria

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Home** | 📱 Provata sul telefono | 1.18.6 | Continua a leggere, ultimi aggiunti, raccolte in evidenza, preferiti e statistiche della libreria. |
| **Libreria a griglia o elenco** | 📱 Provata sul telefono | 1.18.6 | Copertine, titolo, autore, formato e avanzamento; filtri per formato, preferiti, stato, segnalibri e Manga; ordinamento. |
| **Selezione multipla** | 📱 Provata sul telefono | 1.18.6 | Preferiti, aggiungi a raccolta o ai manga, stato di lettura, nascondi, rimuovi dalla libreria per più file insieme. |
| **Libreria su schermo largo** | 🧪 Collaudata su emulatore | 1.19.0 | Da 720 dp (tablet, telefono in orizzontale) catalogo e dettaglio affiancati, con scorrimenti indipendenti. |
| **Copertine dai file** | 🧪 Collaudata su emulatore | 1.19.1 | Prima pagina dei PDF, prima immagine di CBZ/ZIP, copertina interna degli EPUB, immagini; create in sottofondo. Si può spegnere. |
| **Aggiungi file e cartelle** | 📱 Provata sul telefono | 1.18.6 | Un pannello unico: file singoli o multipli, cartelle, provider cloud installati sul telefono, ricezione da un altro dispositivo. |
| **Foto come PDF** | 📦 Presente, da ricollaudare | 1.18.2 | Scatta una foto con la fotocamera del telefono e la salva come PDF di una pagina nella libreria. *Da provare sul telefono.* |

### Cerca

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Ricerca nella libreria** | 🧪 Collaudata su emulatore | 1.19.0 | Titolo, autore, tag, categoria e nome del file; schede per formato con i conteggi; ricerche recenti. Il campo resta fermo mentre i risultati cambiano. |
| **Filtri avanzati e ordinamento** | 🧪 Collaudata su emulatore | 1.19.0 | Tipo, data, categoria, autore, dimensione e stato nella pagina; ordine per pertinenza, titolo, aggiunti o letti di recente. |

### Documento

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Azioni del file** | 📱 Provata sul telefono | 1.18.6 | Scheda dal basso con gruppi: Leggi, Organizza, Modifica, Condividi, Gestione file. Il tocco apre le azioni, «Apri» avvia la lettura. |
| **Dettaglio del documento** | 🧪 Collaudata su emulatore | 1.19.0 | Copertina grande, dati del file, avanzamento, descrizione, informazioni e «Potrebbero interessarti» (serie, autore, categoria, tag). |
| **Modifica metadati** | 🧪 Collaudata su emulatore | 1.19.1 | Titolo, autore, categoria, tag a pulsanti, lingua, data con calendario, valutazione; «Compila dal file» per EPUB e PDF. |
| **Cambia copertina** | 🧪 Collaudata su emulatore | 1.19.1 | Dal documento, sei grafiche con titolo e autore, un'immagine dalla galleria, ripristino. |
| **Rinomina** | 🧪 Collaudata su emulatore | 1.19.2 | Cambia il nome del file nella sua cartella: progressi, segnalibri, raccolte, copertina e metadati restano legati al documento. |
| **Condividi ed esporta una copia** | 🧪 Collaudata su emulatore | 1.19.1 | Condivisione con un link temporaneo in sola lettura, invio a un dispositivo sulla rete locale, copia in una cartella a scelta. |
| **Nascondi, rimuovi, elimina** | 📱 Provata sul telefono | 1.18.6 | Tre azioni distinte con la conseguenza scritta accanto; l'eliminazione del file chiede conferma. |
| **Scegli il lettore** | 🧪 Collaudata su emulatore | 1.18.5 | Per i formati che più lettori sanno aprire (per esempio un PDF come manga), la scelta resta per quel documento. |
| **Sposta in…** | 🗓️ In programma | — | Spostare un file in un'altra cartella conservando i suoi dati. *Serve la scelta della cartella di destinazione e la copia tra provider diversi.* |

### Raccolte e manga

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Raccolte e serie** | 📱 Provata sul telefono | 1.18.6 | Raccolte manuali e serie automatiche, con descrizione, icona, colore e scelta di mostrarle in Home. |
| **Sezione Manga** | 🧪 Collaudata su emulatore | 1.18.8 | Riempita a mano dalla libreria o dal telefono, con serie create da te e riordino dei volumi. Nessun raggruppamento automatico per nome. |
| **Pagina della serie** | 🧪 Collaudata su emulatore | 1.19.2 | Copertina, preferito, autore, generi, descrizione, volumi, pagine e valutazione; «Continua» dal volume giusto; schede Volumi, Informazioni e Correlati; Modifica la serie. |
| **Raccolte intelligenti a regole** | 💭 Da decidere | — | Raccolte che si riempiono da sole secondo regole (autore, tag, stato…). |

### Lettore PDF

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Pagina e navigazione** | 🧪 Collaudata su emulatore | 1.18.9 | Pagina come un foglio, cursore, salto di pagina, miniature; avanti e indietro veloci senza pagine sbagliate. |
| **Indice, segnalibri e ricerca** | 🧪 Collaudata su emulatore | 1.18.9 | Sommario interno del PDF, più segnalibri per documento, ricerca con l'elenco dei risultati e l'estratto. |
| **Modalità di lettura** | 🧪 Collaudata su emulatore | 1.18.9 | Pagina singola, scorrimento continuo o doppia pagina; pagina scura per la sera; ritaglio dei margini; zoom. |

### Lettore EPUB

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Impaginazione vera** | 🧪 Collaudata su emulatore | 1.18.9 | Il libro viene impaginato secondo schermo e testo; la posizione resta cambiando carattere o margini; capitoli dall'indice del libro. |
| **Aspetto del testo** | 🧪 Collaudata su emulatore | 1.18.9 | Temi Chiaro, Seppia, Notte, Amoled; dimensione, carattere (anche TTF/OTF dal telefono), interlinea, margini, sillabazione, capolettera. |
| **Ricerca e segnalibri** | 🧪 Collaudata su emulatore | 1.18.9 | Risultati con capitolo ed estratto, più segnalibri con l'inizio del testo della pagina. |
| **Immagini e stili dei libri** | ⚠️ Disponibile con limiti | 1.18.9 | Le immagini interne e il CSS completo dei libri non vengono ancora riprodotti: il testo mantiene solo gli stili di base. |

### Lettore manga e fumetti

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Formati** | 🧪 Collaudata su emulatore | 1.18.5 | CBZ/ZIP, CBR/RAR, CB7/7Z, PDF letti come manga e immagini; ordine naturale delle pagine; capitoli dalle cartelle dell'archivio. |
| **Barra del lettore** | 🧪 Collaudata su emulatore | 1.18.7 | Cursore e griglia di tutte le pagine; Capitoli · Luminosità · Modo · Zoom · Altro; segnalibro sulla pagina. *La 1.18.7 è stata provata sul telefono; le richieste emerse sono nella 1.18.8.* |
| **Doppia pagina** | 🧪 Collaudata su emulatore | 1.18.8 | Sempre affiancata, anche in verticale; copertina da sola; tavole già larghe intere. |
| **Zoom e gesti** | 🧪 Collaudata su emulatore | 1.18.8 | Pizzico centrato tra le dita, spostamento 1:1 con inerzia, doppio tocco sulla pagina toccata, sfoglio tirando oltre il bordo. *I gesti vanno provati a mano sul telefono.* |
| **Modalità e direzione** | 🧪 Collaudata su emulatore | 1.18.7 | Verticale, orizzontale, Webtoon continuo; sinistra → destra di base, scelta per formato e per singolo file; volume successivo a fine lettura. |
| **Luce, sfondo e tasti volume** | 🧪 Collaudata su emulatore | 1.18.7 | Luminosità e luce calda solo durante la lettura, sfondo nero, grafite, bianco o seppia, sfoglio con i tasti del volume. |
| **Ritaglio, contrasto e grigi** | ⚠️ Disponibile con limiti | 1.18.5 | Ritaglio dei bordi bianchi uniformi, contrasto e scala di grigi; non riconosce le singole vignette. |
| **Cartelle di sole immagini come volumi** | 💭 Da decidere | — | Per scelta si consiglia un file CBZ, ZIP, RAR o PDF per volume. |

### Editor

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Editor PDF** | 📦 Presente, da ricollaudare | 1.18.2 | Annotazioni, penna, evidenziatore, testo, firma grafica, immagini; pagine (ruota, duplica, elimina, sposta, estrai, unisci, dividi, ritaglia); moduli; OCR offline; firma con certificato P12/PFX; stampa. *Funziona come nella 1.18.2; il rifacimento dell'interfaccia è in programma.* |
| **Fogli di calcolo** | 📦 Presente, da ricollaudare | 1.18.2 | XLS, XLSX, XLSM, XLTX, XLTM: formule, fogli, formati, bordi, celle unite, filtri, ordinamento, blocco riquadri, protezione, convalida, commenti, grafici supportati. Le macro VBA si conservano, non si eseguono. *Cartelle di lavoro molto grandi e parti avanzate di Excel sono supportate solo in parte.* |
| **Documenti DOCX** | ⚠️ Disponibile con limiti | 1.18.2 | Editor di base con formattazione, copia, PDF e stampa; i documenti complessi sono protetti dalle sovrascritture. |
| **Testo e dati** | 📦 Presente, da ricollaudare | 1.18.2 | TXT, LOG, XML, JSON, CSV, Markdown, HTML, YAML, INI, Properties: modifica, ricerca e sostituzione, vai alla riga, codifica e terminatori conservati. |
| **Salvataggio sicuro e bozze** | 📦 Presente, da ricollaudare | 1.18.2 | Salva, salva una copia o esporta; conflitti se il file cambia altrove; bozze recuperabili dopo una chiusura improvvisa. |
| **DOC, ODT, RTF** | ⚠️ Disponibile con limiti | 1.18.2 | Si aprono con un'app esterna installata sul telefono. |
| **Nuova interfaccia degli editor** | 🗓️ In programma | — | Comandi contestuali, annulla/ripristina, ricerca e salvataggi uniformi in tutti gli editor; poi editor per EPUB, immagini e archivi. |

### Strumenti

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Smart Library** | ⚠️ Disponibile con limiti | 1.18.5 | Analisi su richiesta di copertine e metadati mancanti, duplicati verificati sull'intero contenuto, raccolte per categoria. *Assistente locale: niente ricerca di dati online. La rifinitura grafica è in programma.* |
| **DICOM** | ⚠️ Disponibile con limiti | 1.18.5 | Esami e serie, frame, finestra e inversione, esportazione PNG, informazioni, modalità privacy, report anonimo, apertura esterna. Uso non diagnostico. *Alcune compressioni richiedono un visualizzatore esterno.* |
| **Sincronizza dispositivi** | 📦 Presente, da ricollaudare | 1.18.2 | Rete locale tra telefoni Android e client Windows: abbinamento con codice di sei cifre, trasferimenti cifrati, confronto della libreria e dei progressi. *Da collaudare tra due dispositivi reali.* |
| **Diagnostica e memoria** | 📦 Presente, da ricollaudare | 1.18.5 | Spazio usato da cache e copertine, svuotamento, report tecnici da condividere. |

### Impostazioni e dati

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Aspetto** | 📱 Provata sul telefono | 1.18.6 | Tema chiaro, scuro, Amoled o di sistema; accento; dimensione e angoli delle copertine; etichette, avanzamento, animazioni, sfondo. |
| **Preferenze di lettura** | 📱 Provata sul telefono | 1.18.6 | Valori predefiniti per PDF, EPUB e manga; orientamento; schermo acceso. Nel lettore resta solo il pannello rapido. |
| **Libreria e cartelle** | 📱 Provata sul telefono | 1.18.6 | Metodo di accesso, cartelle autorizzate, ultima scansione e aggiornamento della libreria nello stesso posto. |
| **Backup e ripristino** | 🧪 Collaudata su emulatore | 1.18.5 | File JSON con indice, progressi, segnalibri, stato, raccolte, serie manga, metadati e preferenze. *Non contiene i documenti, le autorizzazioni delle cartelle e le copertine personalizzate.* |
| **Pagina del progetto e aggiornamenti** | 🧪 Collaudata su emulatore | 1.19.3 | Impostazioni › Informazioni: apre questa pagina e controlla, quando lo chiedi, se su GitHub c'è una versione più recente. |
| **Telefoni piccoli e testo grande** | 🧪 Collaudata su emulatore | 1.18.6 | Interfaccia collaudata da 360 dp di larghezza, con testo al 150% e in orizzontale. |

### Più avanti

| Funzione | Stato | Dalla | Descrizione |
| --- | --- | --- | --- |
| **Rifinitura di Smart Library, DICOM e rete locale** | 🗓️ In programma | — | Schermate allineate al resto dell'app. |
| **Schermi larghi negli editor e negli strumenti** | 🗓️ In programma | — | Pannelli affiancati come nella Libreria. |
| **Misure di velocità sul telefono e pulizia del codice** | 🗓️ In programma | — | Avvio, cataloghi grandi, PDF pesanti, memoria; poi riordino del codice. |
| **Gattino animato nel caricamento** | ⏸️ Rinviata | — | Un'animazione durante il primo caricamento dei file. |
| **Account e sincronizzazione cloud** | 💭 Da decidere | — | Oggi tutto resta sul telefono; i servizi cloud si raggiungono attraverso Android. |
| **Metadati e copertine da Internet** | 💭 Da decidere | — | Ricerca online di titoli, autori, ISBN e copertine. |
| **PIN, impronta e raccolte protette** | 💭 Da decidere | — | Protezione dell'app o di singole raccolte. |
| **Backup protetto da password** | 💭 Da decidere | — | Backup cifrato. |

## Installazione

1. Dal telefono scarica `LumiShelf_1.19.3.apk` dalla [pagina della versione](https://github.com/lumishelf/LumiShelf/releases/tag/v1.19.3).
2. Apri il file dalle notifiche o da Download. La prima volta Android chiede di consentire l'installazione di app dal browser: consenti solo per questa occasione, se preferisci.
3. Tocca **Installa** (o **Aggiorna** se hai già LumiShelf). Una versione nuova si installa sopra la precedente: libreria, progressi e raccolte restano.
4. Per le versioni successive: in LumiShelf apri **Impostazioni › Informazioni › Controlla aggiornamenti**.

Sul telefono l'app si chiama «LumiShelf · UI prova» (pacchetto `com.lumishelf.ui4`): è la versione su cui si sviluppa la nuova interfaccia.

Verifica facoltativa del file:

- SHA-256 dell'APK: `fbeb6afa34a34de9623dbab5f851d83be916b975df548e7d2f3f2ec936e42441`
- SHA-256 del certificato di firma: `f37149ced02f46fd1f7f4d5430c72627e4857effd72840e1469429cdf8292596`

## Dati dell'app

| | |
| --- | --- |
| Versione | 1.19.3 (codice 88), pubblicata il 17 ottobre 2026 |
| Android | da 8.0 (API 26), compilata per Android 15 (API 35) |
| Lingua | Italiano |
| Formati | PDF, EPUB, CBZ, CBR, CB7, ZIP, RAR, 7Z, JPG, PNG, WebP, BMP, DOCX, XLS, XLSX, XLSM, XLTX, XLTM, TXT, LOG, XML, JSON, CSV, Markdown, HTML, YAML, INI, Properties, DICOM; DOC, ODT e RTF con un'app esterna |
| Dati | Catalogo, progressi, raccolte e metadati in database sul telefono. Backup in un file JSON quando lo chiedi |
| Rete | Solo per la sincronizzazione sulla rete locale e per il controllo aggiornamenti, quando lo chiedi. Nessun account, nessun tracciamento |
| Codice sorgente | Non pubblicato in questo repository |

## Versioni

### 1.19.3 · 17 ottobre 2026

**Pagina del progetto e aggiornamenti**

- Impostazioni › Informazioni › LumiShelf su GitHub: apre la pagina del progetto.
- Controlla aggiornamenti: confronta la versione installata con l'ultima pubblicata su GitHub e porta al download.
- «Avvisami delle nuove versioni»: controllo all'apertura, al massimo una volta al giorno. Spento di base.
- Privacy aggiornata: l'app usa Internet solo quando lo chiedi tu.

### 1.19.2 · 16 ottobre 2026

**Pagina della serie manga e Rinomina**

- Pagina della serie con copertina, preferito, autore, generi, descrizione, volumi, pagine e valutazione.
- Continua dal volume giusto; schede Volumi, Informazioni e Correlati; Modifica la serie.
- Rinomina il file: progressi, segnalibri, raccolte, copertina e metadati restano.

### 1.19.1 · 16 ottobre 2026

**Copertine dai file e metadati**

- Copertine vere create in sottofondo da PDF, CBZ/ZIP, EPUB e immagini.
- Modifica metadati con «Compila dal file», tag, lingua, data e stelle.
- Cambia copertina, Aggiungi tag, Esporta una copia.

### 1.19.0 · 16 ottobre 2026

**Ricerca e dettaglio del documento**

- Cerca con schede per formato, ricerche recenti, filtri avanzati e ordinamento.
- Dettaglio del documento con copertina grande, avanzamento e «Potrebbero interessarti».
- Titoli puliti dai nomi dei file.

### 1.18.9 · 16 ottobre 2026

**Lettori PDF ed EPUB**

- EPUB impaginato davvero, capitoli dall'indice, temi, caratteri anche importati.
- PDF con Indice, segnalibri, ricerca, scorrimento continuo e pagina scura.
- Più segnalibri per documento e risultati di ricerca con estratto.

### 1.18.8 · 13 ottobre 2026

**Manga scelti a mano, zoom e doppia pagina**

- Sezione Manga riempita a mano, serie create da te.
- Pizzico, spostamento con inerzia, doppio tocco sulla pagina toccata.
- Doppia pagina sempre affiancata; lettura da sinistra a destra di base.

### 1.18.7 · 12 ottobre 2026

**Lettore manga**

- Barra Capitoli · Luminosità · Modo · Zoom · Altro, griglia delle pagine.
- Webtoon continuo, direzione per formato e per file, volume successivo.

### 1.18.6 · 12 ottobre 2026

**Nuovo aspetto e funzioni in ordine**

- Avvio con benvenuto, cinque schede informative e configurazione in tre passi.
- Home, Libreria, Raccolte e Azioni del file ridisegnate.
- Ogni funzione in un solo posto: Impostazioni, Avanzate, Aggiungi.

### 1.18.5 · 12 ottobre 2026

**Base di partenza**

- Scelta tra cartelle selezionate e scansione totale, primo caricamento prima della Home.

---

Questa pagina è generata da `strumenti/genera.py` a partire dai file in `dati/`. Segnalazioni e idee: [Issues](https://github.com/lumishelf/LumiShelf/issues).
