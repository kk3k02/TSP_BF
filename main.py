import readFile

#Ścieżka do pliku z danymi
filePath = "dane.txt"

def main():
    #Wczytanie macierzy sąsiedztwa
    file = readFile.ReadFile(filePath)
    data = file.readData()
    print(data)

#Start programu
if __name__ == "__main__":
    main()