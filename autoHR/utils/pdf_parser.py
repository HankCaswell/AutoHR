import fitz # PyMuPDF

def extract_text_from_pdf(file_stream):
    """
    Extracts text from the given PDF file stream.
    
    :param file_stream: A file-like object for the PDF.
    :return: A string containing the extracted text.
    """
    doc = fitz.open(stream=file_stream, filetype="pdf")
    text = ""
    
    for page in doc:
        text += page.get_text()
    
    return text