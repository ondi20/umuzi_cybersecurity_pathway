import urllib.request
import urllib.parse
import json

# API endpoint
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# prompt user for location
address = input("Enter location: ")

# Encode the query parameter
params = {"q": address}
url = serviceurl + urllib.parse.urlencode(params)

print("Retrieving", url)

# Fetch and decode the response
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

# Parse the JSON
try:
    js = json.loads(data)
except:
    js = None

# Check and extract plus_code
if js and "features" in js and len(js["features"]) > 0:
    plus_code = js["features"][0]["properties"].get("plus_code")
    if plus_code:
        print("Plus code", plus_code)
    else:
        print("==== Failure To Retrieve ====")
else:
    print("==== Failure To Retrieve ====")
