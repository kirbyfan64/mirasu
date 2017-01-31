mirasu
======

Mirasu is a Python module that uses decorators to allow methods to automatically
call ``super``. Since that's a mouthful that sounds confusing, here's an example:

.. code-block:: python

  import mirasu  # Kind of important, you know!

  class Base:
    def my_method(self):
      print('Hello from Base.my_method!!')

  @mirasu.root_hook  # This needs to be on the derived class.
  class Derived(Base):
    @mirasu.pre_hook      # pre_hook means that Base.my_method will be called
    def my_method(self):  # *before* Derived.my_method.
      print('Hello from Derived.my_method!!')
                          # (For calling it *after*, use mirasu.post_hook.)

  x = Derived()
  x.my_method()

In addition, it will automatically handle methods defined using ``staticmethod``
or ``classmethod``.

Mirasu has been tested on Python 2 *and* Python 3.

Docs
****

There's not much to it. Just take a look at
`ex.py <https://github.com/kirbyfan64/mirasu/blob/master/ex.py>`_ for an example.

FAQ
***

What does the name mean?
^^^^^^^^^^^^^^^^^^^^^^^^

*BEWARE:* Wall of text incoming.

In episode 41 of Smile PreCure! (episode 33 in the English version,
Glitter Force), Lily/Yayoi creates a hero character for the manga she's drawing.
In the English variant, the character's name is Goldenlight, but the Japanese
name makes more sense. Lily's transformation name is Glitter Peace, or Cure
Peace in the Japanese version, and the character's name is Miracle Peace. The
Japanese word is ミラクルピース, or *Mirakurupīsu*. Mirasu is that, put with a bunch
of letters taken out for ease of typing.

As for why that name, Going back to the English variant, Lily describes
Goldenlight/Miracle Peace as a "superhero" (not sure what terminology she uses in
the original JP version). When I started this project and thought of things with
"super" inside, that episode was the first thing I thought of.

Why is there an FAQ for only one question?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

...
