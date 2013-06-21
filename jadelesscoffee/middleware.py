from django.conf import settings

from utils import compile_all

class JadeLessCoffeeMiddleware(object):
    active = False
    def __init__(self):
        #setting to turn off jlc
        self.active = not getattr(settings,"JLC_OFFLINE",None)
        if not self.active:
            return
        #only run this guy if DEBUG is True
        if settings.DEBUG is not None and settings.DEBUG is False:
            raise django.core.exceptions.MiddlewareNotUsed
        else:
            print('JadeLessCoffee compiler will run at every request...\n');

    def process_request(self, request):
        if self.active:
            compile_all()
