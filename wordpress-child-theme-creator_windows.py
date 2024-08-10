import zipfile
import os
import shutil  # Importa shutil para operações de arquivos no Windows


def create_wordpress_child_theme(parent_theme_zip, child_theme_name, output_dir):
    # Extrair o nome do tema principal do arquivo zip
    # Extract the name of the parent theme from the zip file
    extracted_path = os.path.join(output_dir, "extracted_theme")
    with zipfile.ZipFile(parent_theme_zip, "r") as zip_ref:
        zip_ref.extractall(extracted_path)

    # Localizar a pasta do tema extraído
    # Locate the extracted theme directory
    theme_dir = os.path.join(extracted_path, os.listdir(extracted_path)[0])

    # Criar a pasta para o tema filho
    # Create the directory for the child theme
    child_theme_dir = os.path.join(output_dir, child_theme_name)
    os.makedirs(child_theme_dir, exist_ok=True)

    # Criar o arquivo style.css do tema filho
    # Create the style.css file for the child theme
    style_css_content = f"""/*
Theme Name:   {child_theme_name}
Template:     {os.path.basename(theme_dir)}
Description:  Tema filho para o {os.path.basename(theme_dir)}
Author:       Autor
Version:      1.0.0
*/
"""
    with open(os.path.join(child_theme_dir, "style.css"), "w") as f:
        f.write(style_css_content)

    # Criar o arquivo functions.php do tema filho
    # Create the functions.php file for the child theme
    functions_php_content = f"""<?php
function {child_theme_name.replace('-', '_')}_enqueue_styles() {{
    // Enfileirar o estilo do tema pai
    // Enqueue the parent theme style
    wp_enqueue_style('parent-style', get_template_directory_uri() . '/style.css');

    // Enfileirar o estilo do tema filho
    // Enqueue the child theme style
    wp_enqueue_style('child-style', get_stylesheet_uri(), array('parent-style'));
}}
add_action('wp_enqueue_scripts', '{child_theme_name.replace('-', '_')}_enqueue_styles');
"""
    with open(os.path.join(child_theme_dir, "functions.php"), "w") as f:
        f.write(functions_php_content)

    # Compactar o tema filho em um arquivo zip
    # Zip the child theme into a zip file
    child_zip_path = os.path.join(output_dir, f"{child_theme_name}.zip")
    with zipfile.ZipFile(child_zip_path, "w") as zipf:
        for root, dirs, files in os.walk(child_theme_dir):
            for file in files:
                zipf.write(
                    os.path.join(root, file),
                    os.path.relpath(
                        os.path.join(root, file), os.path.join(child_theme_dir, "..")
                    ),
                )

    # Remover arquivos e diretórios temporários no Windows
    # Remove temporary files and directories on Windows
    shutil.rmtree(extracted_path)
    shutil.rmtree(child_theme_dir)

    return child_zip_path


# Exemplo de uso
# Usage example
parent_theme_zip = "/caminho/para/seu/tema.zip"  # Substitua pelo caminho do seu arquivo zip / Replace with the path to your zip file
child_theme_name = "meu-tema-filho"  # Substitua pelo nome desejado para o tema filho / Replace with the desired name for the child theme
output_dir = "/caminho/para/salvar/o/tema-filho"  # Substitua pelo diretório de saída / Replace with the output directory

child_theme_zip_path = create_wordpress_child_theme(
    parent_theme_zip, child_theme_name, output_dir
)
print(f"Tema filho criado: {child_theme_zip_path}")
