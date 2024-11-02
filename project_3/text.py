from pypdf import PdfReader


def pdf_to_text_file(file_path, output_path):
    reader = PdfReader(file_path)
    with open(output_path, "w", encoding="utf-8") as output_file:
        for page in reader.pages:
            text = page.extract_text()
            if text:
                output_file.write(text)


file_path = "Tolkien.pdf"
output_path = "Tolkien.txt"
pdf_to_text_file(file_path, output_path)
print("Text successfully saved to", output_path)
