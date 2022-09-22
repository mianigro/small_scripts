class Vector:

    # Setup the vector
    def __init__(self, *args):

        vector = []

        for arg in args:
            if type(arg) is int:
                vector.append(arg)

            else:
                print("Needs to be all integers.")
                break

        self.vector = vector

    # Function to determine length of the vector
    def __len__(self):
        return len(self.vector)

    # Returning printing of the vector
    def __str__(self):
        return f"{self.vector}"

    # Adding two vectors
    def __add__(self, p2):
        result = []

        if len(self) == len(p2):

            for x in range(0, len(self)):
                result.append(self.vector[x] + p2.vector[x])

            return result
        else:
            return "Vectors need to be the same length."

    # Subtracting two vectors
    def __sub__(self, p2):
        result = []

        if len(self) == len(p2):

            for x in range(0, len(self)):
                result.append(self.vector[x] - p2.vector[x])

            return result
        else:
            return "Vectors need to be the same length."

    # Dot product of two vectors
    def __mul__(self, p2):
        if len(self) == len(p2):

            result = 0

            for x in range(0, len(self)):
                result = result + self.vector[x] * p2.vector[x]

            return result
        else:
            return "Vectors need to be the same length."


p1 = Vector(6, 8, 9, 10)
p2 = Vector(5, 3, 1, 2)

print(p1)
print(p2)
print(len(p1))

out1 = p1 + p2
print(out1)

out2 = p2 + p2
print(out2)

print(p2 - p1)
print(p1 * p2)