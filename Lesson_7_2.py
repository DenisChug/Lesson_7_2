def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding = 'utf-8')
    for line in strings:
        count = file.tell()
        file.write(line + '\n')
        strings_positions[(len(strings_positions) + 1, count)] = line
        rez = strings_positions
    file.close()
    return rez



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)