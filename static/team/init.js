
$.ns('Cls.ToolboxTeamList');
Cls.ToolboxTeamList = $.inherit($.util.Observable, {
    // ..
    btnCreate:null,
    items:[],
    // ..
    constructor : function(config){
        // ...
        this.btnCreate = $("#team-list-toolbox__add-team-btn");

        // ..
        $.extend(this, config);
        Cls.ToolboxTeamList.superclass.constructor.call(this, config);
        // ..
        this.btnCreate
            .on('click',this,this.create);            
    },

    create:function (e) {
        // ...
        var me = e.data;
        // ...
        e.preventDefault();
        App.CreateTeamForm.open();
    },


});



$(function($){

    // ..
    
    App.MenuToggleBtn.add($('#team-list-toolbox'));

    // ..
    $.ns('App.ToolboxTeamList');
    App.ToolboxTeamList = new Cls.ToolboxTeamList();

});
