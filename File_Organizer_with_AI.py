import os
import shutil
from datetime import datetime

# Dictionary mapping file extensions to folder names
FILE_TYPES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Word_Docs": [".doc", ".docx"],
    "Excel_Files": [".xls", ".xlsx"],
    "Text_Files": [".txt"],
    "Presentations": [".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code_Files": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css"],
    "Others": []  # catch-all
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return
    
    # Loop through all files in the directory
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()
        
        # Find target folder
        folder_name = "Others"
        for key, extensions in FILE_TYPES.items():
            if extension in extensions:
                folder_name = key
                break
        
        target_folder = os.path.join(folder_path, folder_name)
        os.makedirs(target_folder, exist_ok=True)
        
        # Create timestamp for renaming
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{os.path.splitext(file_name)[0]}_{timestamp}{extension}"
        new_file_path = os.path.join(target_folder, new_file_name)
        
        # Move and rename file
        shutil.move(file_path, new_file_path)
        print(f"Moved: {file_name} -> {new_file_path}")
    
    print("\n✅ File organization complete!")

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
