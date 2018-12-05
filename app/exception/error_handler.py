
class ErrorHandler(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, f):

        def wrapped_f(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except:
                print "Exception occure"

        return wrapped_f