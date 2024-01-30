import re

# Get user input for text
text = input("Enter some text: ")

# Define regular expressions
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

# Find email addresses in the text
emails = re.findall(email_pattern, text)
print("Email addresses:", emails)


