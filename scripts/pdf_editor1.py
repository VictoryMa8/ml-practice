import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf_path, start_page, end_page):
    """
    arguments:
        input_pdf_path (string): Path to the input PDF file
        start_page (int): Starting page number
        end_page (int): Ending page number
    """

    # make sure input file exists
    if not os.path.exists(input_pdf_path):
        raise FileNotFoundError(f'Input pdf file not found: {input_pdf_path}')
    
    # create output path
    output_pdf_path = f"{os.path.splitext(input_pdf_path)[0]}_extracted.pdf"
    
    # read pdf
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    # convert to zero based indexing
    start = start_page - 1
    end = end_page - 1
    
    # add selected pages to writer
    for page_num in range(start, end + 1):
        writer.add_page(reader.pages[page_num])
    
    # write output pdf
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)
    
    return output_pdf_path

def main():
    # get input from user
    input_pdf = input('Enter the path to the pdf file: ')
    start_page = int(input('Enter the start page number: '))
    end_page = int(input('Enter the end page number: '))
    
    # extract pages
    output_path = extract_pages(input_pdf, start_page, end_page)
    print(f'Successfully created extracted pdf at: {output_path}')

if __name__ == '__main__':
    main()  
