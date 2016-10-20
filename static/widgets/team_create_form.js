$.ns('Cls.CreateTeamForm');
Cls.CreateTeamForm = $.inherit(Cls.LightBoxForm, {
    // ..
    form_id:'create-team-form',
    action:TeamActions.create,
    // ..

});

$(function($){
    $.ns('App.CreateTeamForm');
    App.CreateTeamForm = new Cls.CreateTeamForm();
});