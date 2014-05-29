# -*-coding:Latin-1 -*
import os
from mainFunctions import *
from cipher import *
import pprint
#pprint.pprint(globals())
#pprint.pprint(locals())


#Debut du programme
getUser();
print("Choississez votre emplacement...");
path = registerPath();

print("Donnez le nom de votre repertoire...");
dirName=input();
##########################
### Creation Dir + key ###
##########################
finalPath=createDir(path,dirName);

print("Quel est le texte à encrypter ?...")
data = input();

encoded= encodeData(data)
encodedDataInString = listToString(encoded)
editFile(finalPath,encodedDataInString)

##newList = []
##newList = stringToIntList(encodedDataInString)
##
##decodedData = decodeData(newList)
##print(decodedData)
os.system("pause")
