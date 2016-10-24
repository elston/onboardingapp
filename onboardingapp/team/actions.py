
from django.http import QueryDict
# Team
from .forms import (
    CreateTeamForm, 
    CreateTeamAndOrgForm,)

from organization.validators import OrgOwnerValidator

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
        form = form_cls(qd_data).test()        
        # form = form_cls({
        #     'whith_org':True,
        #     'team_name':'gdsgds',
        # }).test()
        # ...
        validator = OrgOwnerValidator(
            org =form.cleaned_data['organization'],
            user=user)\
            .test()

        record = {
            'organization':form.cleaned_data['organization'],
            'team_name':form.cleaned_data['team_name'],
            'team_description':form.cleaned_data['team_description'],            
        }
        return {
            'success':True,
            'message':'Team created successfully',
            'record':record,
        }
