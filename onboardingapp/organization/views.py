from django.http import Http404, JsonResponse
from django.views.generic import DetailView, ListView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db.models import Q
from .models import Organization
from .forms import OrganizationCreateForm
from team.forms import CreateTeamForm


class OrganizationDetail(DetailView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'organization/details.html'

    def get_context_data(self, **kwargs):
        context = super(OrganizationDetail, self).get_context_data(**kwargs)
        obj = self.get_object()
        if self.request.user != obj.owner:
            raise Http404

        teams = obj.team.all()
        context['teams'] = teams

        team_form = CreateTeamForm(user=self.request.user)
        context['form'] = team_form

        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(
            OrganizationDetail, self).dispatch(request, *args, **kwargs)


class OrganizationList(FormView, ListView):
    model = Organization
    form_class = OrganizationCreateForm
    template_name = 'organization/list.html'
    context_object_name = 'organizations'

    def get_context_data(self, **kwargs):
        context = super(OrganizationList, self).get_context_data(**kwargs)
        context['form'] = self.get_form()

        org_filter = self.request.GET.get('filter', None)
        if org_filter:
            context['filter'] = int(org_filter)

        return context

    def get_queryset(self):
        org_filter = int(self.request.GET.get('filter', -1))

        if org_filter == -1:
            return set(Organization.objects.filter(
                Q(owner=self.request.user) | Q(team__member=self.request.user)
            ))

        if org_filter == -2:
            return Organization.objects.filter(
                owner=self.request.user)

        if org_filter == -3:
            return set(Organization.objects.filter(
                team__member=self.request.user))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        response = {}
        for k in form.errors:
            response[k] = form.errors[k][0]

        return JsonResponse({'response': response}, status=400)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()

        messages.success(
            self.request, 'The organization is created successfully')
        return JsonResponse({}, status=200)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OrganizationList, self).dispatch(request, *args, **kwargs)


@login_required
@require_http_methods(["POST"])
@csrf_exempt
def check_organization_limit(request):
    orgs = request.user.organizations.all()

    if orgs:
        if request.user.account:
            orgs_count = Organization.objects.filter(
                owner=request.user).count()
            if orgs_count >= request.user.account.org_limit:
                response = 'Organization limit!'
                return JsonResponse({'response': response}, status=400)
        else:
            response = 'Please update your account!'
            return JsonResponse({'response': response}, status=400)

    return JsonResponse({}, status=200)
