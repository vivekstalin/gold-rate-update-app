import requests
from bs4 import BeautifulSoup as BS
from twilio.rest import Client


def getGoldPrice():
    try:
        to_list=['+918971511155']
        url = 'https://www.grtjewels.com/'
        r = requests.get(url)
        soup = BS(r.text,'html.parser')
        ans = soup.find("div", class_ = "fL todaysRateNew").text
        account_sid = 'ACe0a7c2d9d2ebbf00f4afec63013a4b7f'
        auth_token = 'dccc83e42dd111b3e502a5aa76f7e4fd'
        client = Client(account_sid, auth_token)
        for number in to_list:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body="GRT JEWELS"+"\n\n"+"Todays Gold Rate:"+"\n"+ans[1:30].strip()+"\n\n-Vivek",
                to='whatsapp:'+number
            )
            print(message.body)
            print(message.sid)
    except Exception as e:
        print("Exception "+e)

if __name__ == '__main__':
    getGoldPrice()