import requests
import argparse

parser = argparse.ArgumentParser(
    description="Generate random passwords using the DinoPass API.",
    epilog="Example: python dino_pass.py -n 5 -t strong"
    )
# TODO: Add usage as default
# TODO: Add usuage help with -h or --help and example usage in the help message
parser.add_argument('-n', '--number', type=int, default=10, help='Number of passwords to generate. Simple 1-300, Strong 1-10')
parser.add_argument('-t', '--type', type=str, default='simple', choices=['simple', 'strong'], help='Type of passwords to generate (simple or strong)')
parser.add_argument('-f', '--file', type=str, help='Output file to save the passwords (optional)') 
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

# Save to file if specified, otherwise print to console
if args.file:
    with open(args.file, 'w') as f:
        f.write("\n".join(passwords_list))
else:
    print("\n".join(passwords_list))

if args.file:
    print(f"Saved {len(passwords_list)} passwords to {args.file}")
else:
    print(f"Generated {len(passwords_list)} passwords")