from listener import OutfitListener
from clothing import Top, Bottom, Jacket
from closet import Closet
from outfitgenerator import OutfitGenerator


class ConsoleOutfitListener(OutfitListener):
    def outfit_generated(self, outfit):
        print ("Your outfit: ")
        for category, item in outfit.items():
            print(f"{category}: {item}")
        

    def outfit_failed(self, message):
        print(f"Outfit could not be completed: {message}")

def main():
    # name, color, fabric, seasons, (waterproof if jacket)
    tshirt = Top("T-shirt", "white", "cotton", ["spring", "summer", "fall"])
    jeans = Bottom("Jeans", "blue", "denim", ["spring", "summer", "fall"])
    jacket = Jacket("Jacket", "black", "leather", ["winter", "fall"], waterproof=True)

    # Closet with sample clothes
    closet = Closet()
    closet.add_item(tshirt)
    closet.add_item(jeans)
    closet.add_item(jacket)

    #Generator that reads from the closet
    generator = OutfitGenerator(closet)

    # ConsoleOutfitListener that prints outfit results
    listener = ConsoleOutfitListener()
    generator.add_outfit_listener(listener)

    # an example outfit generation.
    print("75 degrees F, sunny, summer")
    generator.generate("sunny", 75, "summer")

    # a failure caused by missing items.
    print("25 degrees F, snowy, winter")    
    generator.generate("snowy", 25, "winter")


if __name__ == "__main__":
    main()