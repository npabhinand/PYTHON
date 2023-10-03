import colorgram
colors=colorgram.extract('color.jpg',30)

rgb_colors=[]
for i in colors:
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.b
    color=(r,g,b)
    rgb_colors.append(color)
print(rgb_colors)