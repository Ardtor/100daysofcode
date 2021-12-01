# Day 27

Graphical UIs using Tkinter and expanding on class/function arguments using *Args and **Kwargs

*Args is for giving many positional arguments 
**Kwargs is for many keyword arguments (KWargs) eg size="300", width="300"


## Unlimited Positional Arguments (*ARGS)

```
# the *<name> tells python that a unlimited amount of arguments may be passed through

def add(*args):
    for n in args:
        print(n)


Such as add(1,2,4,5,6,7)
```
Args are returned as a tuple, since they're positional the position they're entered in are important.

## Unlimited Positional Arguments (**KWARGS)

```
# ** denotes multiple keyword arguments

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print (n)

caculate(2,add=3,multiply=5)

Kwargs are returned as a dictionary in a key:value pairs 

```

# TKinter has three different ways of laying out widgets using layout managers

## Pack
*Pack* will place them from the top then any else below the previous one. You can add a side from top,left,right,bottom. 
As Doesn't have a precise way of laying them out

## Place
*Place* will place them using a coordinate system of x,y. The downside is that you need to manually place them but if you have dozens they can be overwhelming. 

## Grid
*Grid* allows you to divide the screen space into rows and columns relative to another widget, using row=, column = however you cannot mix it with pack








More modern alternatives to TKinter
PyQT5
Pyside2