File Organizer Script

A simple Python script that automatically organizes files in a given folder into categorized subfolders based on their file type. Each file is also renamed with a **timestamp** to prevent duplicates.

Perfect for keeping your **Downloads folder** or **work directories** clean and structured.

Features

* Automatically sorts files into categories (PDFs, Images, Word Docs, Excel, Code, Archives, etc.).
* Adds a **timestamp** to file names to prevent overwriting.
* Creates target folders on the fly if they don’t exist.
* Catch-all **`Others`** folder for unknown file types.
* Works on Windows, macOS, and Linux.

Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/file-organizer.git
   cd file-organizer
   ```

2. Make sure you have **Python 3.x** installed.

3. Run the script:

   ```bash
   python3 file_organizer.py
   ```

4. Enter the path to the folder you want to organize when prompted:

   ```
   Enter the folder path to organize: /Users/nik/Downloads
   ```

Before running the script:

```
Downloads/
│── report.pdf
│── selfie.png
│── project.docx
│── script.py
│── archive.zip
```

After running the script:

```
Downloads/
│── PDFs/
│    └── report_20250825_201233.pdf
│
│── Images/
│    └── selfie_20250825_201233.png
│
│── Word_Docs/
│    └── project_20250825_201233.docx
│
│── Code_Files/
│    └── script_20250825_201233.py
│
│── Archives/
│    └── archive_20250825_201233.zip
│
│── Others/  (if any unmatched files)
```

Customization

You can add or modify file type categories in the `FILE_TYPES` dictionary at the top of the script. Example:

```python
"Videos": [".mp4", ".mkv", ".avi"]
```

## 📜 License

This project is licensed under the MIT License.
