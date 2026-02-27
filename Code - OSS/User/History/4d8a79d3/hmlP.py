import fitz  # PyMuPDF


def pdf_extract_text(path):

    doc = fitz.open(path)
    text = ""

    for page in doc:
        text += page.get_text()

    print(text)

pdf_extract_text("da")
