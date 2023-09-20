with open("1.txt", encoding='utf-8') as f:
    list_1 = []
    for idx, line in enumerate(f):
        list_1.append({idx + 1:line[:-1]})
    countris_1 = {"1.txt": list_1}


with open("2.txt", encoding='utf-8') as f:
    list_2 = []
    for idx, line in enumerate(f):
        list_2.append({idx + 1: line[:-1]})
    countris_2 = {"2.txt": list_2}

with open("3.txt", encoding='utf-8') as f:
    list_3 = []
    for idx, line in enumerate(f):
        list_3.append({idx + 1: line[:-1]})
    countris_3 = {"3.txt": list_3}


with open("sorted_file.txt", 'w', encoding='cp1251') as f:
    count = 0
    counter = 1
    while count < 3:
        if len(list_1) == counter:
            for key, value in countris_1.items():
                f.write(f"{key}\n{len(list_1)}\n")
                for i in value:
                    for k, v in i.items():
                        f.write(v + "\n")
                f.write(f"\n")
            count += 1
        if len(list_2) == counter:
            for key, value in countris_2.items():
                f.write(f"{key}\n{len(list_2)}\n")
                for i in value:
                    for k, v in i.items():
                        f.write(v + "\n")
                f.write(f"\n")
            count += 1
        if len(list_3) == counter:
            for key, value in countris_3.items():
                f.write(f"{key}\n{len(list_3)}\n")
                for i in value:
                    for k, v in i.items():
                        f.write(v + "\n")
                f.write(f"\n")
            count += 1
        counter += 1

with open("sorted_file.txt") as f:
    for l in f:
        print(l.strip())
