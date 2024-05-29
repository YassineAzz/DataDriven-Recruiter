import os
from docx2pdf import convert

def convert_word_to_pdf(folder_path):
    # Obtenir la liste de tous les fichiers dans le dossier
    files = os.listdir(folder_path)
    
    # Filtrer pour ne garder que les fichiers .docx
    word_files = [f for f in files if f.endswith('.docx')]
    
    # Créer un dossier pour les fichiers PDF s'il n'existe pas
    pdf_folder_path = os.path.join(folder_path, 'pdfs')
    if not os.path.exists(pdf_folder_path):
        os.makedirs(pdf_folder_path)
    
    # Convertir chaque fichier Word en PDF
    for word_file in word_files:
        word_file_path = os.path.join(folder_path, word_file)
        pdf_file_path = os.path.join(pdf_folder_path, word_file.replace('.docx', '.pdf'))
        convert(word_file_path, pdf_file_path)
        print(f"Converted {word_file} to PDF.")
    
    print("Conversion terminée.")

# Chemin vers le dossier contenant les fichiers Word
folder_path = r"C:\Users\yassi\Desktop\Final_Project\test\Resumes"

convert_word_to_pdf(folder_path)
