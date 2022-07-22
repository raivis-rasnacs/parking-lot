class ParkingLot:
    def __init__(self):
        self.p = []

    def newFloor(self):
        self.p.append([])

    def removeFloor(self):
        self.p.pop()

    def addCars(self, floor, amount):
        try:
            if self.p[floor]:
                self.p[floor] += amount
            else:
                self.p[floor] = amount
        except IndexError:
            print("Stāvs neeksistē!")

    def removeCars(self, floor, amount):
        if amount <= self.p[floor]:
            try:
                self.p[floor] -= amount
            except IndexError:
                print("Stāvs neeksistē!")
        else:
            print("Pārāk liels skaits")

P = ParkingLot()
pass
