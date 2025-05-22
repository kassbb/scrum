from rest_framework.views import exception_handler
import sentry_sdk


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None and response.status_code >= 400:
        # Log the exception with Sentry
        sentry_sdk.capture_exception(exc)

    return response
