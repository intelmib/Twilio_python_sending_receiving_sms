# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC*******************************"
auth_token = "6*******************************"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+15103882627",
    from_="+15187307070",
    body="Hello there! This is a test....Madhuri")
