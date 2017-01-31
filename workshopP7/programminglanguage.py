class Programminglanguage:
    def __init__(self,name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection ={}, First appeared in {}".\
        format(self.name, self.typing, self.reflection, self.year)
    def is_dynamic(self, avai):
        if self.typing == "Dynamic":
            available = True
        elif self.typing == "Static":
            available = False
        return available