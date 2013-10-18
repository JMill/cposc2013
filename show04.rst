{% import "macros/ork.jinja" as ork with context %}

Show 04: Hobbits
*******************************************

Below are data [#]_ acquired from *The Lord of the Rings* and other books about Middle Earth by J.R.R. Tolkien.

=============  ==========================
Race            Life Expectancy (years)
=============  ==========================
Hobbits          96.0
Dwarves          194.0
Humans           163.0
=============  ==========================

If we assume that the population of Hobbits, Dwarves, and Humans is about equal, and we collectively refer to these three races as People, then what's the mean life expectancy of a Person? To calculate mean, sum all the values and then divide by how many values you summed.

.. math::

    \text{mean} = \frac{\text{sum of values}}{\text{number of values summed}}

For our Middle Earth data, the mean is calculated this way:

.. math::

    \text{mean} = \frac{96.0 + 194.0 + 163.0}{3}
    = \frac{453.0}{3}
    = 151.0 \text{ years}

The average life expectancy of a Person is 151.0 years.

What to type
============================

Lets calculate the average life expectancy of the Middle Earth People in three different ways:

{{ ork.code('code/04-01-mean_lifeexpectancy.py|pyg') }}

Save this file as ex4-life_expectancy.py. Then run it.

What you should see
============================

You should get this::

    {{ d['code/04-01-mean_lifeexpectancy.py|py']|indent(4) }}


While each approach gives the same result, each subsequent approach is more *powerful*, that is, more easily applied to much bigger and more interesting problems beyond just Hobbits, Dwarves, and Humans.  However, you are likely concerned about the stuff that appears in Approach #2 and especially in Approach #3.

Lets dig into Approach #2:

{{ ork.code('code/04-01-mean_lifeexpectancy-approach2.py|pyg') }}


In plain English, here is what the above code tells your computer to do:

- **Lines 1 and 2:** Disregard these comments because they are for humans and you are a robot.
- **Lines 3-6:** Put four numbers in four separate folders.
- **Line 7:** Get all four folders that were just created, arrange their contents in a particular way, and then stuff the result into a fifth folder, labeled 'mean'.
- **Line 8:** Display on the screen what is inside the 'mean' folder.

From now on, I will not pretend that variables are akin to physical folders.  I'll just call them variables like everyone else.  You may be comfortable with the concepts of variables, printing, and basic math in Python.  If not, do not worry -- review the code, try changing a word here, a number there, and see what happens.

Read through Approach #3 now and see if you can guess what each line does.  On a sheet of paper, write what you think is happening, line-by-line.  It's okay if you don't understand everything -- there are new concepts here that you may have never seen before. If your eyes gloss over, skip it and go to the next exercise.  You can come back later when you're more comfortable.


Study Drill
==================
Search online for "python lists". 

- Read about what they look like and some ways to use lists.
- If you see sample code, open a new window in IDLE and run the code to see what happens.


Challenge
=====================
If you think you understand Approach #3, try simplifying it.  I can shorten it to just 2 lines of code.  *Hint:* Try creating only a single variable to hold the data.



.. [#] The table does not include Elves or Ainur since they live forever unless killed. Also, there is much variation in the death dates of Dwarves due to battle and of Humans because there are several types of Humans, including First, Second, and Third Ages, as well as Númenóreans.  Data table based on work by Emil Johansson of http://lotrproject.com.


