# Secure Data Hiding in Images Using Steganography

## Overview
This project implements a **steganography** technique to securely hide sensitive data within images. Steganography is the practice of concealing messages or information within other non-secret text or data. The goal of this project is to provide a secure and efficient method to encode and decode hidden information inside images without significantly altering their visual appearance.

## Features
- **Data Encoding:** Embed secret messages inside an image file.
- **Data Decoding:** Retrieve hidden messages from the stego-image.
- **Encryption Support:** Optionally encrypt the hidden message for enhanced security.
- **Supported Image Formats:** JPEG, PNG, BMP.
- **Minimal Distortion:** Ensures minimal change in image quality.

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - OpenCV (cv2) – for image processing
  - NumPy – for numerical operations
  - Cryptography – for optional encryption
  - PIL (Pillow) – for image handling

## Usage
### Encoding Data into an Image
```sh
python encode.py -i input_image.png -m "Your secret message" -o output_image.png
```
- `-i` : Input image file
- `-m` : Message to hide
- `-o` : Output image file with hidden data

### Decoding Data from an Image
```sh
python decode.py -i output_image.png
```
- `-i` : Stego-image containing the hidden message

### Optional Encryption
To enhance security, use the encryption flag:
```sh
python encode.py -i input_image.png -m "Your secret message" -o output_image.png --encrypt
```
```sh
python decode.py -i output_image.png --decrypt
```

## Applications
- Secure communication
- Watermarking and copyright protection
- Digital forensics
- Data protection

## Limitations
- Image quality may degrade if excessive data is embedded.
- Large messages require higher resolution images.

## Contributing
Contributions are welcome! Feel free to submit pull requests or report.

