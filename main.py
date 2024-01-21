import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")


# finds all jobs
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements: # prints out each job's title and company
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print()


# code below to create a html file and fill it with the content of the url
# content = page.text
# file_html = open("site.html", "w")
# file_html.write(content)

