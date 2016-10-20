

$.ns('Cls.MenuToggleBtn');
Cls.MenuToggleBtn = $.inherit($.util.Observable, {
    // ..
    el:null,    
    el_body:null,        
    id:'menu-toggle',
    id_body:'body-wrapper',
    // ..
    constructor : function(config){
        // ...
        this.el = $("#"+this.id);
        this.el_body = $("#"+this.id_body);
        // ..
        $.extend(this, config);
        Cls.MenuToggleBtn.superclass.constructor.call(this, config);
        // ..
        this.el
            .on('click',this,this.onclick);            
    },

    onclick:function (e) {
        var me = e.data;
        // ...
        e.preventDefault();
        me.el_body.toggleClass("toggled");                
    },
});








$(function($){

    // ..
    $.ns('App.MenuToggleBtn');
    App.MenuToggleBtn = new Cls.MenuToggleBtn();


});



