iters = [list, tuple, set, frozenset]


class _Hack(tuple):
    pass

iters = _Hack(iters)
iters.__doc__ = """a list of iterable items like lists but not strings. Includes whichever
of lists, tuples, sets, and Sets are available in this version of Python."""


def _strips(direction, text, remove):
    if isinstance(remove, iters):
        for subr in remove:
            text = _strips(direction, text, subr)
        return text

    if direction == 'l':
        # left direction
        if text.startswith(remove):
            return text[len(remove) :]
        elif direction == 'r':
            # right direction
            if text.endswith(remove):
                return text[:-len(remove)]
        else:
            raise ValueError(f'direction {direction} needs to be either l or r')
        return text


def right_strips(text, remove):
    """
    removes the string 'remove' from the right 'text'
        >>> right_strips('foobar', 'bar')
        'foo'
    """
    return _strips('r', text, remove)


def left_strips(text, remove):
    """
    removes the string 'remove' from the left 'text'
    >>> left_strips('foobar', 'bar')
    'bar'
    >>> left_strips('https://foo.org', ['https://', 'http://'])
    'foo.org'
    """
    return _strips('l', text, remove)


def strips(text, remove):
    """
    removes the string 'remove' from the both sides of 'text'
    >>> strips('foobarfoo', 'foo')
    'bar'
    """
    return right_strips(left_strips(text, remove), remove)
