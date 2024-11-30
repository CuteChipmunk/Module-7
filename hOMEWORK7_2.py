def custom_write(file_name: str, strings: list):
    n = 1
    st = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        line_byte = file.tell()
        file.write(f'{i}\n')
        st[(n, line_byte)] = i
        n += 1
    file.close()
    return st

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)