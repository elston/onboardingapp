$(function($){

    // ..
    $.ns('App.MenuToggleBtn.Cmp');
    App.MenuToggleBtn.Cmp = new App.MenuToggleBtn.Cls();

    // ..
    $.ns('App.Alerts.Cmp');
    App.Alerts.Cmp = new App.Alerts.Cls();    

    // ...
    setTimeout(function() { 
        App.Alerts.Cmp.ell.hide('slow');
    }, 15000);    
    // ...
});



