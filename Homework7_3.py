import string

class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = []
        with open(self.file_name, encoding='utf-8') as file:
            for line in file:
                line = line.lower()  # Приводим всю строку к нижнему регистру
                line = line.translate(str.maketrans("", "", string.punctuation))  # Удаляем знаки препинания
                all_words.extend(line.split())  # Разбиваем строку на слова и добавляем в список
        return all_words

    def find(self, word):
        word = word.lower()
        if word in self.all_words:
            index = self.all_words.index(word) + 1  # Индекс + 1 для счета со второго слова
            return {self.file_name: index}
        return {self.file_name: None}  # Если слово не найдено

    def count(self, word):
        word = word.lower()
        count = self.all_words.count(word)
        return {self.file_name: count}

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('grace'))      # Индекс первого вхождения слова 'grace'
print(finder2.count('SabbaTh'))     # Количество вхождений слова 'SabbaTh'