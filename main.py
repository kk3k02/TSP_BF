import readFile
import tsp

#Ścieżka do pliku z danymi
filePath = "dane.txt"

def main():
    #Wczytanie macierzy sąsiedztwa
    file = readFile.ReadFile(filePath)
    data = file.readData()

    #Wykonanie algorytmu
    algorithm = tsp.Tsp(file.num_ver, data)
    path, distance = algorithm.start()

    #Wydrukowanie wyniku
    print("Najlepsza trasa:", path)
    print("Minimalna odległość:", distance)

#Start programu
if __name__ == "__main__":
    main()