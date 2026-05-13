import requests
import argparse

parser = argparse.ArgumentParser(
    description="Generate random passwords using the DinoPass API.",
    epilog="Example: python dino_pass.py -n 5 -t strong"
    )

parser.add_argument('-n', '--number', type=int, default=10, help='Number of passwords to generate (1-300)')
parser.add_argument('-t', '--type', type=str, default='simple', choices=['simple', 'strong'], help='Type of passwords to generate (simple or strong)') 
args = parser.parse_args()

# Validate input parameters
if args.type == "simple":
    max_passwords = 300
else:  # strong
    max_passwords = 10

if args.number < 1 or args.number > max_passwords:
    raise ValueError(
        f"For '{args.type}' passwords, number must be between 1 and {max_passwords}"
    )

response = requests.get(f"https://www.dinopass.com/password/{args.type}?n={args.number}&format=json", timeout=10)

response.raise_for_status() # Raises an HTTP Error if the request returned an unsuccessful status code

data = response.json()

# Validate the response structure
if "passwords" not in data:
    raise ValueError("Unexpected response, no passwords field found")

# Validate the number of passwords returned by the API
if data["count"] != args.number:
    raise ValueError("API returned fewer passwords than requested")

passwords_list = data['passwords']

# TODO: Add options for output to text file
print("\n".join(passwords_list))
