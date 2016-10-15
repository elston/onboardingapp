
from django.http import QueryDict
# Team
from .forms import (
    CreateTeamForm, 
    CreateTeamAndOrgForm,)

from .validators import OrgOwnerValidator

class TeamActions(object):
    # ...
    def create(self,data,user):
        # ..
        qd_data =  QueryDict(data)
        whith_org = qd_data.get('whith_org',False)
        form_cls = CreateTeamForm
        if whith_org:
            form_cls = CreateTeamAndOrgForm
        # ..
        # form = form_cls(qd_data)        
        form = form_cls({'team_name':'gdsgds'})        
        form.test()
        # ...
        validator = OrgOwnerValidator(
            org =form.cleaned_data['organization'],
            user=user)
        validator.test()

        return {'success':True}
# .....