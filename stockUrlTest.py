import urllib2
import cookielib

url = "http://table.finance.yahoo.com/table.csv?s=000001.sz"

print "stock test"
response = urllib2.urlopen(url)
print response.getcode()
print response.read()

