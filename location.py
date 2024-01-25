import requests
import folium
import time

def get_user_location(api_key):
    try:
        # Fetch user's IP address
        response = requests.get('https://ipinfo.io?token=' + api_key)
        response.raise_for_status()
        location_data = response.json()

        # Extract latitude and longitude from the response
        latitude, longitude = location_data['loc'].split(',')

        return latitude, longitude

    except requests.exceptions.RequestException as e:
        print(f"Error fetching location: {e}")
        return None, None

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual ipinfo.io API key
    ipinfo_api_key = '689c5158ec257f'

    # Get user's location
    user_latitude, user_longitude = get_user_location(ipinfo_api_key)

    if user_latitude is not None and user_longitude is not None:
        print(f"User's Location - Latitude: {user_latitude}, Longitude: {user_longitude}")

        # Display the location on a map
        user_map = folium.Map(location=[float(user_latitude), float(user_longitude)], zoom_start=10)
        folium.Marker(location=[float(user_latitude), float(user_longitude)], popup='Your Location').add_to(user_map)
        user_map.save('user_location_map.html')
        print("Map saved as user_location_map.html")

    else:
        print("Unable to fetch user's location.")

    # Introduce a delay of 5 seconds between requests
    time.sleep(5)
