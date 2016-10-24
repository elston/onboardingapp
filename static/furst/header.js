

$.ns('Cls.MenuToggleBtn');
Cls.MenuToggleBtn = $.inherit($.util.Observable, {
    // ..
    el:null,
    items:[],
    // ..
    constructor : function(config){
        // ...
        this.el = $("#menu-toggle");
        this.items = [
            $('#content-wrapper'),
            $('#sidebar-wrapper'),
            $('#header-wrapper'),
            $('#message-wrapper'),
            $('#footer-wrapper')
        ];

        // ..
        $.extend(this, config);
        Cls.MenuToggleBtn.superclass.constructor.call(this, config);
        // ..
        this.el
            .on('click',this,this.onclick);            
    },

    onclick:function (e) {
        // ...
        var me = e.data;
        // ...
        e.preventDefault();
        for (var i = 0; i < me.items.length; i++) {
            me.items[i].toggleClass("hugeled");            
        };
    },

    add:function (item) {
        this.items.push(item);
    },
});








$(function($){

    // ..
    $.ns('App.MenuToggleBtn');
    App.MenuToggleBtn = new Cls.MenuToggleBtn();


});



