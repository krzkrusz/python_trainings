
def tags(tag):

    def inner_decorator(func):

        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            return f"<{tag}>{result}</{tag}>"

        return wrapper
    return inner_decorator

#@tags("span")

@tags("div")
@tags("span")
def core_string(name,firstname):
    return f"Hello {name} {firstname}"


print(core_string("Jacek", "jaki"))
