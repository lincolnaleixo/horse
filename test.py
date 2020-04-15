
# print(glob.glob("http://10.0.0.45/downloads/PublicFreakout"))
# import requests
# from bs4 import BeautifulSoup

from src.Horse import Horse

horse = Horse()

# URL = "http://10.0.0.45/downloads/PublicFreakout/"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# clips_links = soup.find_all('a')
# files = [fi.get('href') for fi in clips_links if fi.get('href').endswith(".mp4")]
# print(files)
# for link in clips_links:
#     print(link.get('href'))
horse.download(
    "http://10.0.0.45/downloads/PublicFreakout/-stay-_Domino's_effect_fw4ei7.mp4",
    'video.mp4'
)
