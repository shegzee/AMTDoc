import requests

# URL of the patient detail endpoint
patient_id = 1  # replace with actual patient ID
url = f'http://127.0.0.1:8000/api/agent-patient/1/'

# Token obtained after login
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE2NDQ2NTM3LCJpYXQiOjE3MTY0Mjg1MzcsImp0aSI6IjhmMGUyZGViZDg1ZTRlYTc5OWQyOWM0MmU4Yjk2ZTJkIiwidXNlcl9pZCI6MX0.eMr33hSt5M8-BXuoOouo35OwEHUNnfJ_SdpEnV_mnnU'

# Updated patient data
# payload = {
#     # 'name': 'Janet Doe',   
#     # 'age': 30,
#     # 'gender': '1',
#     # 'dob': "2000-06-15",
#     # 'address': '24 street'
# }
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

try:
    # Send a PUT request to the patient detail endpoint
    # response = requests.put(url, json=payload, headers=headers)
    # Send a PUT request to the patient detail endpoint
    
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
