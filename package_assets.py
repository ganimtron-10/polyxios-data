"""Automated packaging script to bundle Polyxios test data into a distinct packages directory."""

import os
from zipfile import ZipFile, ZIP_DEFLATED

IGNORED_ITEMS = {"README.md", "package_assets.py"}
OUTPUT_DIR_NAME = "packages"


def package_formats():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(root_dir, OUTPUT_DIR_NAME)

    # Ensure the target packages directory exists up front
    os.makedirs(output_dir, exist_ok=True)

    subdirs = [
        d
        for d in os.listdir(root_dir)
        if os.path.isdir(os.path.join(root_dir, d))
        and not d.startswith(".")
        and d != OUTPUT_DIR_NAME
    ]

    if not subdirs:
        print(
            "No format directories detected. Ensure this script is in the root folder."
        )
        return

    print(f"Detected {len(subdirs)} asset groups. Starting compression...\n")

    for folder in subdirs:
        folder_path = os.path.join(root_dir, folder)
        zip_name = f"{folder}.zip"
        zip_path = os.path.join(output_dir, zip_name)

        files_to_zip = [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
            and not f.startswith(".")
            and f not in IGNORED_ITEMS
        ]

        if not files_to_zip:
            continue

        with ZipFile(zip_path, "w", ZIP_DEFLATED) as archive:
            for file in files_to_zip:
                file_path = os.path.join(folder_path, file)
                archive.write(file_path, arcname=file)

        # Calculate the compressed payload metrics
        bytes_size = os.path.getsize(zip_path)
        mb_size = bytes_size / (1024 * 1024)

        print(
            f"Packaged {len(files_to_zip):>3} files into -> "
            f"{OUTPUT_DIR_NAME}/{zip_name:<10} ({mb_size:.2f} MB)"
        )

    print(f"\nAll assets successfully synchronized inside './{OUTPUT_DIR_NAME}/'.")


if __name__ == "__main__":
    package_formats()
