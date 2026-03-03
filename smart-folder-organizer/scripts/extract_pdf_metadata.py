"""
Extract PDF Metadata Script
---------------------------
A helper script that extracts text from a PDF using the docling library. 
Docling preserves document layout and tables, returning high-quality markdown.
Returns output as a JSON dictionary to stdout.
"""

import sys
import json
try:
    from docling.document_converter import DocumentConverter
except ImportError:
    print(json.dumps({"error": "docling is not installed. Please install it using 'pip install docling'."}))
    sys.exit(0)

def extract_pdf_metadata(file_path):
    """
    Reads a PDF and returns the text in markdown format.
    Uses Docling for structural and layout-aware extraction.
    """
    try:
        converter = DocumentConverter()
        result = converter.convert(file_path)
        
        # Docling exports high quality text, typically in markdown format
        full_text = result.document.export_to_markdown()
        
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
