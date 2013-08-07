

class isStr(str):
    '''
    case_insensitive string calss
    '''

    def __init__ (self, *args):
        self._lowered = str.lower(self)
    def __repr__ (self):
        return '%s(%s)' % (type(self). __name__, str.__repr__(self))
    def __hash__(self):
        return hash(self.lowered)


