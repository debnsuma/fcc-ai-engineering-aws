from langchain.tools import BaseTool
import json
from typing import Optional, Type
from pydantic import BaseModel, Field

class RecipeSearchInput(BaseModel):
    dish_name: str = Field(..., description="Name of the Indian dish to search for")
    dietary_restrictions: Optional[list] = Field(None, description="List of dietary restrictions")

class RecipeSearchTool(BaseTool):
    name = "recipe_search"
    description = "Search for authentic Indian recipes and cooking methods"
    args_schema: Type[BaseModel] = RecipeSearchInput
    
    def _run(self, dish_name: str, dietary_restrictions: Optional[list] = None) -> str:
        # Implement basic recipe template based on dish name
        recipe_template = {
            "name": dish_name,
            "cooking_time": "45 minutes",
            "difficulty": "medium",
            "servings": 4,
            "base_ingredients": [
                "Main ingredients will be listed based on the dish",
                "Common Indian spices (turmeric, cumin, coriander)",
                "Cooking oil",
                "Salt to taste"
            ],
            "method": [
                "Preparation steps will be generated",
                "Cooking steps will follow",
                "Final garnishing instructions"
            ]
        }
        return json.dumps(recipe_template, indent=2)

class IngredientSubstitutionInput(BaseModel):
    ingredient: str = Field(..., description="Ingredient to find substitutions for")
    dietary_restriction: Optional[str] = Field(None, description="Specific dietary restriction")

class IngredientSubstitutionTool(BaseTool):
    name = "ingredient_substitution"
    description = "Find suitable substitutions for ingredients based on dietary restrictions"
    args_schema: Type[BaseModel] = IngredientSubstitutionInput
    
    def _run(self, ingredient: str, dietary_restriction: Optional[str] = None) -> str:
        # Common substitution dictionary
        substitutions = {
            "ghee": {
                "vegan": "coconut oil or vegetable oil",
                "dairy-free": "coconut oil or vegetable oil"
            },
            "cream": {
                "vegan": "coconut cream",
                "dairy-free": "cashew cream or coconut cream"
            },
            "paneer": {
                "vegan": "firm tofu",
                "dairy-free": "firm tofu"
            },
            "yogurt": {
                "vegan": "coconut yogurt",
                "dairy-free": "coconut yogurt or soy yogurt"
            }
        }
        
        if ingredient.lower() in substitutions:
            if dietary_restriction and dietary_restriction.lower() in substitutions[ingredient.lower()]:
                return f"For {ingredient}, you can use {substitutions[ingredient.lower()][dietary_restriction.lower()]}"
            return f"Common substitutes for {ingredient}: {', '.join(set(sub for diet in substitutions[ingredient.lower()].values() for sub in sub.split(' or ')))}"
        
        return f"No specific substitutions found for {ingredient}. Consider consulting with a culinary expert."

class CookingTipsInput(BaseModel):
    technique: str = Field(..., description="Cooking technique to get tips for")
    skill_level: Optional[str] = Field("intermediate", description="Skill level of the cook")

class CookingTipsTool(BaseTool):
    name = "cooking_tips"
    description = "Get expert tips for Indian cooking techniques"
    args_schema: Type[BaseModel] = CookingTipsInput
    
    def _run(self, technique: str, skill_level: Optional[str] = "intermediate") -> str:
        # Dictionary of cooking tips
        tips_database = {
            "tempering": [
                "Heat oil until it shimmers but doesn't smoke",
                "Add spices in the correct order - harder seeds first",
                "Keep a lid handy to control spluttering",
                "Don't burn the spices - they should release aroma"
            ],
            "marination": [
                "Use yogurt-based marinades for tender meat",
                "Let marinate for at least 4 hours, preferably overnight",
                "Bring to room temperature before cooking",
                "Pat dry excess marinade before cooking"
            ],
            "rice_cooking": [
                "Rinse rice until water runs clear",
                "Use the correct water ratio (usually 1:2)",
                "Let rice rest for 5-10 minutes after cooking",
                "Fluff with fork, don't stir with spoon"
            ],
            "masala_grinding": [
                "Dry roast spices before grinding",
                "Let spices cool completely",
                "Grind in small batches for best results",
                "Store in airtight containers"
            ]
        }
        
        technique_key = technique.lower().replace(" ", "_")
        if technique_key in tips_database:
            tips = tips_database[technique_key]
            return f"Tips for {technique}:\n" + "\n".join(f"- {tip}" for tip in tips)
        
        return f"No specific tips found for {technique}. Consider consulting with an Indian cuisine expert." 