import requests
from bs4 import BeautifulSoup as bs


def get_session_id(raw_resp):
    soup = bs(raw_resp.text, 'lxml')
    token = soup.find_all('input', {'name':'survey_session_id'})[0]['value']
    return token

payload = {
    'f213054909': 'o213118718',  # 21st checkbox
    'f213054910': 'Ronald',  # first input-field
    'f213054911': 'ronaldG54@gmail.com',
    }

url = r'https://app.e2ma.net/app2/survey/39047/213008231/f2e46b57c8/?v=a'

with requests.session() as s:
    resp = s.get(url)
    payload['survey_session_id'] = get_session_id(resp)
    response_post = s.post(url, data=payload)
    print response_post.text




"""
url = 'https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=kair&realmId=702&categoryId=1617'
soup = BeautifulSoup(urllib2.urlopen(url=url))

print([meta.get('content') for meta in soup.find_all('meta', itemprop='datePublished')])
"""
