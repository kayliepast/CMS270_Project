from clothing import WEATHER, Top, Bottom, Jacket

SEASONS = {"winter", "spring", "summer", "fall"}
WEATHER = {"sunny", "rainy", "cloudy", "snowy"}

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
        if temperature <= 70:
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
            listener.outfit_generated(outfit)
        return outfit



    def _find_match(self, category, weather, temperature, season):
        for item in self._closet:
            if isinstance(item, category) and item.matches_season(season) and item.is_suitable(weather,temperature):
                return item
        return None