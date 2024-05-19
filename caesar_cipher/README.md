# Vigenère Cipher

This Python script implements the Vigenère cipher for encryption and decryption of alphabetic text using a given key.

## How It Works

- **Functions**:
  - `vegenere(message, key, direction=1)`: Core function for encryption (`direction=1`) and decryption (`direction=-1`).
  - `encrypt(message, key)`: Encrypts the message.
  - `decrypt(message, key)`: Decrypts the message.
  
- **Details**:
  - Non-alphabetic characters are preserved in the output.
  - The key is cycled through for each character in the message.
  - Characters are shifted based on the key character positions.

## Usage

The script includes example usage to decrypt a provided text with a custom key. Adjust the `text` and `custom_key` variables as needed, then run the script to see the encrypted and decrypted messages.

### Example

```plaintext
Encrypted text: mrttaqrhknsw ih puggrur
Key: python

Decrypted text: exampleplaintext
