$(function() {
    $('.remove_btn').on('click', function () {
        if (confirm('Are you sure you want to remove this meal?')) {
            window.location = remove_link + $(this).attr('id').substr(4)
        }
    });

    $('.dec_selector').on('click', function () {
        update_counter($(this).parent(), -1)
    });
    $('.inc_selector').on('click', function () {
        update_counter($(this).parent(), 1)
    });

    calculate_page()
});

function extract_item_id_from_html_id(html_element){
    parts = html_element.attr('id').split('_');
    return parts[parts.length - 1]
}

function update_counter(num_selector, add_value){
    current_count = parseInt(num_selector.find('.number').text());
    current_count += add_value;
    if (current_count < 0) return;
    num_selector.find('.number').text(current_count);

    meal_id = extract_item_id_from_html_id(num_selector);
    unit_price = Number($("#unit_price_" + meal_id).text().replace(/[^0-9.-]+/g,""));
    total = current_count * unit_price;
    $('#order_total_' + meal_id).text('$' + total.toFixed(2));
    calculate_page();
}

function calculate_page(){
    sub_total = 0;
    $('.order_total').each(function(){
        sub_total += Number($(this).text().replace(/[^0-9.-]+/g,""))
    });
    $('#sub_total').text('$' + sub_total.toFixed(2))
}