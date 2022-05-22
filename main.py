import os

def main():
    directory = input ("Please enter the directory that you want to save the file: ")
    filename = input ("Please enter the filename : ")
    name = input ("Please enter your name : ")
    address =input("Please enter your address : ")
    phone_number = input("Please enter your mobile phone number : ")
    #checking if the directory exists
    if os.path.isdir(directory):
        #creating and opening the file to write
        writeFile=open(os.path.join(directory,filename),'W')
        #writing the data by comma seperated
        writeFile.write(name+''+address+''+phone_number+'\n')
        #close the file after writing is done
        writeFile.close ()

        print("File contents:")
        #reading the file for proof of storing
        readFile=open(os.path.join(directory,filename),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry this directory does not exist...")
main()