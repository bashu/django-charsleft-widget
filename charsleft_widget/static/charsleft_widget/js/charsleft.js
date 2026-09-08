(function () {
    "use strict";

    function charsleft(field, maxlength) {
        // Split by Unicode code point, not UTF-16 code unit, so a surrogate
        // pair (emoji, astral characters) is never cut in half - this also
        // matches how Django's max_length validates (Python len() counts
        // code points too).
        var chars = Array.from(field.value);
        if (chars.length > maxlength) {
            field.value = chars.slice(0, maxlength).join("");
            return 0;
        }
        return maxlength - chars.length;
    }

    function updateCount(field, maxlength) {
        var current = field.parentNode.querySelector(".current");
        if (current) {
            current.textContent = charsleft(field, maxlength);
        }
    }

    function addCharsleftHandlers(scope) {
        var containers = Array.prototype.slice.call(scope.querySelectorAll(".charsleft"));
        if (scope.matches && scope.matches(".charsleft")) {
            containers.push(scope);
        }

        containers.forEach(function (container) {
            if (container.dataset.charsleftBound) {
                return;
            }
            container.dataset.charsleftBound = "true";

            var name = container.getAttribute("data-charsleft-field");
            var maxlength = parseInt(container.getAttribute("data-maxlength"), 10);
            var field = container.querySelector("textarea[name='" + name + "']");
            if (!field) {
                return;
            }

            ["input", "change"].forEach(function (type) {
                field.addEventListener(type, function () {
                    updateCount(field, maxlength);
                });
            });

            // Re-sync immediately in case the browser restored a value
            // (bfcache, autofill) after the server-rendered count was baked in.
            updateCount(field, maxlength);
        });
    }

    function ready(callback) {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", callback);
        } else {
            callback();
        }
    }

    ready(function () {
        addCharsleftHandlers(document);
    });

    // Exposed so pages that inject markup after page load (formsets, ajax)
    // can (re)bind newly-added .charsleft widgets, e.g. window.charsleft(newRow).
    window.charsleft = addCharsleftHandlers;
}());
