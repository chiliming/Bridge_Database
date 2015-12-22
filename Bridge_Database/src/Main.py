# -*- coding: utf-8 -*-
'''
Created on 2015年12月22日

@author: "Kael.Chi"
'''
from FileOperate import FileOperate
import os
from bs4 import BeautifulSoup


if __name__ == "__main__":
    code = 'utf-16'
    base_dir = os.getcwd()
    input_dir  = os.path.dirname(base_dir) + "/External_File/Input_Files/"
    content_temp_0 = []
    #content_temp_1 = []
    pass


#Get list of input file names.
file_list = os.listdir(input_dir)
print file_list

#Handle input files.
fhand01 = FileOperate()
for name in file_list:
    content_temp_0 =fhand01.HandleInputFile(name, code)
    content_temp_1 = ''.join(content_temp_0)
    soup = BeautifulSoup(content_temp_1, "html.parser")
    #content_temp_1.append(content_temp_0)
    title = soup.find_all('td', align = 'center')
    for item in title:
        print item.text