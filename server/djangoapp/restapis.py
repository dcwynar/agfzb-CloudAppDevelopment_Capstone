import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

DEALERSHIP_API = 'https://service.eu.apiconnect.ibmcloud.com/gws/apigateway/api/01b28f2350fa121cb3dd7a87ab47d8df4cdd102d0d53cfde82ed87d1b58b24d7/api/dealership'

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


def get_dealers_from_cf(url = DEALERSHIP_API, **kwargs):
    results = []
    json_result = get_request(url)
    if json_result:
        for dealer_doc in json_result:
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)
    return results


def get_dealer_by_id(dealerId, url = DEALERSHIP_API):
    url = url + '?id=' + str(dealerId)
    return get_dealers_from_cf(url)[0]

def get_dealer_by_state(state, url = DEALERSHIP_API):
    url = url + '?state=' + str(state)
    return get_dealers_from_cf(url)

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



