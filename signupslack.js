jQuery(function($) {
    $('form[data-async]').on('submit', function(event) {
        var $form = $(this);
        var $target = $($form.attr('data-target'));
        var datainput = {
            "email": $("input#email").val(),
            "name": $("input#name").val()
        };
        $.ajax({
            type: "POST",
            url: "http://use.yt/slack_signup",
            contentType: "application/json",
            data: JSON.stringify(datainput),

            success: function(data, status) {
                $target.modal('hide');
            }
        });

        event.preventDefault();
    });
}); 
