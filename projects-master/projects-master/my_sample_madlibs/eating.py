def madlib():
    verb1 = input("Verb: ")
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    city1 = input("City: ")
    number1 = input("Number: ")
    name1 = input("Name: ")
    food1 = input("Food: ")
    restaurant1 = input("Restaurant: ")
    name2 = input("Name: ")
    food2 = input("Food: ")
    verb2 = input("Verb: ")
    noun1 = input("Noun: ")

    madlib = f"I like to {verb1} lunch with my coworkers. These meals are usually {adjective1} and {adjective2} " \
             f"especially since we live and work in {city1}. Every now and then, we come up with a product idea " \
             f"worth ${number1}! My team mate {name1} really likes {food1}, so we eat at {restaurant1} pretty often." \
             f" {name2} prefers {food2}, but nobody else really {verb2} it so they don't get their way very often. " \
             f"Anyway, it's getting close to {noun1} time so let's catch up again later!"

print(madlib)