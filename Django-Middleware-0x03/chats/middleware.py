
import os
from datetime import datetime
from django.http import HttpResponseForbidden


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now().time()
        start = now.replace(hour=18, minute=0, second=0, microsecond=0)
        end = now.replace(hour=21, minute=0, second=0, microsecond=0)
        # Allow only between 18:00 (6PM) and 21:00 (9PM)
        if not (start <= now <= end):
            return HttpResponseForbidden(
                "Access to the chat is only allowed between 6PM and 9PM."
            )
        return self.get_response(request)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = os.path.join(
            os.path.dirname(__file__),
            '../requests.log'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_entry = f"{datetime.now()} - User: {user} - Path: {request.path}\n"
        with open(self.log_file, 'a') as f:
            f.write(log_entry)
        response = self.get_response(request)
        return response
