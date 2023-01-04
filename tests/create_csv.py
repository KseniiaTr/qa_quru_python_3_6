#Создание csv файла
import csv


with open('../resources/doc2.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Elena', 'Irina', 'Pavel'])
    csvwriter.writerow(['Alina', 'Kristina', 'Anna'])
