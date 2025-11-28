# SIMPLE TRANSLATOR (EN -> ES)

    Description
- Purpose: translate English words to Spanish from the terminal.
- Main features: translate words, save words to a dictionary file, view logs, clear data.


    Completed functionality and approximate grades
- Menu system with return to menu after actions — +1
- Console design: colors + animation — +2
- Decomposition, main.py only calls menu — +1
- Git repo + requirements + .gitignore +1
- README — +0.5
- External files for data (dictionary/log) — +1
- External API (MyMemory) — +1
- Video in README +2
- Two classes (`Translator`, `DictionaryManager`) — +1
- Validation via Regex + try/except in API call — +1
- Tests for 3 functions (utils, file manager, translator) — +1
- All interaction inside app — +1
- Logging — +1


    Usage
demo_video.mov

    Project Structure
translator/
├── README.md
├── requirements.txt
├── main.py
├── menu.py
├── translator.py
├── file_manager.py
├── utils.py
├── tests/
│   ├── test_tests.py
│   ├── test_dictionary_manager.py
│   └── test_translator.py
└── data/
    ├── dictionary.txt
    └── log.txt