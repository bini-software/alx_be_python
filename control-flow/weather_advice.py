weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print ("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print ("Take an umbrella.")
elif weather == "cold":
    print ("Wear coat.")
else:
    print ("Sorry, I don't have recommendation for this weather.")
