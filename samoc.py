# import csv

# nombrearchivo = 'example3.csv'
# # archivo = open("example2.csv", 'r')
# archivo = "example2.csv"
# # nuevo = open(nombrearchivo, 'w')
# nuevo = open(nombrearchivo,'w',encoding='utf-8')


# with open(archivo, newline='\n') as File:  
#     reader = csv.reader(File)
#     for row in reader:
#         # row = row+",,,"
#         print(row[len(row)-1])
#         # row[len(row)-1] = row[len(row)-1]+",,,"
#         # print(row[len(row)-1])
#         # arreglo = []
#         # arreglo.append(row)
#         # writer = csv.writer(nuevo)
#         # writer.writerows(arreglo)
nombrearchivo = 'nuevo.txt'
archivo = open(nombrearchivo, 'r')

# nuevo = open("example3.txt", 'w')


# for linea in archivo.readlines():
linea = archivo.read()
print(linea)
    #  nuevo.write(linea)

# archivo.close() 
# nuevo.close()