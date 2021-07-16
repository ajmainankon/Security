import string
# write your code here!
# alphabet = ' ',"abcdefghijklmnopqrst"


alphabet =  " "+ string.ascii_lowercase
letters = dict(enumerate(alphabet))

def caesar(message, encryption_key):
    encoding = {}
    for i in range(encryption_key, len(alphabet) + encryption_key, 1):
        character = alphabet[i-encryption_key]
        encode = i%27
        encoding[character] = encode

    new_character = ""
    for i,character in enumerate(message):
        # print(new_character)
        new_character += str(letters[encoding[character]])
    return new_character
message = "hi my name is caesar"
encryption_key = 3
encoded_message = caesar(message, encryption_key)
print(encoded_message)