
import re
import requests

f = open('source','r')
html = f.read()
f.close()

pic_url = re.findall('data-src="(.*?)"',html,re.S)
i = 0
for each in pic_url:
    print 'now downloading'
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.png','wb')
    fp.write(pic.content)
    fp.close()
    i += 1

