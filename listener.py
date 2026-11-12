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