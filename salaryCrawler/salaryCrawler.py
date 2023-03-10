import requests
import re

#url = "https://www.seek.com.au/job/59762135"
#url = "https://www.seek.com.au/job/5976218"
#html_content = requests.get(url).text
#dollars = re.findall('[$][0-9,]*', html_content)
#company = re.findall('company*', html_content)
#print(dollars)
#print(company)


for i in range(1,100000000):
	url = "https://www.seek.com.au/job/"+str(i)
	#url = "https://www.seek.com.au/job/5976213"
	
	html_content = requests.get(url).text
	soup_content = BeautifulSoup(html_content,'html.parser')

	html_content_to_focus = str(soup_content.find('div',{'class':"yvsb870 v8nw070 v8nw076"}))
	dollars = re.findall(r'\$[\d,]+', html_content_to_focus)

	if dollars:
		print("URL         : .....")
		print("Job Title   : .....")
		print("Advertiser  : .....")
		print("Company     : .....")
		print("Location    : .....")
		print("Salary range: .....")
		print("----------------------------------------------------------------------------------")
	else:
		print("URL         : ", url, " --> No salary\n----------------------------------------------------------------------------------")
