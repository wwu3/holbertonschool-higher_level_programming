# PYTHON, EVERYTHING IS AN OBJECT.  

Each object has an identity, type, and value,
Everything means everything, including functions and classes. Data type is a property of the object and not of the variable.

![image](https://user-images.githubusercontent.com/113806658/218303921-475b07f0-3a23-4907-91e3-1c09c5769f36.png)

<!-- ID -->  
## id() is an inbuilt function in Python

It prints the memory address for the specified object.  All objects in Python has their own id and this is assigned to the object when it is created.

#### Syntax : id(object)
Example:

<img width="179" alt="Screenshot 2023-02-12 at 7 06 44 pm" src="https://user-images.githubusercontent.com/113806658/218299922-61942885-5b28-4d78-b1dc-3beef1a0ab6d.png">

<img width="167" alt="Screenshot 2023-02-12 at 7 07 54 pm" src="https://user-images.githubusercontent.com/113806658/218299975-5d590b1e-fc29-4158-a8ca-b5fa612a4265.png">

<!-- TYPE --> 
## type() is an inbuilt function in Python

The type() function returns the type of the specified object.  type() function is mostly used for debugging purposes.

#### Syntax: (Two different forms of type() function)
#### type(object)
Example: 

<img width="358" alt="Screenshot 2023-02-12 at 7 58 51 pm" src="https://user-images.githubusercontent.com/113806658/218301924-3a27f6ba-62ac-487e-92c8-5882dca8bf92.png">

#### type(name, bases, dict)
***Example: type() With name, bases and dict Parameters***

If three arguments (name, bases and dict) are passed, it returns a new type object.

****name****: name of class, which later corresponds to the __name__ attribute of the class.

****bases****: tuple of classes from which the current class derives. Later corresponds 
        to the __bases__ attribute.
****dict****:  a dictionary that holds the namespaces for the class. Later corresponds 
        to the __dict__ attribute.

## Mutable and Immutable objects in Python

![image](https://user-images.githubusercontent.com/113806658/218304016-a910665b-e094-4ead-aa90-af791ef7a119.png)

Every variable holds an instance of an object in Python.There are two types of objects  Mutable and Immutable objects.

A ***mutable object*** can be modified after initial defined.  Mutable ‘s id is the same, value changeable.
mutable objects including: list, dictionary, set, byte array etc.

Example: Mutable list

<img width="239" alt="Screenshot 2023-02-12 at 8 18 06 pm" src="https://user-images.githubusercontent.com/113806658/218302639-b20b9dde-74ad-4808-bdf1-a98947aa439b.png">

An ***immutable Object*** of built-in types including int, float, bool, str, tuple and unicode etc.  An immutable object can’t be changed after it is created.

Example: Immutable Typles

<img width="426" alt="Screenshot 2023-02-12 at 8 21 20 pm" src="https://user-images.githubusercontent.com/113806658/218302780-52264ad9-19b2-46e9-bb40-08ecf34e0dfa.png">

Example: Tuple allows duplicate values

<img width="442" alt="Screenshot 2023-02-12 at 8 22 39 pm" src="https://user-images.githubusercontent.com/113806658/218302832-8d1377e0-da47-40ac-a8c7-4e3ef4adba20.png">

Python tuples are immutable built-in type, but their values may change.

Example: A comma after the item when only one item, otherwise Python will not read it as tuple.

<img width="201" alt="Screenshot 2023-02-12 at 8 26 19 pm" src="https://user-images.githubusercontent.com/113806658/218302988-693c9290-b319-4f63-b068-a7a1283f9bc9.png">


Python works differently on mutable and immutable objects. Assignment in Python never copies values. It only copies references. 

According to the article from WIKIPEDIA, “...If an object is known to be immutable, it is preferred to create a reference of it instead of copying the entire object.  This is done to conserve memory by preventing data duplication and avoid calls to constructors and destructors; it also results in a potential boost in execution speed.”

There are two ways we can pass data to a function:
        
***Pass a data directly to a function***:
Example: 
        
<img width="200" alt="Screenshot 2023-02-12 at 8 30 26 pm" src="https://user-images.githubusercontent.com/113806658/218303135-43608b79-8566-4f1c-9a48-47edd15a0171.png">

***Pass a variable to a function***:
Example:
        
<img width="156" alt="Screenshot 2023-02-12 at 8 32 11 pm" src="https://user-images.githubusercontent.com/113806658/218303226-74713057-2c80-4375-bd6e-9f8045657faa.png">
   
This scenario via variable  allows us to access the data even after passing the functions.

All the values contained in the data are copied over into the function, that means if the data changs inside of the function, the data won't change outside of the funcion.  This is called pass by value.
Example:
        
<img width="218" alt="Screenshot 2023-02-12 at 8 39 41 pm" src="https://user-images.githubusercontent.com/113806658/218303575-7f7e1447-6824-4b67-956d-ab33e4ea1243.png">

When mutable data passes a function, the data isn’t copied over,  only a reference  to the data passed to the function, this is called pass by reference.  When data changes in the function, it also changes outside of the function.
Example:
 
<img width="222" alt="Screenshot 2023-02-12 at 8 41 32 pm" src="https://user-images.githubusercontent.com/113806658/218303653-058fc73c-134f-48ee-b045-caaab9c00511.png">



<!-- AUTHORS -->
### Author: Wendy Wu

