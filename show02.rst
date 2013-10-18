{% import "macros/ork.jinja" as ork with context %}

Show 02: Strings, Integers, and Floats
*********************************************

Before you can use software to solve real-world problems, you have to get more familiar with Python.  It will take practice and will be hard and confusing, but it will be worth it.

Open a new script in Canopy. Type in the following code exactly. Remember, do not copy and paste. 

.. NOTE::
    For this and future exercises, I will not show you screenshots of my computer screen. Instead, I'll show you the code like below, which you will type in to your computer.
 
 
{{ ork.code('code/02-01-printing_math.py|pyg') }}

Save this file as *ex2-phoenix_weather.py*. Then click Run. 

(That ``_`` character is called "underscore". Look up how to type it with your keyboard. On my keyboard I press ``Shift`` + ``-``.)


What you should see
============================

Here is what the output of that program would look like::

    {{ d['code/02-01-printing_math.py|py']|indent(4) }}



Study Drills
==============
- In the code you typed above, what do you think the ``%s`` does?  See if you can change what appears in the ``%s`` locations without modifying a ``%s``.