Install
=======

::

   $ git clone git://github.com/matts1/pygments-style-idleclassic.git
   $ cd pygments-style-idleclassic
   $ (sudo) python setup.py install

Usage Sample
------------
::

   >>> from pygments.formatter import HtmlFormatter
   >>> HtmlFormatter(style='idleclassic').style
   <class 'pygments_style_solarized.light.IdleClassicStyle'>


Export the style as CSS
-----------------------
::

   pygmentize -S idleclassic -f html > idleclassic.css

