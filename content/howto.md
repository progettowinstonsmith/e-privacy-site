Title: e-privacy HOWTO contenuti
Date: 2007-04-03 10:20
Category: howto
Tags: howto
lang: it

_"La paranoia è una virtù." - Anonimo, 1984_


Questa pagina spiega come realizzare le pagine del sito di e-privacy.

## Keyword

Ogni pagina inizia con un set di keyword:

    Title: e-privacy <anno> - <tema>
    Date: <data> (es. 2007-04-03 10:20)
    Category: <anno>
    Tags: <anno>, eprivacy, <altre keyword prese dal tema>
    lang: it

## Citazione

Tutte la pagine iniziano con una citazione:

_"La paranoia è una virtù." - Anonimo, 1984_


## Primo paragrafo

Il primo paragrafo (*non* introdotto da un titolo) include le
informazioni basilari dell'incontro. Ad es:

Il (`<quamdo>`) 18 e 19 maggio 2007, in (`<dove>`) **Palazzo Vecchio**
a Firenze si è svolto il (`<cosa>`) convegno **e-privacy**, dedicato ai
problemi della privacy nell'era digitale.

## Secondo paragrafo

Il secondo paragrafo (sempre senza titolo) contiene una descrizione
dell'evento:

Durante questi due giorni sono stati svolti interventi di carattere
tecnologico e giuridico sul tecnocontrollo come evoluzione del
controllo sociale, sulle problematiche legali in riferimento alla
196/2003 ed alla data retention prevista delle leggi vigenti e future,
sulla crittografia, e su altri argomenti fortemente legati alla tutela
della privacy individuale e dei diritti civili in Rete, come il
diritto all'anonimato e la riforma del codice penale in materia di
cybercrime.

## Paragrafi successivi

I paragrafi successivi possono contenere altre informazioni
descrittive del convegno, come ad esempio la descrizione del Big
Brother Award o informazioni su altri eventi speciali tenuti
all'interno del convegno (eventuali titoli a livello 3).

    ### Big Brother Awards

    Durante il convegno, nella mattinata di sabato, è avvenuta la
    cerimonia di consegna dei
    [Big Brother Award Italia 2007](http://bba.winstonsmith.info).
    [...]

## Programma del convegno

Dopo il titolo a livello 2 con la definizione dell'ancora `programma`:

    ## <a name="programma"></a>Programma del Convegno

Si riporta una tabella del programma del convegno.

Ogni giornata è indicata come titolo a livello 4 con ancora (ad es. `ve`):

    #### <a name="ve"></a>Venerdì 18 Maggio

Di seguito la definizione delle 4 colonne:

    **Inizio** | **Fine** | **Relatore** | **Titolo** 
    --- | --- | --- | --- | ---

e i relativi interventi ad iniziare dalla **Registrazione dei
partecipanti** (in questo caso notare come l'unione delle ultime due
colonne è indicata da una doppia sbarra messa di seguito)

    **09:00** | **09:30** || **Registrazione partecipanti**
    **09:30** | **09:45** || Saluto degli organizzatori
    **09:45** | **10:30** | [Il Progetto Winston Smith: relazione annuale](#i1) | Marco A. Calamari


Ogni singolo intervento è indicato da:

- orario di inizio
- orario di fine
- titolo (da indicare come link ad un'ancora interna che definiremo in
  seguito - denominare tutte le ancore in modo consecutivo, tipo
  `i1`,`i2`,`i3`, ecc.)
- infine il nome del relatore (possibilmente nel formato `Nome
Cognome`), più relatori sono separati da uno slash (`/`).

Ad esempio:

    **10:30** | **11:15** | [Dal controllo della tecnologia al controllo sulla tecnologia](#i2) | Shara Monteleone

## Dettaglio degli Interventi

Introdotti dal titolo a livello 2 con ancora `interventi`:

    ## <a name="interventi"></a>Interventi

Ci sono i singoli interventi formattati come segue:

- autore (titolo a livello quattro con ancora progressiva, es. `i1`),
  al termine del titolo introdurre l'espressione `[^](#ve)` (al posto
  di `ve` l'ancora definita per la giornata dell'intervento)
- titolo
- slides, audio, video
- paragrafo descrittivo

Ad esempio:

    #### <a name="i1"></a>Marco A. Calamari - Progetto Winston Smith [^](#ve)
    _Progetto Winston Smith: relazione annuale_  
    slide in formato  [ pdf](/atti/ep2007_Calamari_PWS_relazione_2006.pdf), [ odp](/atti/ep2007_Calamari_PWS_relazione_2006.odp); audio mp3 dell' [intervento](./audio/ep2007_Calamari_PWS_relazione_2006.mp3).

    La relazione descriverà i progetti realizzati e pianificati, gli
    obbiettivi raggiunti e mancati, le attività in corso e gli
    orientamenti generali del Progetto per le attività future: Privacy
    Box, DDL 1728 sulla Data Retention, Progetto 95%, gestione delle
    risorse per la privacy in rete, partecipazione a convegni e gruppi di
    lavoro.


## <a name="sede"></a>Sede del convegno

Dopo tutti gli interventi viene riportata la sede del convegno.

    ## <a name="sede"></a>Sede del convegno


Ad esempio:

    Il convegno si terrà a Firenze in Palazzo Vecchio, la giornata di
    venerdì sarà nel
    [Salone dei 200 e nella Sala degli 8 ](/images/site/fi-pv-palazzovecchio_pianta_grande.gif)
    mentre sabato nella Sala Incontri.


## Organizzatori, Patrocini e Sponsor

A seguire saranno riportati gli organizzatori, i patrocini e gli sponsor.

    ## Organizzatori, Patrocini e Sponsor
    
    Il convegno è stato organizzato dal
    [Progetto Winston Smith](http://pws.winstonsmith.info/),
    un'associazione senza fini di lucro che si occupa della difesa del
    diritto alla privacy in Rete e fuori fin dallo scorso millennio.


Se esistono tabelle o gruppi di icone/link degli organizzatori/sponsor
vanno riportate in questa sezione così come sono, es:

    [ ![](img/logoq1.gif) ](http://www.comune.firenze.it/comune/organi/q1/1q.htm) |  [ ![](img/pws-logo.png) ](http://pws.winstonsmith.info) |  [ ![](img/logo_sm.gif) ](http://www.privacyinternational.org) |  [ ![](img/bonw.gif) ](http://www.bigbrotherawards.org)
    ---|---|---|---
    [ ![](img/sikurezza_logo.png) ](http://www.sikurezza.org) |  [ ![](img/s0ftpj_logo.png) ](http://www.s0ftpj.org) |  [ ![](img/metro_logo.png) ](http://www.olografix.org) |  [ ![](img/recursiva_logo.png) ](http://www.recursiva.org) |  [ ![](img/cgt_logo.gif) ](http://www.giuristitelematici.it/)
    ---|---|---|---|---

## Cose da cancellare o tralasciare

 I contatti e la nota di copyright al fondo sono da cancellare
