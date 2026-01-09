# Digital Evidence Extractor 🕵️‍♂️

A Python-based digital forensics tool designed to extract and analyze EXIF metadata from image files. This tool helps investigators retrieve hidden information such as camera models, GPS coordinates, and timestamps.

## 🚀 Features
* **Automated Extraction:** Instantly pulls EXIF data from JPEG/TIFF images.
* **Forensic Analysis:** Identifies Device Model, Software Version, and DateTime Original.
* **Error Handling:** robust file validation to prevent crashes on invalid inputs.

## 🛠️ Technology Used
* Python 3.x
* Pillow (PIL) Library

## 💻 How to Run
1. Install dependencies:
   `pip install Pillow`
2. Run the tool:
   `python metadata_tool.py`
3. Enter the filename (e.g., `evidence.jpg`) when prompted.
