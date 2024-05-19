# Downloads Folder Organizer

This script is designed to help you keep your Downloads folder on Windows organized by automatically sorting files into designated folders based on their file type (extension). Additionally, it moves any folders found in the Downloads folder into a specific folder named "Folders" to maintain a clutter-free environment.

## How It Works

The script scans your Downloads folder and categorizes each file into pre-defined folders such as Images, Videos, Documents, Data, Music, Compressed files, Programming files, and Installation files. If a file does not match any of the predefined categories, it will be moved to an "Others" folder. Here's a brief overview of each category and the types of files they include:

- **Images**: jpg, jpeg, png, gif, tiff, bmp, svg, webp
- **Videos**: mp4, mov, avi, mkv, flv, wmv
- **Documents**: pdf, doc, docx, xls, xlsx, ppt, pptx, txt, odt
- **Data**: csv, json, xml, yaml, asd
- **Music**: mp3, wav, aac, flac, mpeg
- **Compressed**: zip, rar, 7z, tar, gz, torrent
- **Programming**: py, java, cpp, js, html, css, sql
- **Installation**: exe, msi, bat, sh

Any folders (not including system folders or the script-generated folders) found in the Downloads folder will be moved to a "Folders" folder to further organize your Downloads directory.

## Setup Instructions

1. **Modify the Script Path**: Before running the script, make sure to update the `descargas_path` variable with the correct path to your Downloads folder. Replace `YourUserName` with your Windows username.

    ```python
    descargas_path = 'C:\\Users\\YourUserName\\Downloads'
    ```

2. **Run the Script**: Execute the script using your favorite Python environment. This can be done from the command line, an IDE, or any Python execution method you prefer.

## Automation

To automatically run this script daily at 11:00 AM, follow these steps:

1. **Create a Batch File**: Create a `.bat` file to run the script. For example, create a file named `run_script.bat` with the following content:

    ```batch
    @echo off
    "C:\path\to\python.exe" "C:\path\to\your\script.py"
    ```

    Replace `C:\path\to\python.exe` with the path to your Python executable and `C:\path\to\your\script.py` with the path to your Python script.

2. **Schedule the Task**:
    - Open Task Scheduler by pressing `Win + R`, typing `taskschd.msc`, and pressing `Enter`.
    - Click on "Create Basic Task..." in the right-hand pane.
    - Follow the wizard to set the task name and description.
    - Set the trigger to "Daily" and the start time to 11:00 AM.
    - Set the action to "Start a program" and browse to select your `.bat` file.
    - Complete the wizard and ensure the task is set to run even if the user is not logged in and with the highest privileges.

3. **Test the Task**: Manually run the task from Task Scheduler to ensure it works correctly.

## Important Notes

- Ensure you have Python installed on your Windows machine to run this script.
- It's a good practice to backup your Downloads folder before running the script for the first time to prevent any unintended file movements.
- The script is designed for Windows. If you're using a different operating system, you may need to adjust the file paths accordingly.

## Customization

You can easily customize the script to fit your needs by adding or removing file extensions in the `extensiones` dictionary or by modifying the folder names to better suit your organizational preferences.

## Disclaimer

This script moves files and folders automatically based on their extensions and names. While it's designed to organize your Downloads folder, the author is not responsible for any misplaced or incorrectly moved files. Always review the script's actions and adjust as necessary for your specific needs.
