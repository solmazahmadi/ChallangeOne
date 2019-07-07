#first quastion:color decorator

def red(fn):
    def inner(x):
        out = "\033[31m"
        out+= fn(x)
        out+= "\033[0m"
        return out
    return inner
@red
def echo(s):
    return s
print(echo("hi"))

def green(fn):
    def inner(x):
        out = "\033[32m"
        out+= fn(x)
        out+= "\033[0m"
        return out
    return inner

@green
def echo(s):
    return s

def yellow(fn):
    def inner(x):
        out = "\033[33m"
        out+= fn(x)
        out+= "\033[0m"
        return out
    return inner

@yellow
def echo(s):
    return s


# second quastion: color decorator general form

def colorize(color_name):
    color_map = {"red": 1, "green": 2, "yellow": 3, "blue": 4, "purple": 5, "cyan":6,
                 "gray":7}
    def color(fn):
        def inner(x):
            out = "\033[3"+str(color_map[color_name])+"m"
            out+= fn(x)
            out+= "\033[0m"
            return out
        return inner
    return color


@colorize("green")
def say_hello(name):
    return "Hello " + name
print((say_hello)("jack"))
#
def intensentize(intensity_of_colors):
    intensity_map={"default": 3, "highlight": 4, "exaggerated colors":9 }
    def intensity(fn):
        def inner(x):
            out="\033["+str(intensity_map[intensity_of_colors])+"1m"
            out+=fn(x)
            out+="\033[0m"
            return out
        return inner
    return intensity

@intensentize("highlight")
def say_hello(name):
    return "Hello " + name
print(say_hello("solmaz"))
#
def type_kind(font_type):
    type_map={"default": 0, "bold": 1, "underline":4, "revert": 7 }
    def types(fn):
        def inner(x):
            out="\033[31;"+str(type_map[font_type])+"m"
            out+=fn(x)
            out+="\033[0m"
            return out
        return inner
    return types

@type_kind("underline")
def say_hello(name):
    return "Hello " + name
print(say_hello("solmaz"))
