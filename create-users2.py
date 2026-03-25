#!/usr/bin/python3

import os
import re
import sys
# This script includes a dry run mode.
# If the user selects "Y", the script will only print commands instead of actually doing them.
# This allows safe testing without making changes to the system.
# If the user selects "N", the script runs normally and does all commands.


def main():
    # Ask user if they want dry run
    choice = input("Run in dry-run mode? (Y/N): ").strip().upper()

    dry_run = True if choice == "Y" else False

    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(':')

        # Skip bad or commented lines
        if match or len(fields) != 5:
            if dry_run:
                print("Skipping invalid or commented line:", line.strip())
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        print("==> Setting password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print("==> Assigning %s to %s..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
