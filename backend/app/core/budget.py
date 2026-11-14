# Budget handling utilities

class Budget:
    def __init__(self, limit):
        self.limit = limit
    def remaining(self):
        return self.limit
