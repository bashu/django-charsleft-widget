(function ($) {
    "use strict";

    function charsleft($field, maxlength) {
        // Split by Unicode code point, not UTF-16 code unit, so a surrogate
        // pair (emoji, astral characters) is never cut in half - this also
        // matches how Django's max_length validates (Python len() counts
        // code points too).
        var chars = Array.from($field.val());
        if (chars.length > maxlength) {
            $field.val(chars.slice(0, maxlength).join(""));
            return 0;
        }
        return maxlength - chars.length;
    }

    function updateCount($field, maxlength) {
        $field.parent().find(".current").text(charsleft($field, maxlength));
    }

    function addCharsleftHandlers($scope) {
        $scope.find(".charsleft").addBack(".charsleft").each(function () {
            var $container = $(this);
            if ($container.data("charsleftBound")) {
                return;
            }
            $container.data("charsleftBound", true);

            var field = this.getAttribute("data-charsleft-field");
            var maxlength = parseInt(this.getAttribute("data-maxlength"), 10);
            var $field = $("textarea[name='" + field + "']", this);

            $field.on("input change", function () {
                updateCount($(this), maxlength);
            });

            // Re-sync immediately in case the browser restored a value
            // (bfcache, autofill) after the server-rendered count was baked in.
            updateCount($field, maxlength);
        });
    }

    $(function () {
        addCharsleftHandlers($(document));
    });

    // Exposed so pages that inject markup after page load (formsets, ajax)
    // can (re)bind newly-added .charsleft widgets, e.g. $(newRow).charsleft().
    $.fn.charsleft = function () {
        addCharsleftHandlers(this);
        return this;
    };
}(window.jQuery || (window.django && window.django.jQuery)));
