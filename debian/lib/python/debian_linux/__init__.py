# Module

# Python 2.6 compat
def _compat():
    import collections

    if hasattr(collections, 'OrderedDict'):
        return

    class OrderedDict(dict):
        __slots__ = '_list',

        def __init__(self, entries=None):
            super(OrderedDict, self).__init__()
            self._list = []
            if entries is not None:
                for key, value in entries:
                    self[key] = value

        def __delitem__(self, key):
            super(OrderedDict, self).__delitem__(key)
            self._list.remove(key)

        def __setitem__(self, key, value):
            super(OrderedDict, self).__setitem__(key, value)
            if key not in self._list:
                self._list.append(key)

        def iterkeys(self):
            for i in iter(self._list):
                yield i

        def iteritems(self):
            for i in iter(self._list):
                yield (i, self[i])

        def itervalues(self):
            for i in iter(self._list):
                yield self[i]

    collections.OrderedDict = OrderedDict

_compat()
