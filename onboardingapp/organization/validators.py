from django.core.exceptions import ValidationError


from .models import Organization
class OrgOwnerValidator(object):

    def __init__(self, org=None,user=None):
        # ..
        self.org = org
        self.user = user

    def test(self):
        if isinstance(self.org, Organization):
            if self.org.owner != self.user:
                raise ValidationError(
                    'You don\'t have permission',
                    code='access_forbidden'
                )