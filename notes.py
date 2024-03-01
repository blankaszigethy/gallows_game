# 1. Megszámolni hány betűből áll a mondat, kiírni.
# 2. A választott betűnek a helyének megkeresése.(hanyadik helyen áll a mondatban)
# 3. Kötőjelekkel szimbolizálni a foglalt és a szabad betűk helyét.


def create_placeholder(sentence):
  placeholder = ""

  i = 0

  while i < len(sentence):

      if sentence[i] == " ":
          placeholder +=  " "   # += hozzáad a strighez új karaktereket
      else:
          placeholder += "_"
      i = i + 1

  return placeholder


def fill_with_correct_letters(sentence, placeholder, correct_letters):

  for letter in correct_letters:
      i = 0
      while i < len(sentence):
        if letter.lower() == sentence[i].lower():
          placeholder = placeholder[:i] + sentence[i] + placeholder[i + 1:]

        i = i + 1
  return placeholder


def get_character_indexes(sentence, letter):

  indexes = []


  i = 0
  n = len(sentence)

  while i < n:
      character = sentence[i]

      if letter.lower() == character.lower():
          indexes.append(i)
          
      i += 1


  if len(indexes) > 0:
      print("van benne")
  else:
      print("nincs benne")

  return indexes


# INVOKE FUNCTIONS


SENTENCE = "Ez egy teszt feladat"

p = create_placeholder(SENTENCE)
print(p)

f = fill_with_correct_letters(SENTENCE, p, ["e", "t"])
print(f)



# irj fuggvenyt, ami megmondja, hogy a fill_with_correct_letters fuggveny visszatérési erteke es a 
# SENTENCE konstans ekvivalens-e es ha igen, adrjon vissza true-t, ha nem, false-ot



letter = input("Enter a letter: ")

indexes = get_character_indexes(SENTENCE, letter)

print(indexes)

