#Создание zip-архива

from zipfile import ZipFile


with ZipFile('../hw_archive.zip', 'w') as myzip:
    myzip.write('resources/exmpl.pdf')
    myzip.write('resources/doc2.csv')
    myzip.write('resources/testdoc1.xlsx')





