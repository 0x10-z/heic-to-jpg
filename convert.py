from PIL import Image
import pyheif
import os
from PIL.ExifTags import TAGS
from datetime import datetime
from pillow_heif import register_heif_opener
from PIL import ExifTags

register_heif_opener()

def heic_to_jpg(input_path, output_path, quality=100):
    heif_file = pyheif.read(input_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    image_for_exif = Image.open(input_path)

    # extracting the exif metadata
    exifdata = image_for_exif.getexif()
    
    # looping through all the tags present in exifdata
    for tagid in exifdata:
        tagname = TAGS.get(tagid, tagid)
        if tagname is "DateTime":
            date_suffix = exifdata.get(tagid)
            date_suffix = date_suffix.replace(':', '-')
            print(date_suffix)

    if date_suffix:
        base_name = os.path.splitext(os.path.basename(output_path))[0]
        output_path = os.path.join(os.path.dirname(output_path), f"{date_suffix}_{base_name}.jpg")
                    
    image.save(output_path, "JPEG", quality=quality, exif=exifdata)
    
def convert_and_delete_heic_files(directory, output_directory, quality=100):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(".heic"):
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, directory)
                output_path = os.path.join(output_directory, relative_path, f"{os.path.splitext(filename)[0]}.jpg")
                
                if not os.path.exists(os.path.dirname(output_path)):
                    os.makedirs(os.path.dirname(output_path))
                
                heic_to_jpg(input_path, output_path, quality)
                print(f"Converted {input_path} to {output_path}")
                
                #os.remove(input_path)
                print(f"Deleted {input_path}")
                
# Example usage
input_directory = "/mnt/d/Google Drive/A"
output_directory = "/mnt/d/Google Drive/A"
convert_and_delete_heic_files(input_directory, output_directory, 100)
