import os

def get_files_info(working_directory, directory=None):
    """
    Get information about files in a directory with security guardrails.
    
    Args:
        working_directory (str): The permitted working directory
        directory (str): The directory to list (defaults to working_directory if None)
    
    Returns:
        str: Formatted string with file information or error message
    """
    try:
        # If directory is None, use working_directory
        if directory is None:
            directory = working_directory
        
        # Convert working directory to absolute path
        working_dir_abs = os.path.abspath(working_directory)
        
        # Handle target directory path
        if os.path.isabs(directory):
            # If directory is absolute, use it directly
            target_dir_abs = os.path.abspath(directory)
        else:
            # If directory is relative, resolve it relative to working_directory
            target_dir_abs = os.path.abspath(os.path.join(working_directory, directory))
        
        # Check if target directory is within the working directory
        try:
            # Use os.path.commonpath to check if target is within working directory
            common_path = os.path.commonpath([working_dir_abs, target_dir_abs])
            if common_path != working_dir_abs:
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        except ValueError:
            # This happens when paths are on different drives (Windows) or have no common path
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if the target path exists and is a directory
        if not os.path.exists(target_dir_abs):
            return f'Error: "{directory}" does not exist'
        
        if not os.path.isdir(target_dir_abs):
            return f'Error: "{directory}" is not a directory'
        
        # List directory contents
        entries = []
        for item in sorted(os.listdir(target_dir_abs)):
            item_path = os.path.join(target_dir_abs, item)
            try:
                # Get file size and check if it's a directory
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                entries.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except OSError as e:
                entries.append(f"- {item}: Error getting info - {str(e)}")
        
        return "\n".join(entries)
        
    except Exception as e:
        return f"Error: {str(e)}"
