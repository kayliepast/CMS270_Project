**1. Topic and scope**

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


**3. Requirements plan**

1. A class design with at least one clear use of inheritance or interfaces
ClothingItem is an abstract class, it will store name, color, fabric, and season. ClothingItem will declare an abstract method is_suitable(weather, temperature). Top, bottom, jacket, socks, and shoes will extend from ClothingItem. There will be another Accessory Abstract class for glasses, necklace, earring, and bracelet classes. All of the accessories won’t be affected by the temperature, but sunglasses will be the only object that will depend on the weather. 

2. A functioning graphical user interface
The Tkinter window will have a dropdown for weather, vibe, and season as well as a slider for temperature. Once that is filled out, then the “Find me an outfit” button will be able to be pressed. When the button is clicked, it will list an item from each category.

3. At least one design pattern, applied deliberately (not just present by accident)
A really important design pattern will be the way that the outfits will be generated based off of the vibe. Fancy, Casual, and Comfy have some overlap when it comes to fabrics, but they also have strict rules that make them different from each other. So each vibe will have its own set of rules so the generations are accurate. 

4. A test suite covering the core logic, at 70% code coverage or higher
The logic is going to be separate from the GUI. In addition, the logic that needs to be followed in order to make this project useful. So there will be many tests in order to ensure that:
If the temp is > 70 F then the outfit has no jacket 
If the weather is rainy, then a rain jacket is part of the outfit
If the outfit is fancy, no comfy clothing items are picked
If there is not enough items for a specific weather, vibe, and temperature, then there is an error message rather than it giving something inaccurate or generating nothing at all.
if the weather is <70 then the outfit will have a jacket
specific colors that will correlate to each season, with colors like black, white, and beige being able to be worn no matter the season


**4. Event-driven design**
The event is the outfit being put together or “generated”. When the outfitGenerator finishes, it calls outfit_ready(outfit) on every listener registered through add_outfit_listener() as long as there are enough matching items. If there are not enough matching items, then outfit_failed(message) will be called. OutfitListener is an abstract class that declares those two methods. Once there is a GUI, the outfit display panel will be the listener so it will show the outfit or error message. 
