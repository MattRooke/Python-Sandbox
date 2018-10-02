class MyEception (Exception):
    """My custom exeption"""
    pass


class BlankInput (Exception):
    """Blank Input Exception"""
    pass


user_input = input(">")

if not user_input:
    raise BlankInput