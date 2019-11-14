#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:29:04 2019

@author: jonathanbrooks
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:15:26 2019

@author: jonathanbrooks
"""
#we do not need to open the csv until the data is complete 
import os
import csv
import xml.etree.ElementTree as et


HEAD = ['FULL_NAME','BIRTH_DATE','VISIT_DATE','IMAGE_FILE_NAME','X','Y','Result']

STAGS = {'LAST_NAME','FIRST_NAME','BIRTH_DATE','GENDER','VISIT_DATE','IMAGE_FILE_NAME','DATE_TIME','SITE','NUM_THRESHOLD_POINTS','THRESHOLD_1','X','Y','Result_1'}

directory = os.getcwd()

def xml_parse(root):
    for i in root.iter():
        if (i.tag == 'FULL_NAME'):
            FULL_NAME = i.text
        elif (i.tag == 'VISIT_DATE'):
            VISIT_DATE = i.text
        elif (i.tag == 'BIRTH_DATE'):
            BIRTH_DATE = i.text
        elif (i.tag == 'IMAGE_FILE_NAME'):
            EYE = i.text
    my_dict = {}
    my_dict_list = []
   
    for e in root.findall('.//THRESHOLD_XY_LOCATION'):
       my_dict = {FULL_NAME: [BIRTH_DATE,VISIT_DATE,EYE,e.find('X').text,e.find('Y').text,e.find('RESULT_1').text]}
       my_dict_list.append(my_dict)
    print(my_dict_list)
    
    def write_to_csv(my_dict_list):
        with open('../54point.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter='\n')
            writer.writerow(my_dict_list)

    write_to_csv(my_dict_list)  


for root,dirs,files in os.walk(directory):
    for i in files:
            if (i.endswith('.xml')):
                fullname = os.path.join(root,i)
                tree = et.parse(fullname)
                rooty = tree.getroot()
                xml_parse(rooty)

                
     



