distance = {
    "Voyager 1": 163,
    "Pioneer 10": 78,
    "New Horizons": 50
}

def main():
    for spacecraft, dist in distance.items():
        dist_km = convert(dist)
        print(f"motherfucking {spacecraft} is {dist} AU or {format_distance(dist_km)} KM from Earth")

#we want to convert distance from AU to KM and make sure this conversion is rounded up to the nearest integer.

def convert(AU):
    return int(AU * 149597870.7 + 0.999999)
#format the output to include commas as thousand separators.
def format_distance(dist):
    return f"{dist:,}"

main()