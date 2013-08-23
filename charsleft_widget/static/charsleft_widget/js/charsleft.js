var charsleft = function(source, maxlength) {
    if(source.val().length > maxlength) {
        source.val(source.val().substring(0, maxlength));
        return 0;
    }
    return maxlength - source.val().length;
};
