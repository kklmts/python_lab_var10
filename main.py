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
    import string
    vowels = tuple("aeiouyаеєиіїоуюя")

    file_in = safe_open_file(input_file, 'r')
    file_out = safe_open_file(output_file, 'w')

    if file_in is not None and file_out is not None:
        for line in file_in:
            words = line.split()
            for word in words:
                clean_word = word.strip(string.punctuation)
                if clean_word and clean_word.lower().startswith(vowels):
                    file_out.write(clean_word + '\n')

        file_in.close()
        file_out.close()
        print("Слова на голосну літеру успішно записано у файл.\n")

def print_file_content(file_name):
    file = safe_open_file(file_name, 'r')
    if file is not None:
        print(f"--- Вміст файлу {file_name} ---")
        for line in file:
            print(line.strip())
        file.close()
        print("---------------------------------\n")

if __name__ == "__main__":
    file1 = "TF13_1.txt"
    file2 = "TF13_2.txt"

    create_initial_file(file1)
    process_vowels(file1, file2)
    print_file_content(file2)