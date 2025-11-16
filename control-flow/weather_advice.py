# weather_advice.py
# Objective: Provide clothing recommendations based on specific weather conditions 
# using if, elif, and else statements.

def get_weather_advice():
    """
    Prompts the user for weather input and provides a corresponding clothing recommendation.
    """
    # Prompt user for input and convert to lowercase for case-insensitive checking
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

    print() # Add a newline for clean output

    # --- Conditional Statements ---
    if weather == "sunny":
        # Recommendation for sunny weather
        print("Wear a t-shirt and sunglasses.")
    
    elif weather == "rainy":
        # Recommendation for rainy weather
        print("Don't forget your umbrella and a raincoat.")
        
    elif weather == "cold":
        # Recommendation for cold weather
        print("Make sure to wear a warm coat and a scarf.")
        
    else:
        # Catch-all for unexpected input
        print("Sorry, I don't have recommendations for this weather.")

if __name__ == "__main__":
    get_weather_advice()