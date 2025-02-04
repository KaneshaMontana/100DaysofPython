vowel = ["A","E","I", "O", "U"]
name = input("Enter your name into the vowel muncher: ").upper()
word_without_vowels = ""

for letter in name:
    if letter in vowel:
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)