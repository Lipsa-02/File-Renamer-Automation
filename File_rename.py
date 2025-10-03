import os

# Folder path where files are located
folder_path = r"C:\Users\lipsa\C tutorial.c"

def rename_files(folder):
    try:
        # Get all files in the folder
        files = os.listdir(folder)

        # Loop through and rename
        for index, file in enumerate(files, start=1):
            # Get file extension
            file_extension = os.path.splitext(file)[1]

            # Create new file name
            new_name = f"file_{index}{file_extension}"

            # Get full paths
            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, new_name)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")

        print("\n✅ All files renamed successfully!")

    except Exception as e:
        print("Error:", e)


# Run the function
rename_files(folder_path)
