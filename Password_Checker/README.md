Password Strength Checker

A Python script that evaluates the strength of a password based on length, character variety (uppercase, lowercase, digits, symbols), and whether the password appears in a common password list.

This tool is useful for individuals, developers, and security teams who want to quickly assess password security and avoid weak or commonly used passwords.

Features

* Rates passwords as **Weak, Moderate, or Strong**.
* Scoring system considers:

  * Password length
  * Use of uppercase, lowercase, numbers, and symbols
  * Comparison against a list of **common passwords**
* Provides **detailed feedback** for improvement.
* Simple and lightweight, no external dependencies.

Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   ```

2. Make sure you have **Python 3.x** installed.

3. (Optional) Download a list of common passwords (e.g., from [SecLists](https://github.com/danielmiessler/SecLists)) and save it as `common_passwords.txt` in the project folder.

4. Run the script:

   ```bash
   python3 password_checker.py
   ```

5. Enter a password when prompted:

   ```
   Enter a password to check: MyP@ssw0rd123!
   ```

Example Output

Example 1 — Strong Password

```
Enter a password to check: MyP@ssw0rd123!

Password Strength: Strong
Score: 9/9
Details:
 - Length: 13 characters
 - Uppercase letters: Yes
 - Lowercase letters: Yes
 - Numbers: Yes
 - Symbols: Yes
```

Example 2 — Weak Password

```
Enter a password to check: password

Password Strength: Weak
Score: 0/9
Details:
 - Length: 8 characters
 - Uppercase letters: No
 - Lowercase letters: Yes
 - Numbers: No
 - Symbols: No
 - Warning: This password is very common!
```

Customization

* Modify scoring rules inside `password_strength()` if you want different weightings.
* Replace `common_passwords.txt` with a larger or more tailored wordlist for stronger validation.

License

This project is licensed under the MIT License.
