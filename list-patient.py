import requests

# URL of the list patients endpoint
url = 'http://127.0.0.1:8000/api/agent-patients/list/'

# Token obtained after login
token = '969986f8ae788c356dae85b763b8b2786a794937'

headers = {
    'Authorization': f'Token {token}'
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
