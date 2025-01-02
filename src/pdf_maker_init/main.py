#!/usr/bin/env python3

import os
import sys
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

def setup_directories():
    """Create required directory structure."""
    directories = ['00-pdf-orig', '01-tiff', '02-tiff-out']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def move_pdf_file(pdf_file):
    """Move the PDF file to the destination directory."""
    try:
        os.rename(pdf_file, "00-pdf-orig/orig.pdf")
    except FileNotFoundError:
        print(f"Error: The file {pdf_file} does not exist")
        sys.exit(1)

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Create directory structure
    setup_directories()
    
    # Move PDF file to destination directory
    move_pdf_file(args.pdf_file)
    
    # Extract TIFF files from PDF
    extract_tiff_from_pdf("00-pdf-orig/orig.pdf", "01-tiff/", args.resolution)

if __name__ == "__main__":
    main()