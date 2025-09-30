#!/usr/bin/env python3
"""
Simple Password Generator for Cybersecurity Analysis
Educational purposes only
"""

import random
import string

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Generate a random password with specified complexity"""
    
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passphrase(word_count=4):
    """Generate a passphrase using random words"""
    words = [
        "Red", "Blue", "Green", "Sun", "Moon", "Star", "Ocean", 
        "Mountain", "Forest", "River", "Computer", "Keyboard", 
        "Security", "Cyber", "Digital", "Network", "Cloud"
    ]
    
    passphrase = '-'.join(random.sample(words, word_count))
    # Add some complexity
    passphrase += str(random.randint(10, 99)) + "!"
    return passphrase

if __name__ == "__main__":
    print("Password Generator - Educational Tool")
    print("=" * 40)
    
    # Generate different types of passwords
    print("\n1. Strong Password:", generate_password(16))
    print("\n2. Passphrase:", generate_passphrase())
    print("\n3. Simple Password:", generate_password(12, use_symbols=False))
    
    print("\n⚠️  Remember: Use a password manager for real accounts!")
