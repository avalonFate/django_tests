def makeBold(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makeBold
def test1():
    return "hello world-1"

print(test1())