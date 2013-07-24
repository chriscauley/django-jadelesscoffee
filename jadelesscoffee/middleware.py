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

    def process_response(self, request, response):
        if not self.active or request.is_ajax():
            return response
        if str(response.status_code) in ['404','400','500','302','301','304']:
            return response
        print('JadeLessCoffee compiler will run at every request...\n');
        compile_all()
        return response
