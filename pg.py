import requests 
from bs4 import BeautifulSoup
import csv 
from itertools import zip_longest 


# Fetching Url 
result = requests.get("https://wuzzuf.net/search/jobs/?q=Java&a=hpb")

# Getting The Markup of the Page
src = result.content 
# print(src)

# Parsing Content Using Beautifulsoup 
soup = BeautifulSoup(src , "lxml")
# print(soup)

# Getting Information Details :
# Job title - Comp.name - Locations - Job Skills 

# Job title
job_titles = soup.find_all("h2" , {"class":"css-m604qf"})
# print(job_titles)

# Company Name
comp_names = soup.find_all("a" , {"class":"css-17s97q8"})
# print(comp_names)

# Company Location
comp_locations = soup.find_all("span" , {"class":"css-5wys0k"})
# print(comp_locations)

# Job Skills
job_skills = soup.find_all("div" , {"class":"css-y4udm8"})
# print(job_skills)

# Extract Jobs info using Loop into other lists 
job_title = []
comp_name = []
comp_location = []
job_skill = []

for i in range (len(job_titles)):
  job_title.append(job_titles[i].text)
  comp_name.append(comp_names[i].text)
  comp_location.append(comp_locations[i].text)
  job_skill.append(job_skills[i].text)

# print(job_title)
# print(comp_name)
# print(comp_location)
# print(job_skill)

# Import Data Into CSV File 

file_list = [ job_titles , comp_names , comp_locations , job_skills] 
exported = zip_longest(*file_list)
with open("C:/Users/Osama ELsergany/jobs.csv","w") as my_file :
  wr = csv.writer(my_file)
  wr.writerow(['Job title' , 'Company Names' , 'Locations' , 'Skills'])
  wr.writerows(exported)

