# Word Hasher
import hashlib
word = input("Enter a word: ")
hashed_word = hashlib.sha256(word.encode()).hexdigest()
print(f"The SHA-256 hash of the word is {hashed_word}")
