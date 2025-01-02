import PyInstaller.__main__
import sys
import os
from pathlib import Path

def build_executable():
    # Get the path to your CLI entry point
    from pdf_maker_init import main as main_module
    cli_path = Path(main_module.__file__).resolve()

    PyInstaller.__main__.run([
        str(cli_path),
        '--name=pdfMakerInit',  # Name of the executable
        '--hidden-import=pdf_maker_init',  # Include your package
        '--clean',  # Clean PyInstaller cache
        '--noconsole' # Hide console on Windows
    ])

if __name__ == '__main__':
    build_executable()