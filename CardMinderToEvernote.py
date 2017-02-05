#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2017 Osamu Kuniyasu
# Released under the MIT license
# http://opensource.org/licenses/mit-license.php

import os
import datetime
import shutil
import sqlite3
from PyPDF2 import PdfFileWriter, PdfFileReader

d = datetime.datetime.today()
today = d.strftime("%Y%m%d")
source_directory = os.environ["HOME"] + "/Documents/CardMinder/CardMinder DB.cxdb/Images/"
connection = sqlite3.connect(os.environ["HOME"] + "/Documents/CardMinder/CardMinder DB.cxdb/CardMinder1.sqldb")
destination_directory = os.environ["HOME"] + "/Desktop/CardMinderToEvernote/" + today

if os.path.exists(destination_directory):
    for i in range(10):
        destdir = destination_directory + "_" + str(i)
        if not os.path.exists(destdir):
            destination_directory = destdir
            os.mkdir(destination_directory)
            break
else:
    os.mkdir(destination_directory)

cursor = connection.execute("select t1.ZCOMPANY, t1.ZFULL_NAME, t1.ZFACE_IMAGE_FILE, t1.ZBACK_IMAGE_FILE, t1.ZREGISTER_DATE from ZCARD t1, ZCARDBELONG t2, ZFOLDER t3 where t1.ZDELETEDFLAG = 0 and t1.Z_PK = t2.Z_PK and t2.ZFOLDER_ID = t3.ZFOLDER_ID and t3.ZFOLDER_NAME = 'Inbox'")
for row in cursor:
    if row[0]:
        filename = '%s_%s' % (row[0],row[1])
    else:
        filename = '%s' % (row[1])

    output = PdfFileWriter()
    inputFace = PdfFileReader(open(source_directory + row[2], 'rb'))
    output.addPage(inputFace.getPage(0))
    
    if row[3]:
        inputBack = PdfFileReader(open(source_directory + row[3], 'rb'))
        output.addPage(inputBack.getPage(0))
    
    destinationFile = destination_directory + "/" + filename.replace(" ","").replace("/","-") + ".pdf"
    outputStream = open(destinationFile, 'wb')
    output.write(outputStream)
    outputStream.close()

connection.close
