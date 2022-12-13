"""
Global FastAPI exception and warning classes.
"""


class ImproperlyConfigured(Exception):
    """FastAPI is somehow improperly configured"""
    pass


class SuspiciousOperation(Exception):
    """The user did something suspicious"""


class SuspiciousMultipartForm(SuspiciousOperation):
    """Suspect MIME request in multipart form data"""
    pass


class SuspiciousFileOperation(SuspiciousOperation):
    """A Suspicious filesystem operation was attempted"""
    pass
