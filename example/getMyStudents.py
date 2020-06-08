# -*- coding: utf-8 -*-
import getpass
import sys
from lib.helper import Connect,MySoup

#Set username and password to login
user = input('Enter REG username: ')
try:
    p = getpass.getpass()
except Exception as e:
    print('Error',e)
else:
    print('Password entered successfully')

print('Username ',user,' and Password ',p)

#Connect to REG website
url = u'https://reg.src.ku.ac.th/res/authen.php'
header = {"User-Agent":'Sraping Bot',"charset":"UTF-8",'Referer':'https://reg.src.ku.ac.th/res/login.php'}
payload = {'username': user,'password': p,'login': 'Login'}

nisit_url = u'https://reg.src.ku.ac.th/res/select_nisit.php'
con = Connect(url,header,payload)
if(con.doAuthen() != 200):
    print('Cannot login to REG')
    sys.exit()
print('Logged in!!!!')
html = con.getHTML(nisit_url)

#Get data from HTML DOM
soup = MySoup(html)
soup.getMyStudent()