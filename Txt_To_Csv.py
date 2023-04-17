import json
import regex
import csv

# File paths
input_file_path = r'<Path to Saved_Chat_GPT_.txt>'
output_file_path = r'<Path to the csv result file.>'

# Open the text file and read its contents
with open(input_file_path, 'r') as file:
    text = file.read()

# Use regular expressions to find all JSON objects in the text
pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
json_strings = pattern.findall(text)

# Parse JSON and write to CSV
with open(output_file_path, mode='a', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for json_string in json_strings:
        try:
            json_data = json.loads(json_string)
            # Write header row
            writer.writerow([json_data['title'], '', ''])
            # Write each step as a row
            for step in json_data['steps']:
                writer.writerow(['', step['step_action'], step['step_expected_result']])
        except json.JSONDecodeError as e:
            print(f'Error parsing JSON: {e}')
