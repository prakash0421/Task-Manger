import requests

# Replace with your Mapbox access token
mapbox_token = 'pk.eyJ1IjoicGVyMzRzZmoiLCJhIjoiY2x4cHo4eW45MDFwMDJpc2VudTdieDJzNiJ9.l_JEXYo_bEJNNcr9CXoBbQ'

def get_coordinates(address):
    # URL encode the address
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json'
    params = {
        'access_token': mapbox_token,
        'limit': 1  # Limit results to the most relevant
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'features' in data and len(data['features']) > 0:
        feature = data['features'][0]
        longitude, latitude = feature['center']
        place_name = feature['place_name']
        return latitude,longitude
        
    else:
        return None

# Example usage
# address = 'No 49 Thamarai Kulam 2nd Street, 1st Lane, Manali, Chennai, 600068'
# result = get_coordinates(address)
# if result:
  
#     print(f"{result['latitude']}")
#     f"{result['longitude']}")
# else:
#     print("Address not found.")
