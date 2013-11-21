jQuery(function() {

    var cwidth = $("#portal-columns").width();

    if(cwidth > 970) {
        var wwidth = $(window).width();
        var side_margin = (wwidth - 970) / 2;
        var margin = '0 ' + side_margin + 'px';
        $('#portal-columns').css('width', '970px');
        $('#portal-columns').css('margin', margin);
    }

    $(window).resize(function() {

        var cwidth = $("#portal-columns").width();
        var wwidth = $(window).width();
        if (wwidth > cwidth) {
            var side_margin = (wwidth - 970) / 2;
            var margin = '0 ' + side_margin + 'px';
            $('#portal-columns').css('width', '970px');
            $('#portal-columns').css('margin', margin);
        } else {
            $('#portal-columns').css('width', '100%');
        }
    });

});