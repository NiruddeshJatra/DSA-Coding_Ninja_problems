# Time Complexity:
# - O(1) for both encode and decode operations
# - Simple hash map lookups and string concatenation

# Space Complexity:
# - O(N) where N is number of URLs encoded
# - Need to store mapping for each shortened URL

# INTUITION:
# Instead of complex hashing, use simple counter to generate unique short URLs.
# Map short URLs to original URLs using hash map.
# Key insight: Don't need fancy encoding, just need uniqueness.
# Example: 
# - longUrl = "http://example.com"
# - Encode to "http://tinyurl.com/10000X"
# - Store mapping 10000X -> original URL
# - Decode simply looks up original URL

# ALGO:
# Encode:
# 1. Generate unique short URL using counter
# 2. Store mapping of short URL -> long URL
# 3. Return short URL

# Decode:
# 1. Look up original URL in hash map
# 2. Return original URL

from typing import Dict

# Global variables
counter = [10000]  # Use list for mutable reference
urlMapping: Dict[str, str] = {}

def encode(longUrl: str) -> str:
   """
   Encodes a URL to a shortened URL.
   
   Args:
       longUrl: Original URL to be shortened
       
   Returns:
       Shortened URL string
   """
   # Generate unique shortened URL
   shortUrl = f"http://tinyurl.com/{counter[0]}X"
   counter[0] += 1
   
   # Store mapping
   urlMapping[shortUrl] = longUrl
   
   return shortUrl

def decode(shortUrl: str) -> str:
   """
   Decodes a shortened URL to its original URL.
   
   Args:
       shortUrl: Shortened URL to be decoded
       
   Returns:
       Original URL string
   """
   # Retrieve original URL from mapping
   return urlMapping[shortUrl]
