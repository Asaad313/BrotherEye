from Vlad.local_libs.pyzomato.zomato import Zomato


class Pymato:
    def __init__(self, API_KEY):
        self.z = Zomato(API_KEY)
        self.entity_id = None
        self.entity_type = None

    def set_location(self, query, latitude = None, longitude = None):
        if latitude and longitude:
            r = self.z.requester.request(endpoint_name = "locations", payload = {"query": query, "latitude": latitude, "longitude": longitude})
        else:
            r = self.z.requester.request(endpoint_name = "locations", payload = {"query": query,})
        if r['status'] == 'success':
            if len(r['location_suggestions']) > 0:
                self.entity_id = r['location_suggestions'][0]['entity_id']
                self.entity_type = r['location_suggestions'][0]['entity_type']
            else:
                print("Location not found")
                return False
        else:
            print("Server error, try again.")
            return False
        return {
            "entity_id": self.entity_id,
            "entity_type": self.entity_type
        }

    def get_location_details(self):
        if not self.entity_id and self.entity_type:
            print("In local_libs pymato: critial error.")
            return False

        r = self.z.requester.request(endpoint_name = "location_details", payload = {"entity_id": self.entity_id, "entity_type": self.entity_type})
        restaurants = r['best_rated_restaurant']
        if len(restaurants) > 0:
            return restaurants
