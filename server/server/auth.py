from django.contrib.auth import get_user_model


class AlwaysRootBackend(object):
    """This is a backend for short-circuiting authentication across the
    application. For development and demonstration purposes only.
    """
    def authenticate(self, *args, **kwargs):
        """Always return the 'root' user."""
        return get_user_model().objects.get(username='root')

    def get_user(self, user_id):
        return get_user_model().objects.get(username='root')
