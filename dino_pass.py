import requests
# import json # Uncomment if you want to print JSON formatted output

# TODO: Change to command line arguments using argparse
no_of_passwords = 10
password_type = 'simple'

# Validate input parameters
if no_of_passwords < 1 or no_of_passwords > 300:
    raise ValueError("no_of_passwords must be between 1 and 300")

if password_type not in ['simple', 'strong']:
    raise ValueError("password_type must be 'simple' or 'strong'")

response = requests.get(f"https://www.dinopass.com/password/{password_type}?n={no_of_passwords}&format=json", timeout=10)

response.raise_for_status() # Raises an HTTP Error if the request returned an unsuccessful status code

data = response.json()

# Validate the response structure
if "passwords" not in data:
    raise ValueError("Unexpected response")

# Validate that the count field is present
if "count" not in data:
    raise ValueError("Unexpected response: missing count")

# Validate the number of passwords returned
if data["count"] != no_of_passwords:
    raise ValueError("API returned fewer passwords than requested")

passwords_list = data['passwords']

# TODO: Add options for output to text file
print("\n".join(passwords_list))

# print(json.dumps(data, indent=4, sort_keys=True)) # Debug: Pretty print JSON response
