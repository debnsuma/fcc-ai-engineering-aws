# AI Indian Recipe Master 🍛

An intelligent recipe generation system powered by AI that specializes in Indian cuisine. Using Amazon Bedrock and CrewAI, it creates detailed, personalized recipes while considering dietary restrictions and health aspects.

## Features

- 👨‍🍳 Detailed recipe generation with step-by-step instructions
- 🌶️ Customizable spice levels (1-5)
- 🥗 Multiple dietary restriction options (vegetarian, vegan, gluten-free, etc.)
- 📊 Nutritional information and health recommendations
- 💡 Cooking tips and techniques
- 💾 Automatic recipe saving with timestamps
- 🔄 Ingredient substitution suggestions
- ⏲️ Estimated cooking and prep times

## Prerequisites

1. **AWS Configuration**
   - AWS CLI installed and configured
   - Appropriate permissions for AWS Bedrock
   - Region that supports Bedrock service (e.g., us-east-1, us-west-2)
   - AWS Bedrock models enabled in your account

2. **Python Environment**
   - Python 3.9 or higher
   - pip or conda package manager

## Installation

1. Create and activate a virtual environment:
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n recipe-ai python=3.9
conda activate recipe-ai
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Configure AWS credentials:
```bash
aws configure
```

2. Start the application:
```bash
streamlit run app.py
```

3. Access the web interface at `http://localhost:8501`

4. Generate a recipe:
   - Enter the name of an Indian dish
   - Select any dietary restrictions
   - Adjust the spice level (1-5)
   - Specify any ingredient preferences or allergies
   - Click "Generate Recipe"

5. View and save:
   - Generated recipes are displayed in the UI
   - Automatically saved as markdown files in the `final_recipes` folder
   - Each file includes timestamp, dish name, and metadata

## System Components

### AI Agents

- **Master Chef**: Creates authentic recipes and cooking instructions
  - Ensures recipe authenticity
  - Provides regional variations
  - Suggests cooking techniques

- **Ingredient Specialist**: Handles ingredient details and substitutions
  - Manages ingredient proportions
  - Offers alternative ingredients
  - Provides seasonal recommendations

- **Health Advisor**: Provides nutritional guidance and health recommendations
  - Calculates nutritional values
  - Suggests dietary modifications
  - Offers health-conscious alternatives

### Generated Content
- Detailed ingredients list with measurements
- Step-by-step cooking instructions with timing
- Nutritional information per serving
- Health benefits and considerations
- Recommended consumption frequency
- Preparation and cooking time
- Storage and reheating instructions
- Serving suggestions and accompaniments

## Project Structure
```
ai-indian-recipe-master/
├── app.py                 # Streamlit web interface
├── recipe_agents.py       # AI agent definitions
├── tools/
│   └── recipe_tools.py    # Custom tools for agents
├── final_recipes/         # Generated recipe storage
├── requirements.txt       # Project dependencies
└── README.md             # Documentation
```

## Troubleshooting

If you encounter issues:
1. Verify AWS CLI configuration: `aws configure list`
2. Check AWS Bedrock service availability in your region
3. Ensure all dependencies are properly installed
4. Check the logs for specific error messages
5. Verify Bedrock model access in AWS Console
6. Check Python version compatibility
7. Ensure sufficient system memory (recommended: 4GB+)

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests as needed
5. Update documentation
6. Submit a Pull Request
