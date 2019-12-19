$(function(){
    $('.remove_btn').on('click', function(){
        if(confirm('Are you sure you want to remove this meal?')){
            window.location = remove_link + $(this).attr('id').substr(4)
        }
    })
});