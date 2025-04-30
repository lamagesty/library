class Price:
    def get_charge(self, days_rented: int) -> float:
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        pass


class RegulaPrice(Price):
    pass


class NewReleasePrice(Price):
    pass


class ChildrenPrice(Price):
    pass
