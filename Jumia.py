import  requests
from  bs4 import BeautifulSoup
import  pandas as pd
from IPython.display import HTML

page=requests.get('https://www.jumia.ma/sports-loisirs/')
soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

prod=soup.find(class_='-paxs row _no-g _4cl-3cm-shs')
print(prod.prettify())

items=prod.find_all(class_='prd _fb col c-prd')
print(items[0].prettify())

prod_name=[item.find(class_='name').text for item in items]
price=[item.find(class_='prc').text for item in items]
image=[item.find(class_='img').get('data-src') for item in items]

print(prod_name)
print(price)
print(image)

prod_info=pd.DataFrame(
    {
        'PRODUCT':prod_name,
        'PRICE':price,
        'IMAGE': image,
    }
)
print(prod_info)

display(prod_info)
html = prod_info.to_html()
