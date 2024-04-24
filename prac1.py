# practicing the use of urllib and string methods to scrape data
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)

html_raw = page.read()
html = html_raw.decode("utf-8")

# print(html)

begin_title_element = html.find("<title >")
start_point = begin_title_element +len("<title >")

end_point = html.find("</title>")

title = html[start_point:end_point]

print(title)