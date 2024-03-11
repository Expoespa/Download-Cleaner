# Downloads Folder Organizer

This script is designed to help you keep your Downloads folder on Windows organized by automatically sorting files into designated folders based on their file type (extension). Additionally, it moves any folders found in the Downloads folder into a specific folder named "Folders" to maintain a clutter-free environment.

## How It Works

The script scans your Downloads folder and categorizes each file into pre-defined folders such as Images, Videos, Documents, Data, Music, Compressed files, Programming files, and Installation files. If a file does not match any of the predefined categories, it will be moved to an "Others" folder. Here's a brief overview of each category and the types of files they include:

- **Images**: jpg, jpeg, png, gif, tiff, bmp, svg
- **Videos**: mp4, mov, avi, mkv, flv, wmv
- **Documents**: pdf, doc, docx, xls, xlsx, ppt, pptx, txt, odt
- **Data**: csv, json, xml, yaml
- **Music**: mp3, wav, aac, flac
- **Compressed**: zip, rar, 7z, tar, gz
- **Programming**: py, java, cpp, js, html, css, sql
- **Installation**: exe, msi, bat, sh

Any folders (not including system folders or the script-generated folders) found in the Downloads folder will be moved to a "Folders" folder to further organize your Downloads directory.

## Setup Instructions

1. **Modify the Script Path**: Before running the script, make sure to update the `descargas_path` variable with the correct path to your Downloads folder. Replace `luisy` with your Windows username.

    ```python
    descargas_path = 'C:\\Users\\YourUserName\\Downloads'
    ```

2. **Run the Script**: Execute the script using your favorite Python environment. This can be done from the command line, an IDE, or any Python execution method you prefer.

## Important Notes

- Ensure you have Python installed on your Windows machine to run this script.
- It's a good practice to backup your Downloads folder before running the script for the first time to prevent any unintended file movements.
- The script is designed for Windows. If you're using a different operating system, you may need to adjust the file paths accordingly.

## Customization

You can easily customize the script to fit your needs by adding or removing file extensions in the `extensiones` dictionary or by modifying the folder names to better suit your organizational preferences.

## Disclaimer

This script moves files and folders automatically based on their extensions and names. While it's designed to organize your Downloads folder, the author is not responsible for any misplaced or incorrectly moved files. Always review the script's actions and adjust as necessary for your specific needs.

