$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-modalcreatearticleadmin').modal('show');
            },
            success: function(data){
                $('#modal-modalcreatearticleadmin .modal-content').html(data.html_form);
            }
        });
    };
    var SaveForm = function() {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function(data) {
                if(data.form_is_valid) {
                    $('#table-modalcreatearticleadmin tbody').html(data.articleadmin);
                    $('#modal-modalcreatearticleadmin').modal('hide');
                } else {
                    $('#modal-modalcreatearticleadmin .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-modalcreatearticleadmin').on("submit", ".create-form", SaveForm);

// Update form
$('#table-modalcreatearticleadmin').on("click", ".show-form-update", ShowForm);
$('#modal-modalcreatearticleadmin').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-modalcreatearticleadmin').on("click", ".show-form-delete", ShowForm);
$('#modal-modalcreatearticleadmin').on("submit", ".delete-form", SaveForm);

});