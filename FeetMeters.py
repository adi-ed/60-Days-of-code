def parse_into(feet_inches):
    feet_inches = feet_inches.split(" ")
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    return {"feet": feet, "inches": inches}



def convert_feet_inches(feet,inches):
    # print(feet_inches)
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches = input("\nEnter feet and inches: ")
parsed = parse_into(feet_inches)
res = convert_feet_inches(parsed["feet"],parsed["inches"])

print("\nConverted to meters",res,)

if res<1:
    print("\nNot allowed on the rollercoaster.")
else:
    print("\nAllowed on the rollercoaster.")