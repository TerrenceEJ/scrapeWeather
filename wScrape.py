from bs4 import BeautifulSoup as bs
from requests import get

url = "https://forecast.weather.gov/MapClick.php?lat=29.5869&lon=-82.4189"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
response = get(url)
parser = bs(response.text, "html.parser")


overview = parser.find_all('p', class_='short-desc')

for p in overview:
    
    if parser.find_all('p', class_='temp temp-high') is not None:
        forecast = p.text
        print(forecast)
        
        temp = parser.find('p', class_='temp temp-high').text
        print(temp)
        
        #highTemps = parser.find('p', class_='temp temp-high')
        #for tempTag in highTemps:
            #print(tempTag.text)
    
#    lowTemps = parser.find_all('p', class_='temp temp-low')
#    for tempTag in lowTemps:
#        print(tempTag.text)

    



