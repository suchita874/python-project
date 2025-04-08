import requests

#owm_api = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    'lat' :24.543961,
    'lon' :81.301552,
    'appid' : {your API key}
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",params=parameters)

print(response.status_code)
print(response.json())

from twilio.rest import Client


account_sid = {your account id}
auth_token = {your auth token}

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="HEllo Suchita this is your first sms using twilio in python.",
                     from_= "+15075854470",
                     to= {your mobile number}
                 )

print(message.status)