class Student:
    """ Represents a student."""
    def __init__(self, name, number_of_scores):
        self._name = name
        self._scores =[]
        for score in range(number_of_scores):
            self._scores.append(0)

    def get_name(self):#returns student's name
        return self._name

    def set_score(self, i, score):  # reset the ith score, counting from 1
        self._scores[i - 1] = score


    def get_score(self, i):    #returns the ith score, counting from 1
        return self._scores[i - 1]



    def get_average(self):
        return sum(self._scores) / len(self._scores)

    def get_high_score(self):
        return max(self._scores)

    def __str__(self):
        return "name: " + self._name +\
               "\nscores: " + " ".join(map(str, self._scores))

print(Student("solmaz", 3).get_score(1))
print(Student("solmaz", 3).set_score(2, 100))
print(Student("solmaz", 3))
help(Student)