import requests
# import json # Uncomment if you want to print JSON formatted output

# TODO: Change to command line arguments
no_of_passwords = 10
password_type = 'simple'

# TODO: Add error handling for request failures and invalid responses
# TODO: Validate user input and response data
response = requests.get(f"https://www.dinopass.com/password/{password_type}?n={no_of_passwords}&format=json") 
data = response.json()

lst = data['passwords']

# TODO: Add options for output to text file
print("\n".join(lst))

# print(json.dumps(data, indent=4, sort_keys=True)) # Debug: Pretty print JSON response
