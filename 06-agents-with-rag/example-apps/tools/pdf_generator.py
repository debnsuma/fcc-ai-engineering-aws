from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
import tempfile

class PDFGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.style_header = ParagraphStyle(
            'CustomHeader',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30
        )
        self.style_subheader = ParagraphStyle(
            'CustomSubHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=20
        )
        self.style_body = ParagraphStyle(
            'CustomBody',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=12
        )

    def generate_recipe_pdf(self, recipe_data, filename):
        # Create a temporary directory if it doesn't exist
        temp_dir = "temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        # Create the PDF
        pdf_path = os.path.join(temp_dir, filename)
        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )

        # Container for PDF elements
        elements = []

        # Title
        elements.append(Paragraph("Indian Recipe Master", self.style_header))
        elements.append(Spacer(1, 12))

        # Recipe Overview
        if "recipe" in recipe_data:
            elements.append(Paragraph("Recipe Overview", self.style_subheader))
            elements.append(Paragraph(f"Cooking Time: {recipe_data['recipe']['cooking_time']}", self.style_body))
            elements.append(Paragraph(f"Difficulty: {recipe_data['recipe']['difficulty']}", self.style_body))
            elements.append(Paragraph(f"Servings: 4", self.style_body))
            if recipe_data['recipe']['description']:
                elements.append(Paragraph(recipe_data['recipe']['description'], self.style_body))
            elements.append(Spacer(1, 12))

        # Ingredients
        if "shopping_list" in recipe_data:
            elements.append(Paragraph("Ingredients", self.style_subheader))
            for section, items in recipe_data['shopping_list'].items():
                if items:
                    elements.append(Paragraph(section.replace('_', ' ').title() + ":", self.style_body))
                    for item in items:
                        elements.append(Paragraph(f"• {item}", self.style_body))
            elements.append(Spacer(1, 12))

        # Cooking Instructions
        if "cooking_guide" in recipe_data:
            elements.append(Paragraph("Cooking Instructions", self.style_subheader))
            for section, steps in recipe_data['cooking_guide'].items():
                if steps:
                    elements.append(Paragraph(section.replace('_', ' ').title() + ":", self.style_body))
                    for i, step in enumerate(steps, 1):
                        elements.append(Paragraph(f"{i}. {step}", self.style_body))
            elements.append(Spacer(1, 12))

        # Build PDF
        doc.build(elements)
        return pdf_path 