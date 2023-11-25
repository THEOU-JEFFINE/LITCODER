def analyze_email(email):
    # Initialize counters for each category
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    other_count = 0

    # Iterate through each character in the email
    for char in email:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    # Calculate the total length of the email
    total_length = len(email)

    # Calculate the percentage for each category
    uppercase_percentage = (uppercase_count / total_length) * 100
    lowercase_percentage = (lowercase_count / total_length) * 100
    digit_percentage = (digit_count / total_length) * 100
    other_percentage = (other_count / total_length) * 100

    # Return the results
    return uppercase_percentage, lowercase_percentage, digit_percentage, other_percentage

# Get user input for the email address
user_email = input("Enter an email address: ")

# Analyze the user-provided email
result = analyze_email(user_email)

# Display the results
print(f"\nAnalysis for the entered email address:")
print(f"Uppercase letters: {result[0]:.3f}%")
print(f"Lowercase letters: {result[1]:.3f}%")
print(f"Digits: {result[2]:.3f}%")
print(f"Other characters: {result[3]:.3f}%")
