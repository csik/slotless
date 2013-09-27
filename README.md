slotless
========

Filthy scrapers for a filthy industry.

Two phase scraper, first run scrape.py to get the list of all businesses with gambling in Italy, next run either scrape_detail.py or scrape_detail_async.py.

Dependencies:
  requests
  grequests
  libevent gevent
  lxml
  and shelve for now

