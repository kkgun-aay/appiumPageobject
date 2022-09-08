import inspect


def get__function_name():
    return inspect.stack()[1][3]
