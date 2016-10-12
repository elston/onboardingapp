$.ns('Cls.LightBoxForm');
Cls.LightBoxForm = $.inherit($.util.Observable, {
    // ...
    form_id:null,
    action:$.noop,
    // ..
    constructor : function(config){
        // ...
        this.shdowing_el    = $("#"+this.form_id+'_shdowing');
        this.box_el         = $('#'+this.form_id+'_box');
        this.form_el        = $("#"+this.form_id);
        // ..
        $.extend(this, config);
        Cls.LightBoxForm.superclass.constructor.call(this, config);
        // ..
        this.form_el
            .on('submit',this,this.submit);
    },
    
    open: function (){
        // ..
        this.shdowing_el.css('display','block');
        this.box_el.css('display','block');
    },

    close: function (){
        this.shdowing_el.css('display','none');
        this.box_el.css('display','none');
    },

    success:function (result) {
        console.log(result);
        this.reset()
            .close();
    },

    submit:function (e) {
        var me = e.data;
        var data = me.form_el.serialize();        
        // ..
        me.action(
            data,
            me.success, 
            me.error, 
            me
        );
        return false;
    },

    reset:function () {
        this.form_el[0].reset();
        return this;
    },
});

