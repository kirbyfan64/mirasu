import mirasu


def test_basic():
    class Base(object):
        def pre(self): self.xyz = 123
        def post(self): self.xyz = 123

    @mirasu.root_hook
    class Derived(Base):
        @mirasu.pre_hook
        def pre(self): assert self.xyz == 123

        @mirasu.post_hook
        def post(self): assert self.xyz == 123


    obj = Derived()
    obj.pre()
    obj.post()


def test_static():
    class Base(object):
        @staticmethod
        def pre(): xyz.append(123)
        @staticmethod
        def post(): xyz.append(123)

    @mirasu.root_hook
    class Derived(Base):
        @staticmethod
        @mirasu.pre_hook
        def pre(): assert xyz == [123]

        @staticmethod
        @mirasu.post_hook
        def post(): assert xyz == []


    xyz = []
    Derived.pre()
    assert xyz == [123]
    xyz = []
    Derived.post()
    assert xyz == [123]


def test_class():
    class Base(object):
        @classmethod
        def pre(self): self.xyz = 123
        @classmethod
        def post(self): self.xyz = 123

    @mirasu.root_hook
    class Derived(Base):
        @classmethod
        @mirasu.pre_hook
        def pre(self): assert self.xyz == 123

        @classmethod
        @mirasu.post_hook
        def post(self): assert self.xyz == 123


    Derived.pre()
    Derived.post()
