import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD&base=EUR"


payload = {}
headers= {
  "apikey": "3xU67jzawjedud3M0lIzLTLeUr0GfvcX"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(status_code, result, sep='\n')