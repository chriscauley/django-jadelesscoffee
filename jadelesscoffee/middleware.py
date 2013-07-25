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

    def process_request(self, request):
        if not self.active or request.is_ajax():
            return
        if request.path.startswith(settings.MEDIA_URL) or request.path.startswith(settings.STATIC_URL):
            return
        print('JadeLessCoffee compiler will run at every request...\n');
        compile_all()
