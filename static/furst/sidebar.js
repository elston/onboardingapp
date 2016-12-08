$.ns('Cls.Sidebar');
Cls.Sidebar = $.inherit($.util.Observable, {
    // ..
    menuLogout:null,
    dialogLogout:null,

    // ..
    constructor : function(config){
        // ...
        $.extend(this, config);
        // ...
        this.menuLogout = $("#logout__sidbar-menu-item");
        // ..
        Cls.Sidebar.superclass.constructor.call(this, config);
        // ..
        this.menuLogout.on('click',this,this.logout);            
    },

    logout:function (e) {
        // ...
        var me = e.data;
        // ...
        e.preventDefault();
        me.dialogLogout.open();
    },

});