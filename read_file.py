#Otwieranie pliku
filepath = "dane.txt"
file = open(filepath, "r")

#Wczytywanie danych
num_ver = int(file.readline())
cost_list = []

for i in range(num_ver):
    distance = [int(x) for x in file.readline().split()]
    cost_list.append(distance)

#Zamykanie pliku
file.close()