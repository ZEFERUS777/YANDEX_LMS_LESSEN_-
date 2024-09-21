from collections import Counter
import sys
# Чтение входных данных
initial_word = input().strip()
words = [sys.stdin.readlines()]
words = [words[0][i].strip() for i in range(len(words[0]))]

# Подсчет частоты букв в исходном слове
initial_counter = Counter(initial_word)

# Список для хранения корректных слов
valid_words = []

# Проверка каждого слова
for word in words:
    word_counter = Counter(word)
    if all(word_counter[char] <= initial_counter[char] for char in word_counter):
        valid_words.append(word)

# Вывод результатов
print(len(valid_words))
for valid_word in valid_words:
    print(valid_word)
