"""
Implementing a vignere cipher encryption and decryption
"""
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

def vegenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_text = ''