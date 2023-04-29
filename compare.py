# Function to clean a string by removing non-alphanumeric characters
def clean_string(s):
    return ''.join(c for c in s if c.isalnum() or c.isspace())

# Open and read the first file
with open('text1.txt', 'r') as f1:
    txt_1 = f1.read().lower().splitlines()

# Open and read the second file
with open('text2.txt', 'r') as f2:
    txt_2 = f2.read().lower().splitlines()

# Combine the two lists into a single list
new_list = txt_1 + txt_2

# Create an empty set to store unique, cleaned items
unique_items = set()

# Loop through each item in the list
for item in new_list:
    # Clean the item by removing non-alphanumeric characters
    cleaned_item = clean_string(item.lower())

    # If the cleaned item is not already in the set, add it
    if cleaned_item not in unique_items:
        unique_items.add(cleaned_item)

# Sort the set and write the items to a new file
with open('text3.txt', 'w') as f3:
    for item in sorted(unique_items):
        f3.write(item)
        f3.write('\n')
