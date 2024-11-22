from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, features: list[str], price: float):
        self._features = features
        self.__price = price


        @abstractmethod
        def get_price(self) -> float:
            pass

        @abstractmethod
        def get_features(self) -> list[str]:
            pass


class StandardRoom(Room):
    def get_price(self) -> float:
        return self._Room__price

    def get_features(self) -> list[str]:
        return self._features


class LuxuryRoom(Room):
    def get_price(self) -> float:
        return self._Room__price

    def get_features(self) -> list[str]:
        return self._features


class FamilyRoom(Room):
    def get_price(self) -> float:
        return self._Room__price

    def get_features(self) -> list[str]:
        return self._features


class WiFiService:
    def get_wifi_description(self) -> str:
        return "High-speed Wi-Fi included."


class BreakfastService:
    def get_breakfast_description(self) -> str:
        return "Breakfast included in your stay."


class LuxuryRoom(Room, WiFiService, BreakfastService):
    def get_price(self) -> float:
        return self._Room__price

    def get_features(self) -> list[str]:
        features = self._features[:]
        features.append(self.get_wifi_description())
        features.append(self.get_breakfast_description())
        return features


class FamilyRoom(Room, WiFiService):
    def get_price(self) -> float:
        return self._Room__price

    def get_features(self) -> list[str]:
        features = self._features[:]
        features.append(self.get_wifi_description())
        return features


standard_room = StandardRoom(features=["TV", "AC"], price=100.0)
luxury_room = LuxuryRoom(features=["TV", "AC", "Mini Bar"], price=300.0)
family_room = FamilyRoom(features=["TV", "AC", "Extra Bed"], price=200.0)

