
$.ns('Cls.ToolboxTeamList');
Cls.ToolboxTeamList = $.inherit($.util.Observable, {
    // ..
    toolbox_id:'',
    form:null,
    // ...
    btn_create_id:'create-btn',
    btn_remove_id:'remove-btn',    
    // ..
    btnCreate:null,
    btnRemove:null,    
    // ..
    constructor : function(config){
        // ...
        $.extend(this, config);
        // ...
        this.btnCreate = $("#"+this.toolbox_id+"__"+this.btn_create_id);
        this.btnRemove = $("#"+this.toolbox_id+"__"+this.btn_remove_id);

        // ..
        Cls.ToolboxTeamList.superclass.constructor.call(this, config);
        // ..
        this.btnCreate.on('click',this,this.create);            
        this.btnRemove.on('click',this,this.remove);                    
    },

    create:function (e) {
        // ...
        var me = e.data;
        // ...
        e.preventDefault();
        me.form.open();
    },

    remove:function (e) {
        var me  = e.data;
        var currentrecord = me.list.getCurrentRecord();
        if (currentrecord){
            console.log(currentrecord.attr('data-id'));
        };
    },

});



$(function($){

    // ..
    App.MenuToggleBtn.add($('#team-list-toolbox'));

    // ..
    $.ns('App.CreateTeamForm');
    App.CreateTeamForm = new Furst.LightBoxForm({
        form_id:'create-team-form',
        action:TeamActions.create,        
    });        
   
    // ..
    $.ns('App.TeamList');
    App.TeamList = new Furst.List({
        list_id:'team-list-data',
    });    

    // ..
    $.ns('App.ToolboxTeamList');
    App.ToolboxTeamList = new Cls.ToolboxTeamList({
        toolbox_id:'team-list-toolbox',
        form:App.CreateTeamForm,
        list:App.TeamList,
    });

});
