class Person:
    def __init__(self, address, client):
        self.address = address
        self.name = None
        self.client = client
    def __repr__(self):
        return f'Person({self.address},{self.name})'

    def set_name(self, name):
        self.name = name
