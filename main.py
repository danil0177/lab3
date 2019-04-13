import json

data = {
    "FirstName":"Petr",
    "LastName":"Ivskii",
    "Address": {
        "StreetAddress":"Moskow st., 12, f. 5",
        "City":"St.Petersburg",
        "PostalCode": 342009
    },
    "PhoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
    }
with open('result.json', 'w') as outfile:
    json.dump(data, outfile)