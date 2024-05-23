import requests

# URL of the login endpoint
url = 'http://127.0.0.1:8000/api/agent-login/'

# Login credentials
payload = {
    'username': 'b',
    'password': 'buka'
}

# Send a POST request to the login endpoint
response = requests.post(url, data=payload)

# Print the response status code and content
print(f"Status Code: {response.status_code}")
print("Response JSON:", response.json())
