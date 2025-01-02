#!/usr/bin/env python3

import os
import sys
import shutil
from extract_tiff_from_pdf import extract_tiff_from_pdf
import argparse

def parse_arguments():
    """Parse and validate command line arguments."""
    parser = argparse.ArgumentParser(
        description='Process PDF files and convert pages to TIFF format.'
    )
    
    parser.add_argument(
        'pdf_file',
        help='Path to the PDF file to process'
    )
    
    parser.add_argument(
        '-r', '--resolution',
        type=int,
        default=300,
        help='Resolution for TIFF conversion (default: 300)'
    )
    
    args = parser.parse_args()
    return args

def check_pdf_exists(pdf_file):
    """
    Check if the PDF file exists.
    Returns True if the file exists, False otherwise.
    """
    if not os.path.isfile(pdf_file):
        print(f"Error: The file '{pdf_file}' does not exist")
        return False
    return True

def get_user_confirmation(directories):
    """
    Ask user for confirmation before deleting existing directories.
    Returns True if user confirms, False otherwise.
    """
    existing_dirs = [d for d in directories if os.path.exists(d)]
    
    if not existing_dirs:
        return True
        
    print("\nThe following directories will be deleted and recreated:")
    for directory in existing_dirs:
        print(f"  - {directory}")
    
    while True:
        response = input("\nDo you want to proceed? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        if response in ['no', 'n']:
            return False
        print("Please answer 'yes' or 'no'")

def setup_directories(directories):
    """
    Remove existing directories if they exist and create fresh ones.
    """
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)

def move_pdf_file(pdf_file):
    """Move the PDF file to the destination directory."""
    dest_path = os.path.join("00-pdf-orig", "orig.pdf")
    shutil.copy2(pdf_file, dest_path)

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Define working directories
    directories = ['00-pdf-orig', '01-tiff', '02-tiff-out']
    
    # Perform all checks before making any changes
    if not check_pdf_exists(args.pdf_file):
        sys.exit(1)
        
    if not get_user_confirmation(directories):
        print("Operation cancelled by user")
        sys.exit(0)
    
    # All checks passed, now we can make changes to disk
    try:
        # Create fresh directory structure
        setup_directories(directories)
        
        # Copy (not move) PDF file to destination directory
        move_pdf_file(args.pdf_file)
        
        # Extract TIFF files from PDF
        extract_tiff_from_pdf("00-pdf-orig/orig.pdf", "01-tiff/", args.resolution)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()