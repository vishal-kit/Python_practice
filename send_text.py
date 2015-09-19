#!/usr/bin/env python

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC14e5b72adc1906fd721de9ac2b71b3f2"
auth_token  = "21cac4ff646e6da45ecd468447f6d0e0"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi this is test message",
    to="+818064330735",    # Replace with your phone number
    from_="+81345790689") # Replace with your Twilio number
print message.sid
