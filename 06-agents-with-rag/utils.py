import os
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
import numpy as np


os.environ["TOKENIZERS_PARALLELISM"] = "false" 

# Wrapper function to convert PDFs into a dictionary of PIL images which will be used to create embeddings
def convert_pdfs_to_images(pdf_folder, poppler_path="/opt/homebrew/bin"):
    """Convert PDFs into a dictionary of PIL images."""
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    all_images = []

    for doc_id, pdf_file in enumerate(pdf_files):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        
        for page_num, image in enumerate(images):
            all_images.append({"doc_id": doc_id, 
                               "page_num": page_num, 
                               "image": image.convert("RGB")})

    return all_images

def display_image_grid(images, num_cols=5, figsize=(15, 10)):
    """
    Display a grid of images using matplotlib.
    
    Args:
        images: List of images to display (PIL Images or numpy arrays)
        num_cols: Number of columns in the grid (default: 5)
        figsize: Figure size as tuple (width, height) (default: (15, 10))
    """
    # Convert PIL Images to numpy arrays if needed
    if isinstance(images[0], np.ndarray):
        image_arrays = images
    else:
        image_arrays = [np.array(img) for img in images]
    
    num_images = len(image_arrays)
    num_rows = (num_images + num_cols - 1) // num_cols  # Calculate needed rows
    
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    if num_rows == 1:
        axes = [axes]  # Handle single row case
    axes = np.array(axes).flat  # Flatten axes array for easier iteration
    
    # Display images
    for i in range(num_cols * num_rows):
        ax = axes[i]
        if i < num_images:
            ax.imshow(image_arrays[i])
        ax.axis("off")
        
    plt.tight_layout()
    plt.show()