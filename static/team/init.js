$(function($){



    // ...
    $.ns('App.LogoutDialog');
    App.LogoutDialog = new Cls.Dialog({
        dialog_id:'logout-dialog',
    });

    // ...
    $.ns('App.Sidebar');
    App.Sidebar = new Cls.Sidebar({
        dialogLogout:App.LogoutDialog,
    });    
    
    // ..
    $.ns('App.MenuToggleBtn');
    App.MenuToggleBtn = new Cls.MenuToggleBtn();    
    App.MenuToggleBtn.add($('#team-list-toolbox'));
    App.MenuToggleBtn.add($('#create-team-form_box'));
    App.MenuToggleBtn.add($('#logout-dialog_box'));

    // ..
    $.ns('App.CreateTeamForm');
    App.CreateTeamForm = new Cls.Form({
        form_id:'create-team-form',
        action:TeamActions.create,        
    });
   
    // ..
    $.ns('App.TeamList');
    App.TeamList = new Cls.List({
        list_id:'team-list-data',
    });    

    // ..
    $.ns('App.ToolboxTeamList');
    App.ToolboxTeamList = new Cls.ToolboxList({
        toolbox_id:'team-list-toolbox',
        form:App.CreateTeamForm,
        list:App.TeamList,
    });

});
