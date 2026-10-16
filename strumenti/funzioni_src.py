# Fonte del catalogo delle funzioni di LumiShelf (genera dati/funzioni.json).
# stato: telefono | emulatore | ereditata | limiti | programma | rinviata | decidere
F = []
def f(area, nome, desc, dal, stato, nota=""):
    F.append(dict(area=area, nome=nome, descrizione=desc, dal=dal, stato=stato, nota=nota))

A = "Avvio e accessi"
f(A, "Benvenuto e schede informative", "Benvenuto illustrato e cinque schede da toccare: Libreria, Lettori, Editor, Ricerca e Smart Library, Backup e privacy. Si possono saltare.", "1.18.6", "telefono")
f(A, "Scelta dell'accesso ai file", "Cartelle scelte con Android (SAF) oppure scansione totale della memoria, con le garanzie sulla privacy spiegate prima di scegliere.", "1.18.5", "telefono")
f(A, "Primo caricamento della libreria", "Scansione con contatori reali (documenti trovati, file esaminati, cartelle), interruzione e riprova; la Home si apre a caricamento finito.", "1.18.5", "telefono")
f(A, "Riapertura rapida", "Dopo la configurazione l'app apre direttamente la Home, senza introduzione; con cataloghi molto grandi compare un caricamento neutro.", "1.18.5", "telefono")
f(A, "Rivedi l'introduzione e Ripeti configurazione", "Da Impostazioni › Informazioni, senza perdere catalogo, progressi e raccolte.", "1.18.5", "emulatore")

A = "Home e Libreria"
f(A, "Home", "Continua a leggere, ultimi aggiunti, raccolte in evidenza, preferiti e statistiche della libreria.", "1.18.6", "telefono")
f(A, "Libreria a griglia o elenco", "Copertine, titolo, autore, formato e avanzamento; filtri per formato, preferiti, stato, segnalibri e Manga; ordinamento.", "1.18.6", "telefono")
f(A, "Selezione multipla", "Preferiti, aggiungi a raccolta o ai manga, stato di lettura, nascondi, rimuovi dalla libreria per più file insieme.", "1.18.6", "telefono")
f(A, "Libreria su schermo largo", "Da 720 dp (tablet, telefono in orizzontale) catalogo e dettaglio affiancati, con scorrimenti indipendenti.", "1.19.0", "emulatore")
f(A, "Copertine dai file", "Prima pagina dei PDF, prima immagine di CBZ/ZIP, copertina interna degli EPUB, immagini; create in sottofondo. Si può spegnere.", "1.19.1", "emulatore")
f(A, "Aggiungi file e cartelle", "Un pannello unico: file singoli o multipli, cartelle, provider cloud installati sul telefono, ricezione da un altro dispositivo.", "1.18.6", "telefono")
f(A, "Foto come PDF", "Scatta una foto con la fotocamera del telefono e la salva come PDF di una pagina nella libreria.", "1.18.2", "ereditata", "Da provare sul telefono.")

A = "Cerca"
f(A, "Ricerca nella libreria", "Titolo, autore, tag, categoria e nome del file; schede per formato con i conteggi; ricerche recenti. Il campo resta fermo mentre i risultati cambiano.", "1.19.0", "emulatore")
f(A, "Filtri avanzati e ordinamento", "Tipo, data, categoria, autore, dimensione e stato nella pagina; ordine per pertinenza, titolo, aggiunti o letti di recente.", "1.19.0", "emulatore")

A = "Documento"
f(A, "Azioni del file", "Scheda dal basso con gruppi: Leggi, Organizza, Modifica, Condividi, Gestione file. Il tocco apre le azioni, «Apri» avvia la lettura.", "1.18.6", "telefono")
f(A, "Dettaglio del documento", "Copertina grande, dati del file, avanzamento, descrizione, informazioni e «Potrebbero interessarti» (serie, autore, categoria, tag).", "1.19.0", "emulatore")
f(A, "Modifica metadati", "Titolo, autore, categoria, tag a pulsanti, lingua, data con calendario, valutazione; «Compila dal file» per EPUB e PDF.", "1.19.1", "emulatore")
f(A, "Cambia copertina", "Dal documento, sei grafiche con titolo e autore, un'immagine dalla galleria, ripristino.", "1.19.1", "emulatore")
f(A, "Rinomina", "Cambia il nome del file nella sua cartella: progressi, segnalibri, raccolte, copertina e metadati restano legati al documento.", "1.19.2", "emulatore")
f(A, "Condividi ed esporta una copia", "Condivisione con un link temporaneo in sola lettura, invio a un dispositivo sulla rete locale, copia in una cartella a scelta.", "1.19.1", "emulatore")
f(A, "Nascondi, rimuovi, elimina", "Tre azioni distinte con la conseguenza scritta accanto; l'eliminazione del file chiede conferma.", "1.18.6", "telefono")
f(A, "Scegli il lettore", "Per i formati che più lettori sanno aprire (per esempio un PDF come manga), la scelta resta per quel documento.", "1.18.5", "emulatore")
f(A, "Sposta in…", "Spostare un file in un'altra cartella conservando i suoi dati.", "", "programma", "Serve la scelta della cartella di destinazione e la copia tra provider diversi.")

A = "Raccolte e manga"
f(A, "Raccolte e serie", "Raccolte manuali e serie automatiche, con descrizione, icona, colore e scelta di mostrarle in Home.", "1.18.6", "telefono")
f(A, "Sezione Manga", "Riempita a mano dalla libreria o dal telefono, con serie create da te e riordino dei volumi. Nessun raggruppamento automatico per nome.", "1.18.8", "emulatore")
f(A, "Pagina della serie", "Copertina, preferito, autore, generi, descrizione, volumi, pagine e valutazione; «Continua» dal volume giusto; schede Volumi, Informazioni e Correlati; Modifica la serie.", "1.19.2", "emulatore")
f(A, "Raccolte intelligenti a regole", "Raccolte che si riempiono da sole secondo regole (autore, tag, stato…).", "", "decidere")

A = "Lettore PDF"
f(A, "Pagina e navigazione", "Pagina come un foglio, cursore, salto di pagina, miniature; avanti e indietro veloci senza pagine sbagliate.", "1.18.9", "emulatore")
f(A, "Indice, segnalibri e ricerca", "Sommario interno del PDF, più segnalibri per documento, ricerca con l'elenco dei risultati e l'estratto.", "1.18.9", "emulatore")
f(A, "Modalità di lettura", "Pagina singola, scorrimento continuo o doppia pagina; pagina scura per la sera; ritaglio dei margini; zoom.", "1.18.9", "emulatore")

A = "Lettore EPUB"
f(A, "Impaginazione vera", "Il libro viene impaginato secondo schermo e testo; la posizione resta cambiando carattere o margini; capitoli dall'indice del libro.", "1.18.9", "emulatore")
f(A, "Aspetto del testo", "Temi Chiaro, Seppia, Notte, Amoled; dimensione, carattere (anche TTF/OTF dal telefono), interlinea, margini, sillabazione, capolettera.", "1.18.9", "emulatore")
f(A, "Ricerca e segnalibri", "Risultati con capitolo ed estratto, più segnalibri con l'inizio del testo della pagina.", "1.18.9", "emulatore")
f(A, "Immagini e stili dei libri", "Le immagini interne e il CSS completo dei libri non vengono ancora riprodotti: il testo mantiene solo gli stili di base.", "1.18.9", "limiti")

A = "Lettore manga e fumetti"
f(A, "Formati", "CBZ/ZIP, CBR/RAR, CB7/7Z, PDF letti come manga e immagini; ordine naturale delle pagine; capitoli dalle cartelle dell'archivio.", "1.18.5", "emulatore")
f(A, "Barra del lettore", "Cursore e griglia di tutte le pagine; Capitoli · Luminosità · Modo · Zoom · Altro; segnalibro sulla pagina.", "1.18.7", "emulatore", "La 1.18.7 è stata provata sul telefono; le richieste emerse sono nella 1.18.8.")
f(A, "Doppia pagina", "Sempre affiancata, anche in verticale; copertina da sola; tavole già larghe intere.", "1.18.8", "emulatore")
f(A, "Zoom e gesti", "Pizzico centrato tra le dita, spostamento 1:1 con inerzia, doppio tocco sulla pagina toccata, sfoglio tirando oltre il bordo.", "1.18.8", "emulatore", "I gesti vanno provati a mano sul telefono.")
f(A, "Modalità e direzione", "Verticale, orizzontale, Webtoon continuo; sinistra → destra di base, scelta per formato e per singolo file; volume successivo a fine lettura.", "1.18.7", "emulatore")
f(A, "Luce, sfondo e tasti volume", "Luminosità e luce calda solo durante la lettura, sfondo nero, grafite, bianco o seppia, sfoglio con i tasti del volume.", "1.18.7", "emulatore")
f(A, "Ritaglio, contrasto e grigi", "Ritaglio dei bordi bianchi uniformi, contrasto e scala di grigi; non riconosce le singole vignette.", "1.18.5", "limiti")
f(A, "Cartelle di sole immagini come volumi", "Per scelta si consiglia un file CBZ, ZIP, RAR o PDF per volume.", "", "decidere")

A = "Editor"
f(A, "Editor PDF", "Annotazioni, penna, evidenziatore, testo, firma grafica, immagini; pagine (ruota, duplica, elimina, sposta, estrai, unisci, dividi, ritaglia); moduli; OCR offline; firma con certificato P12/PFX; stampa.", "1.18.2", "ereditata", "Funziona come nella 1.18.2; il rifacimento dell'interfaccia è in programma.")
f(A, "Fogli di calcolo", "XLS, XLSX, XLSM, XLTX, XLTM: formule, fogli, formati, bordi, celle unite, filtri, ordinamento, blocco riquadri, protezione, convalida, commenti, grafici supportati. Le macro VBA si conservano, non si eseguono.", "1.18.2", "ereditata", "Cartelle di lavoro molto grandi e parti avanzate di Excel sono supportate solo in parte.")
f(A, "Documenti DOCX", "Editor di base con formattazione, copia, PDF e stampa; i documenti complessi sono protetti dalle sovrascritture.", "1.18.2", "limiti")
f(A, "Testo e dati", "TXT, LOG, XML, JSON, CSV, Markdown, HTML, YAML, INI, Properties: modifica, ricerca e sostituzione, vai alla riga, codifica e terminatori conservati.", "1.18.2", "ereditata")
f(A, "Salvataggio sicuro e bozze", "Salva, salva una copia o esporta; conflitti se il file cambia altrove; bozze recuperabili dopo una chiusura improvvisa.", "1.18.2", "ereditata")
f(A, "DOC, ODT, RTF", "Si aprono con un'app esterna installata sul telefono.", "1.18.2", "limiti")
f(A, "Nuova interfaccia degli editor", "Comandi contestuali, annulla/ripristina, ricerca e salvataggi uniformi in tutti gli editor; poi editor per EPUB, immagini e archivi.", "", "programma")

A = "Strumenti"
f(A, "Smart Library", "Analisi su richiesta di copertine e metadati mancanti, duplicati verificati sull'intero contenuto, raccolte per categoria.", "1.18.5", "limiti", "Assistente locale: niente ricerca di dati online. La rifinitura grafica è in programma.")
f(A, "DICOM", "Esami e serie, frame, finestra e inversione, esportazione PNG, informazioni, modalità privacy, report anonimo, apertura esterna. Uso non diagnostico.", "1.18.5", "limiti", "Alcune compressioni richiedono un visualizzatore esterno.")
f(A, "Sincronizza dispositivi", "Rete locale tra telefoni Android e client Windows: abbinamento con codice di sei cifre, trasferimenti cifrati, confronto della libreria e dei progressi.", "1.18.2", "ereditata", "Da collaudare tra due dispositivi reali.")
f(A, "Diagnostica e memoria", "Spazio usato da cache e copertine, svuotamento, report tecnici da condividere.", "1.18.5", "ereditata")

A = "Impostazioni e dati"
f(A, "Aspetto", "Tema chiaro, scuro, Amoled o di sistema; accento; dimensione e angoli delle copertine; etichette, avanzamento, animazioni, sfondo.", "1.18.6", "telefono")
f(A, "Preferenze di lettura", "Valori predefiniti per PDF, EPUB e manga; orientamento; schermo acceso. Nel lettore resta solo il pannello rapido.", "1.18.6", "telefono")
f(A, "Libreria e cartelle", "Metodo di accesso, cartelle autorizzate, ultima scansione e aggiornamento della libreria nello stesso posto.", "1.18.6", "telefono")
f(A, "Backup e ripristino", "File JSON con indice, progressi, segnalibri, stato, raccolte, serie manga, metadati e preferenze.", "1.18.5", "emulatore", "Non contiene i documenti, le autorizzazioni delle cartelle e le copertine personalizzate.")
f(A, "Pagina del progetto e aggiornamenti", "Impostazioni › Informazioni: apre questa pagina e controlla, quando lo chiedi, se su GitHub c'è una versione più recente.", "1.19.3", "emulatore")
f(A, "Telefoni piccoli e testo grande", "Interfaccia collaudata da 360 dp di larghezza, con testo al 150% e in orizzontale.", "1.18.6", "emulatore")

A = "Più avanti"
f(A, "Rifinitura di Smart Library, DICOM e rete locale", "Schermate allineate al resto dell'app.", "", "programma")
f(A, "Schermi larghi negli editor e negli strumenti", "Pannelli affiancati come nella Libreria.", "", "programma")
f(A, "Misure di velocità sul telefono e pulizia del codice", "Avvio, cataloghi grandi, PDF pesanti, memoria; poi riordino del codice.", "", "programma")
f(A, "Gattino animato nel caricamento", "Un'animazione durante il primo caricamento dei file.", "", "rinviata")
f(A, "Account e sincronizzazione cloud", "Oggi tutto resta sul telefono; i servizi cloud si raggiungono attraverso Android.", "", "decidere")
f(A, "Metadati e copertine da Internet", "Ricerca online di titoli, autori, ISBN e copertine.", "", "decidere")
f(A, "PIN, impronta e raccolte protette", "Protezione dell'app o di singole raccolte.", "", "decidere")
f(A, "Backup protetto da password", "Backup cifrato.", "", "decidere")

STATI = [
  dict(id="telefono", nome="Provata sul telefono", spiegazione="Funziona nell'uso reale su Samsung Galaxy Note 10 Plus (riscontro sulla 1.18.6)."),
  dict(id="emulatore", nome="Collaudata su emulatore", spiegazione="Test automatici superati su due emulatori (tipo Note 10 Plus e telefono compatto); manca la prova sul telefono."),
  dict(id="ereditata", nome="Presente, da ricollaudare", spiegazione="Funzione già presente nelle versioni precedenti e mantenuta; non ancora ricollaudata nelle versioni recenti."),
  dict(id="limiti", nome="Disponibile con limiti", spiegazione="Utilizzabile, con limiti scritti nella descrizione."),
  dict(id="programma", nome="In programma", spiegazione="Prevista nei prossimi lavori."),
  dict(id="rinviata", nome="Rinviata", spiegazione="Rimandata per scelta."),
  dict(id="decidere", nome="Da decidere", spiegazione="Idea possibile, non ancora approvata."),
]

if __name__ == "__main__":
    import json, sys, collections
    out = dict(stati=STATI, funzioni=F)
    c = collections.Counter(x["stato"] for x in F)
    print(len(F), dict(c), file=sys.stderr)
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
