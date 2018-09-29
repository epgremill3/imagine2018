# add names, delete a name
vehicles = []


def delete_vehicle(a):
    vehicles.remove(a)

def main():
    a = "Vehicle A"
    b = "Vehicle B"
    c = "Vehicle C"
    d = "Vehicle D"
    e = "Vehicle E"
    f = "Vehicle F"

    vehicles.append(a)
    vehicles.append(b)
    vehicles.append(c)
    vehicles.append(d)
    vehicles.append(e)
    vehicles.append(f)

    delete_vehicle(c)

    print(vehicles)


main()
