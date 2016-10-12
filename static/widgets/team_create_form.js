$.ns('Cls.CreateTeamForm');
Cls.CreateTeamForm = $.inherit(Cls.LightBoxForm, {
    // ..
    form_id:'create-team-form',
    action:TeamActions.create,
    // ..


    error:function (result) {
        console.log('error',result);
    },        

});

$(function($){
    $.ns('App.CreateTeamForm');
    App.CreateTeamForm = new Cls.CreateTeamForm();
});