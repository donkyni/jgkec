$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-modalcreateactiviteadmin').modal('show');
            },
            success: function(data){
                $('#modal-modalcreateactiviteadmin .modal-content').html(data.html_form);
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
                    $('#table-modalcreateactiviteadmin tbody').html(data.activiteadmin);
                    $('#modal-modalcreateactiviteadmin').modal('hide');
                } else {
                    $('#modal-modalcreateactiviteadmin .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-modalcreateactiviteadmin').on("submit", ".create-form", SaveForm);

// Update form
$('#table-modalcreateactiviteadmin').on("click", ".show-form-update", ShowForm);
$('#modal-modalcreateactiviteadmin').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-modalcreateactiviteadmin').on("click", ".show-form-delete", ShowForm);
$('#modal-modalcreateactiviteadmin').on("submit", ".delete-form", SaveForm);

});