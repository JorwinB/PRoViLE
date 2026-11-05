# PRoViLE starten in Visual Studio Code

Gedeelde teamrepository: https://github.com/JorwinB/PRoViLE (fork van COSSAS/PRoViLE).
Installeer Python 3.12 of nieuwer en clone deze repository in VS Code.
Maak vervolgens de omgeving en configuratie:

    python -m venv .venv
    Copy-Item .env.example .env

Is .env al aanwezig? Bewaar je eigen instellingen en overschrijf het bestand niet.

## 1. API-sleutel
Open .env, plak je sleutel tussen de aanhalingstekens achter OPENROUTER_API_KEY en sla op.
Maak een sleutel via https://openrouter.ai/settings/keys. Deel .env niet.
Git negeert .env en .venv. .env.example bevat geen sleutel.

## 2. Pakketten installeren
Open deze PRoViLE-map in VS Code. Kies Terminal > New Terminal:

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

Dit installeert de dependencies uit pyproject.toml. Gebruik hiervoor niet requirements.txt:
dat meegeleverde bestand bevat ook niet-projectspecifieke systeemonderdelen.
De omgeving hoeft niet handmatig geactiveerd te worden.

## 3. Starten
Optioneel: controleer de lokale configuratie zonder API-verzoeken:

```powershell
.\.venv\Scripts\python.exe start.py --check
```

Start de echte test met:

```powershell
.\.venv\Scripts\python.exe start.py
```

Of installeer de aanbevolen Microsoft Python-extensie en druk op F5.

## Eerste test
De ingestelde modellen zijn voor alle drie rollen openai/gpt-4.1-mini.
Modelinformatie: https://openrouter.ai/openai/gpt-4.1-mini.
De kleine test gebruikt 1 doel (profanity), 1 techniek en de oorspronkelijke 3 pogingen.
Normaal zijn dit 9 modelaanroepen, met meer aanroepen bij retries.
Dit is een eerste werkingstest, nog geen modelvergelijking voor je verslag.
De echte API-verbinding is nog niet getest en er zijn geen credits verbruikt door deze voorbereiding.

## Resultaten
- provile/results/heatmap.png
- provile/results/histogram.png
- provile/results/prompts.csv
- provile/logs/prompts.log

Het startscript maakt deze mappen aan. Bewaar resultaten na iedere run in een aparte map:
een volgende run overschrijft ze. Resultaten en logs worden niet automatisch in Git opgenomen.

## Daarna: volledige tests en andere modellen
Voor de volledige meegeleverde testset wijzig je in .env:

```dotenv
ATK_OBJECTIVES_FILEPATH="attack_objectives/test_objectives.csv"
ATK_TECHNIQUES_FILEPATH="attack_techniques/test_techniques.csv"
```

Dit doet veel meer aanroepen en kost meer credits. Verander TARGET_LLM om andere modellen
te vergelijken en houd de andere twee rollen gelijk. Een beoordelend model kan fouten maken.
Voor Ollama moet je later Ollama en de modellen installeren, LLM_SOURCE op Ollama zetten
en de drie modelnamen vervangen door lokaal geinstalleerde modellen.

## Toegevoegd aan de originele repository
- start.py: controleert instellingen en maakt uitvoermappen aan.
- .env en .env.example: startconfiguratie.
- .vscode: Python-instellingen, aanbevolen extensies en F5-configuratie.
- Twee smoke-CSV-bestanden: kleine selectie uit de originele testset.
- Aanvullende Git-uitsluitingen voor sleutels, logs en resultaten.

De oorspronkelijke evaluatiecode en scoreberekening zijn niet gewijzigd.
Werk per taak op een eigen branch en voeg wijzigingen samen via pull requests. Iedere deelnemer gebruikt een eigen .env; API-sleutels horen niet op GitHub.

