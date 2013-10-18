{% import "macros/ork.jinja" as ork with context %}

Show 03: Variables
**********************

The following code introduces two new programming concepts, *variables* and *if-else* statements. It's okay if you don't understand everything you're typing below.


{{ ork.code('code/03-01-range_fxn_ifelse.py|pyg') }}

Save this file as driving_range.py. Then click Run.

What you should see
=======================

You should get this::

    {{ d['code/03-01-range_fxn_ifelse.py|py']|indent(4) }}


Step through the code
========================

Lets step through this code one line at a time.

**Line 1:**

::
    
    arthurDistance = 200

This line creates a variable named ``arthurDistance`` and assigns it to 'hold' a value of ``200``.  Think of ``arthurDistance`` as a folder that you place the ``200`` into.  If you ever refer to arthurDistance, its like telling Python to go to the ``arthurDistance`` folder and peek inside. 

It might help you to read this line of code right-to-left. E.g., ``200`` is put into ``arthurDistance``.

Notice the capitalization of the variable, ``arthurDistance``.  It is customary to have the first letter of a variable be lowercase with no spaces, dashes, or strange characters (such as %, $, ., or #). Subsequent words in the variable name can be capitalized, e.g. *arthur* **D** *istance*.

**Line 2:**

::
    
    belindaDistance = 300

Take the integer 300 and give it a name, ``belindaDistance``.

**Line 3:**

::
    
    driverIs = "Arthur"

Take the word "Arthur" and give it a name, ``driverIs``.  In programming, the word "Arthur" is called a *string*. A sentence such as "Arthur is happy." is also called a string.  Think of strings as just a string of letters, spaces, numbers, and punctuation in a row.  

Lines 4 and 6 are blank lines, which are used to group the code to make it more readable for us humans. The blank lines have no effect on the code's output.

**Line 5:**

::
    
    driveRange = belindaDistance - arthurDistance

This line may be tricky. To parse it, first look at what's going on to the right of the "=" (equals) sign: ``belindaDistance - arthurDistance``.  These are both variables that were created earlier in the script (see line 1 and line 2). This is just a simple equation that effectively means: ``300 - 200``, since ``belindaDistance`` is just a name for the number ``300`` and ``arthurDistance`` is just a name for the number ``200``.

To understand Line 5, Python looks up the value for ``belindaDistance`` (``300``), looks up the value for ``arthurDistance`` (``200``), subtracts the latter from the former (300 - 200 = 100), and assigns this new value (``100``) to a new variable called ``rangeDistance``.  It's not unlike what you've learned when studying algebra, except you can't readily rearrange the equation like you can with algebra.

**Line 7:**

::
    
    if driverIs == "Arthur":

This is your first look at the *if* half of an *if-else* statement. In English, this line of code tells Python, "If the variable 'driverIs' means the same thing as the word 'Arthur', then do something."  The "==" is a double equal sign. It is a way to check equivalence. E.g. "Is the thing on the left of the == the same as the thing on the right of the ==?"

In Line 3 "Arthur" was assigned to ``driverIs``, so 

::

    driverIs == "Arthur"

is True.  When an *if* statement is True, it executes the indented statements below it. In our case, this is Line 8.


**Line 8:**

::
    
        print "Car travels only %s miles" % arthurDistance

Python will print the sentence to the screen, but substitute whatever value ``arthurDistance`` holds in for the ``%s``, which is a special placeholder.

**Line 9:**

::
    
    else:

*if* statements are often followed by *else* statements. In our example, if the driver is not named "Arthur" then whatever is indented below the *else* statement will be run.  This might not make sense yet. That's okay. Tweak pieces of the code to see what happens. You will get more exposure to if-else logic in later exercises.

**Line 10:**

::
    
        print "Car goes %s to %s miles. Range: %s" % (arthurDistance, belindaDistance, driveRange)

This line is very similar to Line 8, except there are more variables to substitute.  There are three ``%s``'s.  After the string (in quotes), there is a single "%", which tells Python that the contents of the next three variables should be put in place of the three ``%s``'s, in order.  Python will make the printed statement look like this:

::
    
    Car goes 200 to 300 miles. Range: 100


It's likely that this exercise is very difficult for you if you have no prior programming experience. I've been there and know what this feels like. Carefully re-read and re-type what you don't understand. Also, I expect you to search online for additonal help.  Just type "python stuff" in a search engine, replacing "stuff" with whatever you don't understand.  Try this now: search for "python if else" and read through the first several links. You won't understand everything you read. Keep notepaper handy, writing anything you've learned on one page. On another page, keep a list of words or concepts you don't yet understand.


Study Drill
=============

- Right now the program only prints line 8. By changing only the value assigned to the *driverIs* variable in line 3, make the program print line 10 instead.  *Hint:* If the driver is not Arthur, what happens?
- Add a third option to the if-else block. *Hint:* Here's some code. Put it above the 'else' line, line 9. Be mindful of indentation.

::

    elif driverIs == "Belinda":
        print "Car travels %s miles" % belindaDistance

- After adding the code above, change only the value assigned to the ``driverIs`` variable to make the program print line 13.