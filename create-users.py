#!/usr/bin/python3

# INET4031
# Abdirizak Abdullahi
# 03/23/26
# 03/24/26

# Import modules: os = used to run system (Linux) commands
# re = used for pattern matching (like checking for comments in input)
# sys = used to read input from stdin (input file)
import os
import re
import sys

def main():
    # Loops through each line from the input file
    for line in sys.stdin:

        # Checks if the line starts with a hashtag(#) which is used to skip or comment out users)
        match = re.match("^#", line)

        # Split the line into fields using ":" as the place where its split
        fields = line.strip().split(':')

        # Skip the line if:
        # - starts with # (means comment)
        # - or it does not have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # take out user info from the fields
        # username:password:lastname:firstname:groups
        username = fields[0]
        password = fields[1]

        # Create the gecos field (used in /etc/passwd for user info)
        # Firstname Lastname
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups by comma. lets it have more than 1 group assignments
        groups = fields[4].split(',')

        # Print message showing what step the user creation is at
        print("==> Creating account for %s..." % (username))

        # Build command to create user with no password in the beginning
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # print instead of executing
        print(cmd)
        # os.system(cmd)

        #Print message for setting password
        print("==> Setting the password for %s..." % (username))

        # Build command to set user password using passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        print(cmd)

        # Loop through each group and assign user
        for group in groups:
            # Skip if group is "-" (means no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Build command to add user to group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                print(cmd)

if __name__ == '__main__':
    main()
