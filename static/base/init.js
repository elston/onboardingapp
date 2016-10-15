

$.ns('Cls.MenuToggleBtn');
Cls.MenuToggleBtn = $.inherit($.util.Observable, {
    // ..
    el:null,    
    id:'menu-toggle',
    // ..
    constructor : function(config){
        // ...
        this.el = $("#"+this.id);
        // ..
        $.extend(this, config);
        Cls.MenuToggleBtn.superclass.constructor.call(this, config);
        // ..
        this.el
            .click(this.onclick);
    },

    onclick:function (e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");        
    },
});








$(function($){

    // ..
    $.ns('App.MenuToggleBtn');
    App.MenuToggleBtn = new Cls.MenuToggleBtn();


});



