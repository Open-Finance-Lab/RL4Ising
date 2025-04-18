import subprocess
import os
from pdf2image import convert_from_path
import shutil

# Paths to files and directories
tex_file = 'instances_dim_figure.tex'  # Your LaTeX file
output_pdf = tex_file.split('.')[0]+".pdf"  # Output PDF file name
static_dir = '../../_static/'  # Path to the _static directory in your Sphinx project

# Step 1: Run pdflatex to compile the .tex file to .pdf
def compile_latex(tex_file):
    try:
        print(f"Compiling {tex_file} using pdflatex...")
        # Run pdflatex to generate the PDF
        subprocess.run(['pdflatex', tex_file], check=True)
        print(f"Compilation successful, generated {output_pdf}.")
    except subprocess.CalledProcessError:
        print("Error during LaTeX compilation.")
        exit(1)

# Step 2: Convert the PDF to PNG using pdf2image
def convert_pdf_to_png(pdf_file, static_dir):
    try:
        print(f"Converting {pdf_file} to PNG images...")
        # Convert the PDF to images (one image per page)
        images = convert_from_path(pdf_file)
        
        # Save each page as a PNG file in the _static directory
        for i, image in enumerate(images):
            output_name = pdf_file.split('.')[0]
            output_png = os.path.join(static_dir, f'{output_name}.png')
            image.save(output_png, 'PNG')
            print(f"Saved PNG image: {output_png}")
    except Exception as e:
        print(f"Error during PDF to PNG conversion: {e}")
        exit(1)

# Step 3: Move the generated files to the _static folder (if necessary)
def move_to_static(output_pdf, static_dir):
    try:
        # Ensure the _static directory exists
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)

        # Move the PDF to the _static directory
        if os.path.exists(output_pdf):
            shutil.move(output_pdf, os.path.join(static_dir, output_pdf))
            print(f"Moved PDF to {static_dir}.")

    except Exception as e:
        print(f"Error moving files: {e}")
        exit(1)

def clean_up(filename):
    # Remove .aux, .log, and other temporary files generated during LaTeX compilation
    for ext in ['aux', 'log', 'out', 'toc', 'lof', 'lot']:
        temp_file = f"{os.path.splitext(filename)[0]}.{ext}"
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Main execution
def main():
    # Step 1: Compile the LaTeX file
    compile_latex(tex_file)
    
    # Step 2: Convert the PDF to PNG images
    convert_pdf_to_png(output_pdf, static_dir)
    
    # Step 3: Move the PDF to _static folder
    move_to_static(output_pdf, static_dir)

    clean_up(output_pdf.split(".")[0])
    
    print("Process completed successfully.")

if __name__ == '__main__':
    main()