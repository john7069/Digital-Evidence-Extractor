from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


def extract_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image.getexif()  # Using the public function

        # Prepare a list to store our lines of text
        report_lines = []

        # Add a header with the current time of investigation
        investigation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_lines.append(f"--- DIGITAL FORENSIC REPORT ---")
        report_lines.append(f"Target File: {image_path}")
        report_lines.append(f"Investigation Date: {investigation_time}")
        report_lines.append("-" * 30)

        if not exif_data:
            print("No metadata found.")
            return

        print(f"--- Analyzing {image_path}... ---")

        for tag_id in exif_data:
            tag_name = TAGS.get(tag_id, tag_id)
            value = exif_data.get(tag_id)

            # Create a line of text
            line = f"{tag_name:25}: {value}"

            # Print to screen
            print(line)

            # Add to our report list
            report_lines.append(line)

        # --- SAVE TO FILE FEATURE ---
        # This is what makes it a real tool. We save the evidence.
        report_filename = f"report_{image_path}.txt"
        with open(report_filename, "w") as f:
            f.write("\n".join(report_lines))

        print("-" * 30)
        print(f"✅ SUCCESS: Evidence saved to '{report_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found. Did you forget the .jpg?")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- MAIN ---
file_name = input("Enter the image file name (e.g., photo.jpg): ")
extract_metadata(file_name)
