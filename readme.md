# Modern Alphabet Cipher

## Overview
Modern Alphabet Cipher is a Python-based application that utilizes a custom encryption technique to secure text data. By leveraging user-defined coordinates and a random seed generation method, this application offers a unique approach to data encryption and decryption.

## Features
- **Custom Encoding and Decoding**: Encode and decode text using a randomized alphabet based on user-provided coordinates.
- **Base64 Integration**: Safely transport data by first encoding it in Base64 format before applying custom encryption.
- **File I/O**: Load text data from files and save encrypted results back to disk.
- **User-Friendly Interface**: A modern GUI built with Tkinter allows easy interaction and input handling.

## How It Works
1. **Input**: Users can input text and specify a list of comma-separated coordinates.
2. **Random Seed Generation**: The coordinates are used to generate a new random alphabet.
3. **Encoding**: Text is first encoded in Base64 and then transformed using the newly generated alphabet.
4. **Decoding**: The process can be reversed using the same coordinates to retrieve the original text.

## Security
- The use of long and random coordinates significantly increases the difficulty of unauthorized access to encrypted data.
- This application can be further enhanced by integrating additional security measures, ensuring that sensitive information remains protected.

## Requirements
- Python 3.x
- Tkinter (for the GUI)
- Base64