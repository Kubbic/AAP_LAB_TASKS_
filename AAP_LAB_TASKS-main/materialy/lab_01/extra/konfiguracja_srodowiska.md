# ⚙️ Konfiguracja środowiska — Architektura aplikacji w Pythonie

> **Autor:** Prowadzący laboratoria
> **Cel:** Ten dokument przeprowadzi Cię krok po kroku przez konfigurację środowiska pracy z Pythonem, Jupyter Notebookami i VS Code. Zaczniemy od wersji skróconej (10 minut), a potem wyjaśnimy wszystko szczegółowo.

---

# 📋 CZĘŚĆ A: Quick Start (10 minut)

> **Jeśli chcesz po prostu odpalić środowisko i zacząć pracować — ta sekcja wystarczy.**
> Szczegóły i wyjaśnienia "dlaczego" znajdziesz w Części B.

### Krok 1: Zainstaluj Pythona — wybierz JEDNĄ z dwóch ścieżek

> Obie ścieżki są prawidłowe i prowadzą do tego samego celu. Wybierz tę, która Ci bardziej odpowiada. **Jeśli już masz zainstalowaną Minicondę z zajęć — zostań przy niej** (Ścieżka B).

**Ścieżka A: Python z python.org** (lżejsza, bliższa "czystemu" Pythonowi)

1. Wejdź na [python.org/downloads](https://www.python.org/downloads/)
2. Pobierz **Python 3.12** (lub nowszy)
3. ⚠️ **ZAZNACZ "Add Python to PATH"** podczas instalacji — to najczęstszy błąd!
4. Kliknij "Install Now"

**Ścieżka B: Miniconda** (jeśli już ją masz lub wolisz zarządzanie środowiskami przez `conda`)

1. Wejdź na [docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda/)
2. Pobierz instalator dla Windows (64-bit)
3. Podczas instalacji: zaznacz **"Add Miniconda3 to my PATH environment variable"**
4. Zainstaluj

**Weryfikacja** — otwórz terminal (PowerShell / CMD) i wpisz:
```bash
# Ścieżka A:
python --version          # powinno wyświetlić Python 3.12.x

# Ścieżka B:
conda --version           # powinno wyświetlić conda 24.x.x
python --version          # powinno wyświetlić Python 3.12.x
```
Jeśli widzisz numery wersji — jesteś w domu.

### Krok 2: Zainstaluj edytor — wybierz JEDNO z dwóch

> Na zajęciach polecałem **Google Antigravity** — jeśli już je masz, zostań przy nim. Jeśli wolisz klasyczny VS Code — działa równie dobrze.

**Opcja A: VS Code** (sprawdzony standard)

1. Pobierz VS Code: [code.visualstudio.com](https://code.visualstudio.com/)
2. Otwórz VS Code → panel rozszerzeń (`Ctrl+Shift+X`)
3. Zainstaluj:
   - **Python** (Microsoft)
   - **Jupyter** (Microsoft)
   - **GitHub Copilot** (GitHub) — opcjonalnie, ale polecam

**Opcja B: Google Antigravity** (darmowe, AI agent wbudowany, bazuje na VS Code)

1. Wejdź na stronę Google Antigravity i pobierz instalator
2. Zaloguj się kontem Google
3. Zainstaluj rozszerzenia **Python** i **Jupyter** (tak samo jak w VS Code)
4. Agent AI (Gemini 3) jest już wbudowany — nie trzeba nic dodatkowego

> Oba edytory obsługują Jupyter Notebooks, kernele i wirtualne środowiska identycznie. Instrukcje poniżej działają w obu.

### Krok 3: Stwórz projekt z wirtualnym środowiskiem

Otwórz terminal w VS Code (`Ctrl+``) i wpisz po kolei:

**Ścieżka A (python.org + venv):**
```bash
# 1. Stwórz folder projektu
mkdir moj-projekt
cd moj-projekt

# 2. Stwórz wirtualne środowisko
python -m venv .venv

# 3. Aktywuj je
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Mac/Linux:
source .venv/bin/activate

# 4. Zainstaluj potrzebne pakiety
pip install ipykernel jupyter requests

# 5. Zarejestruj kernel dla Jupyter
python -m ipykernel install --user --name=architektura-python --display-name="Python (Architektura)"
```

**Ścieżka B (Miniconda):**
```bash
# 1. Stwórz środowisko conda
conda create -n architektura python=3.12 -y

# 2. Aktywuj je
conda activate architektura

# 3. Zainstaluj potrzebne pakiety
pip install ipykernel jupyter requests

# 4. Zarejestruj kernel dla Jupyter
python -m ipykernel install --user --name=architektura-python --display-name="Python (Architektura)"

# 5. Stwórz / wejdź do folderu projektu
mkdir moj-projekt
cd moj-projekt
```

### Krok 4: Otwórz Jupyter Notebook w VS Code

1. `Ctrl+Shift+P` → wpisz "Jupyter: Create New Blank Notebook"
2. W prawym górnym rogu kliknij **"Select Kernel"**
3. Wybierz **"Python (Architektura)"** — to Twój kernel ze środowiska wirtualnego
4. Gotowe! Wpisz `print("Hello!")` w pierwszej komórce i naciśnij `Shift+Enter`

### Krok 5: Otwórz istniejący notebook (.ipynb)

1. Pobierz plik `.ipynb` z Teams/dysku
2. Otwórz VS Code → `File → Open File` → wybierz plik `.ipynb`
3. Wybierz kernel **"Python (Architektura)"** w prawym górnym rogu

---

**🎉 To wszystko. Masz działające środowisko.**

Jeśli coś nie działa lub chcesz zrozumieć, co właśnie zrobiłeś — czytaj dalej.

---

---

# 📖 CZĘŚĆ B: Szczegółowy przewodnik

> **Tu wyjaśniamy wszystko od podstaw.** Co to jest Python, jak działa, czym jest wirtualne środowisko, co to kernel, i dlaczego to wszystko tak wygląda.

---

## 1. Jak Python działa pod spodem

### Co to jest Python?

Python to **język interpretowany**. Oznacza to, że nie kompilujemy kodu do pliku wykonywalnego (jak w C++ czy Javie), tylko przekazujemy go **interpreterowi**, który wykonuje go linia po linii.

### Co się dzieje, gdy piszesz `python skrypt.py`?

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Twój kod    │────▶│  Interpreter │────▶│  Bytecode    │────▶│   Wynik      │
│  skrypt.py   │     │  python.exe  │     │  (.pyc)      │     │  w terminalu │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

1. **Piszesz kod** w pliku `.py` (zwykły plik tekstowy)
2. **Interpreter** (`python.exe` na Windowsie) czyta Twój kod
3. **Kompiluje go do bytecode'u** (pliki `.pyc` w folderze `__pycache__`)
4. **Wykonuje bytecode** na maszynie wirtualnej Pythona (PVM)

### Czym jest plik `.py`?

To **zwykły plik tekstowy** z kodem Pythona. Możesz go otworzyć w Notatniku, VS Code, czy czymkolwiek innym. Rozszerzenie `.py` to po prostu konwencja, żeby system wiedział, że to Python.

```python
# plik: hello.py
imie = input("Jak masz na imię? ")
print(f"Cześć, {imie}!")
```

### Jak uruchomić plik `.py`?

```bash
# W terminalu:
python hello.py

# Lub jeśli masz Pythona 3 i Pythona 2:
python3 hello.py
```

### A czym jest Jupyter Notebook (`.ipynb`)?

To **inny format pliku** — zamiast zwykłego tekstu, to plik JSON, który zawiera **komórki** (cells). Każda komórka to albo kod Pythona, albo tekst w Markdown. Główna różnica:

| | Plik `.py` | Jupyter Notebook `.ipynb` |
|---|---|---|
| **Format** | Zwykły tekst | JSON z komórkami |
| **Uruchamianie** | `python plik.py` — cały plik naraz | Komórka po komórce (Shift+Enter) |
| **Wyniki** | Tylko w terminalu | Wyświetlane pod komórką |
| **Interaktywność** | Niska | Wysoka — idealne do nauki |
| **Użycie w praktyce** | Aplikacje, skrypty, serwisy | Eksploracja, analiza, nauka |

---

## 2. Czym jest PATH i dlaczego jest ważny

Kiedy wpisujesz `python` w terminalu, system operacyjny szuka programu `python.exe` w folderach zapisanych w zmiennej środowiskowej **PATH**. Jeśli Pythona nie ma w PATH, terminal powie: `'python' is not recognized`.

### Jak sprawdzić PATH:

```bash
# Windows (PowerShell):
$env:Path -split ";"

# Szukaj czegoś takiego:
# C:\Users\TwojeImie\AppData\Local\Programs\Python\Python312\
# C:\Users\TwojeImie\AppData\Local\Programs\Python\Python312\Scripts\
```

### Jak naprawić brak Pythona w PATH:

**Opcja 1:** Zainstaluj Pythona ponownie i **zaznacz "Add Python to PATH"**.

**Opcja 2:** Dodaj ręcznie:
1. `Win + R` → wpisz `sysdm.cpl` → Enter
2. Zakładka **"Zaawansowane"** → **"Zmienne środowiskowe"**
3. W zmiennej `Path` dodaj ścieżkę do Pythona (np. `C:\Users\TwojeImie\AppData\Local\Programs\Python\Python312\`)

### Dwie drogi do tego samego celu: python.org vs Miniconda

Na zajęciach wspominałem o Minicondzie i to jest w pełni działająca opcja. Poniżej porównanie obu podejść — **oba są prawidłowe**, wybierz to, które lepiej Ci pasuje. Jeśli już masz coś zainstalowane i działa — nie zmieniaj.

| | **Python z python.org + venv** | **Miniconda + conda** |
|---|---|---|
| **Instalacja** | Lżejsza (~30 MB) | Nieco większa (~80 MB), ale wciąż lekka |
| **Tworzenie środowisk** | `python -m venv .venv` | `conda create -n nazwa python=3.12` |
| **Aktywacja** | `.venv\Scripts\activate` | `conda activate nazwa` |
| **Instalacja pakietów** | `pip install` | `pip install` lub `conda install` |
| **Kiedy wybrać?** | Jeśli wolisz prostotę i minimalizm | Jeśli już masz Minicondę lub wolisz `conda` |
| **W produkcji** | Standard w web development | Standard w data science / ML |

> **Ważne:** W ramach naszych zajęć nie ma znaczenia, którą ścieżkę wybierzesz. Pakiety instalujemy przez `pip` w obu przypadkach, a kernel Jupyter działa identycznie.

### Miniconda — pełna instrukcja instalacji i konfiguracji

**Co to jest Miniconda?**

Miniconda to lekka wersja Anacondy. Daje Ci Pythona + menedżer pakietów `conda`, bez setek preinstalowanych bibliotek (to odróżnia ją od pełnej Anacondy, która waży ~3 GB). Conda potrafi zarządzać nie tylko pakietami Pythona, ale też bibliotekami systemowymi (np. CUDA do GPU), co jest przydatne w machine learning.

**Instalacja (Windows):**

1. Pobierz instalator: [docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda/)
2. Uruchom instalator
3. ⚠️ Zaznacz **"Add Miniconda3 to my PATH environment variable"**
   - Instalator ostrzega, że to "not recommended" — w naszym przypadku to nie problem
4. Zainstaluj dla "Just Me" (nie wymaga uprawnień admina)

**Weryfikacja:**
```bash
conda --version       # np. conda 24.7.1
python --version      # np. Python 3.12.4
```

**Tworzenie środowiska dla naszego kursu:**
```bash
# Stwórz środowisko z Pythonem 3.12
conda create -n architektura python=3.12 -y

# Aktywuj
conda activate architektura

# Teraz (architektura) jest widoczne w terminalu
# Instaluj pakiety przez pip (jak zwykle):
pip install ipykernel jupyter requests matplotlib

# Zarejestruj kernel:
python -m ipykernel install --user --name=architektura-python --display-name="Python (Architektura)"
```

**Przydatne komendy conda:**
```bash
# Lista Twoich środowisk:
conda env list

# Aktywacja / dezaktywacja:
conda activate architektura
conda deactivate

# Usunięcie środowiska:
conda env remove -n architektura

# Eksport środowiska (odpowiednik requirements.txt):
conda env export > environment.yml

# Odtworzenie środowiska z pliku:
conda env create -f environment.yml
```

**Conda + VS Code:**
1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Powinno pokazać: `Python 3.12.x ('architektura': conda)`
3. Wybierz to — VS Code automatycznie aktywuje środowisko conda w terminalu

### Jeśli masz problemy z Minicondą na komputerach uczelnianych

Na komputerach uczelnianych mogą być ograniczone uprawnienia. Jeśli `conda` nie działa:
1. Spróbuj ścieżki z python.org + venv (nie wymaga uprawnień admina)
2. Lub użyj **Anaconda Prompt** zamiast PowerShell (instalacja Minicondy dodaje go do menu Start)
3. Jeśli PATH nie działa, uruchom conda przez pełną ścieżkę: `C:\Users\TwojeImie\miniconda3\Scripts\conda.exe`


---

## 3. Wirtualne środowiska — co to i po co

### Problem bez wirtualnych środowisk

```
Projekt A wymaga: requests==2.28.0
Projekt B wymaga: requests==2.31.0
                    ↓
           KONFLIKT! 💥
```

Bez wirtualnych środowisk, wszystkie pakiety instalują się globalnie — w jednym miejscu. Jak dwa projekty potrzebują różnych wersji tego samego pakietu, masz problem.

### Rozwiązanie: wirtualne środowisko

Wirtualne środowisko to **izolowana kopia Pythona** w folderze Twojego projektu. Ma własne pakiety, własny `pip`, i nie koliduje z niczym innym.

```
moj-projekt/
├── .venv/                    ← wirtualne środowisko (NIE ruszaj ręcznie!)
│   ├── Scripts/              ← (Windows) aktywacja + python.exe
│   │   ├── activate.bat
│   │   ├── Activate.ps1
│   │   └── python.exe        ← LOKALNA kopia Pythona
│   ├── bin/                   ← (Mac/Linux) aktywacja + python
│   └── Lib/site-packages/     ← tu lądują zainstalowane pakiety
├── notebook_01.ipynb
├── skrypt.py
└── requirements.txt          ← lista zależności projektu
```

### Komendy — ściągawka

**Ścieżka A: venv (python.org)**
```bash
# TWORZENIE
python -m venv .venv

# AKTYWACJA
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# Mac/Linux:
source .venv/bin/activate

# Po aktywacji widzisz (.venv) na początku linii terminala:
# (.venv) PS C:\Users\Jan\moj-projekt>

# INSTALOWANIE PAKIETÓW (w aktywnym środowisku)
pip install requests
pip install ipykernel jupyter

# ZAPISYWANIE ZALEŻNOŚCI
pip freeze > requirements.txt

# ODTWARZANIE ZALEŻNOŚCI (np. na innym komputerze)
pip install -r requirements.txt

# DEZAKTYWACJA
deactivate
```

**Ścieżka B: conda (Miniconda)**
```bash
# TWORZENIE
conda create -n architektura python=3.12 -y

# AKTYWACJA
conda activate architektura

# Po aktywacji widzisz (architektura) na początku linii terminala:
# (architektura) PS C:\Users\Jan\moj-projekt>

# INSTALOWANIE PAKIETÓW (w aktywnym środowisku)
pip install requests
pip install ipykernel jupyter
# lub: conda install requests (obie opcje działają)

# ZAPISYWANIE ZALEŻNOŚCI
pip freeze > requirements.txt
# lub: conda env export > environment.yml

# ODTWARZANIE ZALEŻNOŚCI
pip install -r requirements.txt
# lub: conda env create -f environment.yml

# DEZAKTYWACJA
conda deactivate

# LISTA ŚRODOWISK
conda env list
```

### Częsty problem na Windowsie: "Scripts cannot be loaded"

Jeśli PowerShell blokuje aktywację z komunikatem o polityce wykonywania skryptów:

```powershell
# Uruchom PowerShell jako Administrator i wpisz:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Albo użyj CMD zamiast PowerShell:
```cmd
.venv\Scripts\activate.bat
```

---

## 4. pip — menedżer pakietów

`pip` to narzędzie do instalowania bibliotek (pakietów) Pythona. Pakiety pobierane są z **PyPI** (Python Package Index) — [pypi.org](https://pypi.org).

### Najważniejsze komendy

```bash
# Instalacja pakietu
pip install requests

# Instalacja konkretnej wersji
pip install requests==2.31.0

# Aktualizacja pakietu
pip install --upgrade requests

# Lista zainstalowanych pakietów
pip list

# Szczegóły pakietu
pip show requests

# Odinstalowanie
pip uninstall requests

# Zapisanie wszystkich pakietów do pliku
pip freeze > requirements.txt

# Instalacja z pliku
pip install -r requirements.txt
```

### Co to jest `requirements.txt`?

To plik tekstowy z listą pakietów i ich wersji. Pozwala odtworzyć identyczne środowisko na innym komputerze:

```
# requirements.txt
requests==2.31.0
ipykernel==6.29.0
jupyter==1.0.0
matplotlib==3.8.0
```

---

## 5. Jupyter Notebook w VS Code — konfiguracja krok po kroku

### Co to jest "kernel"?

Kernel to **silnik wykonawczy** stojący za notebookiem. Kiedy naciskasz `Shift+Enter` w komórce, kod jest wysyłany do kernela, kernel go wykonuje i zwraca wynik.

```
┌────────────────┐         ┌────────────────┐
│   VS Code      │◀───────▶│    Kernel      │
│   (interfejs)  │ JSON    │  (python.exe   │
│                │ messages│   z Twojego    │
│   Komórka 1    │         │   .venv)       │
│   Komórka 2    │         │                │
│   Komórka 3    │         │   Pamięta      │
│                │         │   zmienne!     │
└────────────────┘         └────────────────┘
```

Kernel **pamięta stan** między komórkami — zmienne utworzone w komórce 1 są dostępne w komórce 2. Dlatego kolejność uruchamiania komórek ma znaczenie!

### Instalacja kernela z wirtualnego środowiska

```bash
# 1. Upewnij się, że środowisko jest aktywne:
# (.venv) powinno być widoczne w terminalu

# 2. Zainstaluj ipykernel:
pip install ipykernel

# 3. Zarejestruj kernel:
python -m ipykernel install --user --name=architektura-python --display-name="Python (Architektura)"

# Parametry:
# --user         → instaluje dla bieżącego użytkownika
# --name=...     → wewnętrzna nazwa (bez spacji)
# --display-name → nazwa wyświetlana w VS Code
```

### Wybieranie kernela w VS Code

1. Otwórz plik `.ipynb`
2. W **prawym górnym rogu** kliknij przycisk z nazwą kernela (lub "Select Kernel")
3. Wybierz **"Python Environments..."** lub **"Jupyter Kernel..."**
4. Znajdź **"Python (Architektura)"**

Jeśli nie widzisz swojego kernela:
- `Ctrl+Shift+P` → "Python: Select Interpreter" → wybierz `.venv`
- `Ctrl+Shift+P` → "Developer: Reload Window"

### Zarządzanie kernelami

```bash
# Lista zainstalowanych kerneli:
jupyter kernelspec list

# Usunięcie kernela:
jupyter kernelspec uninstall architektura-python
```

---

## 6. Pliki `.py` vs Jupyter Notebooks — kiedy co?

### Pliki `.py` — uruchamianie

```bash
# Najprostszy sposób:
python skrypt.py

# Z argumentami:
python skrypt.py --input dane.csv --output wyniki.txt

# Interaktywny tryb Pythona (REPL):
python
>>> 2 + 2
4
>>> exit()
```

### W VS Code:

- Otwórz plik `.py`
- Kliknij ▶️ (Run Python File) w prawym górnym rogu
- Lub: zaznacz fragment kodu → `Shift+Enter` (uruchomi zaznaczenie w terminalu)

### Konwersja między formatami

```bash
# Notebook → skrypt Python:
jupyter nbconvert --to script notebook.ipynb

# Lub w VS Code: Ctrl+Shift+P → "Jupyter: Export to Python Script"
```

### Kiedy co używać?

**Jupyter Notebook (`.ipynb`):**
- Nauka i eksperymentowanie
- Analiza danych krok po kroku
- Materiały z zajęć
- Prototypowanie

**Plik Python (`.py`):**
- Gotowe skrypty i aplikacje
- Moduły i biblioteki
- Projekt zaliczeniowy
- Wszystko, co ma być uruchamiane automatycznie

---

## 7. GitHub Copilot — Twój asystent AI

### Co to jest?

GitHub Copilot to **asystent AI** wbudowany w VS Code, który podpowiada kod w czasie rzeczywistym. Działa jak bardzo inteligentne autouzupełnianie — analizuje kontekst Twojego kodu i sugeruje kolejne linie.

### Jak działa?

```
Ty piszesz:          │  Copilot sugeruje (szary tekst):
                      │
def oblicz_srednia(   │  def oblicz_srednia(lista):
                      │      return sum(lista) / len(lista)
```

Naciskasz `Tab` żeby zaakceptować sugestię, `Esc` żeby odrzucić.

### Darmowy dostęp dla studentów

1. Załóż konto na [github.com](https://github.com)
2. Wejdź na [education.github.com/pack](https://education.github.com/pack)
3. Kliknij **"Get Student Benefits"** → zweryfikuj się mailem uczelni
4. Po weryfikacji: [github.com/settings/copilot](https://github.com/settings/copilot) → aktywuj
5. W VS Code zainstaluj rozszerzenie **GitHub Copilot** i zaloguj się

**Plan Free (bez weryfikacji studenckiej):** 2000 uzupełnień kodu + 50 wiadomości chat / miesiąc — wystarczy na start.

**Plan Pro (ze studencką weryfikacją):** Bez limitów — warto się zweryfikować!

### Jak korzystać?

- **Podpowiedzi inline:** Po prostu pisz kod — Copilot automatycznie sugeruje. `Tab` = akceptuj.
- **Chat:** `Ctrl+Alt+I` otwiera czat. Możesz pytać o kod, prosić o wyjaśnienia, debug.
- **Inline Chat:** `Ctrl+I` w kodzie — opisz co chcesz zmienić, Copilot zmodyfikuje.

### ⚠️ Ważne zastrzeżenie

Copilot to **narzędzie, nie wyrocznia**. Kod, który sugeruje:
- Może zawierać błędy
- Może nie być optymalny
- Wymaga Twojego zrozumienia — **musisz wiedzieć, co akceptujesz**

Traktuj go jak kolega, który podpowiada — ale Ty jesteś odpowiedzialny za kod.

---

## 8. Google Antigravity — alternatywne IDE (polecane!)

### Dlaczego o tym mówię?

Na zajęciach poleciłem Wam **Google Antigravity** jako IDE i podtrzymuję tę rekomendację. To nowe, **w pełni darmowe** środowisko od Google, które zostało zaprojektowane z myślą o pracy z AI od samego początku. Dla osób, które dopiero wchodzą w programowanie, ma jedną ogromną przewagę: **AI nie jest dodatkiem, tylko centralnym elementem** — zamiast instalować osobno Copilota, tu agent jest wbudowany w samo środowisko.

### Co to jest?

Antigravity to IDE bazujące na VS Code (więc wygląda i działa znajomo), ale z kilkoma kluczowymi różnicami:

- **Agent Manager** — zamiast tylko podpowiedzi inline (jak Copilot), masz panel do zarządzania agentami AI, które mogą planować, pisać kod, testować i debugować autonomicznie
- **Gemini 3 Pro** — wbudowany model Google'a, bez dodatkowych kluczy API, bez płacenia
- **Tryb Planning vs Fast** — możesz poprosić agenta, żeby najpierw zaplanował implementację, albo od razu działał
- **Wbudowana przeglądarka** — agent może testować Twoje aplikacje webowe bezpośrednio w IDE
- **Artefakty** — agent dokumentuje swoją pracę (plany, listy zadań, zrzuty ekranu), więc widzisz co i dlaczego zrobił

### Jak zainstalować?

1. Wejdź na [antigravity.google](https://idx.google.com/antigravity) lub wyszukaj "Google Antigravity IDE download"
2. Pobierz wersję na swój system (Windows / Mac / Linux)
3. Zaloguj się kontem Google (osobistym, np. Gmail)
4. Gotowe — Antigravity jest **darmowe** w fazie Public Preview

### Jak to się ma do VS Code + Copilot?

| | **VS Code + Copilot** | **Google Antigravity** |
|---|---|---|
| **Koszt** | VS Code darmowy, Copilot Free ograniczony (Pro za darmo dla studentów) | W pełni darmowe |
| **AI** | Podpowiedzi inline + chat | Pełni agenci (planowanie + wykonanie + weryfikacja) |
| **Model** | GPT-4o, Claude (przez Copilot) | Gemini 3 Pro (wbudowany) |
| **Jupyter Notebooks** | Pełne wsparcie | Tak (bazuje na VS Code) |
| **Rozszerzenia VS Code** | Pełna kompatybilność | Kompatybilne (fork VS Code) |
| **Stabilność** | Sprawdzony, dojrzały | Preview — może mieć bugi |

### Kiedy co wybrać?

- **Antigravity** — jeśli chcesz mieć AI agenta "za darmo" bez konfiguracji, lubisz eksperymentować z nowymi narzędziami i nie przeszkadza Ci, że to wciąż Preview
- **VS Code + Copilot** — jeśli wolisz sprawdzone rozwiązanie, potrzebujesz pełnej stabilności, lub Twoja uczelnia/praca wymaga VS Code

> **Na nasze zajęcia:** Oba środowiska obsługują Jupyter Notebooks i Pythona w identyczny sposób. Kernele, wirtualne środowiska, pip — wszystko działa tak samo. Wybierz to, w czym Ci wygodniej. Jeśli zaczynałeś/-aś z Antigravity na zajęciach — nie musisz się przesiadać.

---

## 9. Troubleshooting — najczęstsze problemy

### ❌ `'python' is not recognized as an internal or external command`

**Przyczyna:** Python nie jest w PATH.

**Rozwiązanie:**
1. Zainstaluj Pythona ponownie z zaznaczonym "Add Python to PATH"
2. Lub użyj pełnej ścieżki: `C:\Users\TwojeImie\AppData\Local\Programs\Python\Python312\python.exe`
3. Na Windowsie spróbuj też: `py` zamiast `python` (Python Launcher)

### ❌ `Nie mogę aktywować środowiska (PowerShell)`

**Rozwiązanie:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ `pip install` — "Permission denied"

**Rozwiązanie:** Upewnij się, że środowisko wirtualne jest aktywne (widzisz `(.venv)` w terminalu). Nigdy nie używaj `sudo pip install` ani `pip install` bez aktywnego venv.

### ❌ `No kernel found` / kernel nie działa w VS Code

**Rozwiązanie:**
1. Sprawdź, czy `ipykernel` jest zainstalowany: `pip list | findstr ipykernel`
2. Zarejestruj kernel ponownie: `python -m ipykernel install --user --name=architektura-python`
3. Przeładuj VS Code: `Ctrl+Shift+P` → "Developer: Reload Window"

### ❌ Notebook uruchamia się z "globalnym" Pythonem zamiast venv/conda

**Rozwiązanie:**
1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Wybierz interpreter z `.venv/Scripts/python.exe` (venv) lub `Python 3.12.x ('architektura': conda)` (conda)
3. W notebooku: kliknij "Select Kernel" → wybierz właściwy kernel

### ❌ `conda activate` nie działa w PowerShell

**Przyczyna:** Conda wymaga inicjalizacji shella.

**Rozwiązanie:**
```bash
# Uruchom raz:
conda init powershell
# Zamknij i otwórz ponownie terminal
```
Alternatywnie: użyj **Anaconda Prompt** z menu Start zamiast PowerShell.

### ❌ `ModuleNotFoundError: No module named 'requests'`

**Przyczyna:** Pakiet jest zainstalowany w innym środowisku niż to, które używa kernel.

**Rozwiązanie:**
1. Aktywuj właściwe środowisko
2. `pip install requests`
3. Sprawdź kernel w notebooku — musi wskazywać na to samo środowisko

---

## 10. Polecane materiały wideo

| Temat | Materiał | Link |
|-------|----------|------|
| Instalacja Pythona | Corey Schafer — Install and Setup | [youtu.be/YYXdXT2l-Gg](https://youtu.be/YYXdXT2l-Gg) |
| VS Code + Python | Corey Schafer — VS Code Python Setup | [youtu.be/-nh9rCzPJ20](https://youtu.be/-nh9rCzPJ20) |
| Wirtualne środowiska | Corey Schafer — venv (Windows) | [youtu.be/Kg1Yvry_Ydk](https://youtu.be/Kg1Yvry_Ydk) |
| Jupyter w VS Code | VS Code oficjalny tutorial | [youtu.be/DA6ZAHBPF1U](https://youtu.be/DA6ZAHBPF1U) |
| GitHub Copilot | VS Code — Getting Started | [youtu.be/Fi3AJZZregI](https://youtu.be/Fi3AJZZregI) |
| Google Antigravity | Google Codelabs — Getting Started | [codelabs.developers.google.com/getting-started-google-antigravity](https://codelabs.developers.google.com/getting-started-google-antigravity) |

### Dokumentacja oficjalna

- **Python:** [docs.python.org/pl/3/](https://docs.python.org/pl/3/) (po polsku!)
- **pip:** [pip.pypa.io](https://pip.pypa.io/en/stable/)
- **venv:** [docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
- **Miniconda:** [docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda/)
- **conda cheat sheet:** [docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- **VS Code + Jupyter:** [code.visualstudio.com/docs/datascience/jupyter-notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- **VS Code + Kernele:** [code.visualstudio.com/docs/datascience/jupyter-kernel-management](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
- **GitHub Copilot:** [code.visualstudio.com/docs/copilot/overview](https://code.visualstudio.com/docs/copilot/overview)
- **Google Antigravity:** [codelabs.developers.google.com/getting-started-google-antigravity](https://codelabs.developers.google.com/getting-started-google-antigravity)
- **GitHub Student Pack:** [education.github.com/pack](https://education.github.com/pack)

---

## 11. Podsumowanie — mapa mentalna

```
                    ┌─────────────────────────────────────────┐
                    │         TWOJE ŚRODOWISKO PRACY          │
                    └────────────────────┬────────────────────┘
                                         │
          ┌──────────────────────────────┼──────────────────────────────┐
          │                              │                              │
    ┌─────▼──────┐              ┌───────▼────────┐              ┌─────▼──────┐
    │   Python   │              │    Edytor      │              │ Asystent AI│
    │(interpreter│              │                │              │            │
    │  + pip)    │              │  VS Code       │              │ Copilot    │
    └─────┬──────┘              │    lub         │              │ lub Gemini │
          │                     │  Antigravity   │              │(wbudowany) │
    ┌─────┼──────┐              └───────┬────────┘              └────────────┘
    │            │                      │
┌───▼───┐  ┌────▼────┐          ┌──────▼──────┐
│ venv  │  │  conda  │          │ Rozszerzenia│
│(A)    │  │  (B)    │          │  - Python   │
└───┬───┘  └────┬────┘          │  - Jupyter  │
    │           │               └─────────────┘
    └─────┬─────┘
          │
   ┌──────┼──────────┐
   │                  │
┌──▼───────┐   ┌─────▼──────┐
│pip install│   │  ipykernel │
│ requests │   │  (kernel   │
│ matplotlib│   │   Jupyter) │
│ ...      │   └────────────┘
└──────────┘
```

Każdy element ma swoje miejsce:
- **Python** — silnik, który wykonuje kod
- **venv lub conda env** — izolowane środowisko z pakietami dla Twojego projektu (obie opcje dają ten sam efekt)
- **pip** — instalator pakietów (działa wewnątrz venv i wewnątrz conda env)
- **ipykernel** — most między Twoim środowiskiem a Jupyter Notebooks
- **VS Code lub Antigravity** — edytor, w którym piszesz kod i uruchamiasz notebooki (Antigravity = VS Code + wbudowany agent AI)
- **Copilot / Gemini** — AI, które pomaga pisać kod szybciej (Copilot w VS Code, Gemini w Antigravity)

---

> **Pytania?** Pisz na Teams. Nie ma głupich pytań — konfiguracja środowiska to rzecz, z którą borykają się nawet doświadczeni programiści. 🙂
