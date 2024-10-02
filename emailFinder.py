from email_validator import validate_email, EmailNotValidError


def generate_email_formats(first_name, last_name, domain):
    """
    Generates common email formats based on first and last name and a domain.
    """
    first_name = first_name.lower()
    last_name = last_name.lower()
    domain = domain.lower()

    # Define common email formats
    email_formats = [
        f"{first_name}@{domain}",
        f"{last_name}@{domain}",
    ]

    # Add more variations with additional separators
    separators = ['.', '', '_', '-']
    combinations = []

    for sep in separators:
        combinations.append(f"{first_name}{sep}{last_name}@{domain}")
        combinations.append(f"{last_name}{sep}{first_name}@{domain}")
        combinations.append(f"{first_name[0]}{sep}{last_name}@{domain}")
        combinations.append(f"{last_name[0]}{sep}{first_name}@{domain}")
        combinations.append(f"{first_name[0]}{sep}{last_name[0]}@{domain}")
        combinations.append(f"{last_name[0]}{sep}{first_name[0]}@{domain}")

    # Add the separator combinations
    email_formats.extend(combinations)

    return email_formats

def check_email_validity(email):
    """
    Validates the email address using MX DNS records.
    """
    return validate_email(email, verify=True)

# Example usage
first_name = "John"
last_name = "Doe"
domain = "example.com"



email_candidates = generate_email_formats(first_name, last_name, domain)

# Print possible email formats
for email in email_candidates:
    if check_email_validity(email):
        print(f"{email}")
    

