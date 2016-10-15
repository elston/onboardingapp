from django.shortcuts import (
    render, 
    get_object_or_404,)

from django.contrib.auth.decorators import (
    login_required,)

from services.common import (
    check_services,)

from team.models import (
    Service, 
    Team,)

from organization.models import (
    Organization,)

from team.forms import (
    CreateTeamForm, 
    CreateTeamAndOrgForm,)


@login_required
def index(request):
    # ...
    user = request.user
    teams = user.ownerteams.all()
    services_list = []
    data = {}

    for team in teams:
        services = team.service.all()
        members = team.member.all()
        services_list.extend(services)

        for service in services:
            data[service.id] = list(members)

    for service in services_list:
        for item in services_list:
            if check_services(service, item) and (service.id != item.id):
                data[service.id].extend(data[item.id])
                services_list.remove(item)
                del data[item.id]

    result = {}
    for key, item in data.items():
        service = get_object_or_404(Service, id=key)
        unique_members_set = set(item)
        unique_members = list(unique_members_set)
        result[service] = len(unique_members)

    # ...
    context = {
        'teams': teams,
        'services_list': result,
    }

    # ...
    if not teams:
        create_team_form = CreateTeamAndOrgForm()
        if user.organizations.all():
            create_team_form = CreateTeamForm(
                user=user)    
        # ..
        context.update({
            'create_team_form':create_team_form,
        })

    return render(request, 'dashboard/index.html', context)