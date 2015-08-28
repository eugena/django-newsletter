""" Abstractions for generating signed links for secure activation. """

from django.core import signing


class Signer(object):
    """
    Base class for newsletter signers allowing easy overriding
    salt and MAX_AGE.
    """
    def __init__(self, salt, max_age=86400):
        self.salt = salt
        self.max_age = max_age

    def generate(self, **kwargs):
        return signing.dumps(kwargs, salt=self.salt, compress=True)

    def validate(self, token):
        return signing.loads(token, salt=self.salt, max_age=self.max_age)


subscribe_signer = Signer(salt='newsletter_subcsribe')
unsubscribe_signer = Signer(salt='newsletter_unsubscribe')
update_signer = Signer(salt='newsletter_update')
