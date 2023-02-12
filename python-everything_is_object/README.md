# Python, everything is an Object.  

Each object has an identity, type, and value,
Everything means everything, including functions and classes. Data type is a property of the object and not of the variable.

![python-logo](https://user-images.githubusercontent.com/113806658/218299554-4f230a57-2a33-41ad-b64a-88678e6c6aaf.jpg)

<!-- ID -->  
## id() is an inbuilt function in Python.

It prints the memory address for the specified object.  All objects in Python has their own id and this is assigned to the object when it is created.

### Syntax : id(object)
Example:

<img width="179" alt="Screenshot 2023-02-12 at 7 06 44 pm" src="https://user-images.githubusercontent.com/113806658/218299922-61942885-5b28-4d78-b1dc-3beef1a0ab6d.png">

<img width="167" alt="Screenshot 2023-02-12 at 7 07 54 pm" src="https://user-images.githubusercontent.com/113806658/218299975-5d590b1e-fc29-4158-a8ca-b5fa612a4265.png">


<!-- TYPE --> 
## type() is an inbuilt function in Python.

The type() function returns the type of the specified object.  type() function is mostly used for debugging purposes.

### Syntax: (Two different forms of type() function)
### type(object)
### type(name, bases, dict)

Example: single argument 


Example: type() With name, bases and dict Parameters
If three arguments (name, bases and dict) are passed, it returns a new type object.
Parameters:
name: name of class, which later corresponds to the __name__ attribute of the class.
bases : tuple of classes from which the current class derives. Later corresponds 
        to the __bases__ attribute.
dict :  a dictionary that holds the namespaces for the class. Later corresponds 
        to the __dict__ attribute.







Every variable holds an instance of an object in Python.There are two types of objects  Mutable and Immutable objects.
A mutable object can be modified after initial defined.  Mutable ‘s id /memory address is the same, value changeable

mutable objects including: list, dictionary, set, byte array etc.
Example: Mutable list

Immutable Objects of built-in types including int, float, bool, str, tuple and unicode etc.  An immutable object can’t be changed after it is created.
Example: Immutable Typles

Example: Tuple allows duplicate values



Python tuples are immutable built-in type,, but their values may change.
Example: A comma after the item when only one item, otherwise Python will not read it as tuple.

>>> 1, 2 + 3
(1, 5)
>>> ("the", 1, ("and", "only"))
('the', 1, ('and', 'only'))
>>> type( (10, 20) )
<class 'tuple'>
Empty and one-element tuples have special literal syntax.
>>> ()    # 0 elements
()
>>> (10,) # 1 element
(10,)




Assignment in Python never copies values. It only copies references. So when I wrote skills = t_doom[1] I did not copy the list at t_doom[1], I only copied a reference to it, which I then used to change the list by doing skills.append('rap').


Python works differently on mutable and immutable objects.  According to the article <<Immutable object>> from WIKIPEDIA, “...If an object is known to be immutable, it is preferred to create a reference of it instead of copying the entire object.  This is done to conserve memory by preventing data duplication and avoid calls to constructors and destructors; it also results in a potential boost in execution speed.”












Two ways we can pass data to a function:
Pass a data directly to a function:



Or via a variable to a function:



This scenario via variable  allows us to access the data even after passing the functions.


All the values contained in the data are copied over into the function, that means if the data changs inside of the function, the data won't change outside of the funcion.  This is called pass by value.
Example:





When mutable data passes a function, the data isn’t copied over,  only a reference  to the data passed to the function, this is called pass by reference.  When data changes in the function, it also changes outside of the function.
Example:



