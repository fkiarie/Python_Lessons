# Password Generator

This Python script generates a random password that meets specific security requirements. By default, the password will be 16 characters long and include at least one digit, one special character, one uppercase letter, and one lowercase letter.

## How It Works

1. **Character Sets**: The script defines sets of letters, digits, and special characters.
2. **Random Selection**: It randomly selects characters from these sets to build a password.
3. **Constraints Check**: The script ensures the password meets the required number of digits, special characters, uppercase letters, and lowercase letters using regular expressions.
4. **Repetition Until Valid**: If the generated password does not meet the requirements, the process repeats until a valid password is created.

Run the script to generate a secure, random password that complies with the specified criteria.
