import os
import argparse
from collections import Counter

# Set up argument parsing
parser = argparse.ArgumentParser(description="Count occurrences of the first line in .md files.")
parser.add_argument('-d', '--directory', required=True, help="Directory containing the .md files")
args = parser.parse_args()

# Directory specified by the user
directory = args.directory

# Initialize a Counter to keep track of first line occurrences
first_line_counter = Counter()
unique_names = set()  # Set to keep track of unique names

# Walk through all files and subdirectories
for root, _, files in os.walk(directory):
    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                first_line = file.readline().strip()
                first_line_counter[first_line] += 1
                unique_names.add(first_line)  # Add the first line to the set of unique names

# Sort the first lines by count, from largest to smallest
sorted_first_lines = sorted(first_line_counter.items(), key=lambda x: x[1], reverse=True)

# Print out the sorted counts with the count first, followed by the first line
for line, count in sorted_first_lines:
    print(f"{count} file(s): '{line}'")

# Print the total number of unique users who submitted
total_users = len(unique_names)
print(f"\n{total_users} users have submissions")

