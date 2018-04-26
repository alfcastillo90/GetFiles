import os
import shutil

global txt

balance = "C:/lesskomplex/GetFilesApp/BALANCE"
rent = "C:/lesskomplex/GetFilesApp/RENTA"
emptied = "C:/lesskomplex/GetFilesApp/VACIADO"
xlsx = "C:/lesskomplex/GetFilesApp/archivos excel"
textFile = "C:/lesskomplex/GetFilesApp/otros.txt"
mainFolder = "C:/lesskomplex/GetFilesApp/data/"

dirs = os.listdir( mainFolder )

if not os.path.exists(balance):
    os.makedirs(balance)
if not os.path.exists(emptied):
    os.makedirs(emptied)
if not os.path.exists(rent):
    os.makedirs(rent)
if not os.path.exists(xlsx):
    os.makedirs(xlsx)

if not os.path.exists(textFile):
    txt = open("C:/lesskomplex/GetFilesApp/otros.txt","w")


for subdir in dirs:
    subdirPath = mainFolder+subdir
    files = os.listdir(mainFolder+subdir)
    for file in files:
        filePath = subdirPath+'/'+file
        #coloco .lower() porque hay archivos con extension pdf en mayusculas y en minisculas, entonces para evitarme problemas, pongo el nombre completo del archivo en minusculas
        if ".pdf" in file.lower():
            if "BALANCE" in file:
                shutil.move(filePath,balance+'/'+file)
            if "RENTA" in file:
                shutil.move(filePath,rent+'/'+file)
            if "VACIADO" in file:
                shutil.move(filePath,emptied+'/'+file)            
        elif ".xls" in file.lower():
            shutil.move(filePath,xlsx+'/'+file)
        else:
            txt = open("C:/lesskomplex/GetFilesApp/otros.txt","a+")
            txt.write(file+'\n')
            print(file)
                