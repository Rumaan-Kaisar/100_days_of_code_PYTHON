import caesar_cipher_art
print(caesar_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# --------------- Encode/Decode ------------

def caeser(plain_text, shift_amount, dirCtn):
    new_text = ''
    if dirCtn == "decode":
        shift_amount *= -1
    for letter in plain_text :
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            elif new_position < 0:
                new_position += 26
            new_text += alphabet[new_position]
        else:
            new_text += letter
    print(f"The {dirCtn}d text is {new_text}")


cont_state = True

while cont_state == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if shift > 25:
        shift %= 26

    caeser(plain_text = text, shift_amount = shift, dirCtn = direction)

    user_ask = input("Type 'yes' to continiue. To teminate enter any key : ").lower()
    if user_ask == "no":
        cont_state = False
        print("Goodbye")

# python caeser_cipher.py