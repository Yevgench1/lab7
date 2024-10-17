words = []
print("Введіть слова (кожне в окремому рядку). Для завершення введення введіть порожній рядок:")

while True:
    word = input() 
    if word == "": 
        break
    words.append(word)

max_length = max(len(word) for word in words)
aligned_words = ["&" * (max_length - len(word)) + word for word in words]
print("\n Слова після вирівнювання:")
for word in aligned_words:
    print(word)
