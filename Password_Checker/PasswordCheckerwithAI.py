import string

# Load common passwords from a file
def load_common_passwords(file_path):
    try:
        with open(file_path, 'r') as f:
            return set(p.strip() for p in f.readlines())
    except FileNotFoundError:
        print("Common passwords file not found.")
        return set()

# Function to check password strength
def password_strength(password, common_passwords):
    score = 0
    length = len(password)
    
    # Criteria
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    # Scoring
    if length >= 8:
        score += 2
    if length >= 12:
        score += 2
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 2
    if password in common_passwords:
        score = 0  # Penalize common passwords
    
    # Rating
    if score >= 7:
        rating = "Strong"
    elif score >= 4:
        rating = "Moderate"
    else:
        rating = "Weak"
    
    return score, rating

# Main program
def main():
    common_passwords = load_common_passwords('common_passwords.txt')  # Add your text file path
    password = input("Enter a password to check: ")
    score, rating = password_strength(password, common_passwords)
    
    print(f"\nPassword Strength: {rating}")
    print(f"Score: {score}/9")
    
    # Detailed feedback
    print("Details:")
    print(f" - Length: {len(password)} characters")
    print(f" - Uppercase letters: {'Yes' if any(c.isupper() for c in password) else 'No'}")
    print(f" - Lowercase letters: {'Yes' if any(c.islower() for c in password) else 'No'}")
    print(f" - Numbers: {'Yes' if any(c.isdigit() for c in password) else 'No'}")
    print(f" - Symbols: {'Yes' if any(c in string.punctuation for c in password) else 'No'}")
    if password in common_passwords:
        print(" - Warning: This password is very common!")

if __name__ == "__main__":
    main()
