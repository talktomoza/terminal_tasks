import os
from datetime import date

def add_date_prefix(folder_path="files"):
    today = date.today().strftime("%Y-%m-%d")
    
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)
    renamed_count = 0

    for filename in files:
        # Skip files that already have a date prefix
        if filename[:10].replace("-", "").isdigit() and filename[10] == "_":
            print(f"Skipping (already dated): {filename}")
            continue

        old_path = os.path.join(folder_path, filename)

        # Only rename files, not subdirectories
        if os.path.isfile(old_path):
            new_filename = f"{today}_{filename}"
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
            renamed_count += 1

    print(f"\nDone! {renamed_count} file(s) renamed.")

if __name__ == "__main__":
    add_date_prefix()
