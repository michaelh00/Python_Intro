"""
One-shot builder for v_2/course_roadmap.ipynb.

Run once from the repo root:
    python v_2/build_roadmap.py

Produces: v_2/course_roadmap.ipynb

Design notes
------------
- Teacher-facing roadmap. You read from this while typing into a fresh
  notebook in front of students.
- Legend: 🟢 Core (must show)  🟡 Optional (if time)  🔵 Bonus (skip unless asked)
- Every code cell is preceded by a teacher-note markdown cell:
  tag, time budget, what to say, error to provoke, common confusion.
- Code cells are verbatim from basic_python_exec.ipynb (Session 2) and
  from python_automation_orig.ipynb (Session 3 automation half).
- Sessions 2 and 3 are 90 min each. Session 3 = logic/functions (~35 min) +
  automation + capstone (~55 min). Tight; skip 🟡/🔵 aggressively.
"""

from pathlib import Path
import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

def md(src):
    cells.append(nbf.v4.new_markdown_cell(src))

def code(src):
    cells.append(nbf.v4.new_code_cell(src))

def note(tag, minutes, say, error=None, confusion=None):
    """Teacher-note markdown cell that sits above a code cell."""
    parts = [f"**{tag} · {minutes}**", "", f"*Say:* {say}"]
    if error:
        parts += ["", f"*Provoke:* {error}"]
    if confusion:
        parts += ["", f"*Watch for:* {confusion}"]
    md("\n".join(parts))

# ============================================================
# TOP MATTER
# ============================================================

md("""# Course roadmap — teacher notebook

**How to use this file.** Keep this notebook open on one screen. On the
other screen, open a *fresh, empty* notebook and type into that one while
students watch. Read the teacher-notes here, type the code cell below
into the student-facing notebook, run it, discuss. Do **not** project
this file — it contains solutions.

## Legend

| Tag | Meaning |
|-----|---------|
| 🟢 Core     | Must show. Everyone needs it for later. |
| 🟡 Optional | Show if you're on time. Skip without guilt. |
| 🔵 Bonus    | Only if a student asks or you're way ahead. |

## Session map

| Session | Block                          | Cumulative | Content |
|---------|--------------------------------|-----------:|---------|
| **2**   | Calculator + `print` + vars    | 10 min     | 🟢 |
|         | Types + conversions            | 20 min     | 🟢 |
|         | Comparisons + booleans         | 25 min     | 🟢 |
|         | **Exercise Block 1**           | 45 min     | 🟢 |
|         | Strings + f-strings            | 60 min     | 🟢 |
|         | Lists, sets, dicts             | 80 min     | 🟢 |
|         | **Exercise Block 2**           | 90 min     | 🟢 (start; finish as HW) |
| **3**   | `if` / `for` / `while`         | 15 min     | 🟢 |
|         | Functions                      | 30 min     | 🟢 |
|         | **Exercise Block 3**           | 45 min     | 🟢 |
|         | `pathlib`: explore folder      | 60 min     | 🟢 |
|         | `mkdir`, `shutil`, `write_text`| 75 min     | 🟢 |
|         | **Capstone** (start)           | 90 min     | 🟢 (finish as HW) |

## Rules of thumb while teaching

- **Always type, never paste.** Students copy your rhythm, not your code.
- **Provoke the errors marked below.** Meeting `NameError`, `TypeError`,
  `SyntaxError` on purpose is worth more than any lecture about them.
- **When you fall behind:** cut 🟡 first, then compress exercise
  debrief. Never cut Exercise Block 1 or the capstone.
- **When a student asks "why?":** answer briefly, offer the 🔵 deep-dive
  after class. Do not derail the session.

---
""")

# ============================================================
# SESSION 2
# ============================================================

md("""# Session 2 — Python basics (90 min)

Goal: by the end, every student can read and write Python that uses
variables, the four everyday types, strings, lists, and dictionaries,
and knows what a traceback is.

Nothing today touches disk. That's Session 3.

---
""")

# ---------- Calculator ----------
md("## Part 1 — Python as a calculator")

note("🟢 Core", "2 min",
     "Open a fresh notebook. Show that a code cell prints its last expression.",
     confusion="Shift+Enter runs the cell. Ctrl+Enter runs and stays.")
code("2 + 3")

note("🟢 Core", "3 min",
     "Rattle through the four basic operators. Don't linger.")
code("5 - 1")
code("3 * 4")
code("10 / 5")

note("🟢 Core", "3 min",
     "Now the three that surprise people: floor div, modulo, the fact that "
     "`/` always returns a float even when it divides evenly.",
     confusion="`//` is not a comment here. `%` is not percent.")
code("12 // 5")
code("12 % 5")
code("12 / 5")

md("---")

# ---------- print() and variables ----------
md("## Part 2 — `print()` and variables")

note("🟢 Core", "1 min",
     "First `print`. Explain: strings need quotes.")
code('print("Hello from the Data Science Lab!")')

note("🟢 Core — provoke error", "2 min",
     "Type it without quotes on purpose. Read the SyntaxError together, "
     "bottom line first.",
     error="Missing quotes → SyntaxError",
     confusion="Students read tracebacks top-down. Train them to read bottom-up.")
code('print(Hello from the Data Science Lab!)')

note("🟢 Core", "3 min",
     "Introduce assignment. The `=` is a label sticker, not maths.")
code('country = "Switzerland"\ncountry')
code("print(country)")
code('print("I live in", country)')

note("🟢 Core — provoke three errors", "4 min",
     "Show each broken name, let the SyntaxError happen, then fix. "
     "This is the one time you should type broken code deliberately.",
     error="spaces, leading digit, special char in variable names")
code('country of interest = "USA"')
code('country_of_interest = "USA"')
code('2nd_country = "USA"')
code('&country = "USA"')

note("🟡 Optional", "2 min",
     "Reassignment. Types can change with reassignment — Python is dynamic.")
code("my_variable = 25\nmy_variable")
code('my_variable = "12"\nmy_variable')
code('my_variable_2 = "34"\nmy_variable_2')

note("🟢 Core — the punchline", "3 min",
     "Add two strings vs add two ints. This is the first time students see "
     "that `+` means different things depending on type.",
     confusion="`\"12\" + \"34\"` is `\"1234\"`, not `46`.")
code("my_variable + my_variable_2")
code("my_variable_3 = 12\nmy_variable_3")
code("my_variable_4 = 34\nmy_variable_4")
code("my_variable_3 + my_variable_4")

note("🟢 Core — provoke TypeError", "2 min",
     "Now mix a string and an int with `+`. Read the traceback together.",
     error="TypeError: unsupported operand type(s) for +: 'str' and 'int'")
code("my_variable_2 + my_variable_4")

md("---")

# ---------- Types ----------
md("## Part 3 — The four everyday types")

note("🟢 Core", "3 min",
     "int, float, str, bool. `type()` is your friend. Show all four.")
code('integer_type = 316\nprint(integer_type, "is of type", type(integer_type))')
code('float_type = 316.0\nprint(float_type, "is of type", type(float_type))')
code('string_type = "Hello World"\nprint(string_type, "is of type", type(string_type))')
code('bool_type = True\nprint(bool_type, "is of type", type(bool_type))')

note("🟢 Core — provoke TypeError, then fix", "3 min",
     "Classic 'Case number: ' + 316 mistake. Read the error, then fix with str().",
     error="TypeError concatenating str and int",
     confusion="`str(x)` converts, it does not modify x.")
code('case_number = 316\nmessage = "Case number: " + case_number')
code('case_number = 316\nmessage = "Case number: " + str(case_number)\nprint(message)')

note("🟡 Optional", "3 min",
     "int() truncates, round() rounds. Not the same. Show both.",
     confusion="`int(5.9)` is 5, not 6.")
code("i = int(5.9)\ni")
code("r = round(5.9)\nr")
code("type(r)")

note("🟡 Optional", "1 min",
     "float() from a string, str() from a number. Round-trip.")
code('f = float("3.14")\nf')
code("s = str(2024)\ns")

note("🟢 Core", "3 min",
     "Comparisons return bool. Double-equals for comparison, single for assign. "
     "Write this on the board.",
     confusion="`=` vs `==` is the #1 beginner bug.")
code("""tariff_rate = 5.5

result = tariff_rate > 10
print(result)

result = tariff_rate < 10
print(result)

result = tariff_rate == 10
print(result)

result = tariff_rate != 10
print(result)""")

note("🟢 Core", "2 min",
     "Combine with `and` / `or`. English words, not `&&`.")
code("""tariff_rate = 5.5

result = tariff_rate > 10 and tariff_rate < 20
print(result)

result = tariff_rate < 10 or tariff_rate > 20
print(result)""")

md("---")

# ---------- Exercise Block 1 ----------
md("""## Exercise Block 1 — Variables and operators

*(20 min. Everyone should finish Core. Stretch if fast. Homework never
required for the capstone.)*

### Core (everyone)

1. Create three variables describing a country: `name` (str),
   `population_millions` (float), and WTO membership (bool).
2. Print a sentence using all three, of the shape
   `"Kenya has 55.1 million people. Is it member of the WTO? True"`.
   Use `print()` with commas.
3. A document has 142 pages. Using `//` and `%`, compute full chapters
   of 20 pages, and leftover pages. Print both.
4. Given `year_signed = 1994`, compute `age` in 2026. Print it.

### Stretch

1. Given `tariff_rate = 7.5` and `discount = 0.20`, print the discounted
   rate with a message.
2. Check whether `population_millions` is between 10 and 100 inclusive.
   Store in `is_medium_sized`. Print.
3. Deliberately trigger a `TypeError`. Read the traceback. Fix.

### Homework — none for this block.
""")

note("🟢 Core solutions", "kept visible for you",
     "Do not project. If a student is stuck, walk over and code with them.")

code("""# Core 1 & 2
name = "Germany"
population_millions = 83.24
member_wto = True
print(name, "has", population_millions, "people. Is it member of the WTO?", member_wto)""")

code("""# Core 3
doc_size = 142
chapter_size = 20
num_chapters = doc_size // chapter_size
pages_left = doc_size % chapter_size
print("Number of chapters:", num_chapters)
print("Pages left:", pages_left)""")

code("""# Core 4
year_signed = 1994
age = 2024 - year_signed
print("Age since signing:", age)""")

code("""# Stretch 1
tariff_rate = 7.5
discount = 0.2
discounted_tariff_rate = tariff_rate * (1 - discount)
print("Discounted tariff rate:", discounted_tariff_rate)""")

code("""# Stretch 2
population_millions = 83.24
is_medium_sized = population_millions > 10 and population_millions < 100
print("Population between 10 and 100 millions:", is_medium_sized)""")

md("---")

# ---------- Strings ----------
md("## Part 4 — String manipulations")

note("🟢 Core", "5 min",
     "Introduce string methods on a deliberately messy filename. "
     "Every method returns a NEW string. The original never changes.",
     confusion="`.strip()` alone does nothing lasting — you must assign the result.")
code('filename = "  Costa Rica - Tariff Schedule FINAL.csv  "\nfilename')
code("filename.strip()")
code("filename.lower()")
code("filename.strip().lower()")
code('filename.replace(" ", "_")')
code('filename.endswith(".csv")')
code('filename.strip().endswith(".csv")')
code("len(filename)")

note("🟢 Core — the point", "2 min",
     "Show that `filename` is unchanged. Then assign the chained result.")
code("filename")
code('cleaned = filename.strip().lower().replace(" ", "_")\ncleaned')

note("🟢 Core", "4 min",
     "Indexing and slicing on a WTO symbol. Positions start at 0. "
     "`[a:b]` is up-to-but-not-including b.",
     confusion="Off-by-one. Students expect [3:6] to include position 6.")
code('symbol = "WT-DS316-AB-R"')
code("symbol[0]")
code("symbol[5]")
code("symbol[3:6]")
code("symbol[-1]")

note("🟢 Core — provoke TypeError", "3 min",
     "Try to assign to a character. Strings are IMMUTABLE. Read the error.",
     error="TypeError: 'str' object does not support item assignment")
code("symbol[3] = 'X'\nsymbol")
code("var = symbol[3]\nvar")
code('symbol = symbol.replace(var, "X")\nsymbol')

md("---")

# ---------- f-strings ----------
md("## Part 5 — f-strings")

note("🟢 Core", "5 min",
     "Show the three ways to build a sentence: commas, +, f-string. "
     "Land firmly on f-strings.",
     confusion="Missing the `f` prefix → `{country}` prints literally.")
code('country = "Kenya"\ntariff_rate = 5.5\nyear = 2024')
code('print("In", year, ",", country, "had a tariff rate of", tariff_rate, "%", ".")')
code('print("In " + str(year) + ", " + country + " had a tariff rate of " + str(tariff_rate) + "%.")')
code('print(f"In {year}, {country} had a tariff rate of {tariff_rate}%.")')

note("🟡 Optional", "2 min",
     "Format specifiers for decimals.")
code("""tariff_rate = 5.12986

print(f"{tariff_rate}")
print(f"{tariff_rate: .2f}")
print(f"{tariff_rate: .4f}")""")

md("---")

# ---------- Lists ----------
md("## Part 6 — Lists")

note("🟢 Core", "3 min",
     "Lists hold anything, in order. `len()` for size. Mixed types allowed "
     "but usually a smell.")
code('my_list = [10, 21, 0.512, "Hello"]\nprint(my_list)\nprint(len(my_list))')

note("🟢 Core", "3 min",
     "Indexing and slicing — same rules as strings. Position 0. Half-open range.")
code("my_list[1]")
code("my_list[0:3]")
code("my_list[:3]")
code("my_list[2:]")
code("""my_short_list = my_list[1:4]
print(my_list)
print(my_short_list)""")

note("🟢 Core", "4 min",
     "Lists ARE mutable, unlike strings. Show append, pop, replace-by-index, "
     "remove, insert.",
     confusion="`pop(3)` uses an INDEX. `remove('France')` uses a VALUE.")
code("my_list = [10, 21, 0.512, 'Hello']\nmy_list")
code('my_list.append("Switzerland")\nmy_list')
code("my_list.pop(3)\nmy_list")
code('my_list[1] = "France"\nmy_list')
code('my_list.remove("France")\nmy_list')
code('my_list.insert(0, "Germany")\nmy_list')

md("---")

# ---------- Sets ----------
md("## Part 7 — Sets (briefly)")

note("🟡 Optional", "2 min",
     "Sets keep only unique values. One-liner to dedupe. Move on.")
code("""tariff_rates = [5.0, 7.5, 5.0, 10.0, 7.5, 5.0]

unique_rates = set(tariff_rates)
unique_rates""")

md("---")

# ---------- Dicts ----------
md("## Part 8 — Dictionaries")

note("🟢 Core", "5 min",
     "Lookup by name instead of position. Introduce with a country record.")
code("""country = {
    "name" : "Kenya",
    "population_millions" : 55.1,
}
country""")
code('country["name"]')

note("🟢 Core", "3 min",
     "Add a key by assignment. Update with `.update({...})`.")
code('country["capital"] = "Nairobi"')
code("country")
code('country.update({"region": "Africa", "wto_member": True})')
code("country")

note("🟢 Core — the workhorse shape", "4 min",
     "List of dicts. This is what real data looks like. "
     "Show two-level indexing: `countries[2][\"name\"]`.")
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

*(10 min in class, rest as homework. Time budget is tight — set them
loose on Core, take questions, wrap the session.)*

### Core

1. Clean `raw = "  KENYA - Tariff Schedule 2024.CSV  "` into
   `"kenya_-_tariff_schedule_2024.csv"` by chaining methods.
2. Build a list `un_founders` (≥ 4 countries). Print first, last, length.
3. From `symbol = "WT-DS316-AB-R"`, slice out `"DS316"`.
4. Make a dict with `name`, `capital`, `population_millions`. Print a
   sentence with an f-string.

### Stretch

1. From `rates = [1.8, 12.0, 13.5, 4.3, 7.5, 9.0, 5.5]`, slice last three
   and middle three.
2. Add `"is_wto_member": True` to your dict, print, then bump population
   by 1.0 and print again.
3. Build a `set` from `rates`. Print how many distinct.

### Homework (optional)

1. From `raw = "population: 55.1 million"`, extract `55.1` as a float
   using slicing.
2. Given a `docs` list of dicts, print the `kind` of the first, the
   `year` of the last, and an f-string identifying the oldest.
""")

note("🟢 Solutions", "kept visible for you", "Do not project.")

code("""# Core 1
raw = "  KENYA - Tariff Schedule 2024.CSV  "
cleaned = raw.strip().lower().replace(" ", "_")
cleaned""")

code("""# Core 2
un_founders = ["United States", "Sowjet Union", "United Kingdom", "France", "China"]
print(un_founders[0])
print(un_founders[-1])
print(len(un_founders))""")

code("""# Core 3
symbol = "WT-DS316-AB-R"
symbol[3:8]""")

code("""# Core 4
d = {"name": "Brazil", "capital": "Brasília", "population_millions": 213}
print(f"{d['name']} has a population of {d['population_millions']} million and its capital is {d['capital']}.")""")

code("""# Stretch 1
rates = [1.8, 12.0, 13.5, 4.3, 7.5, 9.0, 5.5]
print(rates[-3:])
print(rates[2:5])""")

code("""# Stretch 2
d["is_wto_member"] = True
print(d)
d["population_millions"] = d["population_millions"] + 1
print(d)""")

code("""# Stretch 3
distinct_rates = set(rates)
print(len(distinct_rates))""")

code("""# Homework 1
raw = "population: 55.1 million"
str_55 = raw[12:17]
float_55 = float(str_55)
print(float_55)
print(type(float_55))""")

code("""# Homework 2
docs = [
    {"filename": "DS316-AB-R.txt", "year": 2011, "kind": "appellate"},
    {"filename": "DS135-panel.txt", "year": 2001, "kind": "panel"},
    {"filename": "gatt_1994.txt", "year": 1994, "kind": "legal"},
    {"filename": "DS58-shrimp-turtle.txt", "year": 1998, "kind": "appellate"},
]
print(docs[0]["kind"])
print(docs[-1]["year"])
print(f"The oldest of these four documents was signed in {docs[2]['year']}.")""")

md("""---

## End of Session 2

If Core of Block 1 and Block 2 are done, they have every language piece
they need. Session 3 adds control flow, functions, and applies all of it
to a folder on disk.
""")

# ============================================================
# SESSION 3
# ============================================================

md("""# Session 3 — Control flow, functions, and the file organiser (90 min)

Goal: `if` / `for` / `while` / `def`, then use them to organise a messy
folder of WTO documents into tidy subfolders.

**Pace warning.** This session is dense. If you fall behind:
- Drop the rock-paper-scissors game (🟡).
- Drop the dice `while`-loop demo (🟡).
- Never drop the file-organiser capstone start.

**Before class:** run `python setup_sample_data.py` in the terminal so
`sample_data/` exists.

---
""")

# ---------- if ----------
md("## Part 1 — Decisions with `if`")

note("🟢 Core", "3 min",
     "Indentation matters. Four spaces. `if` / `elif` / `else`. "
     "Categorise a tariff rate.",
     confusion="Mixed tabs and spaces → IndentationError. Configure editor to spaces.")
code("""tariff_rate = 7.5

if tariff_rate > 10:
    category = "high"
elif tariff_rate > 5:
    category = "moderate"
else:
    category = "low"

print(category)""")

note("🟡 Optional — rock/paper/scissors", "5 min",
     "Fun demo of chained conditions. Skip if behind schedule.")
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
md("## Part 2 — `for` loops")

note("🟢 Core", "3 min",
     "Walk through a list. Loop variable takes each value in turn.")
code("""countries = ["Switzerland", "USA", "Brazil", "Kenya"]

for country in countries:
    print(f"Country: {country}")""")

note("🟢 Core", "2 min",
     "Counter inside a loop. Foreshadows accumulator pattern used in capstone.")
code("""countries = ["Switzerland", "USA", "Brazil", "Kenya"]

count = 0
for country in countries:
    count = count + 1
    print(f"{count} -> {country}")""")

note("🟢 Core", "2 min",
     "`range(0, 5)` gives 0..4. Half-open again.")
code("for i in range(0, 5):\n    print(i)")

note("🟢 Core", "3 min",
     "`enumerate` when you need both index and item. Cleaner than manual counter.")
code("""countries = ["Switzerland", "USA", "Brazil", "Uganda", "Kenya"]

for index, country in enumerate(countries):
    print(f"{index}: {country}")""")

note("🟢 Core", "3 min",
     "Combine `for` and `if`. Then show `break` (stop at first hit) and "
     "`continue` (skip this item).")
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

note("🟡 Optional", "2 min",
     "Loop over a dict with `.items()`.")
code("""country = {"name": "Kenya", "population_millions": 55.1}

for key, value in country.items():
    print(f"{key} -> {value}")""")

note("🟢 Core — the pattern of the day", "3 min",
     "Loop, decide, accumulate into a new list. This IS the file-organiser "
     "pattern, just with countries instead of files.")
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
md("## Part 3 — `while` loops")

note("🟡 Optional", "2 min",
     "Countdown. Emphasise that the loop variable MUST change or you loop forever.",
     confusion="Forgetting to decrement → infinite loop. Show interrupt button.")
code("""counter = 10
while counter > 0:
    print(counter)
    counter = counter - 1
print("Liftoff!")""")

note("🟡 Optional — dice", "3 min",
     "Nice `while` example: roll until a 6. Unknown number of iterations. Skip if tight.")
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
md("## Part 4 — Functions")

note("🟢 Core", "2 min",
     "`def`, no args, no return. Just packaging a print.")
code("""def greet():
    print(f"Welcome to the course.")

greet()""")

note("🟢 Core", "2 min",
     "Add a parameter. Call twice with different args.")
code("""def greet(name):
    print(f"Welcome to the course, {name}.")

greet("Matteo")
greet("Ana")""")

note("🟢 Core — the key idea", "3 min",
     "`return` hands a value back. Compare to `print`. "
     "A function that only prints is much less useful.",
     confusion="`return` vs `print` — students conflate them for weeks.")
code("""def calculate_sum(a, b):
    sum = a + b
    return sum

calculate_sum(3, 5)""")

note("🟡 Optional — dice function", "3 min",
     "Wrapping the while-loop into a function that takes `sides` as a parameter. "
     "Nice composition example. Skip if very tight.")
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

note("🟢 Core", "3 min",
     "Functions calling functions. Small pieces composed. "
     "This is exactly the shape of the file organiser we'll write in an hour.")
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

*(15 min. Tight. Set them loose, walk the room, debrief briefly.)*

Use throughout:

```python
countries = [
    {"name": "Switzerland", "population_millions": 8.8,   "avg_tariff": 1.8,  "wto_member": True},
    {"name": "Kenya",       "population_millions": 55.1,  "avg_tariff": 12.0, "wto_member": True},
    {"name": "Brazil",      "population_millions": 214.3, "avg_tariff": 13.5, "wto_member": True},
    {"name": "Japan",       "population_millions": 125.7, "avg_tariff": 4.3,  "wto_member": True},
    {"name": "Argentina",   "population_millions": 45.4,  "avg_tariff": 13.6, "wto_member": True},
    {"name": "Iran",        "population_millions": 88.6,  "avg_tariff": 20.1, "wto_member": False},
]
```

### Core

1. Loop and print each name.
2. Loop and print `"<name>: high tariff"` only for `avg_tariff > 10`.
3. Function `is_populous(country, threshold=50)` returning bool. Test twice.
4. Count WTO members with a `for` + `if`. Print the count.

### Stretch

1. Build `wto_only` list with only WTO-member dicts. Print its length.
""")

note("🟢 Solutions", "kept visible for you", "Do not project.")

code("""countries = [
    {"name": "Switzerland", "population_millions": 8.8,   "avg_tariff": 1.8,  "wto_member": True},
    {"name": "Kenya",       "population_millions": 55.1,  "avg_tariff": 12.0, "wto_member": True},
    {"name": "Brazil",      "population_millions": 214.3, "avg_tariff": 13.5, "wto_member": True},
    {"name": "Japan",       "population_millions": 125.7, "avg_tariff": 4.3,  "wto_member": True},
    {"name": "Argentina",   "population_millions": 45.4,  "avg_tariff": 13.6, "wto_member": True},
    {"name": "Iran",        "population_millions": 88.6,  "avg_tariff": 20.1, "wto_member": False},
]""")

code("""# Core 1
for c in countries:
    print(c["name"])""")

code("""# Core 2
for c in countries:
    country_tariff = c["avg_tariff"]
    if country_tariff > 10:
        print(f"{c['name']}: high tariff")""")

code("""# Core 3
def is_populous(contry, threshold=50):
    if contry["population_millions"] > threshold:
        return True
    else:
        return False
print(is_populous(countries[0]))
print(is_populous(countries[2]))""")

code("""# Core 4
wto_member = 0
for country in countries:
    if country["wto_member"] == True:
        wto_member = wto_member + 1
print(wto_member)""")

code("""# Stretch 1
wto_only = []
for country in countries:
    if country["wto_member"] == True:
        wto_only.append(country)
print(len(wto_only))""")

md("---")

# ---------- pathlib ----------
md("""## Part 5 — Exploring a folder with `pathlib`

We're now applying every pattern from the last hour — loops, ifs,
dictionaries, functions — to a real folder on disk. Nothing about the
language is new. Only the objects (`Path`) are.

**Check first:** run the next cell. If it fails, run
`python setup_sample_data.py` in the terminal.
""")

note("🟢 Core — safety check", "1 min",
     "If sample_data/ isn't there, stop and run the setup script in the terminal.",
     error="FileNotFoundError → tells students exactly what to do")
code("""from pathlib import Path

data_dir = Path("sample_data")

if not data_dir.exists():
    raise FileNotFoundError(
        "sample_data/ not found — run 'python setup_sample_data.py' in the terminal, then re-run this cell."
    )

files = list(data_dir.iterdir())
print(f"Found {len(files)} files in {data_dir.resolve()}")""")

note("🟢 Core", "1 min",
     "Peek at the mess so students see why organising is worth doing.")
code("""for f in files[:8]:
    print(f.name)""")

note("🟢 Core", "4 min",
     "A `Path` is an object. The `/` operator joins path parts — no manual "
     "slashes, no OS-specific bugs. Show what a Path knows about itself.",
     confusion="Path is not a string. `.name`, `.stem`, `.suffix` are attributes/props.")
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

note("🟢 Core", "3 min",
     "`iterdir()` gives one Path per entry. Combine with `for` + `if` + counter — "
     "exactly the pattern from Exercise Block 3.")
code("""data_dir = Path("sample_data")

for f in data_dir.iterdir():
    print(f.name)""")
code("""count_csv = 0

for f in data_dir.iterdir():
    if f.suffix == ".csv":
        count_csv = count_csv + 1

print(f"{count_csv} CSV files")""")

note("🟢 Core", "3 min",
     "`.name` is a string — all Session-2 string methods still work. "
     "This is the payoff: yesterday's toys, today's work.")
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

note("🟢 Core — accumulator into dict", "3 min",
     "Counting by category into a dict. THIS is the pattern the capstone needs. "
     "Show both the long form and `.get(key, default)`.")
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

note("🟡 Optional", "1 min",
     "`glob` is a shortcut when you just want a pattern match. Skip if tight.")
code("""csvs = list(data_dir.glob("*.csv"))
print(len(csvs), "CSV files")

for c in csvs:
    print(" ", c.name)""")

md("---")

# ---------- mkdir / shutil / write_text ----------
md("""## Part 6 — Making folders, copying, writing files

Now we change disk. Only ever write into new folders we create ourselves.
Never touch `sample_data/`. If anything breaks, rerun the setup script.
""")

note("🟢 Core", "2 min",
     "`mkdir(parents=True, exist_ok=True)` = safe 'make sure this exists'.",
     confusion="Without `exist_ok=True`, second run raises FileExistsError.")
code("""target = Path("organised") / "appellate_body"
target.mkdir(parents=True, exist_ok=True)

print(target.exists())""")

note("🟢 Core", "2 min",
     "`shutil.copy(src, dst)`. Destination folder must already exist — "
     "that's what mkdir was for.")
code("""import shutil

source = Path("sample_data") / "WT-DS316-AB-R.txt"
destination = Path("organised") / "appellate_body" / source.name

shutil.copy(source, destination)
print(destination.exists())""")

note("🟡 Optional", "2 min",
     "Renaming with `.rename`. Skip unless a student asks.")
code("""old = destination
new = destination.with_name("renamed_example.txt")

old.rename(new)

print("old exists?", old.exists())
print("new exists?", new.exists())""")

note("🟢 Core", "2 min",
     "`write_text` writes a whole string, overwriting. `read_text` reads it back. "
     "This is how the capstone will produce a summary.txt.")
code("""report = Path("organised") / "summary.txt"

report.write_text(
    "Organisation summary\\n"
    "--------------------\\n"
    "Files handled so far: 1\\n"
)

print("wrote", report)""")
code("""content = report.read_text()
print(content)""")

note("🟢 Core — THE moment", "5 min",
     "Everything comes together. A function that classifies a filename. "
     "A loop that classifies, mkdirs, copies. Walk through it slowly. "
     "This is the whole point of the course.",
     confusion="`classify` uses `if / elif` order — first match wins. Order matters.")
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

*(15 min in class to start, finish as homework.)*

**Safety:** only write to new folders (`my_organised/`), never into
`sample_data/`. If anything breaks, rerun the setup script.

### Core (start in class)

1. Create `my_organised/` next to this notebook.
2. Inside it, create `csv_files/` and `txt_files/`.
3. Loop through `sample_data/`. Copy every `.csv` into `csv_files/`,
   every `.txt` into `txt_files/`. Skip everything else.
4. Print how many files ended up in each subfolder using `.iterdir()`
   and a counter.

### Stretch (homework — real summary)

1. Reuse the `classify` function. Sort by all six categories.
2. Keep a running dict `counts` inside the loop.
3. Write `my_organised/summary.txt` with one line per category and a
   `total:` line. Read it back and print.

### Homework (optional — collisions)

1. Handle the two shrimp-turtle duplicates: if a file with the same
   case-number prefix is already in the target folder, append `_dup`
   to the stem instead of overwriting.
2. Add a duplicates section to the summary.
3. Wrap everything in `organise(source_folder, target_folder)` that
   returns the counts dict.

---

## Wrap-up

**Say to the class:** "You've written a script that would take an
afternoon by hand. For 100 files or 10 000 files, it's the same amount
of typing. The pattern — *loop over a folder, decide, act, record* — is
the shape of a huge fraction of research automation. Swap in interview
transcripts, court PDFs, scraped articles: same scaffolding."
""")

note("🟢 Core capstone solution", "kept visible for you",
     "Do not project. If a student is stuck at minute 10, walk over.")
code("""from pathlib import Path
import shutil

data_dir = Path("sample_data")
out = Path("my_organised")

(out / "csv_files").mkdir(parents=True, exist_ok=True)
(out / "txt_files").mkdir(parents=True, exist_ok=True)

for f in data_dir.iterdir():
    if f.suffix == ".csv":
        shutil.copy(f, out / "csv_files" / f.name)
    elif f.suffix == ".txt":
        shutil.copy(f, out / "txt_files" / f.name)

n_csv = 0
for f in (out / "csv_files").iterdir():
    n_csv = n_csv + 1

n_txt = 0
for f in (out / "txt_files").iterdir():
    n_txt = n_txt + 1

print(f"csv_files: {n_csv}")
print(f"txt_files: {n_txt}")""")

md("*End of roadmap.*")

# ============================================================
# WRITE
# ============================================================

nb["cells"] = cells

out = Path(__file__).parent / "course_roadmap.ipynb"
out.parent.mkdir(exist_ok=True)
with open(out, "w", encoding="utf-8") as fh:
    nbf.write(nb, fh)

print(f"Wrote {out} ({len(cells)} cells)")