import requests
from bs4 import BeautifulSoup
import shelve
def process():
    print('Popular Downloads')
    for i in range(0,len(popular_downlaods_year)):
        print('{}. {} --> {}'.format(i+1,popular_downlaods_name[i], popular_downlaods_year[i]))
    print('\n')
    print('Latest Releases')
    for i in range(0,len(latest_releases_year)):
        print('{}. {} --> {}'.format(i + 1, latest_releases_name[i], latest_releases_year[i]))
    F = shelve.open('datafile')
    for i in range(0,len(movies)):
        F[str(i)] = movies[i]
    F.close()
    input()
    quit()


URL = 'https://yts.lt/'
movies = []
year = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
page = requests.get(URL, headers=headers).text
soup = BeautifulSoup(page, 'html.parser')


for name in soup.find_all('div', class_="browse-movie-wrap col-xs-10 col-sm-5"):
    mov_name = name.find('div', class_="browse-movie-bottom")
    movie_name = mov_name.a.text
    movie_year = mov_name.div.text
    movies.append(movie_name)
    year.append(movie_year)
    movies = movies[0:12]
    year = year[0:12]


popular_downlaods_name = movies[0:4]
popular_downlaods_year = year[0:4]
latest_releases_name = movies[4:]
latest_releases_year = year[4:]


F = shelve.open('datafile')
if list(F.keys()) == []:
    process()
check = True
for i in range (0,12):
    if F[str(i)] == movies[i]:
        check = True
    else:
        check = False
        break
F.close()


if check==False:
    process()
else:
    quit()

