####ALL possible assignment of 2n users
import itertools

def split(alist,n):
    ###find out all the possible ways to split a list into two parts
    ###n is the number you need in the treatment group
    users = set(alist)
    for comb in itertools.combinations(users,n):
        treatment = set(comb)
        control = users-treatment
        yield treatment, control

users = ["a","b","c","d","e"]
for treatment, control in split(users,2):
    print "control: ", control, "treatment", treatment
