from PIL import Image
import os

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Simple encryption: adding key to each channel
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    encrypted_path = "encrypted_" + os.path.basename(image_path)
    img.save(encrypted_path)
    print(f"Image encrypted successfully! Saved as {encrypted_path}")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Decryption: subtracting key
            pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    decrypted_path = "decrypted_" + os.path.basename(image_path)
    img.save(decrypted_path)
    print(f"Image decrypted successfully! Saved as {decrypted_path}")

def main():
    print("--- Simple Image Encryption Tool ---")
    while True:
        choice = input("\nDo you want to (e)ncrypt or (d)ecrypt an image? (q to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice.")
            continue

        image_path = input("Enter the path to the image: ")
        if not os.path.exists(image_path):
            print("Image not found! Please check the path.")
            continue

        try:
            key = int(input("Enter the encryption key (integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue

        if choice == 'e':
            encrypt_image(image_path, key)
        else:
            decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
