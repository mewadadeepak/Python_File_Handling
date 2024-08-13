'''
f = open("Demo.txt", "a")
print(f)                    '''
import os.path

'''
f = open("Demo.txt", "r")
print(f.read())                '''

'''
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.txt", "r")
print(f.read())                                                         '''

'''
#Return the 5 first characters of the file:
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.txt", "r")
print(f.read(5))                                                  '''

'''
#Return the 3 first characters of the file:
f = open("Demo.txt", "r")
print(f.read(3))                                        '''

'''
#Read one line of the file:
f = open("Demo.txt", "r")
print(f.readline())                '''

'''
#Read one line of the file:
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.txt", "r")
print(f.readline())                                 '''

'''
#Read two lines of the file:
f = open("Demo.txt", "r")
print(f.readline())
print(f.readline())                '''

'''
#Read two lines of the file:
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.txt", "r")
print(f.readline())
print(f.readline())                        '''

'''
#Read first 5 charecters of both two lines of the file:
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.txt", "r")
print(f.readline(5))
print(f.readline(5))                    '''


'''
#Loop through the file line by line:
f = open("Demo.txt", "r")
for x in f:
  print(x)             '''

'''
#Loop through the file line by line:
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.cpp", "r")
for x in f:
  print(x)                                   '''

'''
#CloseFiles:  Close the file when you are finish with it:
f = open("Demo.txt", "r")
print(f.readline())
f.close()                         '''

'''
#CloseFiles:  Close the file when you are finish with it:
f = open("C:\\Users\Deepak Mewada\Desktop\ATM_Machine.cpp", "r")
print(f.readline())
f.close()                            '''

''' 
#CloseFiles:  Close the file when you are finish with it:
f = open("Demo.txt", "r")
print(f.read())
f.close()                   '''

'''
#CloseFiles:  Close the file when you are finish with it(Reading for first 5 charecters:
f = open("Demo.txt", "r")
print(f.readline(5))
f.close()                      '''


'''
#Python File Write: Write to an Existing File
f = open("Demo.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("Demo.txt", "r")
print(f.read())                       '''

'''
#Python File Write: Write to an Existing File
f = open("Demo2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("Demo2.txt", "r")
print(f.read())                         '''

'''
#Open the file "Demo3.txt" and overwrite the content:
f = open("Demo3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("Demo3.txt", "r")
print(f.read())                    '''

'''
#Create a New File: Create a file called "myfile.txt":
#Python File Write: Write to an Existing File
f = open("myfile.txt", "x")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())                          '''

'''
#Python Delete File:Delete a File-:  Remove the file "deleee.txt"(make sure import "os module"):
import os
os.remove("deleee.txt")          '''

'''
#check if file exist than delete it.
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("the file does not exist") #o/p: the file does not exist     '''


'''
#Result: Code if file exist than delete it.
#check if file exist than delete it.
import os
if os.path.exists("exist.txt"):
   os.remove("exist.txt")
else:
   print("the file does not exist")           
     
                                         '''

#Remove the folder "myfolder":
import os
os.rmdir("New folder")   










