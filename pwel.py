# couleurs du terminal

class kolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def crypto(phrase):
    result = ""
    for letter in phrase:
        convert = " " if letter == " " else chr(ord(letter)+3)
        result += convert
    return result

def decrypto(phrase):
    result = ""
    for letter in phrase:
        result += chr(ord(letter)-3) if letter != " " else " "
    return result

def decrypte(lines):
    for line in lines:
        print(decrypto(line))

def crypte(lines):
    for line in lines:
        print("           ", end = "")
        for char in decrypto(line):
            print(hex(ord(char)), end = "")
        print('\n')