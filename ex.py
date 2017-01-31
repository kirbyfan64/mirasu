#!/usr/bin/env python

import mirasu


# ********************NORMAL METHODS********************


class Base(object):
    @classmethod
    def a(self): print('Inside Base.a!')
    @classmethod
    def b(self): print('Inside Base.b!')


@mirasu.root_hook
class Derived(Base):
    @classmethod
    @mirasu.pre_hook
    def a(self): print('Inside Derived.a, called *after* Base.a!')
    @classmethod
    @mirasu.post_hook
    def b(self): print('Inside Derived.b, called *before* Base.b!')


x = Derived()
x.a()
x.b()


# ********************CLASSMETHODS********************


class Base(object):
    @classmethod
    def a(cls): print('Inside classmethod Base.a!')
    @classmethod
    def b(cls): print('Inside classmethod Base.b!')


@mirasu.root_hook
class Derived(Base):
    @classmethod
    @mirasu.pre_hook
    def a(cls): print('Inside classmethod Derived.a, called *after* Base.a!')
    @classmethod
    @mirasu.post_hook
    def b(cls): print('Inside classmethod Derived.b, called *before* Base.b!')


Derived.a()
Derived.b()


# ********************STATICMETHODS********************


class Base(object):
    @staticmethod
    def a(): print('Inside staticmethod Base.a!')
    @staticmethod
    def b(): print('Inside staticmethod Base.b!')


@mirasu.root_hook
class Derived(Base):
    @staticmethod
    @mirasu.pre_hook
    def a(): print('Inside staticmethod Derived.a, called *after* Base.a!')
    @staticmethod
    @mirasu.post_hook
    def b(): print('Inside staticmethod Derived.b, called *before* Base.b!')


Derived.a()
Derived.b()
