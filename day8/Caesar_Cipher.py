from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(start_text, shift_amount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
        shift_amount = -shift_amount
    # for num in range(len(start_text)):
    for char in start_text:
        if char in alphabet:
            current_letter = alphabet.index(char)
            end_text += alphabet[current_letter + shift_amount]
        else:
            end_text += char
    print("The {}  text is {}".format(cypher_direction, end_text))


should_continue = True
while should_continue:
    should_continue = True
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(text, shift, direction)
    result = input(
        "type 'yes' if you want to continue and 'no' if you want to stop.")
    if result == 'no':
        should_continue = False
        print('bye')
