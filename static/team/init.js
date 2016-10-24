
$.ns('Cls.ToolboxTeamList');
Cls.ToolboxTeamList = $.inherit($.util.Observable, {
    // ..
    btnCreate:null,
    btnRemove:null,    
    // ..
    constructor : function(config){
        // ...
        this.btnCreate = $("#team-list-toolbox__create-btn");
        this.btnRemove = $("#team-list-toolbox__remove-btn");        

        // ..
        $.extend(this, config);
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
        App.CreateTeamForm.open();
    },

    remove:function (e) {
        console.log('sdfgsdf');

    },

});


// ...
$.ns('Cls.CreateTeamForm');
Cls.CreateTeamForm = $.inherit(Furst.LightBoxForm, {
    // ..
    form_id:'create-team-form',
    action:TeamActions.create,
    // ..

});




$.ns('Cls.TeamList');
Cls.TeamList = $.inherit($.util.Observable, {
    // ..
    list:null,
    items:[],
    // ..
    constructor : function(config){
        // ...
        this.list = $("#team-list-data");

        // ..
        $.extend(this, config);
        Cls.TeamList.superclass.constructor.call(this, config);
        // ..
        var list = this.list.children();
        for (var i = 0; i < list.length; i++) {
            var item = $(list[i]);
            item.on('click',this,this.onClickRecord);            
        };

    },
    onClickRecord:function (e) {
        var me = e.data;
        var item = $(e.currentTarget);
        // ...
        me.list.children().each(function () {
            $(this).removeClass('active');
        });
        item.toggleClass('active');
    },

});





$(function($){

    // ..
    App.MenuToggleBtn.add($('#team-list-toolbox'));

    // ..
    $.ns('App.CreateTeamForm');
    App.CreateTeamForm = new Cls.CreateTeamForm();    
   
    // ..
    $.ns('App.ToolboxTeamList');
    App.ToolboxTeamList = new Cls.ToolboxTeamList();

    // ..
    $.ns('App.TeamList');
    App.TeamList = new Cls.TeamList();    

});
