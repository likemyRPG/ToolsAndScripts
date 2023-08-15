import json
import os

def json_to_netscape(json_file, output_file):
    with open(json_file, 'r') as f:
        cookies = json.load(f)

    with open(output_file, 'w') as f:
        for cookie in cookies:
            domain = cookie['domain']
            initial_dot = 'TRUE' if domain.startswith('.') else 'FALSE'
            path = cookie['path']
            secure = 'TRUE' if cookie['secure'] else 'FALSE'
            expires = str(int(cookie['expirationDate'])) if 'expirationDate' in cookie else '0'
            name = cookie['name']
            value = cookie['value']
            
            f.write(f"{domain}\t{initial_dot}\t{path}\t{secure}\t{expires}\t{name}\t{value}\n")

# Get the directory where the script resides
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to the input and output files, relative to the script's location
json_file = os.path.join(script_dir, 'input_cookies.json')
output_file = os.path.join(script_dir, 'output_cookies.txt')

json_to_netscape(json_file, output_file)
