"""
Middleware to use the X-Forwarded-For header as the request IP.
Updated the libray to use HTTP_HOST and X-Forwarded-Port as
SERVER_NAME and SERVER_PORT.
"""

from django.utils.deprecation import MiddlewareMixin
from edx_django_utils.monitoring import set_custom_attribute


class XForwardedForMiddleware(MiddlewareMixin):
    """
    Gunicorn 19.0 has breaking changes for REMOTE_ADDR, SERVER_* headers
    that can not override with forwarded and host headers.
    This middleware can be used to update these headers set by proxy configuration.

    """

    def process_request(self, request):  # lint-amnesty, pylint: disable=useless-return
        """
        Process the given request, update the value of REMOTE_ADDR, SERVER_NAME and SERVER_PORT based
        on X-Forwarded-For, HTTP_HOST and X-Forwarded-Port headers
        """
        # Give some observability into X-Forwarded-For length. Useful
        # for monitoring in case of unexpected changes, etc.
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        xff_len = xff.count(',') + 1 if xff else 0
        # IP chain is XFF + REMOTE_ADDR
        set_custom_attribute('ip_chain.count', xff_len + 1)

        for field, header in [("HTTP_X_FORWARDED_FOR", "REMOTE_ADDR"), ("HTTP_HOST", "SERVER_NAME"),
                              ("HTTP_X_FORWARDED_PORT", "SERVER_PORT")]:
            if field in request.META:
                if ',' in request.META[field]:
                    request.META[header] = request.META[field].split(",")[0].strip()
                else:
                    request.META[header] = request.META[field]

        return None
