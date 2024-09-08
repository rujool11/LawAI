import os
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

# Define the folder paths
input_folder = 'data/selected_data'   
output_folder = 'data/selected_data_txt' 

os.makedirs(output_folder, exist_ok=True) # make output folder if does not exist

def pdf_to_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = []
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text.append(page.extract_text())
            return '\n'.join(text)
    except PdfReadError as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""  # Return an empty string if there's an error

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(input_folder, filename)
        text = pdf_to_text(pdf_path)
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_path = os.path.join(output_folder, text_filename)
        
        # Write the text to a new file
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        print(f'Converted {filename} to {text_filename}')
