alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True

def caesar(start_text, shift_amount,cipher_direction):
        shift_amount = shift_amount % 26
        caesar_text=''
        if cipher_direction == "decode":
            shift_amount = -shift_amount
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                caesar_text += new_letter
            else:
                caesar_text += letter
        print(caesar_text)

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    question = input("Do you want to continue? type 'y' or 'n' \n " )
    if question == "n":
        should_continue = False
        print("program ended")


