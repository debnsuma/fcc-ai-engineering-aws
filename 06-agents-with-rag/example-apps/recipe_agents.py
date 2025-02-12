from crewai import Agent, Task, Crew, Process, LLM
from tools.recipe_tools import RecipeSearchTool, IngredientSubstitutionTool, CookingTipsTool

# Initialize AWS Bedrock LLM
llm = LLM(model='us.amazon.nova-pro-v1:0')

class IndianRecipeCrewSystem:
    def __init__(self):
        # Initialize tools
        self.recipe_search = RecipeSearchTool()
        self.ingredient_sub = IngredientSubstitutionTool()
        self.cooking_tips = CookingTipsTool()
        
        self.recipe_master = Agent(
            role="Master Indian Chef",
            goal="Create authentic and detailed Indian recipes with perfect spice combinations",
            backstory="""Expert chef with 30 years of experience in Indian cuisine, 
            specializing in both traditional and modern Indian cooking techniques. 
            Deep knowledge of regional variations, spice combinations, and cooking methods.""",
            llm=llm,
            tools=[self.recipe_search, self.cooking_tips]
        )
        
        self.ingredient_specialist = Agent(
            role="Ingredient and Spice Expert",
            goal="Provide detailed ingredient information and substitutions",
            backstory="""Specialized in Indian spices and ingredients, with expertise in 
            their nutritional values, combinations, and possible substitutions for dietary restrictions.""",
            llm=llm,
            tools=[self.ingredient_sub]
        )
        
        self.health_advisor = Agent(
            role="Nutritional Expert",
            goal="Provide health-conscious modifications and nutritional information",
            backstory="""Nutritionist specializing in Indian cuisine, expert at making 
            recipes healthier while maintaining authentic taste.""",
            llm=llm
        )

    def create_recipe_tasks(self, dish_name, dietary_restrictions=None):
        task1 = Task(
            description=f"Research and analyze the recipe for {dish_name}. Consider any dietary restrictions: {dietary_restrictions}. Provide detailed information about ingredients, cooking steps, and cooking methods.",
            expected_output="A detailed analysis of the recipe including ingredients, steps, and methods",
            agent=self.recipe_master
        )

        task2 = Task(
            description=f"""Analyze the ingredients for {dish_name} and provide:
            1. Detailed spice measurements
            2. Possible substitutions for dietary restrictions: {dietary_restrictions}
            3. Tips for ingredient preparation""",
            expected_output="A detailed analysis of the recipe including ingredients, steps, and methods",
            agent=self.ingredient_specialist
        )

        task3 = Task(
            description=f"""Provide comprehensive health analysis for {dish_name}:
            1. Total calories per serving
            2. Detailed macronutrients breakdown
            3. Preparation and cooking time
            4. Recommended frequency of consumption for optimal health
            5. Health benefits of key ingredients
            6. Any health precautions or considerations""",
            expected_output="A detailed nutritional analysis and health recommendations",
            agent=self.health_advisor
        )

        return [task1, task2, task3]

    def get_recipe(self, dish_name, dietary_restrictions):
        try:
            tasks = self.create_recipe_tasks(dish_name, dietary_restrictions)
            
            crew = Crew(
                agents=[self.recipe_master, self.ingredient_specialist, self.health_advisor],
                tasks=tasks,
                verbose=True
            )
            
            return crew.kickoff({
                "dish_name": dish_name,
                "dietary_restrictions": dietary_restrictions
            })
        except Exception as e:
            print(f"Error in get_recipe: {str(e)}")
            return None 