import requests
from bs4 import BeautifulSoup
import json
from track_downloader import download_track

# User input (playlist)
url = input("Enter playlist: ")

# Parse playlist for IDs
# URL and headers
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

# Send the request
response = requests.request("GET", url, headers=headers)

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find the script tag containing the JSON data
script_tag = soup.find('script', text=lambda t: t and 'window.__sc_hydration' in t)

if script_tag:
    # Extract the JSON string
    json_str = script_tag.string.split('=', 1)[1].strip().rstrip(';')

    # Convert the JSON string into a JSON object
    try:
        json_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
else:
    print("Script tag with JSON data not found")

# Assuming 'data' is your JSON data
playlist_data = json_data[-1]  # The last item in the list contains the 'playlist' data
try:
    tracks = playlist_data['data']['tracks']  # Extracting the 'tracks' list
except TypeError:
    print("Playlist link invalid")
    raise

# Extracting the IDs
try:
    track_ids = [track['id'] for track in tracks]
    purchase_urls = []
except NameError:
    print("No download links found")
    raise

# Scrape playlist for individual song links and put them in a list
for track_id in track_ids:
    url = f"https://api-v2.soundcloud.com/tracks?ids={track_id}&client_id=RMDyLXBETEYF6qcE4jmndm0VF1QZt2T4&%5Bobject%20Object%5D=&app_version=1704293545&app_locale=en"

    payload = {}
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.1',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'OAuth 2-294581-1165057507-e8iIyI3MFGedy',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://soundcloud.com',
        'Referer': 'https://soundcloud.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Convert the response to a string (assuming it's already in JSON format)
    response_string = response.text

    # Parse the string into a JSON object
    try:
        response_json = json.loads(response_string)

        # Check if the response is a list
        if isinstance(response_json, list):
            # Iterate through each item in the list
            for item in response_json:
                # Check if 'purchase_url' exists in the item
                if 'purchase_url' in item:
                    purchase_url = item['purchase_url']
                    if purchase_url and "hypeddit.com/" in purchase_url:
                        print("Downloading track from:", purchase_url)
                        download_track(purchase_url)
                        print("Track downloaded successfully.")
                else:
                    print("purchase_url not found in this item.")
        else:
            # Handle the case where the response is not a list
            print("The JSON response is not a list.")
    except json.JSONDecodeError:
        print("The response is not in valid JSON format.")

print("Finishing up downloads...")
input("Press enter to exit...")