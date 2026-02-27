#basic caser cipher

dict={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def encrypt(text, shift):
    cipher = ""
    for i in text:
        if i.isalpha():
            for j in dict:
                if i.upper() == dict[j]:
                    pos = (j + shift) % 26
                    if i.islower():
                        cipher += dict[pos].lower()
                    else:
                        cipher += dict[pos]
        else:
            cipher += i
    return cipher


def decrypt(text, shift):
    cipher = ""
    for i in text:
        if i.isalpha():
            for j in dict:
                if i.upper() == dict[j]:
                    pos = (j - shift) % 26
                    if i.islower():
                        cipher += dict[pos].lower()
                    else:
                        cipher += dict[pos]
        else:
            cipher += i
    return cipher

def main():
    choice=int(input("1.Encrpyt\n2.Decrypt\nEnter your choice:"))
    text=input("Enter the text:")
    shift=int(input("Enter the shift:"))
    if choice==1:
        print("Encrypted text:",encrypt(text,shift))
    elif choice==2:
        print("Decrypted text:",decrypt(text,shift))

if __name__=="__main__":
    main()
