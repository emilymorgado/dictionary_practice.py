colors = {
	"green": {
		"pink": ["red", "white"],
		"maroon": ["red", "purple"]
	},
	"grey": {
		"sky": ["blue", "white"],
		"purple": ["blue", "red"]
	}
}

def print_colors(input_dict):
    """Iterates both the dictionaries and the lists and prints logical sentences
        list.items() indexes items, making looping possible"""

    for lead_color, secondary_colors in colors.items():
        # print lead_color, "is unrelated to the others"
            # the above line runs, bt the next print is even better!
        printable_secondary_colors = secondary_colors.keys()
        print lead_color, "is unrealted to {} and {}".format(printable_secondary_colors[0], printable_secondary_colors[1])
        
        for secondary_colors, color_mixes in secondary_colors.items():
            print "{} is made of {} and {}".format(
                                                    secondary_colors, 
                                                    color_mixes[0], 
                                                    color_mixes[1]
                                                    )

print_colors(colors)





# print colors["red"]
# {'pink': ['red', 'white'], 'maroon': ['red', 'purple']}

# print colors["red"]["pink"]
# ['red', 'white']

# print colors["red"]["pink"][1]
# 'white'

# print colors["red"]["pink"][1][0]
# 'w'
