from abc import ABC, abstractmethod

# Weather options
WEATHER = {"sunny", "cloudy", "rainy", "snowy"}

# Fabric options, split into light and heavy
# light for when it is hot out, heavy for when it is cold out
HEAVY = {"wool", "fleece", "knit"}
LIGHT = {"cotton", "linen", "chiffon"}


class ClothingItem(ABC):
    def __init__(self, name, color, fabric, season):
        self._name = name
        self._color = color
        self._fabric = fabric.lower()
        self._seasons = [s.lower() for s in season]

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_fabric(self):
        return self._fabric


    def matches_season(self,season):
        return season.lower() in self._seasons

    def _check_weather(self, weather):
        if weather not in WEATHER:
            raise ValueError("Invalid weather, please enter sunny, cloudy, rainy, or snowy")

    def _fabric_temp(self, temperature):
        if self._fabric in HEAVY and temperature > 70:
            return False
        if self._fabric in LIGHT and temperature < 60:
            return False
        return True


    @abstractmethod
    def is_suitable(self, weather, temperature):
        """Return True or False based on this item's suitability."""
        pass


class Top(ClothingItem):
    def is_suitable(self, weather, temperature):
        self._check_weather(weather)
        return self._fabric_temp(temperature)


class Bottom(ClothingItem):
    def is_suitable(self, weather, temperature):
        self._check_weather(weather)
        return self._fabric_temp(temperature)


class Jacket(ClothingItem):
    def __init__(self,name,color,fabric,season, waterproof):
        super().__init__(name, color, fabric, season)
        self._waterproof = waterproof
        
    def is_suitable(self, weather, temperature,):
        self._check_weather(weather)
        if weather == "rainy":
            return self._waterproof
        
        return temperature <= 70
    

