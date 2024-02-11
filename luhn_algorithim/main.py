"""
implement Luhn Algorithim
"""
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digits in odd_digits:
        sum_of_odd_digits += int(digits)
def main():
    card_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-':'', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    verify_card_number()
