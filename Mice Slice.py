# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)  # Count the number of occurrences of 2 in prices
num_pizzas = len(toppings)  # Find the length of the
# print(num_two_dollar_slices)
print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]

]

pizza_and_prices.sort()  # Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
# print(pizza_and_prices)
# print(sorted(pizza_and_prices)) # the same as .sort()
cheapest_pizza = pizza_and_prices[0]
# print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
# print(priciest_pizza)
pizza_and_prices.pop()
print(*pizza_and_prices, sep="\n")
print(10 * "-----")
pizza_and_prices.insert(4, [2.5, "peppers"])
# print(*pizza_and_prices, sep="\n")

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)