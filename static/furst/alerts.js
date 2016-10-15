$.ns('Cls.Alerts');
Cls.Alerts = $.inherit($.util.Observable, {
    // ..
    ell:null,
    wrp_el:null,
    class:'alert',
    wrp_id:'messages-wrapper',
    templ:'\
        <div class="alert alert-{{type}} alert-message" role="alert"> \
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"> \
                <span aria-hidden="true">&times;</span> \
            </button> \
            {{message}} \
        </div> \
    ',
    // ..
    constructor : function(config){
        // ...
        this.ell = $("."+this.class);
        this.wrp_el = $("#"+this.wrp_id);
        // ..
        $.extend(this, config);
        Cls.Alerts.superclass.constructor.call(this, config);
        // ..
        // if (this.ell){        
        //     setTimeout(this.hide, 15000);
        // };          
    },

    hide:function() {
        // ...
        this.ell.hide('slow');
    },

    show:function (msg) {
        // ...
        var html = $(this.compile({
            type:'danger',
            message:msg,
        }));
        // ..
        this.wrp_el.append(html);
    },

    compile:function (kwargs) {
        var templ = this.templ;
        for (i in kwargs){
            var o = kwargs[i];
            var re = new RegExp('(\\{{\\ *'+i+'\\ *\\}})', 'g')
            // ..
            if(!re.test(templ)){
                throw('not compile regexp')
            };
            templ = templ.replace(re,o)
        };
        return templ;
    },
});





$(function($){

    // ..
    $.ns('App.Alerts');
    App.Alerts = new Cls.Alerts();    

});
