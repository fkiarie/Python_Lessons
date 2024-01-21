"""
Implementing a vignere cipher encryption and decryption
"""
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def vegenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_text = ''

    for char in message.lower():

        # Append any non-character to message
        if not char.isalpha():
            final_text += char
        else:
            #Find the right key character to encode/decrypt
            key_char = key[key_index % len(key)]
            key_index +=1

            # Define the offset and the encrypted/decrypted letter

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_text += alphabet[new_index]
    
    return final_text
