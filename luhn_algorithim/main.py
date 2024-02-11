"""
implement Luhn Algorithim
"""
def main():
    card_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-':'', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    