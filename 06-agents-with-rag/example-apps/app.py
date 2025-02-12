import streamlit as st
from recipe_agents import IndianRecipeCrewSystem
from datetime import datetime
import os
import random

# Initialize the recipe system
recipe_system = IndianRecipeCrewSystem()

# Create directory for recipes if it doesn't exist
RECIPE_DIR = "final_recipes"
if not os.path.exists(RECIPE_DIR):
    os.makedirs(RECIPE_DIR)

# Fun cooking messages
COOKING_MESSAGES = [
    "🎉 Voila! Your recipe is ready faster than you can say 'Where's my spice box?'",
    "✨ Recipe created! Now you're ready to cook like a pro (no pressure!)",
    "🌶️ Hot and fresh recipe coming through! Just like your future cooking!",
    "🧙‍♂️ The AI cooking wizards have worked their magic!",
    "👩‍🍳 Recipe generated! Time to channel your inner MasterChef!",
    "🎨 Your culinary canvas is ready! Time to paint with flavors!",
    "🚀 Recipe successfully launched! Mission 'Delicious Dinner' is a go!",
    "🎭 The stage is set, and your kitchen is the theater. Time to perform!",
    "🎪 The recipe circus has arrived! Let the cooking show begin!",
    "🎮 Achievement unlocked: Recipe acquired! Next level: Actually cooking it!"
]

def save_recipe_to_markdown(dish_name, raw_text):
    """Save the recipe as a markdown file with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_dish_name = "".join(x for x in dish_name if x.isalnum() or x in [' ', '-']).strip()
    clean_dish_name = clean_dish_name.replace(' ', '_').lower()
    
    filename = f"{timestamp}_{clean_dish_name}.md"
    filepath = os.path.join(RECIPE_DIR, filename)
    
    markdown_content = f"""# {dish_name} Recipe
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{raw_text}
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    return filepath

# Set up the Streamlit page
st.set_page_config(page_title="AI Indian Recipe Master", layout="wide")

st.title("🍛 AI Indian Recipe Master")
st.subheader("Your Personal Indian Cuisine Expert")

# Update the styling section with more colors and formatting
st.markdown("""
<style>
    .recipe-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section-header {
        color: #2c3e50;
        font-size: 1.5em;
        font-weight: bold;
        margin: 20px 0 10px 0;
        padding-bottom: 8px;
        border-bottom: 2px solid #e74c3c;
    }
    .ingredient-item {
        color: #34495e;
        padding: 5px 0;
        margin: 5px 0;
        font-size: 1.1em;
    }
    .instruction-item {
        color: #2c3e50;
        padding: 8px 0;
        margin: 8px 0;
        font-size: 1.1em;
        line-height: 1.6;
    }
    .nutrition-item {
        color: #27ae60;
        padding: 5px 0;
        margin: 5px 0;
        font-size: 1.1em;
    }
    .health-item {
        color: #8e44ad;
        padding: 5px 0;
        margin: 5px 0;
        font-size: 1.1em;
    }
    .recipe-title {
        color: #e74c3c;
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 3px solid #e74c3c;
    }
</style>
""", unsafe_allow_html=True)

def format_recipe_output(raw_text):
    """Format the raw recipe text into structured sections"""
    sections = {}
    current_section = None
    current_content = []
    
    # Split the raw text into lines
    lines = raw_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        lower_line = line.lower()
        if "ingredients:" in lower_line:
            if current_section and current_content:
                sections[current_section] = current_content
            current_section = "ingredients"
            current_content = []
        elif "instructions:" in lower_line or "steps:" in lower_line:
            if current_section and current_content:
                sections[current_section] = current_content
            current_section = "instructions"
            current_content = []
        elif "nutritional" in lower_line:
            if current_section and current_content:
                sections[current_section] = current_content
            current_section = "nutrition"
            current_content = []
        elif "health benefits" in lower_line:
            if current_section and current_content:
                sections[current_section] = current_content
            current_section = "benefits"
            current_content = []
        elif current_section:
            # Clean up the line
            cleaned_line = line.strip('•-*> ')
            if cleaned_line:
                current_content.append(cleaned_line)
    
    # Add the last section
    if current_section and current_content:
        sections[current_section] = current_content
    
    # Format the output HTML
    html_output = []
    
    # Format each section
    if "ingredients" in sections:
        html_output.append("""
        <div class="recipe-section">
            <h3>🧂 Ingredients</h3>
            <ul>
                {}
            </ul>
        </div>
        """.format('\n'.join(f'<li>• {item}</li>' for item in sections['ingredients'])))
    
    if "instructions" in sections:
        html_output.append("""
        <div class="recipe-section">
            <h3>👩‍🍳 Cooking Instructions</h3>
            <ol>
                {}
            </ol>
        </div>
        """.format('\n'.join(f'<li>{item}</li>' for item in sections['instructions'])))
    
    if "nutrition" in sections:
        html_output.append("""
        <div class="recipe-section">
            <h3>📊 Nutritional Information</h3>
            <ul>
                {}
            </ul>
        </div>
        """.format('\n'.join(f'<li>• {item}</li>' for item in sections['nutrition'])))
    
    if "benefits" in sections:
        html_output.append("""
        <div class="recipe-section">
            <h3>🌿 Health Benefits</h3>
            <ul>
                {}
            </ul>
        </div>
        """.format('\n'.join(f'<li>• {item}</li>' for item in sections['benefits'])))
    
    return '\n'.join(html_output)

# Create two columns for layout
input_col, output_col = st.columns([1, 2])

with input_col:
    # Create the input form
    with st.form("recipe_form"):
        dish_name = st.text_input("Enter Dish Name", "Paneer Biryani")
        dietary_restrictions = st.multiselect(
            "Dietary Restrictions",
            ["Vegetarian", "Gluten-Free", "Dairy-Free", "Low-Carb", "Non-Vegetarian", "Bengali", "South Indian", "North Indian"],
            default=["Vegetarian"]
        )
        spice_level = st.slider("Preferred Spice Level", 1, 5, 3)
        submitted = st.form_submit_button("Generate Recipe")

with output_col:
    if submitted:
        try:
            with st.spinner("🤖 AI Chefs are cooking up your recipe..."):
                # Get recipe
                result = recipe_system.get_recipe(dish_name, dietary_restrictions)
                
                if result and hasattr(result, 'raw'):
                    # Save to markdown file
                    recipe_file = save_recipe_to_markdown(dish_name, result.raw)
                    
                    # Show success message with random fun message
                    st.success(random.choice(COOKING_MESSAGES))
                    
                    # Display the recipe in a nicely formatted way
                    st.markdown(f'<div class="recipe-card">', unsafe_allow_html=True)
                    
                    # Title
                    st.markdown(f'<div class="recipe-title">{dish_name}</div>', unsafe_allow_html=True)
                    
                    # Parse and display the content
                    sections = result.raw.split('\n\n')
                    for section in sections:
                        if not section.strip():
                            continue
                            
                        section_lower = section.lower()
                        
                        if "ingredients:" in section_lower:
                            st.markdown('<div class="section-header">🧂 Ingredients</div>', unsafe_allow_html=True)
                            ingredients = section.split('\n')[1:]  # Skip the header
                            for ingredient in ingredients:
                                if ingredient.strip():
                                    st.markdown(f'<div class="ingredient-item">• {ingredient.strip()}</div>', 
                                              unsafe_allow_html=True)
                                    
                        elif "instructions:" in section_lower or "steps:" in section_lower:
                            st.markdown('<div class="section-header">👩‍🍳 Cooking Instructions</div>', unsafe_allow_html=True)
                            instructions = section.split('\n')[1:]  # Skip the header
                            for idx, instruction in enumerate(instructions, 1):
                                if instruction.strip():
                                    st.markdown(f'<div class="instruction-item">{idx}. {instruction.strip()}</div>', 
                                              unsafe_allow_html=True)
                                    
                        elif "nutritional" in section_lower:
                            st.markdown('<div class="section-header">📊 Nutritional Information</div>', unsafe_allow_html=True)
                            nutrition_info = section.split('\n')[1:]  # Skip the header
                            for info in nutrition_info:
                                if info.strip():
                                    st.markdown(f'<div class="nutrition-item">• {info.strip()}</div>', 
                                              unsafe_allow_html=True)
                                    
                        elif "health benefits" in section_lower:
                            st.markdown('<div class="section-header">🌿 Health Benefits</div>', unsafe_safe_html=True)
                            benefits = section.split('\n')[1:]  # Skip the header
                            for benefit in benefits:
                                if benefit.strip():
                                    st.markdown(f'<div class="health-item">• {benefit.strip()}</div>', 
                                              unsafe_allow_html=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Show file location with a nice format
                    st.info(f"📝 Your recipe has been saved to: {os.path.basename(recipe_file)}")
                else:
                    st.error("Oops! Our AI chefs got a bit confused. Please try again!")
        
        except Exception as e:
            st.error(f"Kitchen mishap! 🔥 {str(e)}")
    
    # Add a retry button with fun text
    if st.button("Cook Up Another Recipe! 🎲"):
        st.rerun() 