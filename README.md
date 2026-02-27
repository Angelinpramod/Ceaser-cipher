# 🔐 Caesar Cipher CLI

A command-line tool for encrypting, decrypting, and brute-forcing Caesar ciphers — built in pure Python with zero dependencies. Useful for CTF challenges, learning classical cryptography, or just having fun with secret messages.

---

## What is a Caesar Cipher?

One of the oldest encryption techniques in the book. Every letter in your message gets shifted by a fixed number of positions in the alphabet. Julius Caesar used a shift of 3 — so `A` became `D`, `B` became `E`, and so on.

```
"Hello, World!"  →  shift 3  →  "Khoor, Zruog!"
```

The alphabet wraps around, so `Z + 3 = C`. Spaces, numbers, and symbols are left completely untouched.

Decryption is just the reverse — shift back by the same amount and you're home.

---

## Requirements

- Python 3.x
- No external libraries needed

---

## Usage

```bash
python3 main.py --mode <mode> [--shift <n>] [--text <text>] [--file <path>]
```

Not sure where to start? This always helps:

```bash
python3 main.py --help
```

Output:
```
usage: main.py [-h] --mode {encrypt,decrypt,bruteforce} [--shift SHIFT] [--text TEXT] [--file FILE]

Caesar Cipher

options:
  -h, --help            show this help message and exit
  --mode {encrypt,decrypt,bruteforce}
                        Mode of operation: encrypt, decrypt or bruteforce
  --shift SHIFT         Shift value for the cipher (default: 0)
  --text TEXT           Text to encrypt or decrypt
  --file FILE           Path to input file
```

---

## Arguments

| Argument  | Required         | Description                               |
|-----------|------------------|-------------------------------------------|
| `--mode`  | ✅ Always        | `encrypt`, `decrypt`, or `bruteforce`     |
| `--shift` | For enc/dec      | Number of positions to shift (default: 0) |
| `--text`  | One of these two | Inline text to process                    |
| `--file`  | One of these two | Path to a `.txt` file to process          |

---

## Examples

### Encrypt
```bash
python3 main.py --mode encrypt --shift 3 --text "Hello, World!"
# Encrypted text: Khoor, Zruog!
```

### Decrypt
```bash
python3 main.py --mode decrypt --shift 3 --text "Khoor, Zruog!"
# Decrypted text: Hello, World!
```

### Brute Force — when you have no idea what the shift is
```bash
python3 main.py --mode bruteforce --text "Khoor, Zruog"
# Shift 1: Jgnnq, Yqtnf
# Shift 2: Ifmmp, Xpsme
# Shift 3: Hello, World   ← the readable one
# Shift 4: Gdkkn, Vnqkc
# ...
```

### Reading from a file
```bash
python3 main.py --mode bruteforce --file cipher.txt
python3 main.py --mode decrypt --shift 13 --file cipher.txt
```

---

## Features

- Preserves original casing — `hello` → `khoor`, `HELLO` → `KHOOR`
- Non-alphabet characters (spaces, punctuation, numbers) pass through unchanged
- Brute force mode tries all 25 possible shifts when the key is unknown
- File input support for processing `.txt` files directly
- Clean error messages for missing files — no ugly Python tracebacks

---

## CTF Notes

Caesar cipher is a staple of beginner CTF challenges. When you're handed ciphertext with no shift value, brute force is your best friend — scan the output for whichever line looks like readable English.

ROT13 (shift 13) deserves a special mention — it's by far the most common variant and worth trying first.

```bash
python3 main.py --mode decrypt --shift 13 --text "Uryyb, Jbeyq!"
```

---

## File Structure

```
caesar-cipher/
├── main.py       # entire tool lives here
├── cipher.txt    # example ciphertext file
└── README.md
```

---

## Author

Built from scratch as a learning project — every line understood, nothing copy-pasted.