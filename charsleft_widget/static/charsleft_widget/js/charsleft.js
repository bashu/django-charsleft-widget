var charsleft = function(source, maxlength) {
    if(source.val().length > maxlength) {
        source.val(source.val().substring(0, maxlength));
        return 0;
    }
    return maxlength - source.val().length;
};

(function ($) {
    "use strict";
    function add_charsleft_handlers() {
        $(".charsleft").each(function () {
            var field = this.getAttribute("data-charsleft-field");
            var maxlength = this.getAttribute("data-maxlength");

            var $charsleftfield = $("textarea[name='" + field + "']", this);

            $charsleftfield.keyup(function (e, data) {
                $(this).parent().find(".current").text(
                    charsleft($(this), maxlength));
            });

            $charsleftfield.change(function (e, data) {
                $(this).parent().find(".current").text(
                    charsleft($(this), maxlength));
            });
        });
    }
    $(function () {
        add_charsleft_handlers();
    });
}(jQuery || django.jQuery));
