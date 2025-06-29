"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Jordán
email: danieljordan445@gmail.com
"""
# Texty
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Registrovaní uživatelé
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

# Ověření uživatele
if username not in users:
    print("This user is not registered.")
    exit()
elif users[username] != password:
    print("Incorrect password.")
    exit()
else:
    print("-" * 40)
    print(f"Welcome to the app, {username}.")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-" * 40)

# Výběr textu
selection = input("Enter a number between 1 and 3 to select: ")
try:
    selection = int(selection)
    if not 1 <= selection <= len(TEXTS):
        print("Selected number is out of range.")
        exit()
except ValueError:
    print("Invalid input! Please enter a number between 1 and 3.")
    exit()

# Získání vybraného textu
text = TEXTS[selection - 1]
words = text.split()

# Úprava pro korektní počty a délky slov
cleaned_words = [word.strip('.,!?;:"\'()[]{}') for word in words]

# Celkový počet slov
word_count = len(cleaned_words)

# Projdi každé slovo w v seznamu a pokud podmínka platí, přidej jedničku do součtu

# Počet slov začínajících velkým písmenem
titlecase_count = sum(1 for w in cleaned_words if w.istitle())
# Počet slov psaných velkými písmeny
uppercase_count = sum(1 for w in cleaned_words if w.isupper() and w.isalpha())
# Počet slov psaných malými písmeny,
lowercase_count = sum(1 for w in cleaned_words if w.islower())
# Počet čísel (ne cifer)
count = sum(1 for w in cleaned_words if w.isdigit())
# Sumu všech čísel (ne cifer) v textu
sum_of_numbers = sum(int(w) for w in cleaned_words if w.isdigit())

# Výstup
print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {count} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}")
print("-" * 40)

# Sloupcový graf
lengths = {}
for word in cleaned_words:
    l = len(word)
    lengths[l] = lengths.get(l, 0) + 1

print("LEN|  OCCURENCES        |NR.")
print("-" * 40)
for length in sorted(lengths):
    stars = '*' * lengths[length]
    print(f"{length:>3}|{stars:<20}|{lengths[length]}")
<<<<<<< HEAD
    
=======
    
>>>>>>> 2694fa990135becd04cda83d1bf934eb21c8656d
