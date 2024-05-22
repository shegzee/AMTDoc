import requests

# URL of the patient detail endpoint
patient_id = 1  # replace with actual patient ID
url = f'http://127.0.0.1:8000/api/agent-patients/{patient_id}/'

# Token obtained after login
token = '969986f8ae788c356dae85b763b8b2786a794937'

# Updated patient data
payload = {
    'name': 'Jane Doe',
    'age': 31,
    'condition': 'Updated condition details',
    # Add any other fields that need to be updated
}

headers = {
    'Authorization': f'Token {token}'
}

try:
    # Send a PUT request to the patient detail endpoint
    response = requests.put(url, json=payload, headers=headers)
    
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
