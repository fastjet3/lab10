import request

url = "https://icanhazdadjoke.com/

payload{}
headers = {
	'accept': 'application/json'
}

responese = request.request("get",url, header=header, data=payload)

print(response.TEXT)
