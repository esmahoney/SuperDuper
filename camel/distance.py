distance = {
    "Voyager 1": 163,
    "Pioneer 10": 78,
    "New Horizons": 50
}

def main():
    for spacecraft, dist in distance.items():
        print(f"motherfucking {spacecraft} is {dist} AU from Earth")

main()