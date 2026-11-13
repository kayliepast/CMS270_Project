from abc import ABC, abstractmethod


class OutfitListener(ABC):
    @abstractmethod
    def outfit_ready(self, outfit):
        """Called when an outfit is successfully generated."""
        pass

    @abstractmethod
    def outfit_failed(self, message):
        """Called when an outfit cannot be generated."""
        pass

class PrintListener(OutfitListener):
    def outfit_ready(self, outfit):
        print("Your outfit is ready! It is your:")
        for category, item in outfit.items():
            print(f"{category}: {item.get_name()}")

    def outfit_failed(self, message):
        print(f"Your outfit failed because {message}")