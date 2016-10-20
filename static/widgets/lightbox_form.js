$.ns('Cls.LightBoxForm');
Cls.LightBoxForm = $.inherit($.util.Observable, {
    // ...
    form_id:null,
    action:$.noop,
    templErrField: new Furst.Template('\
        <div class="error" style="color: red;">\
            {{error}} \
        </div>\
    '),
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
        // ...
        this
            .removeErrLabel()
            .reset();        
    },

    submit:function (e) {
        var me = e.data;
        var data = me.form_el.serialize();        
        // ..
        me.removeErrLabel();
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

    success:function (result) {
        // ...
        this.reset()
            .close();
    },

    error:function (result, request) {
        // ..
        var xhr = request.xhr;
        var response = xhr.responseJSON
        // ...
        App.Alerts.show(response.message);
        if (xhr.status == 400) {        
            this.markErrField(response.params);
        };
    },   

    markErrField:function (param) {
        for (var k in param) {
            this.form_el
                .find('input[name=' + k + ']')
                .before(this.templErrField.compile({
                    error:param[k]
                }));
        }; 
    },  

    removeErrLabel:function (argument) {
        this.form_el
            .find('.error')
            .remove();
        return this;
    },
});

