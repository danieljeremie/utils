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
        convert = ({True : " ", False : chr(ord(letter)+3)} [letter ==" "])
        result += convert
    return result

def decrypto(phrase):
    result = ""
    for letter in phrase:
        result += ({True : " ", False : chr(ord(letter)-3)} [letter ==" "])
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

def read_all(texte):
    for textline in texte:
        result = ""
        parts  = textline.split("0x")
        parts.remove('')

        for part in parts:
            result += chr(int(part, 16))

        print(result)

# je ne suis pas un imbecile
# et tout est a prendre en compte
# bon on efface tout ça 