import PyPDF2
import easygui

def extract_text_from_pdf(pdf_path, output_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

if __name__ == "__main__":
    input_pdf_path = easygui.fileopenbox(title='Select PDF file')
    if not input_pdf_path:
        print("No file selected. Exiting.")
        exit()
    
    output_text_path = easygui.filesavebox(title='Save as text file')
    if not output_text_path:
        print("No output file selected. Exiting.")
        exit()
    
    extract_text_from_pdf(input_pdf_path, output_text_path)
    print("Text extracted and saved to", output_text_path)
