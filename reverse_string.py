def reverse(name):
    name_reverse=name[::-1]   #negative index
    print(name_reverse)
#name=(input("value "))
#reverse(name)

def reverse_function(text):
    output_value=list(reversed(text))  # here list for converting from reversed object into list of elemets
    reverse_string=" ".join(output_value) # " " this empty string, it will be placed bw every element of list
    print(reverse_string)
text=input("value:- ")
reverse_function(text)





''' It is about Join methodresult = " ".join(words) – How join method work in string

Understanding Each Part
1.	" " (Space String)
o	This is a separator that will be placed between each element of the words list.
o	If you change it (e.g., "-".join(words)), it will join elements with - instead.
2.	.join(words) (Join Method)
o	join() is a string method (belongs to str class).
o	It takes an iterable (like a list or tuple) and joins its elements into a single string.
o	Every element in the iterable must be a string; otherwise, it will raise an error.
3.	How it works step by step
o	The list: ["Hello", "world", "!"]
o	" ".join(words) → "Hello" + " " + "world" + " " + "!"
o	The result: "Hello world !"  '''


'''Reversed_function
Why Doesn’t reversed() Directly Show a List?
reversed() returns an iterator, not a list. Iterators do not store elements in memory;
instead, they generate elements one by one when needed.
reversed(s) creates an iterator, but printing it directly does not show the elements. 
Instead, it gives a memory reference.'''


