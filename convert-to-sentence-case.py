string = "hey i am rounak. i am a gen ai developer"
corrected = ""
for sentence in string.split(". "):
    words = sentence.split()
    for j, word in enumerate(words):
        if len(word) == 1 and word == "i":
            words[j] = word.upper()
        elif j == 0:
            words[j] = word[0].upper() + word[1:]
        else:
            words[j] = word.lower()
    corrected += " ".join(words) + ". "

print(corrected)