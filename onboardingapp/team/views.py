from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import (
    Team,)

from .forms import (
    CreateTeamForm, 
    CreateTeamAndOrgForm,)

class Teams(ListView):
    template_name = 'team/index.html'
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super(Teams, self).get_context_data(**kwargs)

        # ..
        context.update({'sidebar':{'team':{'active':True}}})

        # ..orgs
        user = self.request.user
        orgs = user.organizations.all()
        if orgs:
            context.update({
                'orgs':orgs
            })

        # ...create form
        create_team_form = CreateTeamForm(user=user)
        if orgs:
            create_team_form = CreateTeamAndOrgForm()
        context.update({
            'create_team_form':create_team_form,
        })

        # ...filter
        team_filter = self.request.GET.get('team_filter', None)
        if team_filter:
            context['team_filter'] = int(team_filter)
            if int(team_filter) > 0:
                org = get_object_or_404(Organization, id=int(team_filter))
                context.update({
                    'org':org,
                })

        return context

    def get_queryset(self):
        team_filter = int(self.request.GET.get('team_filter', -1))
        org = None

        if team_filter == -1:
            return Team.objects\
                .filter(
                    Q(owner=self.request.user) | Q(member=self.request.user))\
                .distinct()

        if team_filter > 0:
            org = get_object_or_404(Organization, id=team_filter)
            return Team.objects.filter(
                organizations=org)

        if team_filter == -2:
            return Team.objects.filter(
                owner=self.request.user)

        if team_filter == -3:
            return Team.objects.filter(
                member=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Teams, self).dispatch(request, *args, **kwargs)
