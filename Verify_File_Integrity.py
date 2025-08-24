# VERIFY INTEGRITY OF FILES USING DIGEST IN PYTHON

# STEP 1: LIBRARY IMPORTS
import hashlib
import os

# STEP 2: HASH CALCULATION FUNCTION
def calculate_hash(file_path):
    """Calculate SHA-256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # Read file in 64KB chunks for efficiency
        while chunk := file.read(65536):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

# STEP 3: HASH VERIFICATION FUNCTION
def verify_hash(downloaded_file, expected_hash):
    calculated_hash = calculate_hash(downloaded_file)
    return calculated_hash == expected_hash

# --- STEP 4: HARDCODED FILE & HASH FOR DEMO ---

# Create a test file automatically (if it doesn’t exist yet)
file_to_check = "example.txt"
if not os.path.exists(file_to_check):
    with open(file_to_check, "w") as f:
        f.write("This is a test file for hash verification.\n")

# Pre-computed SHA-256 hash of example.txt with the above content
expected_hash = "2c52e3c46cb84a82f7270f3b9a1ce221de0d3e62306f16f5a1a56df5d41e93cf"

# STEP 5: HASH VERIFICATION
if verify_hash(file_to_check, expected_hash):
    print(f"✅ Hash verification successful! {file_to_check} is original and untampered.")
else:
    print(f"❌ Hash verification failed! {file_to_check} may have been tampered with.")
