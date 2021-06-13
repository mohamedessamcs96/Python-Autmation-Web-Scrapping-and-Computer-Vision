"""
1.pip3 install selenium

2.install chrome driver using this link :https://sites.google.com/a/chromium.org/chromedriver/downloads
and choose the same version of your chrome and set it in the same place or add path.

3.1.pip install pytesseract
download tesseract and add it to your capatcha
https://github.com/UB-Mannheim/tesseract/wiki

4.pip install bs4
5.pip install requests

"""

from selenium import webdriver
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image, ImageEnhance, ImageFilter
from bs4 import BeautifulSoup
import pytesseract
import requests

def automate_appointement():
    web=webdriver.Chrome()
    web.maximize_window()

    web.get('https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=kair&realmId=702&categoryId=1617')

    #Last name
    LastName="Essam"
    last = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_lastname"]')
    last.send_keys(LastName)
    #Last name

    #First Name
    FirstName="Mohamed"
    first = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_firstname"]')
    first.send_keys(FirstName)
    #First Name

    #Email
    Email="mhmd96.essam@gmail.com"
    email = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_email"]')
    email.send_keys(Email)
    #Email

    #Repait Email
    RepeatEmail="mhmd96.essam@gmail.com"
    repeatEmail = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_emailrepeat"]')
    repeatEmail.send_keys(RepeatEmail)
    #Repait Email

    #Dates
    dates = web.find_element_by_xpath('//*[@id="fields0content"]')
    dates.click()
    dates.send_keys("29.09.1996")

    """
    dateWidget = web.find_element_by_class_name("ui-datepicker-calendar")
    rows = dateWidget.find_elements_by_tag_name("tr")
    columns = dateWidget.find_elements_by_tag_name("td")

    print(columns)
    for cell in columns:
        if cell=='10':
            cell.find_element_by_link_text('10').click()
            break
    """

    #Dates

    #Passport Number
    PassportNumber="123123123123123"
    passportnumber = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_fields_1__content"]')
    passportnumber.send_keys(PassportNumber)
    #Passport Number

    #Phone Number
    PhoneNumber="+201144931949"
    phonenumber = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_fields_2__content"]')
    phonenumber.send_keys(PhoneNumber)
    #PhoneNumber

    #Certificate
    Certificate="Master"
    certificate = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_fields_3__content"]')
    certificate.send_keys(Certificate)
    #Certificate

    #Refrence Number
    RefrenceNumber="01002112332"
    refrencenumber = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_fields_4__content"]')
    refrencenumber.send_keys(RefrenceNumber)
    #Refrence Number

    #Captcha
    TextCaptcha=convert_captcha_2_text()
    captcha = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_captchaText"]')
    captcha.send_keys(TextCaptcha)
    #Captcha

    #Submit
    submit=refrencenumber = web.find_element_by_xpath('//*[@id="appointment_newAppointmentForm_appointment_addAppointment"]')
    submit.click()
    #Submit



def get_captcha():

    def getdata(url):
        r = requests.get(url)
        return r.text

    htmldata = getdata("https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=kair&realmId=702&categoryId=1617")
    soup = BeautifulSoup(htmldata, 'html.parser')
    start = htmldata.find("url('")
    end = htmldata.find("');")
    url = htmldata[start+len("url('"):end]
    print(url)
    return url



def convert_captcha_2_text():
    url=get_captcha()
    img = Image.open(url)
    textCaptcha = pytesseract.image_to_string(img)
    print(textCaptcha)
    return textCaptcha


automate_appointement()
#download_captcha()
