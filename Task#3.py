# coding = utf-8
text = {}


def open_file(names):
    """Функция открывает файл и создание словарь"""
    for name in names:
        with open(name, encoding='utf-8') as f:
            line = []
            for l in f:
                line.append(l)
            text[len(line)] = {name: line}


def writ_file(text):
    """Функция сортирует словарь и записывает в файл sorted_file"""
    with open("sorted_file.txt", 'w', encoding='cp1251') as f:
        sorted_text = (sorted(text.items()))
        for i in sorted_text:
            for key, val in i[1].items():
                f.write(f"{key}\n{i[0]}\n")
                for a in val:
                    f.write(f"{a}")
                f.write(f"\n")
            f.write(f"\n")


open_file(["1.txt", "2.txt", "3.txt"])
writ_file(text)
