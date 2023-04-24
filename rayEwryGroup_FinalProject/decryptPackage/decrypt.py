#decrypt.py


#Name: Ray Ewry Group - Graham Davis, Catherine Dimbath, Ryan O'Connor, Erin Herlily
#email: davisgh@mail.uc.edu, dimbatcs@mail.uc.edu, oconnorp@mail.uc.edu, herlihej@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can pull data from a json and use it to decrypt a txt file and load an image
#Citations:

#https://www.w3schools.com/python/python_while_loops.asp

#https://note.nkmk.me/en/python-function-return-multiple-values/

#https://www.datacamp.com/tutorial/python-time-sleep?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720830&utm_adgroupid=143216588377&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=655068781152&utm_targetid=dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=9015712&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-us_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-aprfs23&gclid=CjwKCAjw0ZiiBhBKEiwA4PT9z5GKV6HFVWo18U5fLsgSqIlfOmDF5spmNVWXlZ4imE0oXwvkIGx1NBoConsQAvD_BwE

#https://chat.openai.com/

#https://www.askpython.com/python/examples/rotate-an-image-by-an-angle-in-python

#Anything else that's relevant:


import json
import time
from PIL import Image
import random
    
    
    
def ewryVerification():
    print ("User: Ray Ewry")
    print("Hint -- The Password is 'password'")
    time.sleep(1)
    print("Password: ")
    
    while True:
        
        answer = input(">")
        if answer == "password":
            print("-------Loading---------")
            time.sleep(2)
            print("")
            print("")
            print("Welcome Ray. Your encryption key is:")
            print("")
            print("_____________________")
            verifCode = str(random.randint(1000, 9999))
            print("DeerLiveStream" + verifCode)
            print("_____________________")
            time.sleep(2)
            
            return (True, verifCode)
        else:
            print("")
            print("")
            print("!!!!!!!!Invalid Password. Please Re-enter!!!!!!!!!!!!!")
            print("")
            print("")
            pass

def pullEncryptedData(name):
    if name == "Ray":
        with open('EncryptedGroupHints Spring 2023 Section 001.json', 'r') as file:
            json_data = file.read()
            data = json.loads(json_data)
            encrypted_data = (data['Ray Ewry'])  
            return encrypted_data 

def decryptor(verifCode):
    time.sleep(1)
    print("~~Loading FERPA Decryptor v182.1~~")
    time.sleep(1)
    print("~")
    time.sleep(1)
    print("~")
    while True:
        print("Enter Decryption Key:")
        key = input(">")
        if key == ("DeerLiveStream" + verifCode):
            with open('english-2.txt', 'r') as f:
                lines = f.readlines()
                unformatted = pullEncryptedData("Ray")
                
                txt_lines = []
                for line_number in unformatted:
                    txt_lines.append(lines[int(line_number) - 1])
                
                list_of_words = txt_lines
                
                sentence = ' '.join(list_of_words).replace('\n', '')
                
                time.sleep(1)
                print("")
                print("")
                print("Your Secret Location is:")
                print("_____________________")
                print(sentence)
                print("_____________________")
                print("Be Safe Ray. Program Self-Destructing.")
                break
        else:
            print("~~~~~~~~~")
            print("Invalid Key. Please Re-enter.")
            print("~~~~~~~~~")
            pass
    
        
    

 
def imageVerification():
    
    
    print ("Enter Image Viewing Password")
    print("Hint -- The Password is 'password'")
    time.sleep(1)
    print("Password: ")
    
    while True:
        answer = input(">")
        if answer == "password":
            print("___________________________________________")
            print("Program Will Terminate On Image Load.")
            print("Loading Image...")
            return True
        else:
            print("Invalid Password. Try Again.")
            pass
        
    
    

def showImage():
    img = Image.open('HappyStudents.jpg')
    rotated_img = img.rotate(-90)
    rotated_img.show()


    
        
        
        
        