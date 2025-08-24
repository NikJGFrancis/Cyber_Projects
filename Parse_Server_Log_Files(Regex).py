import re

log_file = 'server.log'

with open(log_file, 'r') as file:
    for line in file:
        match = re.match(
            r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+)', line)
        if match:
            timestamp = match.group(1)
            severity = match.group(2)
            message = match.group(3)
            # Process extracted information as needed
            print(
                f"Timestamp: {timestamp}, Severity: {severity}, Message: {message}")