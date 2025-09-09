def main():
  spacecraft = {"name": "Voyager 1", "distance": 163}
  print (create_report(spacecraft))

def create_report(spacecraft):
  report = f"""
  =======Binky========
  
  Name: {spacecraft["name"]}
  Distance: {spacecraft["distance"]} AU

  ====================
  """
  return report

main()