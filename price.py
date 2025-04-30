class Price:
    def get_charge(self, days_rented: int) -> float:
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        pass


class RegulaPrice(Price):
    def get_charge(self, days_rented: int) -> float:
        amount = 2
        if days_rented > 2:
            amount += (days_rented - 2) * 1.5
        return amount

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return 1


class NewReleasePrice(Price):
    def get_charge(self, days_rented: int) -> float:
        return days_rented * 3

    def get_frequent_renter_points(self, days_rented: int) -> int:
        points = 1
        if days_rented > 1:
            points += 1
        return points


class ChildrenPrice(Price):
    def get_charge(self, days_rented: int) -> float:
        amount = 1.5
        if days_rented > 3:
            amount += (days_rented - 3) * 1.5
        return amount

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return 1