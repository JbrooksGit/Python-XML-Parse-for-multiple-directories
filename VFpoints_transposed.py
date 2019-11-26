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

def write_to_csv(my_dict):
    with open('../54point.csv', 'a') as csvfile:
        wr = csv.writer(csvfile)
        wr.writerow(my_dict)

def xml_parse(root):
    FULL_NAME = 'FULL_NAME' in locals() or 'FULL_NAME' in globals()
    for i in root.iter():
        if (i.tag == 'FULL_NAME'):
            FULL_NAME = i.text.replace(",",";")
        elif (i.tag == 'VISIT_DATE'):
            VISIT_DATE = i.text
        elif (i.tag == 'BIRTH_DATE'):
            BIRTH_DATE = i.text
        elif (i.tag == 'IMAGE_FILE_NAME'):
            EYE = i.text
    
    
    if(FULL_NAME):
        my_dict = [FULL_NAME,BIRTH_DATE,VISIT_DATE,EYE]
        for e in root.findall('.//THRESHOLD_XY_LOCATION'):
            my_dict.append(e.find('THRESHOLD_1').text)                
        print(my_dict)
        write_to_csv(my_dict)
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

                
     



