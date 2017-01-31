# mirasu.py

# Copyright (c) 2017 Ryan Gonzalez

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

__version__ = '0.1'
__all__ = ['pre_hook', 'post_hook', 'root_hook']

import inspect, functools


def _hook(fn, hook):
    if not inspect.isfunction(fn):
        raise TypeError("Non-function type %s passed to %s_hook" % (type(fn), hook))
    fn._mirasu_hook = hook


def pre_hook(fn):
    _hook(fn, 'pre')
    return fn


def post_hook(fn):
    _hook(fn, 'post')
    return fn


def _descriptor(cls, name, method):
    if inspect.ismethod(method) and method.__self__ is cls:
        return classmethod

    for source in cls.mro():
        if name in source.__dict__:
            if isinstance(source.__dict__[name], staticmethod):
                return staticmethod
            else:
                return None


_null = object()


def _partial(fn, *args):
    return lambda *args2, **kw: fn(*(args + args2), **kw)


def root_hook(cls):
    for name in dir(cls):
        member = getattr(cls, name)
        hook = getattr(member, '_mirasu_hook', None)
        if hook is not None:
            assert inspect.isfunction(member) or inspect.ismethod(member)
            assert hook in ('pre', 'post')

            # The underscores are to avoid kw conflicts.
            def super_(___A, ___B, ___NAME, *args, **kw):
                getattr(super(___A, ___B), ___NAME)(*args, **kw)
            def nothing(*args, **kw): pass

            if hook == 'pre':
                pre, post = super_, nothing
            else:
                pre, post = nothing, super_

            descr = _descriptor(cls, name, member)
            if descr is staticmethod:
                # Again, argument names are two avoid conflicts.
                def new(___CLS, ___NAME, ___MEMBER, ___PRE, ___POST, ___DESCR,
                        *args, **kw):
                    ___PRE(___CLS, ___CLS, ___NAME, *args, **kw)
                    ___MEMBER(*args, **kw)
                    ___POST(___CLS, ___CLS, ___NAME, *args, **kw)
            else:
                def new(___CLS, ___NAME, ___MEMBER, ___PRE, ___POST, ___DESCR,
                        ___SELF=_null, *args, **kw):
                    if ___SELF is _null:
                        # Let the normal error handler take care of things.
                        ___MEMBER(*args, **kw)
                    else:
                        ___PRE(cls, ___SELF, ___NAME, *args, **kw)
                        if ___DESCR is None:
                            ___MEMBER(___SELF, *args, **kw)
                        else:
                            ___MEMBER(*args, **kw)
                        ___POST(cls, ___SELF, ___NAME, *args, **kw)

            new = functools.wraps(member)(_partial(new, cls, name, member, pre,
                                                   post, descr))
            if descr is not None:
                new = descr(new)

            setattr(cls, name, new)

    return cls
