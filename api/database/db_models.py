from odmantic import Model

class Advisor(Model):
    name: str
    expertise: str = "Finance"