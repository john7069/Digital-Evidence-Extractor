from PIL import Image
from PIL.ExifTags import TAGS


def extract_metadata(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Extract the raw EXIF data
        exif_data = image._getexif()

        if exif_data is None:
            print("No metadata found in this image.")
            return

        print(f"--- Metadata for: {image_path} ---")

        # Loop through the raw data and decode it
        for tag_id, value in exif_data.items():
            # Get the human-readable name of the tag (e.g., "DateTime", "Model")
            tag_name = TAGS.get(tag_id, tag_id)

            # Print the Tag Name and the Value
            print(f"{tag_name:25}: {value}")

    except IOError:
        print("Error: The file could not be opened. Check the path.")


# --- HOW TO USE ---
# Replace 'test_image.jpg' with the name of a real photo on your computer
# Note: Photos downloaded from WhatsApp/Facebook usually have metadata stripped out for privacy.
# Use a photo taken directly from your phone camera for the best results.
file_name = input("Enter the image file name (e.g., photo.jpg): ")
extract_metadata(file_name)