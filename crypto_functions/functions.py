import re, base64

CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}

def camel_to_snake(input):
    snake_case = input
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    snake_case = pattern.sub('_', snake_case).lower()
    return snake_case

def caesar_cipher(input, shift):
    cipher = list()
    for item in input:
        cipher.append(chr(ord(item)+shift))
    ans = ''.join(cipher)
    return ans

def base64_en(input):
    sample_string = input
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string

def base64_de(input):
    base64_string = input
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")  
    return sample_string  

def text_to_morse(input):
    english_plain_text = input
    morse_code = ''
    for char in english_plain_text:
        if char == ' ':
            morse_code += '  '
        else:
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()] + ' '
    return morse_code

def morse_to_text(input):
    morse_code = input

    morse_code += ' '

    decipher = ''
    citext = ''
    for letter in morse_code:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(CHARS_TO_MORSE_CODE_MAPPING.keys())[list(CHARS_TO_MORSE_CODE_MAPPING.values()).index(citext)]
                citext = ''
    return decipher

def inverseCase(input):
    return input.swapcase()

def vigenere_cipher(input,key):
    #keygen
    key = list(key) 
    if len(input) == len(key): 
        fin_key = key 
    else: 
        for i in range(len(input) -len(key)): 
            key.append(key[i % len(key)]) 
    fin_key = ("" . join(key))

    #encryption
    encrypt_text = [] 
    for i in range(len(input)): 
        x = (ord(input[i]) +ord(fin_key[i])) % 26
        x += ord('A') 
        encrypt_text.append(chr(x)) 
    return ("" . join(encrypt_text))

print(inverseCase('vathsalTAMMEWAR'))