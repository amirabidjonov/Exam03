def data_file():

    with open("data.txt", "r") as f:
        for line in f:
            print(line.strip())

if data_file() != ' ':
    print(data_file())
else:
    print("fayl topilmadi!")