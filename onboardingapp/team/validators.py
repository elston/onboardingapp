from django.core.exceptions import ValidationError

class ValidationFormMixin(object):
    # ...
    def test(self):
        if not self.is_valid():
            raise ValidationError(
                'Form not valid',
                code='form_invalid',
                params={k:self.errors[k][0] for k in self.errors},
            )


from organization.models import Organization
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