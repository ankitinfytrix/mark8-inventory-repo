import os
from pathlib import Path



def print_tree(directory, prefix="", max_depth=3, current_depth=0):
    """Print directory tree structure"""
    if current_depth >= max_depth:
        return
    
    try:
        items = sorted(os.listdir(directory))
    except PermissionError:
        return
    
    dirs = [item for item in items if os.path.isdir(os.path.join(directory, item)) and not item.startswith('.')]
    files = [item for item in items if os.path.isfile(os.path.join(directory, item)) and not item.startswith('.')]
    
    for file in files:
        print(f"{prefix}├── {file}")
    
    for i, dir_name in enumerate(dirs):
        is_last = (i == len(dirs) - 1)
        print(f"{prefix}├── {dir_name}/")
        new_prefix = prefix + ("    " if is_last else "│   ")
        print_tree(os.path.join(directory, dir_name), new_prefix, max_depth, current_depth + 1)

if __name__ == "__main__":
    repo_path = "/Users/ankit.pandey/Ankit/git-repo/mark8-inventory-repo"
    print(f"Repository structure: {repo_path}\n")
    print_tree(repo_path)