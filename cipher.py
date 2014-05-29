import math
import random
import os


def generateVector():
    global v
    u = [random.randint(2,999),random.randint(2,999)]
    v =[u[0]*u[0],u[0]*u[1],u[0]*u[0]+u[1]]
    return v


def encodeData(data):
    vector = generateVector()
    strDic = []
    for i in range(0,(len(data))):
        strDic.append(vector[2]*(ord(data[i])))
    strDic.insert(0,vector[0])
    strDic.append(vector[1])
    print("Encodage Successfull")
    return strDic

def decodeData(data):
    v1 = data[0]
    v2 = data[-1]
 
    x= math.sqrt(v1)
    x =int(x)
    
    y= v2/x
    y=int(y)
    
    solution=[]
    for i in range(1,len(data)):
        var = data[i]/(x*x+y)
        var = int(var)
        solution.append(chr(var))
             
    finalString =''.join(solution)
    return finalString


############################################
##print("Donnez un message à encrypter...")
##string = input()
##encodedData =encodeData(string)
##print("Encoded",encodedData)
##print("Decoded -->",decodeData(encodedData))
##       
    
