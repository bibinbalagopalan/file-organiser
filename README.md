# File Organizer

A Python script that helps organize files in your downloads folder by automatically sorting them into categorized folders based on their file types.

## Features

- Automatically organizes files based on their extensions
- Creates category folders if they don't exist
- Handles file name conflicts by adding a counter to duplicate file names
- Provides a summary of moved files
- Supports multiple file type categories:
  - Images (.jpg, .jpeg, .png, .gif, .bmp, .svg, .webp)
  - Documents (.pdf, .doc, .docx, .txt, .rtf, .odt, .xlsx, .xls, .ppt, .pptx)
  - Audio (.mp3, .wav, .flac, .m4a, .aac, .ogg)
  - Video (.mp4, .avi, .mkv, .mov, .wmv, .flv)
  - Archives (.zip, .rar, .7z, .tar, .gz)
  - Code (.py, .java, .cpp, .html, .css, .js, .json, .xml)
  - Executables (.exe, .msi, .app)
  - Others (any unrecognized file types)

## Usage

Simply run the script:

```bash
python file_organizer.py
```

The script will automatically:

1. Access your Downloads folder
2. Create category folders if they don't exist
3. Move files to their respective folders based on file type
4. Print a summary of all moved files

## Note

- The script automatically uses your system's Downloads folder
- Files with unrecognized extensions will be moved to the 'Others' folder
- The script skips itself when organizing files to prevent errors
