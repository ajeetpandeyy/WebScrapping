import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/dp/B08QT49PXC?pf_rd_r=8CD2SH66WV7D38FGYKZ4&pf_rd_p=f93f3f81-9af5-4258-81b7-942444f637fe'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    p_price = price.replace(',', "")
    p_price_1 = p_price.replace('₹', "")
    converted_price = int(p_price_1[:-3])
    print(f"Current price is : {price}")

    try:
        if(converted_price < 7000):
            send_email()
    except:
        print("Some error Occured")


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("aitajeetpandey@gmail.com", "bdqwcsujuvprqpfe")

    subject = 'Price Fell Down!!'
    body = 'Check Amazon link price fell down' \
           'link: https://www.amazon.in/dp/B08QT49PXC?pf_rd_r=8CD2SH66WV7D38FGYKZ4&pf_rd_p=f93f3f81-9af5-4258-81b7-942444f637fe'
    thanks = 'Thanks & Regards' \
             'Ajeet Pandey' \
             '+91 9325818625'

    msg = f"Subject: {subject}\n\n{body} \n\n\n {thanks}"

    server.sendmail(
        'aitajeetpandey@gmail.com',
        'aitajeet@gmail.com',
        msg
    )

    print("Email Has been sent")

    server.quit()

if __name__ == '__main__':
    check_price()