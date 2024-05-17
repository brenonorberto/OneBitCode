import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os
from PIL import Image

def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        info = reader.metadata
    return info

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        results = []
        for i in range(len(reader.pages)):
            selected_page = reader.pages[i]
            text = selected_page.extract_text()
            results.append(text)
        return ''.join(results)
    
def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'files/{filename}_{page_num+1}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)
            print(f'Pdf {new_filename} criado com sucesso!')    

def split_pdf_page(pdf_path, start_page:int=0, stop_page:int=0):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()
        for page_num in range(start_page, stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'files/{filename}_from_{start_page+1}_to_{stop_page+1}.pdf'
            with open(new_filename, 'wb') as out:
                writer.write(out)
            
def fetch_all_pdf_files(parent_folder:str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith('.pdf'):
                target_files.append(os.path.join(path, name))
    return target_files

def merge_pdfs(list_pdfs, output_filename='files/final_pdf.pdf'):
    merger = PdfMerger()
    with open(output_filename, 'wb') as out:
        for file in list_pdfs:
            merger.append(file)
        merger.write(out)
        
def rotate_pdf(pdf_path, page_num:int, rotation:int=90):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        new_filename = f'files/{filename}_{rotation}_page_rotated.pdf'
        with open(new_filename, 'wb') as out:
            writer.write(out)
            

def extract_images_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)

        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            # print(selected_page.images)
            for img_file_obj in selected_page.images:
                with open(f'files/{img_file_obj.name}', 'wb') as out:
                    out.write(img_file_obj.data)
                    
def convert_img_pdf(image_file):
    my_image = Image.open(image_file)
    # print(my_image)
    img = my_image.convert('RGB')
    # print(os.path.splitext(image_file)[0])
    filename = f'{os.path.splitext(image_file)[0]}.pdf'
    img.save(filename)

# 1 - Buscando dados e metadados de um PDF
# print(get_pdf_metadata('files/teste.pdf'))
# print(extract_text_from_pdf('files/teste.pdf'))

# 2 - Dividindo um PDF em arquivos individuais
# split_pdf('files/teste2.pdf')

# 3 - Dividindo um PDF por paginas selecionadas
# split_pdf_page('files/teste2.pdf', 0, 2)

# 4 - Listando PDFs / Merge PDF
# pdf_list = fetch_all_pdf_files('files/')
# merge_pdfs(pdf_list)

# 5 - Rotacionando uma pagina de um PDF
# rotate_pdf('files/teste.pdf', 0)

# 6 - Extrair imagens de um PDF
# extract_images_from_pdf('files/teste2.pdf')

# 7 - Convertendo imagem em PDF
convert_img_pdf('files/Im1.jpg')