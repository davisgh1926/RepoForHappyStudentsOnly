#main.py

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

from decryptPackage.decrypt import *


print("Welcome. Do you want to display secret photo or decrypt?")
print("To Display Photo, Enter '1'")
print("To Decrypt, Enter '2'")

while True:

    answer1 = input(">")
    if answer1 == "1":
        verify = False
        if verify == False:
            verify = imageVerification()
        if verify == True:
            showImage()
            break
        
        
    elif answer1 == "2":
        startEncryption = False
    
        if startEncryption == False:
            result, code = ewryVerification()
            
        
        if result == True:
            decryptor(code)
            break
            
            
    
    else:
        print("Invalid Response. Try Again.")
        pass
    
    







