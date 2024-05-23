import requests

# URL of the add patient endpoint
url = 'http://127.0.0.1:8000/api/agent-patients/add/'

# JWT access token obtained after login
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDQ2NTM3LCJpYXQiOjE3MTY0Mjg1MzcsImp0aSI6IjhmMGUyZGViZDg1ZTRlYTc5OWQyOWM0MmU4Yjk2ZTJkIiwidXNlcl9pZCI6MX0.eMr33hSt5M8-BXuoOouo35OwEHUNnfJ_SdpEnV_mnnU'

# Patient data
payload = {
    'name': 'Jan Do',
    'age': 300,
    'gender': '1',
    'dob': "2000-06-15",
    'address': '124 street'

}

# Set the headers with the JWT access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

try:
    # Send a POST request to the add patient endpoint
    response = requests.post(url, json=payload, headers=headers)

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