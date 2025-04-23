import subprocess
import os
from pdf2image import convert_from_path
import shutil

# Get directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to _static directory (relative to script location)
STATIC_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '../../_static'))

# Step 0: Clean up all PDFs in _static
def clean_static_dir(static_dir):
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    print(f"Cleaning up PDFs in {static_dir}...")
    for file in os.listdir(static_dir):
        if file.endswith('.pdf'):
            os.remove(os.path.join(static_dir, file))
            print(f"Removed {file}")

# Step 1: Compile all .tex files in the current directory
def compile_latex(tex_file):
    try:
        print(f"Compiling {tex_file}...")
        subprocess.run(['pdflatex', tex_file], check=True, cwd=SCRIPT_DIR)
        print(f"Compiled {tex_file} successfully.")
    except subprocess.CalledProcessError:
        print(f"Error compiling {tex_file}.")
        exit(1)

# Step 2: Convert a PDF to PNG and save in _static
def convert_pdf_to_png(pdf_path, static_dir):
    try:
        print(f"Converting {pdf_path} to PNG...")
        images = convert_from_path(pdf_path)
        output_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_png = os.path.join(static_dir, f'{output_name}.png')
        images[0].save(output_png, 'PNG')
        print(f"Saved PNG to {output_png}")
    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")
        exit(1)

# Step 3: Move a file to _static
def move_to_static(file_path, static_dir):
    try:
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        shutil.move(file_path, os.path.join(static_dir, os.path.basename(file_path)))
        print(f"Moved {file_path} to {static_dir}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")
        exit(1)

# Step 4: Clean up LaTeX-generated temporary files
def clean_aux_files(base_name):
    for ext in ['aux', 'log', 'out', 'toc', 'lof', 'lot']:
        temp_file = os.path.join(SCRIPT_DIR, f"{base_name}.{ext}")
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Main
def main():
    clean_static_dir(STATIC_DIR)

    for file in os.listdir(SCRIPT_DIR):
        if file.endswith('.tex'):
            base_name = os.path.splitext(file)[0]
            pdf_file = os.path.join(SCRIPT_DIR, f"{base_name}.pdf")

            compile_latex(file)
            convert_pdf_to_png(pdf_file, STATIC_DIR)
            move_to_static(pdf_file, STATIC_DIR)
            clean_aux_files(base_name)
        
    clean_static_dir(STATIC_DIR)

    print("All .tex files processed successfully.")

if __name__ == '__main__':
    main()
