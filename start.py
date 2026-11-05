"""Start PRoViLE; --check checks local configuration without API requests."""
import argparse
import importlib.util
import os
from pathlib import Path
import runpy
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    required = ('dotenv', 'openai', 'langchain_ollama', 'pandas', 'numpy', 'matplotlib', 'seaborn')
    missing = [name for name in required if importlib.util.find_spec(name) is None]
    if missing:
        print('Installeer eerst: .\\.venv\\Scripts\\python.exe -m pip install -e .')
        print('Ontbrekend: ' + ', '.join(missing))
        return 1
    from dotenv import load_dotenv
    load_dotenv(root / '.env', override=True, encoding='utf-8-sig')
    if os.getenv('LLM_SOURCE', 'OpenRouter') == 'OpenRouter' and not os.getenv('OPENROUTER_API_KEY', '').strip():
        print('Vul OPENROUTER_API_KEY in .env in en sla het bestand op.')
        return 1
    for name in ('ATTACKER_LLM', 'TARGET_LLM', 'JUDGE_LLM'):
        if not os.getenv(name, '').strip():
            print(f'Vul {name} in .env in.')
            return 1
    app = root / 'provile'
    for name in ('ATK_OBJECTIVES_FILEPATH', 'ATK_TECHNIQUES_FILEPATH'):
        value = os.getenv(name, '')
        if not value or not (app / value).is_file():
            print(f'Bestand voor {name} ontbreekt; controleer .env.')
            return 1
    if args.check:
        print('Lokale configuratie OK. API-sleutel en modeltoegang zijn niet online getest.')
        return 0
    os.chdir(app)
    for folder in ('logs', 'results'):
        (app / folder).mkdir(exist_ok=True)
    print('PRoViLE start. Resultaten in provile/results. Bestaande resultaten worden overschreven.')
    runpy.run_module('provile.main', run_name='__main__')
    print('Klaar. Bekijk provile/results en provile/logs.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
