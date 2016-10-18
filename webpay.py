# https://docs.clover.com/faq/how-do-i-use-the-web-api-to-pay-for-an-order/
# https://docs.clover.com/build/developer-pay-api/

import urlfetch
from Crypto.PublicKey import RSA
from base64 import b64encode

# CC info
cardNumber = 'XXXXXXXXXXXXXX'
expMonth = 12
expYear = 2018
CVV = 'XXX'

# Getting secrets to encrypt cc info
url = 'https://apisandbox.dev.clover.com/v2/merchant/{mId}/pay/key'
headers = {"Authorization": "Bearer XXXXXXXXXXXXXX"}
response = eval(urlfetch.fetch(url = url, headers = headers).content)

modulus = long(response['modulus'])
exponent = long(response['exponent'])
prefix = long(response['prefix'])

RSAkey = RSA.construct((modulus, exponent))

publickey = RSAkey.publickey()
encrypted = publickey.encrypt(cardNumber, prefix)
cardEncrypted = b64encode(encrypted[0])

# YYBQTK5SVXQ2P

post_data = {
    "orderId": XXXXXXX,
    "currency": "usd",
    "amount": 100,
    "expMonth": expMonth,
    "cvv": CVV,
    "expYear": expYear,
    "cardEncrypted": cardEncrypted,
    "last4": cardNumber[-4:],
    "first6": cardNumber[0:6]
}

posturl = 'https://apisandbox.dev.clover.com/v2/merchant/{mId}/pay'
postresponse = urlfetch.fetch(
    url = posturl,
    headers = headers,
    method='POST',
    data = post_data
    )

print postresponse.content
