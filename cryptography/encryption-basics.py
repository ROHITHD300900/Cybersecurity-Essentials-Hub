#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔐 Cryptography Essentials - Encryption Basics
Demonstrating fundamental encryption concepts and algorithms
Author: Rohith D | CEH in Progress
"""

import hashlib
import base64
import os

# ============================================================================
# 1. HASHING ALGORITHMS - One-way cryptographic functions
# ============================================================================

def demonstrate_hashing():
    """🔍 MD5 and SHA Hashing Examples"""
    print("\n" + "="*60)
    print("📊 HASHING ALGORITHMS DEMONSTRATION")
    print("="*60)
    
    message = "Cybersecurity is crucial"
    
    # SHA-256 Hash (256-bit) - Industry standard
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    print(f"\n✅ SHA-256 (256-bit): \n   {sha256_hash}")
    
    # SHA-512 Hash (512-bit) - Maximum security
    sha512_hash = hashlib.sha512(message.encode()).hexdigest()
    print(f"\n🔒 SHA-512 (512-bit): \n   {sha512_hash}")

# ============================================================================
# 2. PASSWORD HASHING WITH SALT - Industry Best Practice
# ============================================================================

def hash_password(password):
    """🔐 Secure password hashing with salt"""
    salt = os.urandom(32)
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + pwdhash

def demonstrate_password_hashing():
    """🔑 Secure password storage demonstration"""
    print("\n" + "="*60)
    print("🔐 SECURE PASSWORD HASHING WITH SALT")
    print("="*60)
    
    password = "SuperSecure@123"
    hashed = hash_password(password)
    
    print(f"\n🔑 Original Password: {password}")
    print(f"💾 Stored Hash (base64): {base64.b64encode(hashed).decode()}")
    print("\n✅ Password stored securely!")

if __name__ == "__main__":
    print("\n\n")
    print("████████████████████████████████████████████████████████████")
    print("🔐 CRYPTOGRAPHY ESSENTIALS - INTERACTIVE LEARNING MODULE 🔐")
    print("████████████████████████████████████████████████████████████")
    
    demonstrate_hashing()
    demonstrate_password_hashing()
    
    print("\n" + "="*60)
    print("✅ ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY")
    print("="*60)
    print("\n📚 Key Takeaways:")
    print("   • Use SHA-256 or SHA-512 for hashing")
    print("   • Implement salt-based password hashing")
    print("   • Never log or expose encryption keys")
    print("   • Keep cryptographic libraries updated\n")
