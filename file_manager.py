import os


def get_files_in_folder(folder_path):
    """
    Get all files in the specified folder.
    
    Args:
        folder_path: Path to the folder to scan
        
    Returns:
        List of file paths
    """
    try:
        # Check if folder exists
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist")
            return []
        
        all_files = []
        
        # Walk through all directories and subdirectories
        for folder_path, _, files in os.walk(folder_path):
            for filename in files:
                full_path = os.path.join(folder_path, filename)
                all_files.append(full_path)
                #(f"Found: {full_path}")
        
        print(f"\nTotal files found: {len(all_files)}")
        return all_files
    
    except Exception as e:
        print(f"Error reading folder: {e}")
        return []