from django.conf.urls import url

from team import views

urlpatterns = [

    # TEAM
    # ...list
    url(r'^teams', 
        views.Teams.as_view(), 
            name='teams'),

    # ...read
    url(r'^team/(?P<id>\d+)$', 
        views.team_info, 
            name='team_info'),

    # ...create
    url(r'^team/create$', 
        views.create_team, 
            name='create_team'),

    # ...update descr
    url(r'^team/edit$', 
        views.edit_team, 
            name='edit_team'),

    # ...update owner
    url(r'^team/changeteamowner$', 
        views.changeteamowner_team, 
            name='changeteamowner_team'),    

    url(r'^team/(?P<t_id>\d+)/member/(?P<m_id>\d+)/accept-changeteamowner$',
        views.accept_changeteamowner, 
            name='accept_changeteamowner'),    

    # ...delete
    url(r'^team/(?P<team_id>\d+)/delete$', 
        views.delete_team, 
            name='delete_team'),

    # ..LIMIT
    url(r'^team/limit/check$',
        views.check_team_limit, 
            name='check_team_limit'),

    # ..MYTEAM
    url(r'^myteam/(?P<id>\d+)$', 
        views.myteam_info, 
            name='myteam_info'),

    # ..ADDITIONAL_INFO
    url(r'^team/(?P<id>\d+)/additional-info$', 
        views.additional_info, 
            name='additional_info'),

    url(r'^team/(?P<id>\d+)/additional-info/add$', 
        views.add_additional_info, 
            name='add_additional_info'),

    # ..MEMBERS
    url(r'^team/members/get-email$', 
        views.get_members_email, 
            name='get_members_email'),

    url(r'^team/member/remove$', 
        views.remove_member, 
            name='remove_member'),

    # ..INVITES
    url(r'^team/invite/remove$', 
        views.remove_invite, 
            name='remove_invite'),    

    url(r'^team/(?P<t_id>\d+)/member/(?P<m_id>\d+)/accept-invitation-step1$',
        views.accept_invitation_step1, 
            name='accept_invitation_step1'),

    url(r'^team/(?P<t_id>\d+)/member/(?P<m_id>\d+)/accept-invitation-step2$',
        views.accept_invitation_step2, 
            name='accept_invitation_step2'),

    # ..SERVICE
    url(r'^team/(?P<id>\d+)/tools$', 
        views.add_service, 
            name='add_service'),

    url(r'^team/(?P<t_id>\d+)/service/(?P<s_name>.+)/add$',
        views.add_service_real, 
            name='add_service_real'),

    # ..ADMIN
    url(r'^team/(?P<team_id>\d+)/admin/add/(?P<user_id>\d+)$',
        views.add_admin, 
            name='add_admin'),

    url(r'^team/(?P<team_id>\d+)/admin/remove/(?P<user_id>\d+)$',
        views.remove_admin, 
            name='remove_admin'),



    # ....USER
    url(r'^user/registration/check$',
        views.check_registration, 
            name='check_registration'),

    url(r'^user/invite$', 
        views.invite_user, 
            name='invite_user'),

    url(r'^user/plan$', 
        views.plan, 
            name='plan'),

    url(r'^user/account/update$', 
        views.update_account, 
            name='update_account'),

    url(r'^user/account/charge$', 
        views.charge_account, 
            name='charge_account'),

    url(r'^user/account/cancel$', 
        views.cancel_account, 
            name='cancel_account'),


    # ....SERVICE
    url(r'^service/search$', 
        views.search_service, 
            name='search_service'),

    url(r'^service/(?P<s_name>.+)/auth-finish',
        views.add_service_auth_finish, 
            name='add_service_auth_finish'),

    url(r'^service/remove$', 
        views.remove_service, 
            name='remove_service'),

    url(r'^service/get-form/', 
        views.get_form, 
            name='get_form'),

    # ..STRIPE
    url(r'^stripe/webhook$', 
        views.stripe_webhook, 
            name='stripe_webhook'),

    # ..ERROR-LOG
    url(r'^error-log/(?P<id>\d+)/remove$',
        views.remove_error_log, 
            name='remove_error_log'),
]


# from .router import router
# api = router.api
# # ...
# urlpatterns = urlpatterns + [
#     url(r'^team/api/$', api, name='team_api'),               
#     url(r'^team/router/$', router, name='team_router'),    
# ]