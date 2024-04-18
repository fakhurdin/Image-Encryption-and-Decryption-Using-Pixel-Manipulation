# PRODIGY_CS_02
INTERNSHIP CYBER SECURITY Prodigy Infotech TASK 2 : Pixel Manipulation for Image Encryption
use this to run .py file : pip install Pillow
Detailed Explaination :
Image Encryption using Pixel Manipulation
This Python script demonstrates image encryption and decryption using pixel manipulation. It encrypts an image by altering the RGB values of each pixel and then decrypts it to restore the original image.
Requirements
Python 3.x
Pillow library (Python Imaging Library fork) - Install using pip install Pillow
Usage
Clone the repository or download the image_encryption.py script.
Place the image you want to encrypt in the same directory as the script.
Modify the input_image variable in the script to specify the input image file name.
Run the script using the command python image_encryption.py.
The encrypted image will be saved as encrypted_image.jpg in the same directory.
To decrypt the encrypted image, run the script again. The decrypted image will be saved as decrypted_image.jpg.
Encryption Algorithm
The script uses a simple encryption algorithm by adding fixed values to the RGB components of each pixel for encryption and subtracting the same values for decryption.
Adjust the encryption and decryption manipulation values (10, 20, 30) in the script for stronger or weaker encryption.
Example
Original Image:


Encrypted Image:

Encrypted Image

Decrypted Image:

Decrypted Image

Notes
This script is for educational purposes and demonstrates a basic encryption technique. It may not provide strong security and is not suitable for encrypting sensitive data.
