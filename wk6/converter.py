def convert(num, ingredient):
    print(f"\n> {num} cup(s) of {ingredient} = {round(num * conversions[ingredient], 2)}g")

print("=== Cups to Grams Converter ===")

# Conversion rates (cups per gram)
conversions = {
        'flour': 120,
        'sugar': 200,
        'butter': 227,
        'milk': 240,
        'cocoa': 85,
    }

convert(3, "flour")
convert(2.5, "sugar")
convert(2, "butter")
convert(1, "milk")
convert(0.5, "cocoa")
