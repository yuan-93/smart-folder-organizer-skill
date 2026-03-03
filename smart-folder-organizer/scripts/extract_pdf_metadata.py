"""
Extract PDF Metadata Script
---------------------------
A helper script that extracts text from the first few pages of a PDF
using the pypdf library. Returns output as a JSON dictionary to stdout.
"""

import sys
import json
try:
    from pypdf import PdfReader
except ImportError:
    print(json.dumps({"error": "pypdf is not installed. Please install it using 'pip install pypdf'."}))
    sys.exit(0)

def extract_pdf_metadata(file_path, num_pages=2):
    """
    Reads the first `num_pages` of a PDF and returns the text.
    Uses pypdf for deterministic and reliable extraction.
    """
    try:
        reader = PdfReader(file_path)
        
        extracted_text = []
        pages_to_read = min(num_pages, len(reader.pages))
        
        for i in range(pages_to_read):
            page = reader.pages[i]
            extracted_text.append(page.extract_text() or "")
            
        full_text = "\n".join(extracted_text).strip()
        
        return {
            "success": True,
            "text": full_text
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Please provide the path to the PDF file."}))
        sys.exit(0)
        
    target_file = sys.argv[1]
    result = extract_pdf_metadata(target_file)
    print(json.dumps(result, indent=2))
