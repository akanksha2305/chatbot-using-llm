import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_path = "task1/data/pdfs/Apple_Vision_Pro_Privacy_Overview.pdf"  # Replace with actual PDF file path
    pdf_text = extract_text_from_pdf(pdf_path)
    with open("task1/data/pdfs/pdf_text.txt", "w", encoding="utf-8") as file:
        file.write(pdf_text)
