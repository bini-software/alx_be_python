weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print ("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print ("Don't forgrt your umbrella and raincoat.")
elif weather == "cold":
    print ("Make sure to wear a warm coat and a scarf.")
else:
    print ("Sorry, I don't have recommendstion for this weather.")
