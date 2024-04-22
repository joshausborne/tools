#!/usr/bin/env python3

import sys

# Dictionary mapping usernames to corresponding name and email
user_info = {
    'jmaus': {
        'name': 'Josh Ausborne',
        'email': 'joshausborne@gmail.com'
    },
    'jausborne': {
        'name': 'Josh Ausborne',
        'email': 'jausborne@endpointdev.com'
    }
}

def usage():
    print("Usage: git-user username command [args ...]", file=sys.stderr)
    sys.exit(1)

# Check if there are enough arguments
if len(sys.argv) < 3:
    usage()

user = sys.argv[1]
if user not in user_info:
    print(f"Username {user} not configured", file=sys.stderr)
    sys.exit(2)

name = user_info[user]['name']
email = user_info[user]['email']

# Set environment variables and execute git command
import os
os.environ['GIT_AUTHOR_NAME'] = name
os.environ['GIT_AUTHOR_EMAIL'] = email
os.environ['GIT_COMMITTER_NAME'] = name
os.environ['GIT_COMMITTER_EMAIL'] = email

import subprocess
subprocess.run(['git'] + sys.argv[2:])
