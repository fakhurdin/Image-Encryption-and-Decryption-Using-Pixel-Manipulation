from PIL import Image

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Manipulate pixel values for encryption
            r = (r + 10) % 256
            g = (g + 20) % 256
            b = (b + 30) % 256

            encrypted_pixel = (r, g, b)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Manipulate pixel values for decryption
            r = (r - 10) % 256
            g = (g - 20) % 256
            b = (b - 30) % 256

            decrypted_pixel = (r, g, b)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

# Image paths
input_image = "input.jpg"
encrypted_image = "encrypted_image.jpg"
decrypted_image = "decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)
