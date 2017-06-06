import sys
reload (sys)
sys.setdefaultencoding('utf8')
import re
import requests
from bs4 import BeautifulSoup
import csv
import codecs


url="https://www.mygov.in/group-issue/share-your-ideas-pm-narendra-modis-mann-ki-baat-26th-march-2017/"





r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")



for i in range(100):
		
        url_page_2=url+"?field_hashtags_tid=&sort_by=created&sort_order=DESC&page=0,"+str(i)+"%2C1"
	print url_page_2
	r=requests.get(url_page_2)
	soup=BeautifulSoup(r.content,"html.parser")
	g_data=soup.find_all("div",{"class":"comment_body"})
	g_data_user=soup.find_all("span",{"class":"username"})
 	g_data_like=soup.find_all("span",{"class":"like_count_value"})


	list=[]

	#writer=csv.writer(open("items.csv","a"),delimiter=' ')
	output = open("all_data.txt", "a")
	o=open("like_comment.txt","a")
	for item,item1,like1 in zip(g_data,g_data_user,g_data_like):
		print item1.text
		print item.contents[0].text
		print like1.text
		output.write(item.contents[0].text)
		output.write("->")
		output.write(like1.text)
		
		l=like1.text
		l=l.strip("()")
		l=int(l)
		print "l",l
		s=10
		
		if l>=s:
			print "yes"
			o.write(item.contents[0].text)
			o.write(like1.text)
			o.write("\n")
			o.write("\n")
			o.write("\n")
			o.write("\n")
			
			
                #writer.writerow(item1.text)
		#writer.writerow(item.contents[0].text)

#print r.content
'''soup.find_all("a")
for link in soup.find_all('div'):
	print link.text


for div in soup.fina_all('div','res'):
	a=div.find('a','comment_content')
      	if a:
		print a.text
'''
#for comments
#	myfile=open('items.csv','wb')
	#wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
	
	
	
	#print item.contents[1].text

	

	
'''
g_data_user=soup.find_all("span",{"class":"username"})
print g_data_user
'''
'''
for item in g_data_user:
	print item.contents[0].text
'''
