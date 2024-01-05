
import requests
import json
from track_downloader import download_track

url = input("Input chart URL: ")

url = "https://hypeddit.com/top100tracks"

payload = "page=1&type=bass-house"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-US,en;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': '_gid=GA1.2.1954962873.1704408455; _fbp=fb.1.1704408455801.507135226; _hjIncludedInSessionSample_315166=0; _hjSessionUser_315166=eyJpZCI6IjM1YTE4N2RkLWJjZmUtNWNjZS04NjMyLTcwNjc2MzBjNGIyMiIsImNyZWF0ZWQiOjE3MDQ0MDg0NTY4MTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_315166=eyJpZCI6ImRkNDAyMDBjLTJiN2EtNDUxZS05OGFjLTRkNTMwYjJkNWEwZiIsImMiOjE3MDQ0MTQwNzkyOTgsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; _dc_gtm_UA-53065024-1=1; _ga_L3SC8DYBDD=GS1.1.1704408455.1.1.1704415150.0.0.0; _ga=GA1.2.895745054.1704408455; XSRF-TOKEN=eyJpdiI6Ijd3TUFuZFFLNUJRZ29MVnB2YWEzSGc9PSIsInZhbHVlIjoiVWRuQWRQVkp2c0RiNE13UnZJZ3RuUmtqTkZxR0xFaktkREdIcldIVk85aHFBQ2VIM3RXRFdPSXB4NGZORDI3U0ExWFArMWZ2N2o5UEJFNGFnWGpOSmtMQVZTNGhlTjRCZWEySWMranhaS3g1S3NzUk42S0tIdk1CUElQK3JrUkMiLCJtYWMiOiJmZDYxMjYwMTVkYTcyMGNjOGZmMzk4YWMwZWUzNWRmMzQ4OTgwYTc1ZjIwNTNlNmMyZjhkNmQxZGNhZTUwOGE5IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlR5UFp1QmpTcVFCU3FWKzg5UGdNNGc9PSIsInZhbHVlIjoiajRPVkw4TTF2WnlxbWFsdmZXNmFpTExreEtlYmV5VW9PMEpWOGhld1hORDBUaGhVUUZzclFSNmlvZDJjUEQ4dWE2bFIwdmFLNS9BTHZzd25hSHhwRTh2ZlhjUCtuTks3SlV2TlhaSmU2VXpRdW1NdElYTmMrMVlKbmNUS0ZiZ0MiLCJtYWMiOiIxZTVkMjM2NDY5M2UwMzU1ZDBmYTUzZmEwZTJkZGRlZGU2MWI0YTYwMzkzNjgzZjI4YzA5ZTNmZDE3MGI5NzhjIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkpWVUQzR0hKMUU3eWJoWTZjQ0g5ZEE9PSIsInZhbHVlIjoiQ21sSVkwcUtxYnhIQndUODFKaGpaOWFHSFp4SnVleThlc3o0VmNyWGpJbE1TTzhDYkU0dGRCVVpWNW5nN1NEcnlmMkphN216SlNpajBjczRpbkdFV0xtRUdZTjd2S1NzTjRkb054NGtWcUswSVZGN29XZHJ4d2FKK2dMSkl0M1ciLCJtYWMiOiJkY2Q4ODNjODc1NjI2Y2NiNjc0MTcyYzE5NTJmYTAwZDk1NGVjMjMzNTlhZmM2MDEzZWQzYWFlNzkxNDNkMGVmIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IklsOHJrMFgwU2RLOWIraEQyekFtMEE9PSIsInZhbHVlIjoiWkNpM3ZpQ2RUZVZKcVJGTjJnSG0rL3djM0hQb0pGdWIyNVAwQ2JSU3pRUUozc3g2RmhFcE1lNUFLNHpOMUhUREZJcUxwZFNHMFU5TWxmb1NJSElKeGw5Y0lxV3dwaEV2elZBSUh4WUxSaWQxd3ZNeHJhRmFVNzIzSVdHU05KVHciLCJtYWMiOiIyNDIxYTkxMDAwMjMyNDIwNGNhOTBlZDZhNmUwZGJmOTQxYjA0ZjBiYTNlZmU1ZjY1OTVjNDMxY2YyZGQ1NjJiIiwidGFnIjoiIn0%3D',
  'Origin': 'https://hypeddit.com',
  'Referer': 'https://hypeddit.com/charts/downloads/genre/bass-house',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = json.loads(response.text)
# Assuming 'data' is the parsed JSON response
buy_links = [item['buylink'] for item in data['response']] if 'response' in data else []

for link in buy_links:
    print("Downloading track: ", link)
    download_track(link)
    print("Track downloaded successfully.") 

print("Finishing up downloads...")
input("Press enter to exit...")