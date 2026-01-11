import requests
# val = input()
requestUrl = requests.get('https://api.alquran.cloud/v1/edition')
val = requestUrl.json()['data']
for i in val:
    print('Original Name : ',i['name'],' ; English Name :',i['englishName'],' language  :',i['language'] )

