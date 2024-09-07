import os
from PIL import Image

def convert_to_webp(source_dir, option):
    # Walk through the directory and subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check for jpeg, jpg, or png extensions
            if file.lower().endswith(('.jpeg', '.jpg', '.png')):
                file_path = os.path.join(root, file)
                
                # Open the image
                img = Image.open(file_path)

                # Create the destination file path with .webp extension
                webp_file_path = os.path.splitext(file_path)[0] + '.webp'

                # Convert and save the image as webp
                img.save(webp_file_path, 'webp')

                print(f"Converted: {file_path} -> {webp_file_path}")
                
                # If the option is 'replace', delete the original file
                if option == 'replace':
                    os.remove(file_path)
                    print(f"Deleted original file: {file_path}")

if __name__ == "__main__":
    # Specify the source directory
    source_directory = input("Enter the directory to convert images: ")
    
    # Ask whether to replace the original images or keep both
    user_option = input("Do you want to 'replace' the original images or 'keep both'? (replace/keep both): ").strip().lower()
    
    # Validate input
    while user_option not in ['replace', 'keep both']:
        print("Invalid option. Please choose 'replace' or 'keep both'.")
        user_option = input("Do you want to 'replace' the original images or 'keep both'? (replace/keep both): ").strip().lower()

    # Run the conversion with the chosen option
    convert_to_webp(source_directory, user_option)
