import subprocess
import argparse

# Define the list of scripts with their arguments
scripts_to_run = [
    ('testdisc3.py', ['-h', '-u', '-P', '-p']),
    ('testnic2.py', ['-h', '-P', '-u', '-p']),
    ('testproxy2.py', ['-h', '-P', '-u', '-p', '-r', '-t']),
    ('testssh2.py', ['-h', '-P', '-u', '-p']),
    ('testusr2.py', ['-h', '-u', '-p', '-P', '-c']),
    ('testhost2.py', ['-h', '-u', '-p', '-e', '-o', '-P']),
]

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Run multiple scripts with common arguments.')

# Add optional arguments for host, username, password, port, proxy, and expected hostname
parser.add_argument('-H', '--host', default='16.171.17.23', help='Host IP address')
parser.add_argument('-u', '--username', default='amish', help='Username')
parser.add_argument('-p', '--password', default='nikit123', help='Password')
parser.add_argument('-P', '--port', default='22', help='Port number')
parser.add_argument('-r', '--proxy', default='http://www.google.com', help='Proxy URL')
parser.add_argument('-t', '--test-url', default='http://www.google.com', help='Test URL')
parser.add_argument('-c', '--check-user', default='amish', help='Check user')
parser.add_argument('-e', '--expected-hostname', default='DESKTOP-Q9NHJC3', help='Expected hostname')
parser.add_argument('-o', '--command', default='ls -ltra', help='Expected command' )
# Parse the command-line arguments
args = parser.parse_args()

# Iterate through the list and execute each script
for script, script_args in scripts_to_run:
    try:
        print(f"Running {script}...")
        command = ['python', script]
        
        # Add command-line arguments and their values
        for arg in script_args:
            command.append(arg)
            if arg == '-h':
                command.append(args.host)
            elif arg == '-u':
                command.append(args.username)
            elif arg == '-p':
                command.append(args.password)
            elif arg == '-P':
                command.append(args.port)
            elif arg == '-r':
                command.append(args.proxy)
            elif arg == '-t':
                command.append(args.test_url)
            elif arg == '-c':
                command.append(args.check_user)
            elif arg == '-o':
                command.append(args.command)
            elif arg == '-e':
                command.append(args.expected_hostname)
            else:
                command.append(getattr(args, arg[1:]))  # Get the value from the corresponding command-line argument
        
        subprocess.run(command, check=True)
        print(f"{script} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}")
    except Exception as e:
        print(f"An error occurred while running {script}: {e}")

print("All scripts have been executed.")
