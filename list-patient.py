import requests

# URL of the list patients endpoint
url = 'http://127.0.0.1:8000/api/agent-patients/list/'

# Token obtained after login
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDQ2NTM3LCJpYXQiOjE3MTY0Mjg1MzcsImp0aSI6IjhmMGUyZGViZDg1ZTRlYTc5OWQyOWM0MmU4Yjk2ZTJkIiwidXNlcl9pZCI6MX0.eMr33hSt5M8-BXuoOouo35OwEHUNnfJ_SdpEnV_mnnU'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

try:
    # Send a GET request to the list patients endpoint
    response = requests.get(url, headers=headers)
    
    # Print the response status code
    print(f"Status Code: {response.status_code}")
    
    # Try to parse the response as JSON
    try:
        response_json = response.json()
        print("Response JSON:", response_json)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
        print("Response content:", response.text)
        
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
