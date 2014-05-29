import os
import pprint
import string
###
# fonction createDir : prends le nom du repertoire
# crée le repertoire dans le bureau
###
def createDir(path,dirName):
        try:
                fullPath = os.path.join(path,dirName);
                os.mkdir(fullPath);
		#pprint.pprint(fullPath);
                finalPath = createKey(fullPath);
                print("Dossier ",dirName," crée avec succès !");
                return finalPath
		
        except OSError:
                pass
        

def choosePath():
        print("1- Bureau\n");
        print("2- Dropbox\n");
        print("3- Documents\n");

        id = input()
        return id
        
def registerPath():
        id = choosePath();
        if(id=="1"):
                print("Bureau");
                path = "C:\\Users\\"+userName+"\\Desktop\\";
                
        elif(id=="2"):
                print("Dropbox");
                path = "C:\\Users\\",userName,"\\Dropbox\\";
                
        elif(id=="3"):
                print("Documents");
                path = "C:\\Users\\",userName,"\Documents\\";
        else:
                print("Path erroné");
                path = null;
       
        return  path

def createFile(fullPath,fileName,ext):
        try:
                open(fullPath+'\\'+fileName+'.'+ext,'w');
        except:
                pass

def createKey(fullPath):
        try:
                createFile(fullPath,'\\'+userName+'_encryptData','txt');
                
                #open(fullPath+'\\'+userName+'_encryptData.txt','w');
        except:
                pass
        return fullPath+'\\'+userName+'_encryptData.txt'

def getUser():
        global userName
        userName = os.getlogin();
        print("User courant: ",userName);
        return userName;

def readFile(fullPath):
        file =open(fullPath,'r')
        string = file.read()
        file.close()
        return string

def editFile(fullPath,string):
        file=open(fullPath,'w')
        file.write(string)
        file.close()
        #print("Succès!")

def listToString(data):
        string =""
        for i in range(0,len(data)):
                string= string+str(data[i])+"./"
        return string

def stringToIntList(string):
        data = []
        data = string.split('./')
        data.pop()
        for i in range(0,len(data)):
                data[i]=int(data[i])
                
        return data
        

        
        
        
