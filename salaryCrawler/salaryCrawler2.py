import requests
import re
from bs4 import BeautifulSoup

#url = "https://www.seek.com.au/job/5976213"

for i in range(59762139,100000000):
	url = "https://www.seek.com.au/job/"+str(i)
	html_content = requests.get(url).text
	soup_content = BeautifulSoup(html_content,'html.parser')

	html_content_to_focus = str(soup_content.find('div',{'class':"yvsb870 v8nw070 v8nw076"}))
	dollars = re.findall(r'\$[\d,]+', html_content_to_focus)

	if dollars:
		soup_content_to_focus = BeautifulSoup(html_content_to_focus,'html.parser')
		job_title 	= soup_content_to_focus.find('h1',{'data-automation':"job-detail-title"}).text
		advertiser 	= soup_content_to_focus.find('span',{'data-automation':"advertiser-name"}).text
		location 	= soup_content_to_focus.find('span',{'class':"yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya"})
		locationTxt	= soup_content_to_focus.find('span',{'class':"yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya"}).text
		company 	= location.find_next('span',{'class':"yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy21 _1d0g9qk4 _1cshjhya"}).next

		print("URL         : ", url)
		print("Job Title   : ", job_title)
		print("Advertiser  : ", advertiser)
		print("Company     : ", company)
		print("Location    : ", locationTxt)
		print("Salary range: ", dollars)
		print("----------------------------------------------------------------------------------")
	else:
		print("URL         : ", url, " --> No salary\n----------------------------------------------------------------------------------")