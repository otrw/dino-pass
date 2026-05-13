import requests
# import json # Uncomment if you want to print JSON formatted output

# TODO: Change to command line arguments
no_of_passwords = 10
password_type = 'simple'

# TODO: Validate user input and response data
response = requests.get(f"https://www.dinopass.com/password/{password_type}?n={no_of_passwords}&format=json", timeout=10)

response.raise_for_status() # Raises an HTTP Error if the request returned an unsuccessful status code

data = response.json()

# Validate the response structure
if "passwords" not in data:
    raise ValueError("Unexpected response")

# Validate the number of passwords returned
if data["count"] != no_of_passwords:
    raise ValueError("Warning: fewer passwords returned than requested")

passwords_list = data['passwords']

# TODO: Add options for output to text file
print("\n".join(passwords_list))

# print(json.dumps(data, indent=4, sort_keys=True)) # Debug: Pretty print JSON response
