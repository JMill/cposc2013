{% import "macros/ork.jinja" as ork with context %}

Show 06: More Rowing
*******************************

In the previous exercise you calculated the mean weight of the Cambridge crew and then the mean weight of the Oxford crew.  You surely noticed that writing the code to calculate Oxford's mean was pretty easy since it used the same procedure as the code to calculate Cambridge's mean.

The process for calculating the mean is:

1. Put the data in a list.
#. Get the sum of the list.
#. Count how many items are in the list. (Its "length".)
#. Divide the sum by the count.

When working with code, it's common to find yourself repeating a calculation many times.  Computer programmers don't like to repeat themselves, so, to save yourself time, you can put the calculation into a **function**.  When you *define* a function, it's like a recipe for serving ice cream: 

1. Get ice cream
#. Get cone
#. Scoop ice cream into cone
#. Serve


Your first functions
======================

Before you can use your own function, you must define the function. Defining a function is similar to how dictionaries define words. 
    
- **What is the meaning of a particular word?** *It means this, that, or something else.*
- **What is the meaning of a particular function?** *It's defined as doing this, that, or something else.*

You will now define one function, calling it ``mean()``, and the use ``mean()`` to calculate stuff. Type this code:

{{ ork.code('code/06-01-mean-function.py|pyg') }}

Save the program as *my-mean-function.py*.


What you should see
=====================

After clicking Run, you should get::

    {{ d['code/06-01-mean-function.py|py']|indent(4) }}

By making your own function, you just saved yourself a lot of work, since you didn't have to calculate by hand the averages. 

Programmers are lazy, so they make the computer do as much work as possible. This means there is more time to get ice cream. Hooray for functions.



Study Drills
===============

- Go outside and measure five things of the same type, then write a program that calculates the average of the five measurements using the ``mean()`` function above.  For example, find five trees and attempt to hug them. How many percent of a hug is each tree?  A small tree may be 0.25 hugs, an established tree may be 1.0 hug, and a big old tree may be 1.5 or more hugs. Be sure to perform the average calculation by hand as well, just to double check your work.