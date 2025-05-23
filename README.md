# Pdf Maker Init

A simple command-line utility to initialize the Pdf Maker

## Installation

```bash
# Install from local directory
pipx install .

# Or install from git (if published)
pipx install git+https://github.com/yourusername/hello-world-cli.git
```

## Usage

```markdown
pdfMakerInit [-h] [-r RESOLUTION] pdf_file

Process PDF files and convert pages to TIFF format.

positional arguments:
  pdf_file                       Path to the PDF file to process

options:
  -h, --help                     show this help message and exit
  -r, --resolution RESOLUTION    Resolution for TIFF conversion (default: 300)
```
