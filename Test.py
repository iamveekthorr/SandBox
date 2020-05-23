def test():
    weldon = 'this is a string'
    print('welcome back ', weldon)

    # Practicing closures in Python
    '''Closure is a JavaScript Concept that allows functions
        to inherit variables from outer functions even after the function has been executed
        keeping the variables in a memory heap '''

    def closure():
        test_closure = weldon + ' now i have seen closure in Python'
        print(test_closure)

    closure()

    # there should be at least two lines of space before calling another function


test()
