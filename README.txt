BASIC HOROSCOPE API, V1

This project is based off of the tutorial from https://www.freecodecamp.org/news/python-project-build-an-api-with-beautiful-soup-and-flask/, with a few changes!

*Instead of sourcing my horoscopes from horoscope.com, I sourced them from cafeastrology.com. This involved adjusting the way I was scraping the site, to pick up and return exactly the text I wanted. 
*Instead of daily/monthly/weekly APIs, my code includes APIs for "today" and "tomorrow"
*With my original code, I ran into firewalls preventing me from pulling the text from the URLs for Aquarius and Sagittarius. All other signs worked. After some trial and error, I worked around this using a user agent header. Per Stack Overflow: https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit-a-k-a-and-generate-user-agent
