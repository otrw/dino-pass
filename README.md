# DinoPass Password Generator

## About

A small script to generate safe passwords using the DinoPass API.

## Installation

Clone the repository and create a Python virtual environment.

```bash
# Clone and enter directory
git clone https://github.com/otrw/dino-pass.git
cd dino-pass

# Create python virtual environment
python3 -m venv .venv  

# Activate the venv
source .venv/bin/activate  

# install dependencies from requirements.txt
pip install -r requirements.txt
```

### requirements.txt

This project requires the following Python package:

```text
requests
```

## Usage

### Example 1

Running the script with no parameters will return 10 simple passwords by default. The number and type can be changed accordingly.

```bash
python3 dino_pass.py 

graynoise78
trickyboat29
calmmemory21
grayjoke77
loudriver52
dizzyclam25
oliveboot58
wilygame66
wisewing35
goldroll88

Generated 10 passwords
```

### Example 2

Generate 3 simple passwords with rate usage stats.  

```bash
python3 dino_pass.py -n 3 -t simple -r

olddeer29
slimspy50
supertree25

Generated 3 passwords


API requests remaining for this hour: 998
Reset at: 2026-05-14T11:18:54.238Z
```

### Example 3

Generate 10 strong passwords.

```bash
python3 dino_pass.py -n 10 -t strong

5609wit+yDeer
)ryrain5742
937Wild6all
Mintlus#297
(loseFood57
22!guanaWarm
SubtleAppl3331
bIgCIR(LE096
83=aStLynX
Mega5651#ook

Generated 10 passwords
```

### Example 4

Save 5 simple passwords to a file.

```bash
python3 dino_pass.py -n 5 -f passwords.txt

Saved 5 passwords to passwords.txt
```

## API limitations

### Rate Limits

- Capped at 1,000 requests per hour per IP address

- Rate limits are tracked per IP address and when this limit is exceeded, the API returns a `429: Too Many Requests` status code.

### Strong passwords

- Strong passwords are limited to a maximum of 10 per request.

## Official Documentation

- https://www.dinopass.com/api