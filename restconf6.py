import requests

requests.packages.urllib3.disable_warnings()

# Replace these variables with your CML server details
CML_SERVER = "https://192.168.0.50"
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20uY2lzY28udmlybCIsImlhdCI6MTcyNTE4NzU4MiwiZXhwIjoxNzI1MjczOTgyLCJzdWIiOiIwMDAwMDAwMC0wMDAwLTQwMDAtYTAwMC0wMDAwMDAwMDAwMDAifQ.NdzkvMBN0j6R7H9AA5cmZXfejNXHAIBpk7lRx_rxekk"  # Generate this from CML's user interface

# Endpoint for getting logged-in users
USERS_ENDPOINT = f"{CML_SERVER}/api/v0/users"

# Set up headers for authentication
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

try:
    # Make the request to the CML server
    response = requests.get(USERS_ENDPOINT, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        logged_in_users = response.json()
        print("Logged-in users:")
        for user in logged_in_users:
            print(f"User: {user['username']}")
    else:
        print(f"Failed to get users, status code: {response.status_code}, message: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Error connecting to CML server: {e}")



    
