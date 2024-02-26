from PIL import Image
import os

def compress_file(file_path):
    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.encode('utf-8')  # Encode as bytes
    
    # Convert the file data into bytes
    data_bytes = bytearray(data)
    
    # Create an image from the file data and encode the file extension in the first row
    width = 100  # Adjust the width of the image for better visualization
    img = Image.new('RGB', (width, len(data_bytes) // width + 1))
    img.putdata([(len(file_extension), 0, 0)] + [(b, b, b) for b in file_extension] + [(b, b, b) for b in data_bytes])
    
    # Save the image
    img.save('compressed_image.png')
    print("File compressed successfully as 'compressed_image.png'")

def decompress_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get the pixel values from the image
    pixel_values = list(img.getdata())
    
    # Extract file extension length and bytes from the first row
    ext_length = pixel_values[0][0]
    file_extension = bytes([pixel[0] for pixel in pixel_values[1:1+ext_length]]).decode('utf-8')
    
    # Convert pixel values back to bytes
    data_bytes = bytes([pixel[0] for pixel in pixel_values[1+ext_length:]])
    
    # Write the bytes to a new file with the correct extension
    file_name, _ = os.path.splitext(image_path)
    with open(f'{file_name}_decompressed{file_extension}', 'wb') as f:
        f.write(data_bytes)
    
    print(f"Image decompressed successfully as 'decompressed_file{file_extension}'")

def main():
    while True:
        print("\nMenu:")
        print("1. Compress File to Image")
        print("2. Decompress Image to File")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            file_path = input("Enter the path of the file to compress: ")
            if not os.path.exists(file_path):
                print("File does not exist!")
                continue
            compress_file(file_path)
        
        elif choice == '2':
            image_path = input("Enter the path of the image to decompress: ")
            if not os.path.exists(image_path):
                print("Image does not exist!")
                continue
            decompress_image(image_path)
        
        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
