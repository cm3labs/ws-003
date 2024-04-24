# ws-003
Running through webscraper tutorial from RealPython: 'A Practical Introduction to Web Scraping in Python'

ref: https://realpython.com/python-web-scraping-practical-introduction/


##Things I Have Learned
**Tools to use**
urllib
    - from python standard library
    - contains tools for working with URLS

    import urlopen()
    ```
    from urllib.request import urlopen

    ```

    put landing(target) site into a variable
    ```
    url = "http://olympus.realpython.org/profiles/aphrodite"
    ```

    use urlopen()
    ```
    page = urlopen(url)
    ```

string methods
    - use variable.find("<element>")+len("<element>") to get start of where you want to pull text from
    - use variable.find("</element>") to get where it ends
    - take the start and end values (which you hopefully put in variables ...) and use slices (variable[start:end]) to extract code


# Changelog:
2024-04-24
    13:28
        - venv creation works, git created

    13:38
        - Added 'Things I Have Learned' Section