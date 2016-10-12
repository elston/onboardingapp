
# Team
from .forms import (
    CreateTeamForm, 
    CreateTeamAndOrgForm,)

from django.http import QueryDict
class TeamActions(object):
    # ...
    def create(self,data,user):
        # ..
        form = CreateTeamForm(QueryDict(data))    
        print(form.is_valid())
        print('OK')
        return {'success':True}
# .....