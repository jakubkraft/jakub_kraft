import re

class TextAnalyzer:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.text = re.sub(r'[^A-Ža-ž0-9 ,.?!;]', '', file.read())

    def count_characters(self, include_spaces=True):
        if include_spaces:
            return len(self.text)
        else:
            return len(self.text.replace(' ', ''))

    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_sentences(self):
        sentences = re.split(r'[.?!]', self.text)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)

    def write_statistics(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Celkový počet znaků (včetně mezer): {self.count_characters(include_spaces=True)}\n")
            file.write(f"Celkový počet znaků (bez mezer): {self.count_characters(include_spaces=False)}\n")
            file.write(f"Počet slov: {self.count_words()}\n")
            file.write(f"Počet vět: {self.count_sentences()}\n")


input_file = 'C:\\Users\\Jakub\\Desktop\\2. Mgr\\Úvod do programování\\Text.txt'
# Zde napište přesné umístění textového souboru, který má program analyzovat
output_file = 'C:\\Users\\Jakub\\Desktop\\2. Mgr\\Úvod do programování\\Text_counter.txt'
# Zde napište přesné umístění, kde má být textový soubor s výsledky uložen

analyzer = TextAnalyzer(input_file)
analyzer.write_statistics(output_file)
