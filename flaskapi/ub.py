import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":"watsup"}

headers = {
	"X-RapidAPI-Key": "963ab7526cmsh095bdf67241b298p14e76djsn52983cc62955",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)