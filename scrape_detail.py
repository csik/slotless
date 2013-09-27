#!/usr/bin/env python

import requests
import lxml.html
import time
import shelve

s = shelve.open('data.shelve')
IDs=s['ids']
s.close()

newIDs=[]
for i in IDs:
    #time.sleep(1)
    print "Getting ID " + str(i.get('id')) + "----------------------------------------------------"
    payload = {'hcodiscr': i.get('id'), 'el': '3A'}
    html = requests.post("http://www.aams.gov.it/site.php?id=9920", data=payload)
    root = lxml.html.fromstring(html.text)
    for tr in root.cssselect("div[id='boxEvidenza'] tr")[1:-5]:
        new_entry ={}
        td = tr.cssselect('td')
        new_entry['Codice_censimento_esercizio'] = td[0].text
        new_entry['Denominazione'] = td[1].text
        new_entry['Indirizzo'] = td[2].text
        new_entry['Tipologia'] = td[3].text
        new_entry['Superficie_del_locale_in_MQ'] = td[4].text
        for key, value in i.iteritems():
            new_entry[key]=value
        newIDs.append(new_entry)
        
s = shelve.open('data.shelve')
s['newIDs'] = newIDs
s.close()
            
    
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
        
#f= open('data.txt','rw')
#f.write(str(IDs))
#f.close()
        

        




        
