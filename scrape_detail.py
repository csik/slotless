#!/usr/bin/env python

import requests
import lxml.html
import time
import shelve

s = shelve.open('data.shelve')
IDs=s['ids']
s.close()

for i in IDs:
    time.sleep(1)
    print "Getting ID " + str(i.get('id')) + "----------------------------------------------------"
    payload = {'hcodiscr': i.get('id'), 'el': '3A'}
    html = requests.post("http://www.aams.gov.it/site.php?id=9920", data=payload)
    root = lxml.html.fromstring(html.text)
    for tr in root.cssselect("div[id='boxEvidenza'] tr"):
        for t in tr[1:len(tr)-5]:
            print type(t)
    #print html.content
    
    
    ##print html.content
    #root = lxml.html.fromstring(html.text)
    #table = root.cssselect('table')[1]
    #trs = table.cssselect('tr')
    #for tr in trs[1:51]:
    #    tds = tr.cssselect('td')
    #    td = tds[5] #the javascript onclick
    #    taxcode  = tds[4]
    #    numberslots  = tds[6]
    #    print td.items()[1][1]
    #    IDs.append({'id':td.items()[1][1].split("'")[1], 'type':td.items()[1][1].split("'")[3], 'tax_code':taxcode.text, 'number_slots':numberslots.text})
    #    print td.items()[1][1].split("'")[1]
    #    print td.items()[1][1].split("'")[3]
    #    print taxcode.text
    #    print numberslots.text
        
f= open('data.txt','rw')
f.write(str(IDs))
f.close()
        
s = shelve.open('data.shelve')
s['ids'] = IDs
s.close()
        




        
