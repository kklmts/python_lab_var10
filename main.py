import string

def safe_open_file(file_name, mode):
        try:
            file = open(file_name, mode, encoding='utf-8')
        except Exception as e:
            print(f"Помилка: файл {file_name} не вдалося відкрити! Деталі: {e}")
            return None
        else:
            return file

def create_initial_file(file_name):
    # Функція створює файл TF13_1 із символьними рядками різної довжини.
    file = safe_open_file(file_name, 'w')
    file.write("Абрикос, банан, ананас! The apple is green.\n")
    file.write("Fill. Озеро, річка, ліс, океан.\n")
    file.write("123 test. Екран, інтернет, мишка, клавіатура.\n")
    file.close()
    print(f"Файл {file_name} успішно створено.\n")

def process_vowels(input_file, output_file):
    # ЗАВДАННЯ ДЛЯ ОЛІ:
    # Прочитати вміст input_file, розбити на слова.
    # Очистити слова від розділових знаків.
    # Знайти слова, які починаються на голосну літеру, і записати їх у output_file.
    pass

def print_file_content(file_name):
    # ЗАВДАННЯ ДЛЯ КОЛІ:
    # Прочитати вміст file_name і вивести його в консоль по рядках.
    pass

if __name__ == "__main__":
    file1 = "TF13_1.txt"
    file2 = "TF13_2.txt"

    create_initial_file(file1)
    # process_vowels(file1, file2)  # Розкоментувати після виконання Олею
    # print_file_content(file2)     # Розкоментувати після виконання Колею