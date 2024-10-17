sentence = input("Введіть рядок слів, розділених пробілами: ")
words = sentence.split()
def count_a(word):
    return word.lower().count('а') 
max_word = max(words, key=count_a)
print(f"Слово з найбільшою кількістю літер 'а': {max_word}")