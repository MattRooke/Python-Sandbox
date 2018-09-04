class TacoUser:  # saved as TacoUser.py
    def __init__(self, name="", num_tacos=5, score=0):
        """Ths creates and object of a type TacoUser"""
        self.__name = name
        self.num_tacos = num_tacos
        self.score = score

    """Facilitators for the user:"""
    def get_name(self):
        return self.__name

    def get_num_tacos(self):
        return self.num_tacos

    def get_score(self):
        return self.num_tacos

    def update_num_tacos(self, n):
        self.num_tacos = n

    def give_taco(self, receiving_user):
        self.num_tacos -= 1
        self.score += 1
        receiving_user.num_tacos += 1

    def __str__(self):
        return "{}, {} points, {} tacos left.".format(self.__name, self.score, self.num_tacos)


if __name__ == "__main__":
    user1 = TacoUser("Matt")
    user2 = TacoUser("Will")
    # user1._TacoUser__name = "Hello" # Don't do this.
    user2.give_taco(user1)
    print(user2)
    print(user1)
