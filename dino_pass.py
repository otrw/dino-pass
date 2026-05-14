import requests
import argparse

parser = argparse.ArgumentParser(
    description="Generate random passwords using the DinoPass API.",
    epilog=("Example: python dino_pass.py -n 5 -t simple\n\n"
    "This will generate 5 simple passwords and print them to the console.\n\n"
    "Note: For strong passwords, the maximum number you can generate at once is 10 due to API limitations.\n"
    "API Rate Limits: 1000 requests per hour.\n" \
    "For more information, visit https://www.dinopass.com/api"
    ),
    formatter_class=argparse.RawTextHelpFormatter,
    )
parser.add_argument('-n', '--number', type=int, default=10, help='Number of passwords to generate. Simple Max: 300, Strong Max: 10. Default is 10.')
parser.add_argument('-t', '--type', type=str, default='simple', choices=['simple', 'strong'], help='Password type simple or strong. Default is simple.')
parser.add_argument('-f', '--file', type=str, help='Output file to save the passwords (optional)')
parser.add_argument('-r', '--rate-limit', action='store_true', help='Display API rate limit information after generating passwords (optional)')
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
    print(f"\nSaved {len(passwords_list)} passwords to {args.file}\n")
else:
    print(f"\nGenerated {len(passwords_list)} passwords\n")

# Check rate limit headers
if args.rate_limit:
    remaining = response.headers.get('X-RateLimit-Remaining')
    reset_time = response.headers.get('X-RateLimit-Reset') 

    if remaining and reset_time:
        print(f"\nAPI requests remaining for this hour: {remaining}")
        print(f"Reset at: {reset_time}\n")
