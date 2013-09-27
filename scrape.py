#!/usr/bin/env python

import requests
import lxml.html
import time
import shelve


IDs =[]
for i in range(1,196):
    time.sleep(1)
    print "Getting row " + str(i) + "----------------------------------------------------"
    html = requests.get("http://www.aams.gov.it/site.php?id=9920&pagina="+str(i)+"&id_pagina="+str(i+1)+"&anno=0&uff_reg=14&el=0")
    #print html.content
    root = lxml.html.fromstring(html.text)
    table = root.cssselect('table')[1]
    trs = table.cssselect('tr')
    for tr in trs[1:51]:
        tds = tr.cssselect('td')
        td = tds[5] #the javascript onclick
        taxcode  = tds[4]
        numberslots  = tds[6]
        print td.items()[1][1]
        IDs.append({'id':td.items()[1][1].split("'")[1], 'type':td.items()[1][1].split("'")[3], 'tax_code':taxcode.text, 'number_slots':numberslots.text})
        print td.items()[1][1].split("'")[1]
        print td.items()[1][1].split("'")[3]
        print taxcode.text
        print numberslots.text
        
f= open('data.txt','rw')
f.write(str(IDs))
f.close()
        
s = shelve.open('data.shelve')
s['ids'] = IDs
s.close()
        