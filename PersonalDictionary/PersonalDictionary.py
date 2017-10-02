Personal = {}
Personal["First name"] = "David"
Personal["Age"] = "28"
Personal["City of Birth"] = "Chicago"
Personal["Country of Birth"] = "U.S.A"
def Dict(thing2list):
    for key, data in thing2list.iteritems():
        print "my", key, "is", data
Dict(Personal)