
"""
1.pip install pytesseract
https://github.com/UB-Mannheim/tesseract/wiki

pip install bs4
pip install requests
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

import requests
from bs4 import BeautifulSoup


def download_captcha()

    def getdata(url):
        r = requests.get(url)
        return r.text

    htmldata = getdata("https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=kair&realmId=702&categoryId=1617")



    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('captcha'):
        #print(item)
        link=item['url']
        with open('capatcha.jpg','wb') as f:
            im=requests.get(link)
            f.write(im.content)





"""
web=webdriver.Chrome()
web.get('https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=kair&realmId=702&categoryId=1617')
img = web.find_element_by_xpath('//*[@id="_-1562905242"]')
src = img.get_attribute('url')
# download the image
x=urllib.urlretrieve(src, "captcha.png")
print(x)
driver.close()
"""


def convert_captcha_2_text():
    from PIL import Image, ImageEnhance, ImageFilter
    import pytesseract

    img = Image.open("captcha.png")
    textCaptcha = pytesseract.image_to_string(img)
    #print(textCaptcha)
    return textCaptcha
