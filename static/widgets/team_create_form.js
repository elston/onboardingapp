$.ns('Cls.CreateTeamForm');
Cls.CreateTeamForm = $.inherit(Cls.LightBoxForm, {
    // ..
    form_id:'create-team-form',
    action:TeamActions.create,
    // ..


    error:function (result, request) {
        console.log('error',result);
        console.log(request.xhr.status);        
        console.log(request.xhr.statusText);
        var msg = request.xhr.responseJSON.message;
        App.Alerts.show(msg);
    },   


});

$(function($){
    $.ns('App.CreateTeamForm');
    App.CreateTeamForm = new Cls.CreateTeamForm();
});