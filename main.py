import readFile
import tsp
import timeStamp

#Ścieżka do pliku z danymi
filePath = "dane.txt"
time = timeStamp.TimeStamp()

def main():
    #Wczytanie macierzy sąsiedztwa
    file = readFile.ReadFile(filePath)
    data = file.readData()

    #Wykonanie algorytmu
    algorithm = tsp.Tsp(file.num_ver, data)
    time.start()
    path, distance = algorithm.start()
    exec_time = time.end()

    #Wydrukowanie wyniku
    print("Najlepsza trasa:", path)
    print("Minimalna odległość:", distance)
    print("Czas wykonywania:", exec_time)

#Start programu
if __name__ == "__main__":
    main()