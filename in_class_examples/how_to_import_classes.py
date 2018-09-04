from classes import TacoUser

user1 = TacoUser("Matt")
user2 = TacoUser("Will")
# user1._TacoUser__name = "Hello" # Don't do this.
user2.give_taco(user1)
print(user2)
print(user1)