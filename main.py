import re
import requests
from bs4 import BeautifulSoup as bs
url ='https://genius.com/Lana-del-rey-looking-for-america-lyrics'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
script_tag = soup.findAll("script")[17].text
youtube_link_regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
match = youtube_link_regex.search(script_tag)
if match:
    youtube_link = match.group()
    print(youtube_link)
