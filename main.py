import re
from bloom_filter import BloomFilter

# Считываем текст из файла
text = open("text", "r", encoding="UTF-8").read()

# Нормальная форма: приводим к нижнему регистру, убираем знаки препинания
WORDS_REGEX = "[^а-яё]+"
unique_words = list(set([word.lower() for word in re.split(WORDS_REGEX, text, flags=re.IGNORECASE) if len(word) != 0]))

# Определяем параметры для блум фильтра
p = 0.2
n = len(unique_words)

# создаем блум фильтр
bloom_filter = BloomFilter(max_elements=n, error_rate=p)

# заполняем его нашими словами
for word in unique_words:
    bloom_filter.add(word)


# Тестируем наличие различных слов в блум фильтре
print("вино" in bloom_filter)  # Слово есть в тексте
print("автобус" in bloom_filter)  # Слова нет в тексте
print("люб" in bloom_filter)  # Ложноположительное срабатывание

# Тут можно проверить наличие слова в блум фильтре самостоятельно
if __name__ == "__main__":
    in_word = ""
    while in_word != "exit":
        in_word = input()
        print(in_word in bloom_filter)
