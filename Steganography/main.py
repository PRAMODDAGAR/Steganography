from os import system
from Image.ImageDecode import ImageDecode
from Image.ImageEncode import ImageEncode
system('cls')    

#----------- MENU DRIVER--------------#

while True:
    print("---------------------------------\n          STEGANOGRAPHY\n---------------------------------")
    n=(input("\n1--> Encode Image\n2--> Decode Image\n3--> Exit\n\n\nChoice:-"))
    if(n=='1'):
        ImageEncode()
    elif(n=='2'):
        ImageDecode()
    elif(n==3):
        break
    else:
        print("Invalid input")  
    system('cls')        
    exit()