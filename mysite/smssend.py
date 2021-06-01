from urllib.request import urlopen

url = "https://sms.ru/sms/send?api_id=B36C6249-C30C-3209-E2D9-3DB899EBC2FF&to=79500203481,74993221627&msg=hello+world&json=1"
urlopen(url)