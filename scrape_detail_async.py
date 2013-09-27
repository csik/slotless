import gevent.monkey
gevent.monkey.patch_socket()
from gevent.pool import Pool
import requests
import lxml.html
import shelve
import time

s = shelve.open('data.shelve')
IDs=s['ids']
s.close()

payloads=[]
#spin_off urls
for i in IDs:
    #time.sleep(1)
    print "Getting ID " + str(i.get('id')) + "----------------------------------------------------"
    payload = {'hcodiscr': i.get('id'), 'el': '3A'}
    payloads.append(payload)
    

    
newIDs=[]
def check_urls(payloads):
    def fetch(payload):
        import lxml.html
        import requests
        html = requests.post("http://www.aams.gov.it/site.php?id=9920", data=payload, timeout=10.0)
        print "Status: [%s] Payload: %s" % (html.status_code, payload)
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
            print str(len(newIDs))+ "out of " + str(len(payloads)) + "requests complete, or " + str(1.0*len(newIDs)/len(payloads)) + "%"

    pool = Pool(10)
    for payload in payloads:
        pool.spawn(fetch, payload)
    pool.join()

check_urls(payloads)
while(1):
    time.sleep(1)
    #print len(payloads)+ "out of " + len(newIDs) + "requests complete, or " + str(1.0*len(newIDs)/len(payloads)) + "%"
    print "still waiting for responses?"
    if len(payloads) == len(newIDs):
        break

    