count = 0;

$(function() {
    count = parseInt($('#order_quantity').val());
    update_count();

    $('#num_selector_min').on('click',function(){
        if (count > 0){
            count --;
            update_count()
        }
    });

    $('#num_selector_add').on('click',function(){
        count ++;
        update_count()
    });

    $('#add_to_order_btn').on('click', function(){
        if (count > 0){
            $('#order_quantity').val(count)
            $('#order_form').submit()
        }
    })
});


function update_count(){
    $('#num_selector_num').text(count)
}
