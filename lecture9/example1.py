

class Example:

    def __new__(cls, *args, **kwargs):
        print('New method')
        print(args, kwargs)
        instance = super().__new__(cls)
        return instance

    def __init__(self, argument):
        print('Init method')
        self.argument = argument
        print(f'Argument = {self.argument}')

    def __call__(self, *args, **kwargs):
        print('Call method')
        print(args, kwargs)


example = Example('some argument')

example('some attr for call function')
