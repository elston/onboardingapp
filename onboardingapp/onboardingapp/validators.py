from django.core.exceptions import ValidationError

class FormValidationMixin(object):
    # ...
    def test(self):
        if not self.is_valid():
            raise ValidationError(
                'Form not valid',
                code='form_invalid',
                params={k:self.errors[k][0] for k in self.errors},
            )
        return self