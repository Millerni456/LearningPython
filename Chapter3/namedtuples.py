import collections

Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")

aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
print(aircraft.seating.maximum)

print("{0.manufacturer} {0.model}".format(aircraft))
print("{manufacturer} {model}".format(**aircraft._asdict()))
