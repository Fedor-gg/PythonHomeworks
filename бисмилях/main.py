def analyze_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        lines = content.splitlines()
        num_lines = len(lines)
        words = sum(len(line.split()) for line in lines if line.strip())
        chars = len(content)
        empty_lines = sum(1 for line in lines if not line.strip())
        print(f'Количество строк: {num_lines}')
        print(f'Количество слов: {words}')
        print(f'Количество символов (включая пробелы): {chars}')
        print(f'Количество пустых строк: {empty_lines}')
    except FileNotFoundError:
        print('Файл не найден, попробуйте снова.')
    except PermissionError:
        print('Ошибка доступа к файлу. Проверьте права на чтение.')
    except Exception as e:
        print(f'Возникла ошибка: {e}')
file_name = input("Введите имя файла: ")
analyze_file(file_name)