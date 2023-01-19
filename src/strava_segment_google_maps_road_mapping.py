import requests


class StravaMap:
    def __init__(self, access_token, google_maps_api_key):
        self.access_token = access_token
        self.google_maps_api_key = google_maps_api_key

    def get_segments(self, city):
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        params = {
            'city': city,
            'per_page': 200
        }
        url = 'https://www.strava.com/api/v3/segments/explore'
        response = requests.get(url, headers=headers, params=params)
        segments = response.json()['segments']
        return segments

    def map_segments_to_road_name(self, segments):
        segment_road_names = {}
        for segment in segments:
            lat = segment['start_latitude']
            lng = segment['start_longitude']
            url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={self.google_maps_api_key}'
            response = requests.get(url)
            road_name = response.json()['results'][0]['address_components'][1]['long_name']
            segment_road_names[segment['name']] = road_name
        return segment_road_names


access_token = 'YOUR_STRAVA_API_TOKEN'
google_maps_api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
strava_map = StravaMap(access_token, google_maps_api_key)
segments = strava_map.get_segments('Bellevue')
segment_road_names = strava_map.map_segments_to_road_name(segments)
print(segment_road_names)
