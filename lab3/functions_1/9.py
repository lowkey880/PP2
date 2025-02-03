def volume(R):

    Pi = 3.14

    return (4 / 3) * Pi * R**3


radius = int(input("Write a radius: "))

print(round(volume(radius), 2))