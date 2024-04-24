#import urlopen()
from urllib.request import urlopen


# use urlopen() on the target url
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

# open the html you just pulled from urlopen
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# Let's look for the title text and extract just that

# find the index of where the title element is
title_index = html.find("<title>")

# find where the text inside the title element starts
start_index = title_index + len("<title>")

# find where the extraction is going to end
end_index = html.find("</title>")

# use slice on the 'html' string value and the "index" values you just made

title = html[start_index:end_index]

print(title)