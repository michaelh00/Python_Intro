"""
Builds v_2/python_course.ipynb — the student-facing notebook.

Run once:
    python v_2/build_student_notebook.py

Differences from course_roadmap.ipynb:
- No semaphore tags, no time notations.
- Explanatory markdown written TO the student before each code cell.
- All course content preserved (Sessions 2 & 3).
- No exercise solutions — solution cells replaced by empty stubs.
- Exercises reviewed; hard optional challenges added where missing.
"""

from pathlib import Path
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

def md(src):
    cells.append(nbf.v4.new_markdown_cell(src))

def code(src):
    cells.append(nbf.v4.new_code_cell(src))

# ============================================================
# TOP MATTER
# ============================================================

md("""# Python — an introduction

Welcome. This notebook is yours to run, edit, and break. Follow along as
we go through each cell together: I'll explain what it does and why it
matters, then we run it side by side.

## How a notebook works

A notebook is a stack of **cells**. Two kinds:

- **Markdown cells** hold text — like this one.
- **Code cells** hold Python — like the ones you'll run.

Run a cell with `Shift + Enter`. The value of the **last line** shows up
underneath. Cells share memory, so a variable made in one cell is usable
later — *as long as you actually ran the earlier cell*. If something
fails with `NameError`, you probably skipped a cell above.

**You can execute every cell in this notebook yourself, in parallel with
me.** Nothing here needs typing from scratch — read, run, watch, ask.

---
""")

# ============================================================
# SESSION 2
# ============================================================

md("""# Part A — Python basics

We build up the language: numbers, variables, types, strings, and the
containers that hold data. Nothing here touches files on disk yet.
""")

# ---------- Calculator ----------
md("""## 1 — Python as a calculator

The simplest thing a code cell does is evaluate an expression and show
the result. Let's start with arithmetic so you get used to running cells.
""")

md("A plain expression. Run it — the result `5` appears below the cell.")
code("2 + 3")

md("""The four everyday operators. Each cell shows its result. We run them
separately so you can see each one on its own.""")
code("5 - 1")
code("3 * 4")
code("10 / 5")

md("""Three that surprise people:

- `//` is **floor division** — divide and throw away the remainder.
- `%` is **modulo** — the remainder itself.
- `/` **always** gives a decimal (`float`), even when it divides evenly.

Watch the difference between the next three results.""")
code("12 // 5")
code("12 % 5")
code("12 / 5")

md("---")

# ---------- print() and variables ----------
md("""## 2 — `print()` and variables

`print()` shows text on screen. Text in Python is written inside quotes —
that's how Python knows it's words, not code.""")

md("Our first `print`. The quotes mark the text as a string.")
code('print("Hello from the Data Science Lab!")')

md("""Now a deliberate mistake. The next cell has **no quotes**, so Python
tries to read the words as code and fails. Run it, then read the error
message from the **bottom up** — the last line tells you what went wrong.
Meeting errors on purpose is the fastest way to stop fearing them.""")
code('print(Hello from the Data Science Lab!)')

md("""A **variable** is a label stuck onto a value. The `=` attaches the
label on the left to the value on the right. It is not the maths equals
sign — it does one thing, one direction.""")
code('country = "Switzerland"\ncountry')
code("print(country)")
code('print("I live in", country)')

md("""Variable names have rules. The next four cells break them on purpose
(spaces, a leading digit, a special character) so you see exactly what
Python complains about — then the fix. Run each, read the error.""")
code('country of interest = "USA"')
code('country_of_interest = "USA"')
code('2nd_country = "USA"')
code('&country = "USA"')

md("""Reassigning just moves the label. Python is **dynamic** — a variable
can even change type when you reassign it. Watch `my_variable` go from a
number to a string.""")
code("my_variable = 25\nmy_variable")
code('my_variable = "12"\nmy_variable')
code('my_variable_2 = "34"\nmy_variable_2')

md("""Here's the punchline about types. `+` means different things
depending on what's on each side. Two strings get **glued together**; two
numbers get **added**. Compare the next results carefully — `"12" + "34"`
is `"1234"`, not `46`.""")
code("my_variable + my_variable_2")
code("my_variable_3 = 12\nmy_variable_3")
code("my_variable_4 = 34\nmy_variable_4")
code("my_variable_3 + my_variable_4")

md("""And what if you mix a string with a number? Python refuses. Run the
next cell and read the `TypeError` — this is a bug you'll hit often, so
learn to recognise it now.""")
code("my_variable_2 + my_variable_4")

md("---")

# ---------- Types ----------
md("""## 3 — The four everyday types

Python figures out a value's **type** from how you write it. The four you
meet on day one: `int` (whole number), `float` (decimal), `str` (text),
`bool` (`True`/`False`). Ask any value its type with `type()`.""")
code('integer_type = 316\nprint(integer_type, "is of type", type(integer_type))')
code('float_type = 316.0\nprint(float_type, "is of type", type(float_type))')
code('string_type = "Hello World"\nprint(string_type, "is of type", type(string_type))')
code('bool_type = True\nprint(bool_type, "is of type", type(bool_type))')

md("""A classic beginner bug: gluing text and a number with `+`. The first
cell breaks on purpose; the second fixes it by converting the number to
text with `str()`. Note `str()` makes a new text value — it doesn't change
the original number.""")
code('case_number = 316\nmessage = "Case number: " + case_number')
code('case_number = 316\nmessage = "Case number: " + str(case_number)\nprint(message)')

md("""Two ways to turn a decimal into a whole number, and they differ:
`int()` **truncates** (chops the decimal off), `round()` **rounds**. So
`int(5.9)` is `5`, but `round(5.9)` is `6`.""")
code("i = int(5.9)\ni")
code("r = round(5.9)\nr")
code("type(r)")

md("Converting the other way: text to a number, number to text.")
code('f = float("3.14")\nf')
code("s = str(2024)\ns")

md("""Comparisons ask a yes/no question and return a `bool`. Note the
**double** `==` for "is equal to" — a single `=` would try to assign.
Confusing `=` and `==` is the number-one beginner bug.""")
code("""tariff_rate = 5.5

result = tariff_rate > 10
print(result)

result = tariff_rate < 10
print(result)

result = tariff_rate == 10
print(result)

result = tariff_rate != 10
print(result)""")

md("""Combine conditions with `and` / `or` — plain English words, not
symbols. `and` needs both sides true; `or` needs at least one.""")
code("""tariff_rate = 5.5

result = tariff_rate > 10 and tariff_rate < 20
print(result)

result = tariff_rate < 10 or tariff_rate > 20
print(result)""")

md("---")

# ---------- Exercise Block 1 ----------
md("""## Exercise Block 1 — Variables and operators

Work in the empty cell below. Do the **Core** set first; try **Stretch**
if you have time; **Challenge** is a hard optional one — no shame in
skipping it.

### Core

1. Create three variables describing a country: `name` (str),
   `population_millions` (float), and WTO membership (bool).
2. Print a sentence using all three, shaped like
   `"Kenya has 55.1 million people. Is it member of the WTO? True"`.
   Use `print()` with commas.
3. A document has 142 pages. Using `//` and `%`, compute full chapters of
   20 pages, and leftover pages. Print both.
4. Given `year_signed = 1994`, compute `age` in 2026. Print it.

### Stretch

1. Given `tariff_rate = 7.5` and `discount = 0.20`, print the discounted
   rate with a message.
2. Check whether `population_millions` is between 10 and 100 inclusive.
   Store in `is_medium_sized`. Print.
3. Deliberately trigger a `TypeError`. Read the traceback. Fix it.

### Challenge (hard, optional)

Given exactly `total_seconds = 100000`, print the duration as
`"1 day, 3 hours, 46 minutes, 40 seconds"` using only `//` and `%` — no
imports, no libraries. You'll need to peel off days, then hours, then
minutes, then seconds, in that order.
""")
code("# Exercise Block 1 — your code here\n")

md("---")

# ---------- Strings ----------
md("""## 4 — String manipulations

Strings come with built-in helper **methods**. Each one returns a **new**
string; the original never changes. We'll test them on a deliberately
messy filename.""")
code('filename = "  Costa Rica - Tariff Schedule FINAL.csv  "\nfilename')
code("filename.strip()")
code("filename.lower()")
code("filename.strip().lower()")
code('filename.replace(" ", "_")')
code('filename.endswith(".csv")')
code('filename.strip().endswith(".csv")')
code("len(filename)")

md("""Notice `filename` is still the messy original — methods don't change
it. To keep a cleaned version, you must **assign** the result to a
variable.""")
code("filename")
code('cleaned = filename.strip().lower().replace(" ", "_")\ncleaned')

md("""You can reach into a string by position. Counting starts at **0**.
A slice `[a:b]` runs from `a` up to *but not including* `b`. `-1` means
the last character.""")
code('symbol = "WT-DS316-AB-R"')
code("symbol[0]")
code("symbol[5]")
code("symbol[3:6]")
code("symbol[-1]")

md("""Strings are **immutable** — you can't change one character in place.
The first cell tries and fails; read the `TypeError`. The workaround is to
build a new string with `.replace()`.""")
code("symbol[3] = 'X'\nsymbol")
code("var = symbol[3]\nvar")
code('symbol = symbol.replace(var, "X")\nsymbol')

md("---")

# ---------- f-strings ----------
md("""## 5 — f-strings

Building a sentence with variables inside is cleanest with an
**f-string**: put an `f` before the quotes and drop variable names inside
`{ }`. Compare the three approaches below — the f-string wins.""")
code('country = "Kenya"\ntariff_rate = 5.5\nyear = 2024')
code('print("In", year, ",", country, "had a tariff rate of", tariff_rate, "%", ".")')
code('print("In " + str(year) + ", " + country + " had a tariff rate of " + str(tariff_rate) + "%.")')
code('print(f"In {year}, {country} had a tariff rate of {tariff_rate}%.")')

md("""f-strings can also format numbers — for example, fix the number of
decimal places with `:.2f`.""")
code("""tariff_rate = 5.12986

print(f"{tariff_rate}")
print(f"{tariff_rate: .2f}")
print(f"{tariff_rate: .4f}")""")

md("---")

# ---------- Lists ----------
md("""## 6 — Lists

A **list** is an ordered collection, written with square brackets. It can
hold anything, and `len()` tells you how many items.""")
code('my_list = [10, 21, 0.512, "Hello"]\nprint(my_list)\nprint(len(my_list))')

md("""Indexing and slicing work exactly like strings: position 0 is first,
`[a:b]` is half-open, leaving a side blank means "to the end" or "from the
start".""")
code("my_list[1]")
code("my_list[0:3]")
code("my_list[:3]")
code("my_list[2:]")
code("""my_short_list = my_list[1:4]
print(my_list)
print(my_short_list)""")

md("""Unlike strings, lists **can** be changed in place. Watch each
operation modify `my_list`:

- `append` adds to the end,
- `pop(3)` removes by **index**,
- `[1] = ...` replaces by index,
- `remove("France")` removes by **value**,
- `insert(0, ...)` adds at a position.""")
code("my_list = [10, 21, 0.512, 'Hello']\nmy_list")
code('my_list.append("Switzerland")\nmy_list')
code("my_list.pop(3)\nmy_list")
code('my_list[1] = "France"\nmy_list')
code('my_list.remove("France")\nmy_list')
code('my_list.insert(0, "Germany")\nmy_list')

md("---")

# ---------- Sets ----------
md("""## 7 — Sets

A **set** keeps only unique values. Handy for answering "how many distinct
things are there?" — build one from a list and the duplicates vanish.""")
code("""tariff_rates = [5.0, 7.5, 5.0, 10.0, 7.5, 5.0]

unique_rates = set(tariff_rates)
unique_rates""")

md("---")

# ---------- Dicts ----------
md("""## 8 — Dictionaries

A **dictionary** looks things up by **name** (a key) instead of by
position. You write it with `key: value` pairs in curly braces.""")
code("""country = {
    "name" : "Kenya",
    "population_millions" : 55.1,
}
country""")
code('country["name"]')

md("Add a key just by assigning to it. Add several at once with `.update()`.")
code('country["capital"] = "Nairobi"')
code("country")
code('country.update({"region": "Africa", "wto_member": True})')
code("country")

md("""The shape real data usually takes: a **list of dictionaries**, one
dict per record. To reach a field, index twice — first the record, then
the key.""")
code("""country2 = {
'name': 'Germany',
 'population_millions': 83.2,
 'capital': 'Berlin',
 'region': 'Europe',
 'wto_member': True
}""")
code("""country3 = {
'name': 'Switzerland',
  'population_millions': 8.6,
  'capital': 'Bern',
  'region': 'Europe',
  'wto_member': True,
}""")
code("countries = [country, country2, country3]\ncountries")
code('countries[2]["name"]')

md("---")

# ---------- Exercise Block 2 ----------
md("""## Exercise Block 2 — Strings and containers

Use the empty cell below.

### Core

1. Clean `raw = "  KENYA - Tariff Schedule 2024.CSV  "` into
   `"kenya_-_tariff_schedule_2024.csv"` by chaining methods.
2. Build a list `un_founders` (≥ 4 countries). Print first, last, length.
3. From `symbol = "WT-DS316-AB-R"`, slice out `"DS316"`.
4. Make a dict with `name`, `capital`, `population_millions`. Print a
   sentence with an f-string.

### Stretch

1. From `rates = [1.8, 12.0, 13.5, 4.3, 7.5, 9.0, 5.5]`, slice the last
   three and the middle three.
2. Add `"is_wto_member": True` to your dict, print it, then bump the
   population by 1.0 and print again.
3. Build a `set` from `rates`. Print how many are distinct.

### Homework (optional)

1. From `raw = "population: 55.1 million"`, extract `55.1` as a float
   using slicing only.
2. Given a `docs` list of dicts, print the `kind` of the first, the `year`
   of the last, and an f-string identifying the oldest.

### Challenge (hard, optional)

Given the list of dicts below, **without importing anything**, build a new
dictionary that maps each `region` to the list of country names in that
region, e.g. `{"Europe": ["Germany", "Switzerland"], "Africa": ["Kenya"]}`.
You'll need a loop, a dict you grow as you go, and the `.get(key, default)`
trick you'll see in Part B.

```python
data = [
    {"name": "Germany",     "region": "Europe"},
    {"name": "Kenya",       "region": "Africa"},
    {"name": "Switzerland", "region": "Europe"},
    {"name": "Brazil",      "region": "Americas"},
    {"name": "Nigeria",     "region": "Africa"},
]
```
""")
code("# Exercise Block 2 — your code here\n")

md("""---

## End of Part A

With Parts 1–8 you have every language building block: variables, types,
strings, lists, sets, dictionaries. Part B adds decisions, loops, and
functions — and then applies all of it to real files on disk.
""")

# ============================================================
# SESSION 3
# ============================================================

md("""# Part B — Control flow, functions, and organising files

Now we make code that **decides** (`if`), **repeats** (`for`, `while`),
and can be **called by name** (`def`). Then we point all of it at a messy
folder of documents and tidy it up automatically.

**Before running the file sections:** `sample_data/` must exist. If a cell
complains it's missing, open a terminal and run
`python setup_sample_data.py`, then re-run the cell.
""")

# ---------- if ----------
md("""## 1 — Decisions with `if`

`if` runs a block only when its condition is true. The block is whatever
is **indented** below it — Python uses indentation, not braces, and four
spaces is the convention. `elif` and `else` cover the other cases; the
first matching branch wins.""")
code("""tariff_rate = 7.5

if tariff_rate > 10:
    category = "high"
elif tariff_rate > 5:
    category = "moderate"
else:
    category = "low"

print(category)""")

md("""A playful example of chained conditions: rock-paper-scissors against
a random computer choice. Run it a few times and watch the outcome change.""")
code("""import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

your_choice = "rock"

if your_choice == computer_choice:
    print(f"Both chose {your_choice}. It's a tie!")
elif your_choice == "scissors" and computer_choice == "paper":
    print("You chose scissors and computer chose paper. You win!")
elif your_choice == "paper" and computer_choice == "rock":
    print("You chose paper and computer chose rock. You win!")
elif your_choice == "rock" and computer_choice == "scissors":
    print("You chose rock and computer chose scissors. You win!")
else:
    print(f"You chose {your_choice} and computer chose {computer_choice}. You lose!")""")

md("---")

# ---------- for ----------
md("""## 2 — `for` loops

A `for` loop walks through a collection one item at a time. The loop
variable takes each value in turn; the indented body runs once per item.""")
code("""countries = ["Switzerland", "USA", "Brazil", "Kenya"]

for country in countries:
    print(f"Country: {country}")""")

md("""A common pattern: keep a running **counter** that you bump inside the
loop. This "accumulate as you go" idea returns when we organise files.""")
code("""countries = ["Switzerland", "USA", "Brazil", "Kenya"]

count = 0
for country in countries:
    count = count + 1
    print(f"{count} -> {country}")""")

md("`range(0, 5)` produces `0, 1, 2, 3, 4` — half-open, like slicing.")
code("for i in range(0, 5):\n    print(i)")

md("""When you want both the position and the item, `enumerate` gives you
both at once — cleaner than a hand-rolled counter.""")
code("""countries = ["Switzerland", "USA", "Brazil", "Uganda", "Kenya"]

for index, country in enumerate(countries):
    print(f"{index}: {country}")""")

md("""Combine `for` with `if` to act only on some items. Two useful
keywords: `break` stops the loop entirely at the first hit; `continue`
skips the rest of the current item and moves on.""")
code("""for index, country in enumerate(countries):
    if country.startswith("U"):
        print(f"Found a country starting with 'U' in the list of countries at index {index}")""")
code("""for index, country in enumerate(countries):
    if country.startswith("U"):
        print(f"Found a country starting with 'U' in the list of countries at index {index}")
        break""")
code("""for index, country in enumerate(countries):
    if not country.startswith("U"):
        continue
    print(f"Processing country: {country}")""")

md("Looping over a dictionary with `.items()` gives you key and value together.")
code("""country = {"name": "Kenya", "population_millions": 55.1}

for key, value in country.items():
    print(f"{key} -> {value}")""")

md("""The pattern that underlies the whole file organiser: **loop, decide,
collect into a new list**. Here we gather high-tariff country names. Later
we'll do the same with files instead of countries.""")
code("""countries = [
    {"name": "Switzerland", "avg_tariff": 1.8},
    {"name": "Kenya",       "avg_tariff": 12.0},
    {"name": "Brazil",      "avg_tariff": 13.5},
    {"name": "Japan",       "avg_tariff": 4.3},
]

high_tariff_countries = []

for c in countries:
    if c["avg_tariff"] > 10:
        high_tariff_countries.append(c["name"])

print(high_tariff_countries)""")

md("---")

# ---------- while ----------
md("""## 3 — `while` loops

A `while` loop keeps going as long as its condition stays true. You must
change something inside the loop, or it runs forever — if that happens,
use the stop button in the toolbar.""")
code("""counter = 10
while counter > 0:
    print(counter)
    counter = counter - 1
print("Liftoff!")""")

md("""`while` shines when you don't know in advance how many rounds you
need — like rolling a die until you get a 6. Run it a few times; the
number of rolls varies.""")
code("import random\ndice_roll = random.randint(1, 6)\ndice_roll")
code("""dice = 1
rolls = 0

while dice != 6:
    dice = random.randint(1, 6)
    rolls = rolls + 1
    print(f"Rolled: {dice}")

print(f"You needed {rolls} rolls to get a 6.")""")

md("---")

# ---------- functions ----------
md("""## 4 — Functions

A **function** is a named piece of code you define once with `def` and
call as often as you like. Start simple: no inputs, just an action.""")
code("""def greet():
    print(f"Welcome to the course.")

greet()""")

md("Add a **parameter** so the function can vary its behaviour per call.")
code("""def greet(name):
    print(f"Welcome to the course, {name}.")

greet("Matteo")
greet("Ana")""")

md("""The key idea: `return` hands a value back to the caller, so you can
use the result elsewhere. This is different from `print`, which only
shows something on screen. Confusing the two trips people up for weeks —
watch what `return` gives you here.""")
code("""def calculate_sum(a, b):
    sum = a + b
    return sum

calculate_sum(3, 5)""")

md("""Functions compose nicely. Here a `while` loop is wrapped in a
function that takes the number of sides as a parameter, then called for
several dice.""")
code("""import random

def roll_until_six(sides):
    dice = 1
    rolls = 0
    while dice != 6:
        dice = random.randint(1, sides)
        rolls = rolls + 1
    return rolls

dices = {"cube": 6, "octahedron": 8, "dodecahedron": 12, "icosahedron": 20}

for name, sides in dices.items():
    print(f"{name.capitalize()} needed {roll_until_six(sides)} rolls to get a 6.")""")

md("""Functions calling functions — small pieces, each doing one job,
combined. This is exactly the shape of the file organiser we'll build
shortly.""")
code("""def convert_to_chf(amount, rate):
    return amount * rate

def print_price(amount, currency, rate):
    chf = convert_to_chf(amount, rate)
    print(f"{amount} {currency} = {chf} CHF")

print_price(100, "USD", 0.88)
print_price(50, "EUR", 0.95)""")

md("---")

# ---------- Exercise Block 3 ----------
md("""## Exercise Block 3 — Decisions, loops, functions

Use this data (run it first), then work in the empty cell below it.

### Core

1. Loop and print each country's name.
2. Loop and print `"<name>: high tariff"` only for `avg_tariff > 10`.
3. Write `is_populous(country, threshold=50)` returning a bool. Test twice.
4. Count WTO members with a `for` + `if`. Print the count.

### Stretch

1. Build `wto_only`, a list of only the WTO-member dicts. Print its length.
2. Write `tariff_category(rate)` returning `"low"`, `"moderate"`,
   `"high"`, or `"very high"`, and print `"<name>: <category>"` per country.

### Challenge (hard, optional)

Write `top_n_by_tariff(countries, n=3)` that returns the names of the `n`
countries with the highest `avg_tariff`, in descending order — **without**
using `sorted`. Do it manually: on each pass, scan a working copy for the
current maximum, record its name, remove it, repeat `n` times.
""")
code("""countries = [
    {"name": "Switzerland", "population_millions": 8.8,   "avg_tariff": 1.8,  "wto_member": True},
    {"name": "Kenya",       "population_millions": 55.1,  "avg_tariff": 12.0, "wto_member": True},
    {"name": "Brazil",      "population_millions": 214.3, "avg_tariff": 13.5, "wto_member": True},
    {"name": "Japan",       "population_millions": 125.7, "avg_tariff": 4.3,  "wto_member": True},
    {"name": "Argentina",   "population_millions": 45.4,  "avg_tariff": 13.6, "wto_member": True},
    {"name": "Iran",        "population_millions": 88.6,  "avg_tariff": 20.1, "wto_member": False},
]""")
code("# Exercise Block 3 — your code here\n")

md("---")

# ---------- pathlib ----------
md("""## 5 — Exploring a folder with `pathlib`

Everything from here uses the same patterns — loops, ifs, dicts,
functions — but points them at real files. The only new thing is the
`Path` object. `pathlib` is Python's modern, safe way to talk about
files and folders.

Run the next cell first. If `sample_data/` is missing, it tells you
exactly what to do.""")
code("""from pathlib import Path

data_dir = Path("sample_data")

if not data_dir.exists():
    raise FileNotFoundError(
        "sample_data/ not found — run 'python setup_sample_data.py' in the terminal, then re-run this cell."
    )

files = list(data_dir.iterdir())
print(f"Found {len(files)} files in {data_dir.resolve()}")""")

md("A peek at the mess we're going to organise.")
code("""for f in files[:8]:
    print(f.name)""")

md("""A `Path` is an object that knows things about a file's location.
The `/` operator joins path pieces safely — no manual slashes, no
OS-specific bugs. Each `Path` exposes handy properties: `.name`, `.stem`
(name without extension), `.suffix` (the extension), `.parent`.""")
code("""from pathlib import Path

p = Path("sample_data") / "WT-DS316-AB-R.txt"
print(p)""")
code("""p = Path("sample_data") / "WT-DS316-AB-R.txt"

print("full path :", p)
print("name      :", p.name)     # WT-DS316-AB-R.txt
print("stem      :", p.stem)     # WT-DS316-AB-R
print("suffix    :", p.suffix)   # .txt
print("parent    :", p.parent)   # sample_data
print("exists    :", p.exists())""")

md("""`iterdir()` yields one `Path` per entry in a folder. Combine it with
a `for` + `if` + counter — the exact pattern from the exercises — to
answer questions like "how many CSVs are here?".""")
code("""data_dir = Path("sample_data")

for f in data_dir.iterdir():
    print(f.name)""")
code("""count_csv = 0

for f in data_dir.iterdir():
    if f.suffix == ".csv":
        count_csv = count_csv + 1

print(f"{count_csv} CSV files")""")

md("""Because `.name` is just a string, every string method from Part A
still works — `in`, `.startswith`, `.lower()`. This is the payoff:
yesterday's toys, today's real work.""")
code("""for f in data_dir.iterdir():
    if "asbestos" in f.name.lower():
        print(f.name)""")
code("""official_looking = []

for f in data_dir.iterdir():
    name = f.name
    if name.startswith("WT-") or name.startswith("G_") or name.startswith("TN_"):
        official_looking.append(name)

print(len(official_looking), "files look officially named")
for n in official_looking[:5]:
    print("  ", n)""")

md("""Counting into a **dictionary** — the pattern the final organiser
needs. The first version spells it out with `if`; the second uses
`.get(key, default)`, which returns the default when the key isn't there
yet. Same result, less code.""")
code("""counts = {}

for f in data_dir.iterdir():
    suffix = f.suffix
    if suffix in counts:
        counts[suffix] = counts[suffix] + 1
    else:
        counts[suffix] = 1

print(counts)""")
code("""counts = {}

for f in data_dir.iterdir():
    counts[f.suffix] = counts.get(f.suffix, 0) + 1

print(counts)""")

md("""`glob` is a shortcut when you just want files matching a pattern.
`*` means "anything", so `*.csv` grabs every CSV.""")
code("""csvs = list(data_dir.glob("*.csv"))
print(len(csvs), "CSV files")

for c in csvs:
    print(" ", c.name)""")

md("---")

# ---------- Exercise Block 4 ----------
md("""## Exercise Block 4 — Exploring the folder

Run the setup cell below first so `data_dir` and `files` exist, then work
in the empty cell.

### Core

1. Print the total number of files using `iterdir()` and a counter (not
   `len(files)` — practise the loop).
2. Print the `.stem` of each file whose `.suffix` is `.txt`.
3. Count how many filenames contain `"DS"` (case-insensitive). Print it.
4. Using `.glob(...)`, list the `.name` of every `.csv`, one per line.

### Stretch

1. Build `counts_by_suffix` mapping each suffix to its file count. Print it.
2. Build `probably_renamed`: filenames that do **not** start with `WT-`,
   `G_`, or `TN_`. Print the length and first three.
3. Print the longest filename (by `len(f.name)`) and its length.

### Challenge (hard, optional)

Write `filter_by(files, contains=None, suffix=None)` that returns only the
`Path` objects whose name contains `contains` (if given) **and** whose
suffix equals `suffix` (if given). Both default to `None`, meaning "ignore
this filter". Test it three ways: `suffix=".txt"` alone, `contains="ds"`
alone, and both together.
""")
code("""from pathlib import Path

data_dir = Path("sample_data")
files = list(data_dir.iterdir())""")
code("# Exercise Block 4 — your code here\n")

md("---")

# ---------- mkdir / shutil / write_text ----------
md("""## 6 — Making folders, copying, and writing files

Now we change things on disk. That's fine — we only ever write into new
folders we create ourselves. We never touch `sample_data/`; if anything
breaks, re-run the setup script.

`mkdir(parents=True, exist_ok=True)` means "make this folder, including any
missing parents, and don't complain if it already exists" — a safe
"ensure it exists" in one line.""")
code("""target = Path("organised") / "appellate_body"
target.mkdir(parents=True, exist_ok=True)

print(target.exists())""")

md("""`shutil.copy(source, destination)` copies a file. The destination
folder must already exist — that's what the `mkdir` above was for.""")
code("""import shutil

source = Path("sample_data") / "WT-DS316-AB-R.txt"
destination = Path("organised") / "appellate_body" / source.name

shutil.copy(source, destination)
print(destination.exists())""")

md("""Renaming in place with `.rename()`. `with_name(...)` gives you a new
path in the same folder but a different filename.""")
code("""old = destination
new = destination.with_name("renamed_example.txt")

old.rename(new)

print("old exists?", old.exists())
print("new exists?", new.exists())""")

md("""`write_text(...)` writes a whole string to a file (overwriting any
existing content); `read_text()` reads it back. This is how the final
project will produce a summary file.""")
code("""report = Path("organised") / "summary.txt"

report.write_text(
    "Organisation summary\\n"
    "--------------------\\n"
    "Files handled so far: 1\\n"
)

print("wrote", report)""")
code("""content = report.read_text()
print(content)""")

md("""Everything comes together here. A function `classify` decides which
category a filename belongs to (the first matching `if` branch wins, so
order matters). Then a loop classifies every file, makes the matching
folder, and copies the file in. This little script is the whole point of
the course — read it slowly.""")
code("""def classify(filename):
    name = filename.lower()
    if "ab" in name and "ds" in name:
        return "appellate_body"
    elif "panel" in name:
        return "panel_report"
    elif name.endswith(".csv") or "tariff" in name:
        return "tariff_schedule"
    elif "min" in name or name.startswith("tn_"):
        return "ministerial"
    elif "agreement" in name or "understanding" in name or "gatt" in name:
        return "legal_text"
    else:
        return "unclassified"


out_root = Path("organised_demo")

for f in data_dir.iterdir():
    category = classify(f.name)
    dest_folder = out_root / category
    dest_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy(f, dest_folder / f.name)

print("done. contents of organised_demo/:")
for sub in out_root.iterdir():
    n = len(list(sub.iterdir()))
    print(f"  {sub.name}: {n} files")""")

md("---")

# ---------- Capstone ----------
md("""## Capstone — Your own organiser

Build your own version in the empty cell below. **Safety:** only write to
new folders (like `my_organised/`), never into `sample_data/`. If anything
goes wrong, re-run the setup script to restore the source.

### Core

1. Create `my_organised/` next to this notebook.
2. Inside it, create `csv_files/` and `txt_files/`.
3. Loop through `sample_data/`. Copy every `.csv` into `csv_files/`, every
   `.txt` into `txt_files/`. Skip everything else.
4. Print how many files ended up in each subfolder using `.iterdir()` and
   a counter.

### Stretch — a real summary file

1. Reuse `classify`. Sort into all six categories.
2. Keep a running `counts` dict inside the loop.
3. Write `my_organised/summary.txt` with one line per category plus a
   `total:` line. Read it back with `read_text()` and print it.

### Challenge (hard, optional) — collisions and packaging

1. `sample_data/` contains two files describing the same shrimp-turtle
   report under different names. When copying, if the target folder
   already holds a file whose stem shares the same case-number prefix,
   append `_dup` to the new file's stem instead of overwriting.
2. Add a section to the summary listing every `_dup` copy made.
3. Wrap the whole thing in `organise(source_folder, target_folder)` that
   returns the `counts` dict. Call it twice — the second run should be a
   no-op apart from the `_dup` handling.

When stuck, `print()` things. Half of Python is discovering what a
variable actually contains, versus what you imagined.
""")
code("""from pathlib import Path
import shutil

data_dir = Path("sample_data")

# Capstone — your code here
""")

md("""---

## Wrap-up

You've gone from an empty notebook to a script that organises a folder of
documents automatically. Whether it's 10 files or 10,000, it's the same
amount of typing. The pattern — **loop over a folder, decide something
about each item, act on it, record what happened** — is the shape of a
huge amount of everyday research automation. Swap the documents for
interview transcripts, court PDFs, or scraped articles: the scaffolding
is identical.
""")

# ============================================================
# WRITE
# ============================================================

nb["cells"] = cells

out = Path(__file__).parent / "python_course.ipynb"
out.parent.mkdir(exist_ok=True)
with open(out, "w", encoding="utf-8") as fh:
    nbf.write(nb, fh)

print(f"Wrote {out} ({len(cells)} cells)")