# string concatenation (adding strings together)
# as if we want to create a string: "subscribe to _____"

# youtuber = "Think Lowd" # some string variable
#
# # a few ways to do the same thing
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Blockchain is futuristic and {adj}. I'm always eager to learn more and {verb1}. Some people have fun " \
         f"when they {verb2}. {famous_person} has fun when they buy more bitcoin!!"

print(madlib)