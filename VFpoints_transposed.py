#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:29:04 2019

@author: jonathanbrooks
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#This version works but skips lines in the csv
"""
Created on Wed Nov 13 12:15:26 2019

@author: jonathanbrooks
"""
#we do not need to open the csv until the data is complete 
import os
import csv
import xml.etree.ElementTree as et


HEAD = ['FULL_NAME','BIRTH_DATE','VISIT_DATE','IMAGE_FILE_NAME','X','Y','Result']

directory = os.getcwd() #assigns directory to the file path of this python file

#had
def write_to_csv(my_dict):
    print(len(my_dict))
    if(len(my_dict)) < 2:
        print('blank_list')
    else:
        with open('../54point.csv', 'a',newline = '') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(my_dict)

def xml_parse(root):
    FULL_NAME = 'FULL_NAME' in locals() or 'FULL_NAME' in globals()
    FPP = 'FALSE_POSITIVE_PERCENT' in locals() or 'FALSE_POSITIVE_PERCENT' in globals()
    FNP = 'FALSE_NEGATIVE_PERCENT' in locals() or 'FALSE_NEGATIVE_PERCENT' in globals()
    ERRORS = 'ERRORS' in locals() or 'ERRORS' in globals()
    TRIALS = 'TRIALS' in locals() or 'TRIALS' in globals()
    #If someone is missing any of these variables, there scan is excluded
    for i in root.iter():
        if (i.tag == 'FULL_NAME'):
            FULL_NAME = i.text.replace(",",";")
        elif(i.tag == 'VISIT_DATE'):
            VISIT_DATE = i.text
        elif(i.tag == 'BIRTH_DATE'):
            BIRTH_DATE = i.text
        elif(i.tag == 'IMAGE_FILE_NAME'):
            EYE = i.text
        elif(i.tag == 'FALSE_POSITIVE_PERCENT'):
            FPP = i.text
            print(FPP)
            FPP = f"{FPP}%" 
        elif(i.tag == 'FALSE_NEGATIVE_PERCENT'):
            FNP = i.text
            print(FNP)
            FNP = f"{FNP}%"
        elif(i.tag == 'ERRORS'):
            ERRORS = i.text
        elif(i.tag == 'TRIALS'):
            TRIALS = i.text
    
    
    if(FULL_NAME):
        my_dict = [FULL_NAME,BIRTH_DATE,VISIT_DATE,EYE]
        for e in root.findall('.//THRESHOLD_XY_LOCATION'):
            my_dict.append(e.find('THRESHOLD_1').text) 
        if(FPP and FNP and ERRORS and TRIALS):
            FL = f"{ERRORS}/{TRIALS}"
            my_dict.append(FPP)
            my_dict.append(FNP)
            my_dict.append(ERRORS)
            my_dict.append(TRIALS)
            write_to_csv(my_dict)
            
        elif(not FPP and not FNP and not ERRORS and not TRIALS):
            print('world')
        print(my_dict)
    elif(not FULL_NAME):
        print('hello')

for root,dirs,files in os.walk(directory):
    for i in files:
            if (i.endswith('.xml')):
                fullname = os.path.join(root,i)
                print(fullname)
                tree = et.parse(fullname)
                rooty = tree.getroot()
                xml_parse(rooty)

                
     



