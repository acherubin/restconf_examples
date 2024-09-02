import requests

requests.packages.urllib3.disable_warnings()

# Replace with your Cisco Modeling Labs URL and API token
CML_BASE_URL = "https://192.168.0.50"
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20uY2lzY28udmlybCIsImlhdCI6MTcyNTIyMTE2NiwiZXhwIjoxNzI1MzA3NTY2LCJzdWIiOiIwMDAwMDAwMC0wMDAwLTQwMDAtYTAwMC0wMDAwMDAwMDAwMDAifQ.fIW6qjiZWUu0yCuD1wgohb8CIp6kOUxZPwoQHN6fk0U"

# Endpoint to list labs
LIST_LABS_ENDPOINT = f"{CML_BASE_URL}/api/v0/labs"

# Headers for authentication
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

def list_labs():
    try:
        response = requests.get(LIST_LABS_ENDPOINT, headers=headers, verify=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            labs = response.json()
            if labs:
                print("List of Labs:")
                for lab in labs:
                    print('Lab ID: ', lab)
                #print(response.text)
            else:
                print("No labs found.")
        else:
            print(f"Failed to retrieve labs. Status Code: {response.status_code}, Error: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function to list labs
list_labs()