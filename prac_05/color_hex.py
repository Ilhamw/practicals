COLOR_HEX = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
               "aquamarine": "#7fffd4", "azure": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000",
               "BlanchedAlmond": "#ffebcd", "blue": "#0000ff",
               "BlueViolet": "#8a2be2", "brown": "#a52a2a"}

color_name = input("Enter color name: ")
while color_name != "":
    print(color_name, "is", COLOR_HEX[color_name] )