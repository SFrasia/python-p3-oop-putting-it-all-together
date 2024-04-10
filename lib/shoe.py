#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.codition = "New"

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
