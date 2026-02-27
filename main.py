#basic caser cipher
import argparse
dic={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def encrypt(text, shift):
    cipher = ""
    for i in text:
        if i.isalpha():
            for j in dic:
                if i.upper() == dic[j]:
                    pos = (j + shift) % 26
                    if i.islower():
                        cipher += dic[pos].lower()
                    else:
                        cipher += dic[pos]
        else:
            cipher += i
    return cipher


def decrypt(text, shift):
    cipher = ""
    for i in text:
        if i.isalpha():
            for j in dic:
                if i.upper() == dic[j]:
                    pos = (j - shift) % 26
                    if i.islower():
                        cipher += dic[pos].lower()
                    else:
                        cipher += dic[pos]
        else:
            cipher += i
    return cipher

parser = argparse.ArgumentParser(description='Caesar Cipher')
parser.add_argument('--mode', choices=['encrypt', 'decrypt','bruteforce'], required=True, help='Mode of operation: encrypt, decrypt or bruteforce')
parser.add_argument('--shift', type=int, required=False, default=0, help='Shift value for the cipher (default: 0)')
parser.add_argument('--text', type=str, required=False, default=None, help='Text to encrypt or decrypt')
parser.add_argument('--file', type=str, required=False, help='Path to input file')

def main():
    args = parser.parse_args()
    text = args.text
    shift = args.shift
    file=args.file
    if file:
        try:
            with open(file, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
            return
    if args.mode == "encrypt":
        print("Encrypted text:", encrypt(text, shift))
    elif args.mode == "decrypt":
        print("Decrypted text:", decrypt(text, shift))
    elif args.mode == "bruteforce":
        for shift in range(1, 26):
            print(f"Shift {shift}: {decrypt(text, shift)}")



if __name__=="__main__":
    main()
