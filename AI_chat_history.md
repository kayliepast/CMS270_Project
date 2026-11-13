help me with figuring this out for my cms 270 course. this is what i need to do: Tops 

Bottoms
Jackets
Shoes
Earrings
Necklaces
Bracelets
Glasses

Requirements plan
For each of the four requirements, write 1-2 sentences saying specifically how your project will satisfy it. Not "I'll use inheritance," but "Expense is an abstract class; RecurringExpense and OneTimeExpense override amountForMonth() because a recurring expense counts every month and a one-time expense counts once."
For the design pattern you don't have to know the name yet (we cover patterns in Week 13). Describe the spot in your design where something varies, or where several parts of the program need to react to the same change. If you can't find one, say so. That's useful information, and it usually means the design needs another pass before M3.

What it is: A digital closet, where you can tell it the weather and it suggests an outfit based on what is in your closet. It will sort through your tops, bottoms, shoes, and accessories to put together a good outfit. 
Language, GUI toolkit, and test framework: Python, Tkinter + pytest
Must-have features: 

Select temperature and weather
Select vibe (Fancy, Casual, Comfy, etc…)
Select Season (Fall, Winter, Spring, Summer)

  Stretch:

Sorting dirty and clean clothes
Having images of each piece of clothing
Go deeper into color theory and fabric of the clothes
can i put denim in both?

You can, but then it does the opposite of what you want. Denim would fail both checks:

In HEAVY: not allowed above 70°F
In LIGHT: not allowed below 60°F
Jeans would only get picked between 60°F and 70°F.

Leave denim out of both. A fabric that isn’t in either set passes the temperature check at every temperature, so jeans work year-round. Your other fabrics, like nylon and polyester, work the same way.

where do i fix this 

from clothing import WEATHER, Top, Bottom, Jacket

SEASONS = {"winter", "spring", "summer", "fall"}

class OutfitGenerator:
    def __init__(self, closet):
        self._closet = closet
        self._listeners = []

    def add_outfit_listener(self, listener):
        self._listeners.append(listener)

    def generate(self, weather, temperature, season):
        weather = weather.lower()
        season = season.lower()

        if weather not in WEATHER:
            raise ValueError(f"{weather} is invalid, please enter sunny, rainy, cloudy, or snowy")
        if season not in SEASONS:
            raise ValueError(f"{season} is invalid, please enter winter, spring, summer, or fall")

        required = [Top, Bottom]

        if weather == "rainy" or   temperature <= 70:
            required.append(Jacket)

        outfit = {}
        for category in required:
            match = self._find_match(category, weather, temperature, season)
            if match is None:
                for listener in self._listeners:
                    listener.outfit_failed(f"Please add a {category.__name__} that works with this tempature and weather ")
                return None
            outfit[category.__name__] = match

        for listener in self._listeners:
            listener.outfit_ready(outfit)
        return outfit



    def _find_match(self, category, weather, temperature, season):
     for item in self._closet.get_items():
        if (
            isinstance(item, category)
            and item.matches_season(season)
            and item.is_suitable(weather, temperature)):
            return item
        return None
Checking the search function's loop for a bug.
Checking the search function's loop for a bug.
Two spots.

1. The typo is on the listener.outfit_failed(...) line in the middle of generate(). Change “tempature” to “temperature” and delete the space before the closing quote:

python
                    listener.outfit_failed(f"Please add a {category.__name__} that works with this temperature and weather")
2. _find_match has an indentation bug. That’s the main reason your outfits are failing. return None is indented inside the loop, so the method gives up after checking only the first item in the closet. Replace the whole method with this:

python
    def _find_match(self, category, weather, temperature, season):
        for item in self._closet.get_items():
            if (isinstance(item, category)
                    and item.matches_season(season)
                    and item.is_suitable(weather, temperature)):
                return item
        return None
return None now lines up with for, so it only runs after every item has been checked.

Everything else in this file is correct. Save, and make sure the matches_season fix in clothing.py is saved too, then run python3 main.py again.

something is still wrong with this loop because every time i run this it gives me this issue 75 degrees F, sunny, summer
Outfit could not be completed: Please add a Bottom that works with this temperature and weather
25 degrees F, snowy, winter
Outfit could not be completed: Please add a Top that works with this temperature and weather
kay@kaylies-mbp-56 CMS 270 Project %

The loop is fine now. The Top passes, so the loop and the season check both work. What’s left is denim is still in HEAVY in clothing.py. Your jeans are denim, and heavy fabrics are blocked above 70°F, so at 75°F there’s no Bottom that fits.

In clothing.py, change it to:

python
HEAVY = {"wool", "fleece", "knit", "leather"}
Save, then run again. You should get:

75 degrees F, sunny, summer
Your outfit:
Top: T-shirt
Bottom: Jeans
25 degrees F, snowy, winter
Outfit could not be completed: Please add a Top that works with this temperature and weather
The second one should fail, because your T-shirt isn’t marked for winter. That’s your demo of the failure case.