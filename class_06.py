class Third(First, Second):
    ...


class First(object):
    def __init__(self):
        print ("first")

class Second(First):
    def __init__(self):
        print ("second")

class Third(First):
    def __init__(self):
        print ("third")

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print ("that's it")


class First(object):
    def __init__(self):
        print ("first")
        
class Second(First):
    def __init__(self):
        print ("second")

class Third(First, Second):
    def __init__(self):
        print ("third")


# TypeError: Error when calling the metaclass bases
#     Cannot create a consistent method resolution order (MRO) for bases Second, First


# >>> Fourth.__mro__
(class '__main__.Fourth',
 class '__main__.Second',class '__main__.Third',
 class '__main__.First',
 type 'object')


