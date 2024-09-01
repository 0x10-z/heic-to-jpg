# HEIC to JPG Converter

This project is a Python script designed to convert HEIC images to JPG format while preserving the EXIF metadata, such as the date and time the photo was taken. The script can also rename the output files using the original date and time as a suffix, ensuring your images are well-organized and easy to locate.

## Features

- Convert HEIC images to JPG format.
- Preserve EXIF metadata during the conversion process.
- Automatically rename JPG files using the original date and time from the EXIF data.
- Batch processing: Convert and rename all HEIC files in a specified directory.

## Requirements

Ensure you have Python installed. The following Python libraries are required:

- Pillow
- pyheif
- pillow-heif

You can install these dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

````

## Usage

1. **Setup your directories:**

   - `input_directory`: This should be the path to the directory containing your HEIC files.
   - `output_directory`: This should be the path to the directory where you want the converted JPG files to be saved.

2. **Run the script:**

   Update the `input_directory` and `output_directory` variables in the script with your paths and then run the script:

   ```bash
   python convert_heic_to_jpg.py
   ```

   Example usage:

   ```python
   input_directory = "/mnt/d/Google Drive/A"
   output_directory = "/mnt/d/Google Drive/A"
   convert_and_delete_heic_files(input_directory, output_directory, 100)
   ```

3. **Check the output:**

   After running the script, the HEIC files will be converted to JPG format, with each image named based on its original date and time of capture (if available). The converted files will be saved in the specified output directory.

## Code Explanation

### heic_to_jpg(input_path, output_path, quality=100)

This function converts a single HEIC file to JPG format, preserving the EXIF metadata. It also renames the file by appending the original date and time as a suffix to the filename.

- `input_path`: Path to the HEIC file.
- `output_path`: Path to save the converted JPG file.
- `quality`: JPEG quality setting (default is 100).

### convert_and_delete_heic_files(directory, output_directory, quality=100)

This function processes all HEIC files in the specified directory, converting them to JPG and optionally deleting the original HEIC files after conversion.

- `directory`: Directory containing HEIC files.
- `output_directory`: Directory to save the converted JPG files.
- `quality`: JPEG quality setting (default is 100).

## Notes

- The script preserves EXIF metadata, which is crucial for maintaining the original date, time, and other details of the photo.
- The script is currently configured to print debug information about each file it processes. You can modify or remove these print statements as needed.
- The script can be extended or modified to handle other formats or additional EXIF data as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
````
