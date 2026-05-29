# 🐍 Motivational Python Pack

### Architektura aplikacji w Pythonie — materiały wyrównawcze

> **Cel:** Jeśli czujesz, że pierwsze zajęcia były za szybkie — ten dokument jest dla Ciebie. Masz **2 tygodnie** do następnych laboratoriów. Nie musisz robić wszystkiego. Wybierz to, co Ci brakuje, i skup się na tym. Każdy podrozdział ma **konkretny materiał do obejrzenia** i **zadanie do zrobienia**. Jeśli zrealizujesz choćby połowę, będziesz na następnych zajęciach w znacznie lepszej pozycji.

> **Ważne:** Nie musisz umieć wszystkiego na pamięć. Musisz **rozumieć koncepty** i **umieć napisać prosty kod** korzystając z dokumentacji. W pracy programisty nikt nie pisze kodu z pamięci — ale trzeba wiedzieć, czego szukać.

---

## Spis treści

1. [Środowisko pracy](#1-środowisko-pracy)
2. [Tydzień 1: Fundamenty Pythona](#tydzień-1-fundamenty-pythona)
   - [Zmienne, typy danych, stringi](#21-zmienne-typy-danych-stringi)
   - [Listy, słowniki, krotki, zbiory](#22-listy-słowniki-krotki-zbiory)
   - [Pętle i warunki](#23-pętle-i-warunki)
   - [Funkcje](#24-funkcje)
   - [Praca z plikami](#25-praca-z-plikami)
   - [Projekt tygodnia 1](#projekt-tygodnia-1-menedżer-kontaktów)
3. [Tydzień 2: OOP i świat zewnętrzny](#tydzień-2-oop-i-świat-zewnętrzny)
   - [Klasy i obiekty](#31-klasy-i-obiekty)
   - [Moduły i pakiety (pip, venv)](#32-moduły-i-pakiety-pip-venv)
   - [Praca z JSON i API](#33-praca-z-json-i-api)
   - [Integracja z LLM (bonus motywacyjny!)](#34-integracja-z-llm-bonus-motywacyjny)
   - [Projekt tygodnia 2](#projekt-tygodnia-2-asystent-ai-w-terminalu)
4. [Ściągawka: czego potrzebujesz na następne zajęcia](#4-ściągawka-czego-potrzebujesz-na-następne-zajęcia)
5. [Polecane zasoby — pełna lista](#5-polecane-zasoby--pełna-lista)

---

## 1. Środowisko pracy

Zanim zaczniesz cokolwiek pisać, upewnij się, że masz działające środowisko.

### Co potrzebujesz:
- **Python 3.11+** — [python.org/downloads](https://www.python.org/downloads/)
- **VS Code** — [code.visualstudio.com](https://code.visualstudio.com/) + rozszerzenie **Python** od Microsoft
- **Terminal / PowerShell** — będziesz go używać regularnie
- **Git** (opcjonalnie, ale warto) — [git-scm.com](https://git-scm.com/)

### Weryfikacja instalacji:
```bash
python --version    # powinno wyświetlić Python 3.11.x lub wyżej
pip --version       # menedżer pakietów
```

### 📺 Materiał wideo:
- **Corey Schafer** — *Python Tutorial for Beginners 1: Install and Setup for Mac and Windows*
  - [youtu.be/YYXdXT2l-Gg](https://youtu.be/YYXdXT2l-Gg) (~15 min)

---

## Tydzień 1: Fundamenty Pythona

**Cel tygodnia:** Opanować podstawowe konstrukcje języka tak, żebyś mógł/mogła samodzielnie napisać prosty program od zera.

---

### 2.1 Zmienne, typy danych, stringi

**Co musisz wiedzieć:**
- Tworzenie zmiennych, typy: `int`, `float`, `str`, `bool`
- Operacje na stringach: slicing, f-stringi, metody `.upper()`, `.lower()`, `.split()`, `.replace()`, `.strip()`
- Konwersja typów: `int()`, `str()`, `float()`

**📺 Materiały wideo:**
- Corey Schafer — *Strings - Working with Textual Data* — [youtu.be/k9TUPpGqYTo](https://youtu.be/k9TUPpGqYTo) (~21 min)
- Corey Schafer — *Integers and Floats - Working with Numeric Data* — [youtu.be/khKv-8q7YmY](https://youtu.be/khKv-8q7YmY) (~12 min)

**📝 Zadanie:**
```
Napisz program, który:
1. Pyta użytkownika o imię i nazwisko (input())
2. Wyświetla inicjały wielkimi literami (np. "Jan Kowalski" → "J.K.")
3. Wyświetla imię od tyłu (np. "Jan" → "naJ")
4. Informuje, ile liter ma pełne imię i nazwisko (bez spacji)
```

---

### 2.2 Listy, słowniki, krotki, zbiory

**Co musisz wiedzieć:**
- Listy: tworzenie, dodawanie (`append`, `extend`), usuwanie, slicing, iterowanie
- Słowniki: pary klucz-wartość, `.get()`, `.items()`, `.keys()`, `.values()`
- Krotki: kiedy używać zamiast listy
- Zbiory (`set`): unikalne elementy, operacje zbiorowe
- **List comprehensions** — to kluczowe na dalszych zajęciach!

**📺 Materiały wideo:**
- Corey Schafer — *Lists, Tuples, and Sets* — [youtu.be/W8KRzm-HUcc](https://youtu.be/W8KRzm-HUcc) (~29 min)
- Corey Schafer — *Dictionaries* — [youtu.be/daefaLgNkw0](https://youtu.be/daefaLgNkw0) (~18 min)
- Corey Schafer — *Comprehensions* — [youtu.be/3dt4OGnU5sM](https://youtu.be/3dt4OGnU5sM) (~18 min)

**📝 Zadanie:**
```
Masz listę zakupów jako listę słowników:

zakupy = [
    {"nazwa": "mleko", "cena": 4.50, "ilość": 2},
    {"nazwa": "chleb", "cena": 5.00, "ilość": 1},
    {"nazwa": "masło", "cena": 7.99, "ilość": 1},
    {"nazwa": "jajka", "cena": 12.50, "ilość": 1},
    {"nazwa": "mleko", "cena": 4.50, "ilość": 3},
]

Napisz program, który:
1. Oblicza łączny koszt zakupów (cena × ilość dla każdego produktu)
2. Znajduje najdroższy produkt
3. Tworzy listę unikalnych nazw produktów (hint: set)
4. Za pomocą list comprehension tworzy listę produktów droższych niż 5 zł
```

---

### 2.3 Pętle i warunki

**Co musisz wiedzieć:**
- `if` / `elif` / `else`
- Pętla `for` — iterowanie po listach, słownikach, range()
- Pętla `while` — kiedy używać
- `break`, `continue`
- `enumerate()`, `zip()`

**📺 Materiały wideo:**
- Corey Schafer — *Conditionals and Booleans* — [youtu.be/DZwmZ8Usvnk](https://youtu.be/DZwmZ8Usvnk) (~16 min)
- Corey Schafer — *Loops and Iterations* — [youtu.be/6iF8Xb7Z3wQ](https://youtu.be/6iF8Xb7Z3wQ) (~11 min)

**📝 Zadanie:**
```
Napisz prostą grę "Zgadnij liczbę":
1. Program losuje liczbę od 1 do 100 (import random; random.randint(1, 100))
2. Użytkownik zgaduje — program mówi "za dużo" / "za mało"
3. Po odgadnięciu wyświetla liczbę prób
4. Pyta, czy grać ponownie (while loop)
```

---

### 2.4 Funkcje

**Co musisz wiedzieć:**
- Definiowanie funkcji: `def`, parametry, `return`
- Argumenty domyślne
- `*args`, `**kwargs` — na razie wiedzieć, że istnieją i co robią
- Funkcje jako obiekty (można je przypisać do zmiennej, przekazać jako argument)
- Docstringi

**📺 Materiały wideo:**
- Corey Schafer — *Functions* — [youtu.be/9Os0o3wzS_I](https://youtu.be/9Os0o3wzS_I) (~21 min)
- Corey Schafer — *First-Class Functions* — [youtu.be/kr0mpwqttM0](https://youtu.be/kr0mpwqttM0) (~18 min) ⚠️ *ten materiał jest ważny pod dekoratory!*

**📝 Zadanie:**
```
Napisz moduł z funkcjami do analizy tekstu:

def policz_slowa(tekst):
    """Zwraca liczbę słów w tekście."""

def najdluzsze_slowo(tekst):
    """Zwraca najdłuższe słowo w tekście."""

def czestotliwosc_slow(tekst):
    """Zwraca słownik {słowo: liczba_wystąpień}."""

def cenzura(tekst, zakazane_slowa):
    """Zamienia zakazane słowa na '***'."""

Przetestuj swoje funkcje na dowolnym tekście (np. skopiowanym artykule z Wikipedii).
```

---

### 2.5 Praca z plikami

**Co musisz wiedzieć:**
- `open()`, `with open()` — tryby `"r"`, `"w"`, `"a"`
- `.read()`, `.readlines()`, `.write()`
- Czytanie i zapisywanie CSV (moduł `csv`)

**📺 Materiały wideo:**
- Corey Schafer — *File Objects - Reading and Writing to Files* — [youtu.be/Uh2ebFW8OYM](https://youtu.be/Uh2ebFW8OYM) (~24 min)
- Corey Schafer — *CSV Module* — [youtu.be/q5uM4VKywbA](https://youtu.be/q5uM4VKywbA) (~16 min)

**📝 Zadanie:**
```
1. Utwórz plik "studenci.csv" z kolumnami: imię, nazwisko, ocena
2. Napisz program, który:
   - Czyta plik CSV
   - Oblicza średnią ocen
   - Znajduje studenta z najwyższą oceną
   - Zapisuje wyniki do nowego pliku "raport.txt"
```

---

### 🏗️ Projekt tygodnia 1: Menedżer kontaktów

**Cel:** Połączyć wszystkie umiejętności z tygodnia 1 w jeden działający program.

```
Napisz program "Menedżer kontaktów" działający w terminalu:

Menu:
  1. Dodaj kontakt (imię, nazwisko, telefon, email)
  2. Wyświetl wszystkie kontakty
  3. Wyszukaj kontakt (po imieniu lub nazwisku)
  4. Usuń kontakt
  5. Zapisz kontakty do pliku (CSV)
  6. Wczytaj kontakty z pliku (CSV)
  7. Wyjdź

Wymagania:
- Kontakty przechowywane jako lista słowników
- Walidacja: sprawdź, czy email zawiera "@", telefon składa się z cyfr
- Użyj funkcji — każda opcja menu to osobna funkcja
- Program działa w pętli while, aż użytkownik wybierze "Wyjdź"
```

**Czas realizacji:** 2-4 godziny. To jest solidna baza, która pokrywa: listy, słowniki, pętle, warunki, funkcje, pliki.

---

## Tydzień 2: OOP i świat zewnętrzny

**Cel tygodnia:** Zrozumieć klasy i obiekty, zainstalować zewnętrzne pakiety, połączyć się z API — i zbudować coś, co realnie działa.

---

### 3.1 Klasy i obiekty

**Dlaczego to ważne:** Dekoratory, deskryptory, generatory — wszystko to bazuje na obiektowym modelu Pythona. Bez zrozumienia klas, reszta kursu będzie niezrozumiała.

**Co musisz wiedzieć:**
- Klasa vs instancja (obiekt)
- `__init__` — konstruktor
- Atrybuty instancji vs atrybuty klasy
- Metody: zwykłe, `@classmethod`, `@staticmethod`
- Dziedziczenie — tworzenie podklas
- Metody specjalne (dunder): `__str__`, `__repr__`, `__eq__`, `__len__`

**📺 Materiały wideo (OBOWIĄZKOWE — ta seria jest złotem):**
- Corey Schafer — **Python OOP Tutorial** (6 filmów, ~1.5h łącznie):
  1. *Classes and Instances* — [youtu.be/ZDa-Z5JzLYM](https://youtu.be/ZDa-Z5JzLYM)
  2. *Class Variables* — [youtu.be/BJ-VvGyQxho](https://youtu.be/BJ-VvGyQxho)
  3. *classmethods and staticmethods* — [youtu.be/rq8cL2XMM5M](https://youtu.be/rq8cL2XMM5M)
  4. *Inheritance* — [youtu.be/RSl87lqOXDE](https://youtu.be/RSl87lqOXDE)
  5. *Special (Magic/Dunder) Methods* — [youtu.be/3ohzBxoFHAY](https://youtu.be/3ohzBxoFHAY)
  6. *Property Decorators* — [youtu.be/jCzT9XFZ5bw](https://youtu.be/jCzT9XFZ5bw)

**📝 Zadanie:**
```
Napisz system biblioteczny:

class Ksiazka:
    def __init__(self, tytul, autor, rok, isbn):
        ...
    def __str__(self):
        """Zwraca ładny opis książki"""
    def __repr__(self):
        """Zwraca techniczny opis"""
    def __eq__(self, other):
        """Dwie książki są równe, jeśli mają ten sam ISBN"""

class Biblioteka:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.ksiazki = []
    def dodaj(self, ksiazka): ...
    def usun(self, isbn): ...
    def szukaj(self, fraza): ...          # szuka w tytule i autorze
    def __len__(self):
        """Zwraca liczbę książek"""
    def __str__(self):
        """Wyświetla podsumowanie biblioteki"""

# Test:
bib = Biblioteka("Moja Biblioteka")
bib.dodaj(Ksiazka("Władca Pierścieni", "Tolkien", 1954, "978-0-123"))
bib.dodaj(Ksiazka("Hobbit", "Tolkien", 1937, "978-0-456"))
print(len(bib))          # 2
print(bib.szukaj("Tolkien"))  # lista obu książek
```

---

### 3.2 Moduły i pakiety (pip, venv)

**Co musisz wiedzieć:**
- `import`, `from ... import ...`
- Tworzenie własnych modułów (plik `.py` = moduł)
- `pip install` — instalacja pakietów
- `python -m venv` — wirtualne środowisko (bardzo ważne!)
- `requirements.txt` — lista zależności

**📺 Materiały wideo:**
- Corey Schafer — *Import Modules and Exploring The Standard Library* — [youtu.be/CqvZ3vGoGs0](https://youtu.be/CqvZ3vGoGs0) (~22 min)
- Corey Schafer — *VENV* — [youtu.be/Kg1Yvry_Ydk](https://youtu.be/Kg1Yvry_Ydk) (Windows, ~8 min)

**📝 Zadanie:**
```
1. Utwórz wirtualne środowisko:
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows

2. Zainstaluj pakiet:
   pip install requests

3. Sprawdź, że działa:
   python -c "import requests; print(requests.__version__)"

4. Zapisz zależności:
   pip freeze > requirements.txt
```

---

### 3.3 Praca z JSON i API

**Co musisz wiedzieć:**
- Format JSON — jak wygląda, czym się różni od słownika Pythona
- `json.loads()`, `json.dumps()` — serializacja
- Biblioteka `requests` — `requests.get()`, `requests.post()`
- Kody statusu HTTP: 200, 404, 500
- Parsowanie odpowiedzi JSON z API

**📺 Materiały wideo:**
- Corey Schafer — *Requests: HTTP for Humans* — [youtu.be/tb8gHvYlCFs](https://youtu.be/tb8gHvYlCFs) (~25 min)

**📝 Zadanie:**
```
Napisz program "Pogodynka":

1. Zarejestruj się na https://openweathermap.org/api (darmowy plan)
2. Napisz funkcję:

   def pobierz_pogode(miasto, api_key):
       """Pobiera aktualną pogodę dla podanego miasta."""
       url = f"https://api.openweathermap.org/data/2.5/weather?q={miasto}&appid={api_key}&units=metric&lang=pl"
       response = requests.get(url)
       if response.status_code == 200:
           dane = response.json()
           # wyciągnij: temperatura, opis pogody, wilgotność
           return {...}
       else:
           return None

3. Dodaj pętlę — użytkownik wpisuje miasto, dostaje pogodę.
4. BONUS: zapisuj historię zapytań do pliku JSON.
```

---

### 3.4 🤖 Integracja z LLM (bonus motywacyjny!)

> **To jest zabawna część.** Tutaj zobaczysz, jak w kilkunastu liniach kodu możesz zbudować coś, co faktycznie rozmawia i myśli. Jeśli masz mało czasu — zrób chociaż to zadanie, bo pokazuje, po co uczyć się Pythona w 2025/2026 roku.

**Opcja A: OpenAI (GPT)**
```python
# pip install openai

from openai import OpenAI

client = OpenAI(api_key="twój-klucz")  # https://platform.openai.com/api-keys

response = client.chat.completions.create(
    model="gpt-4o-mini",           # tani i szybki model
    messages=[
        {"role": "system", "content": "Jesteś pomocnym asystentem, który odpowiada po polsku."},
        {"role": "user", "content": "Co to jest dekorator w Pythonie? Wytłumacz prosto."}
    ]
)

print(response.choices[0].message.content)
```

**Opcja B: Anthropic (Claude)**
```python
# pip install anthropic

from anthropic import Anthropic

client = Anthropic(api_key="twój-klucz")  # https://console.anthropic.com/

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Co to jest dekorator w Pythonie? Wytłumacz prosto."}
    ]
)

print(message.content[0].text)
```

**Opcja C: Ollama (za darmo, lokalnie, bez klucza API)**
```python
# Zainstaluj Ollama: https://ollama.com/download
# W terminalu: ollama pull llama3.2
# pip install requests

import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3.2",
    "prompt": "Co to jest dekorator w Pythonie? Wytłumacz prosto.",
    "stream": False
})

print(response.json()["response"])
```

> **💡 Uwaga o kosztach:** OpenAI i Anthropic wymagają konta z płatnością, ale model `gpt-4o-mini` kosztuje grosze (dosłownie — cały ten projekt zmieści się w 10 groszach). Ollama jest w 100% darmowa i działa na Twoim komputerze.

**📝 Zadanie — Chatbot w terminalu:**
```
Napisz program, który:

1. Pozwala użytkownikowi rozmawiać z AI w pętli
2. Przechowuje historię rozmowy (listę słowników z "role" i "content")
3. Wysyła całą historię przy każdym zapytaniu (tak działa pamięć kontekstu!)
4. Użytkownik wpisuje "quit" aby zakończyć
5. Na końcu zapisuje historię rozmowy do pliku JSON

Schemat:
  historia = []
  while True:
      user_input = input("Ty: ")
      if user_input.lower() == "quit":
          break
      historia.append({"role": "user", "content": user_input})
      # wyślij historię do API, odbierz odpowiedź
      # historia.append({"role": "assistant", "content": odpowiedź})
      print(f"AI: {odpowiedź}")
```

---

### 🏗️ Projekt tygodnia 2: Asystent AI w terminalu

**Cel:** Połączyć OOP + API + JSON + pliki w jeden program.

```
Napisz "Asystenta AI" z następującymi funkcjami:

class Asystent:
    def __init__(self, imie, specjalizacja, api_key):
        self.imie = imie
        self.specjalizacja = specjalizacja
        self.api_key = api_key
        self.historia = []

    def zapytaj(self, pytanie):
        """Wysyła pytanie do API, zwraca odpowiedź, aktualizuje historię."""

    def zapisz_historie(self, plik):
        """Zapisuje historię rozmowy do pliku JSON."""

    def wczytaj_historie(self, plik):
        """Wczytuje poprzednią rozmowę z pliku JSON."""

    def podsumuj(self):
        """Prosi AI o podsumowanie dotychczasowej rozmowy."""

    def __str__(self):
        return f"Asystent '{self.imie}' ({self.specjalizacja}) — {len(self.historia)} wiadomości"

# Użycie:
bot = Asystent(
    imie="PyHelper",
    specjalizacja="Jesteś ekspertem Pythona. Tłumaczysz koncepty prosto i z przykładami kodu.",
    api_key="..."
)
bot.zapytaj("Co to jest list comprehension?")
bot.zapytaj("Pokaż mi 3 przykłady")
bot.zapisz_historie("rozmowa_01.json")
print(bot)
```

**Czas realizacji:** 3-5 godzin. To jest solidny projekt, który łączy: klasy, API, JSON, pliki, pętle, obsługę błędów.

---

## 4. Ściągawka: czego potrzebujesz na następne zajęcia

Na następnych laboratoriach będziemy pracować z **generatorami i iteratorami**, a potem z **dekoratorami**. Żeby to zrozumieć, musisz czuć się komfortowo z:

| Koncept | Priorytet | Status |
|---------|-----------|--------|
| Zmienne, typy, stringi | 🔴 Obowiązkowy | ☐ |
| Listy, słowniki | 🔴 Obowiązkowy | ☐ |
| Pętle for/while | 🔴 Obowiązkowy | ☐ |
| Funkcje (def, return, parametry) | 🔴 Obowiązkowy | ☐ |
| List comprehensions | 🔴 Obowiązkowy | ☐ |
| Praca z plikami (open, with) | 🟡 Ważny | ☐ |
| Klasy i obiekty (\_\_init\_\_, self) | 🟡 Ważny | ☐ |
| Dunder methods (\_\_str\_\_, \_\_repr\_\_) | 🟡 Ważny | ☐ |
| Funkcje jako obiekty pierwszej klasy | 🟡 Ważny | ☐ |
| pip, venv | 🟢 Przydatny | ☐ |
| requests + JSON | 🟢 Przydatny | ☐ |

> **Jeśli masz mało czasu:** Skup się na 🔴 i obejrzyj przynajmniej filmy Coreya Schafera o OOP (pkt 3.1). To da Ci najlepszy zwrot z inwestycji czasowej.

---

## 5. Polecane zasoby — pełna lista

### 🎬 YouTube — kanały (po angielsku, ale zrozumiałe)

| Kanał | Styl | Najlepsze do... |
|-------|------|-----------------|
| **Corey Schafer** | Spokojny, dokładny, zwięzły | Fundamenty Pythona, OOP, moduły — **nr 1 do tego kursu** |
| **Programming with Mosh** | Profesjonalny, szybki | Szybki przegląd Pythona od zera (6h kurs) |
| **Tech with Tim** | Projekty, gry, wizualizacje | Motywacja — widzisz efekt od razu |
| **Fireship** | Szybki, energiczny, krótki | Przegląd konceptów w 100 sekund |
| **freeCodeCamp** | Długie, kompletne kursy | Jeden duży kurs od A do Z |

### 📚 Dokumentacja i ćwiczenia

| Zasób | Link | Opis |
|-------|------|------|
| **Oficjalna dokumentacja Python** | [docs.python.org/pl/3/](https://docs.python.org/pl/3/) | Po polsku! Referencja do wszystkiego |
| **Python Tutorial (oficjalny)** | [docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/) | Krok po kroku od Pythona |
| **Real Python** | [realpython.com](https://realpython.com) | Najlepsze artykuły i tutoriale w sieci |
| **W3Schools Python** | [w3schools.com/python](https://www.w3schools.com/python/) | Proste przykłady, dobre na start |
| **HackerRank Python** | [hackerrank.com/domains/python](https://www.hackerrank.com/domains/python) | Ćwiczenia z automatycznym sprawdzaniem |
| **Exercism Python Track** | [exercism.org/tracks/python](https://exercism.org/tracks/python) | Ćwiczenia z mentorami |
| **PyNative OOP Exercises** | [pynative.com/python-object-oriented-programming-oop-exercise/](https://pynative.com/python-object-oriented-programming-oop-exercise/) | Zadania OOP z rozwiązaniami |

### 🔗 API do zabawy (darmowe, bez klucza lub z darmowym planem)

| API | Link | Co robi |
|-----|------|---------|
| JSONPlaceholder | [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) | Fake REST API — idealne do nauki requests |
| OpenWeatherMap | [openweathermap.org/api](https://openweathermap.org/api) | Pogoda — darmowy plan |
| PokeAPI | [pokeapi.co](https://pokeapi.co) | Dane o Pokemonach — zero rejestracji |
| REST Countries | [restcountries.com](https://restcountries.com) | Dane o krajach — zero rejestracji |
| Ollama (lokalne LLM) | [ollama.com](https://ollama.com) | Darmowe modele AI na Twoim komputerze |

---

> **Ostatnia rada:** Nie próbuj ogarnąć wszystkiego na raz. Wybierz jedną sekcję dziennie, obejrzyj film, zrób zadanie. **Pisanie kodu > oglądanie filmów.** Każda linia kodu, którą napiszesz sam/sama, jest warta więcej niż godzina oglądania. Powodzenia! 🚀
