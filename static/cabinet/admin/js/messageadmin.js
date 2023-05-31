$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-messageadmin').modal('show');
            },
            success: function(data){
                $('#modal-messageadmin .modal-content').html(data.html_form);
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
                    $('#table-messageadmin tbody').html(data.messageadmin);
                    $('#modal-messageadmin').modal('hide');
                } else {
                    $('#modal-messageadmin .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-messageadmin').on("submit", ".create-form", SaveForm);

// Update form
$('#table-messageadmin').on("click", ".show-form-update", ShowForm);
$('#modal-messageadmin').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-messageadmin').on("click", ".show-form-delete", ShowForm);
$('#modal-messageadmin').on("submit", ".delete-form", SaveForm);

});