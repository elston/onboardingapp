$.ns('App.Alerts');
App.Alerts.Cls = $.inherit($.util.Observable, {
    // ..
    ell:null,
    class:'alert',
    // ..
    constructor : function(config){
        // ...
        this.ell = $("."+this.class);
        // ..
        $.extend(this, config);
        App.Alerts.Cls.superclass.constructor.call(this, config);
        // ..
    },

});

$.ns('App.MenuToggleBtn');
App.MenuToggleBtn.Cls = $.inherit($.util.Observable, {
    // ..
    el:null,    
    id:'menu-toggle',
    // ..
    constructor : function(config){
        // ...
        this.el = $("#"+this.id);
        // ..
        $.extend(this, config);
        App.MenuToggleBtn.Cls.superclass.constructor.call(this, config);
        // ..
        this.el
            .click(this.onclick);
    },

    onclick:function (e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");        
    },
});

