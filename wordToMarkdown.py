import os
import markdown2
from docx import Document
from PIL import Image

def convert_docx_to_md(input_file, output_folder):
    # Abrir o arquivo do Word
    doc = Document(input_file)
    
    # Converter cada parágrafo em Markdown
    md_content = []
    for para in doc.paragraphs:
        md_content.append(para.text)

    # Converter cada imagem em Markdown
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            image_path = os.path.join(output_folder, rel.target_part.partname[1:])
            with open(image_path, "wb") as f:
                f.write(rel.target_part.blob)
            md_content.append(f"![Image](./{rel.target_part.partname[1:]})")

    # Salvar o conteúdo Markdown em um arquivo
    output_file = os.path.splitext(os.path.basename(input_file))[0] + ".md"
    with open(os.path.join(output_folder, output_file), "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

if __name__ == "__main__":
    input_file = "caminho/para/o/arquivo.docx"
    output_folder = "caminho/para/a/pasta/saida"
    convert_docx_to_md(input_file, output_folder)