import os
import shutil
from pathlib import Path
from typing import Dict, List

class FileOrganizer:
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xlsx', '.xls', '.ppt', '.pptx'],
            'Audio': ['.mp3', '.wav', '.flac', '.m4a', '.aac', '.ogg'],
            'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js', '.json', '.xml'],
            'Executables': ['.exe', '.msi', '.app'],
            'Others': []
        }

    def create_folders(self) -> None:
        """Create folders for each file type category if they don't exist."""
        for folder_name in self.file_types.keys():
            folder_path = self.source_dir / folder_name
            if not folder_path.exists():
                folder_path.mkdir(exist_ok=True)
                print(f"Created folder: {folder_name}")

    def get_file_category(self, file_extension: str) -> str:
        """Determine the category of a file based on its extension."""
        for category, extensions in self.file_types.items():
            if file_extension.lower() in extensions:
                return category
        return 'Others'

    def organize_files(self) -> Dict[str, List[str]]:
        """Organize files into their respective folders based on file type."""
        self.create_folders()
        moved_files = {category: [] for category in self.file_types.keys()}

        for file_path in self.source_dir.glob('*'):
            if file_path.is_file():
                file_extension = file_path.suffix
                category = self.get_file_category(file_extension)
                
                # Skip the script file itself
                if file_path.name == Path(__file__).name:
                    continue

                destination_folder = self.source_dir / category
                destination_path = destination_folder / file_path.name

                try:
                    # Handle file name conflicts
                    if destination_path.exists():
                        base_name = destination_path.stem
                        extension = destination_path.suffix
                        counter = 1
                        while destination_path.exists():
                            new_name = f"{base_name}_{counter}{extension}"
                            destination_path = destination_folder / new_name
                            counter += 1

                    shutil.move(str(file_path), str(destination_path))
                    moved_files[category].append(file_path.name)
                    print(f"Moved {file_path.name} to {category}")
                except Exception as e:
                    print(f"Error moving {file_path.name}: {str(e)}")

        return moved_files

def main():
    # Get the downloads folder path
    downloads_path = str(Path.home() / 'Downloads')
    
    # Create FileOrganizer instance and organize files
    organizer = FileOrganizer(downloads_path)
    results = organizer.organize_files()

    # Print summary
    print("\nOrganization Summary:")
    for category, files in results.items():
        if files:
            print(f"\n{category}:")
            for file in files:
                print(f"  - {file}")

if __name__ == '__main__':
    main()