# Scrapy

### AQI_Spider.py

Extract beijing AQI from *http://aqicn.org/city/beijing/* per hour and save it to MYSQL, meantime read last 4 hours AQI data if the quality goes better or worse, send an e-mail.

### Douban spider

For my girlfriend.

Get what books she like.

##### DB_Spider.py

Go to book's douban website, crawl book's tags and save it in hottags.txt.

##### ANLYSIS_TAGS.py

Anlysis tags frequency and sort.

##### Extract_Book_Tags.py

Get tags from hottags.txt, visit every tag's douban website, sort by rating, pick top 40 books. Go to all of these books page, crawl tags, place book names and tags in a excel.

##### In Excel

Each tag times its frequency as a point and sum every book's tag point. Sort by point, so we have a book list she might like.

##### Find out

She like it. :)