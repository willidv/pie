print "hello world!"
x = "hello world"
y = 42
print y
first_name = "david "
last_name = "williams"
print "my name is {}{}".format(first_name, last_name)
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

''' 
LIST OF COMMON STRING METHODS!!
GO TO THIS WEBSITE FOR A FULL LIST: https://docs.python.org/2.6/library/string.html
.string.count(substring): returns number of occurrences of substring in string.
.string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
.string.find(substring): returns the index of the start of the first occurrence of substring within string.
.string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. 
    1) Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
.string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
.string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
'''
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
Lists = arrays (in javascript)
    .append = .push ==> e.g: x = [1,3,5,7]
    x.append(99)
    x = [1,3,5,7,99]
    complete list of methods for lists found at this site: http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14s07.html
    complete list of functions for lists found at this site: https://docs.python.org/2/library/functions.html
'''
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

if age >= 18:
    #colon instead of curly brackets
  print 'Legal age'
  #no semi colon needed after "run code" section
elif age == 17:
    # does not need "else if"
  print 'You are seventeen.'
else:
  print 'You are so young!'
'''
  site for checking conditions for conditionals: https://docs.python.org/2/library/stdtypes.html
'''
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
'''
FOR LOOP IN PYTHON
for <counter> in <sequence or range>:
  # do something

1)example: for val in "string":
  if val == "i":
    break
  print val
  will give an output of 
  s
  t
  r 
  and then it will break 

is the same as FOR LOOP IN JAVASCRIPT
for(counter = 0; counter < range; counter ++){
    //do something
}
while loops are the same in both languages except for the colon/curly bracket difference
while <expression>:
  # do something
'''
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''