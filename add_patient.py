import requests

# URL of the add patient endpoint
url = 'http://127.0.0.1:8000/api/agent-patients/add/'

# JWT access token obtained after login
access_token = '969986f8ae788c356dae85b763b8b2786a794937'  # Replace with your actual access token

# Patient data
payload = {
    'name': 'John Doe',
    'age': 30,
    'condition': 'Condition details',
    # Add any other required fields for the patient
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