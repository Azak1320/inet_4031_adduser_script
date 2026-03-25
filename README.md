# INET 4031 - Automated User Creation Script

## Description
This project has a Py script that automates the making of users and assignment of groups on a Linux system. The script reads an input file that has user info and processes each line to make accounts.

## Files
- create-users.py: Main Python script for creating users
- create-users.input: Input file containing user data

## How It Works
The script reads each line from the input file and splits it into fields using ":". Each line contains:
username, password, last name, first name, and groups.

- Lines starting with "#" are skipped
- Lines with missing fields are ignored
- Users are created using system commands
- Passwords are set automatically
- Users are added to specified groups

## How to Run

### Dry Run (Testing Mode)
Comment out os.system() lines and run:
./create-users.py < create-users.input


### Run for Real
Uncomment os.system() lines and run:
sudo ./create-users.py < create-users.input

