def main():
  spacecraft = {"name": "Voyager 1",
                "distance": 163,
                "mission": "Exploration of the outer solar system",
                "Captain": "James T. Kirk"
                }
  spacecraft.update({"status": "active", 
                     "location": "interstellar space",
                     "fuel": "75%"})
  print (create_report(spacecraft))

def create_report(spacecraft):
  report = f"""
  =======Binky========

  Name: {spacecraft.get("name", "Unknown")}
  Distance: {spacecraft.get("distance", "Unknown")} AU
  Mission: {spacecraft.get("mission", "Unknown")}
  Captain: {spacecraft.get("Captain", "Unknown")}
  Status: {spacecraft.get("status", "Unknown")}
  Location: {spacecraft.get("location", "Unknown")}
  Fuel: {spacecraft.get("fuel", "Unknown")}

  ====================
  """
  return report

main()