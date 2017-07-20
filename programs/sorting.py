class Sorting:

    def sort_dict_values(self, d):
        l = []

        for i, j in d.iteritems():
            l.append(j)

        l.sort()
        return l

d = {"a": 1, "c": 4, "b": 2}
x = Sorting()
print x.sort_dict_values(d)
