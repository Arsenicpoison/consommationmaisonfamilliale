// Get products by category_id using ajax

$(function() {
    $("#category_id").on("change", function() {
        category_id = $(this).val();
        // alert(category_id);
        $.get(
            "/previsions/getProducts", {
                category_id: category_id,
            },
            function(data) {
                $("#id_product").html(data);
            }
        );
    });
});

// Get unit_price by id_product
$(function() {
    $("#id_product").on("change", function() {
        id_product = $(this).val();
        $.get(
            "/previsions/getUnitPrice", {
                id_product: id_product,
            },
            function(data) {
                $("#unit_price").val(data);
            }
        );
    });
});

$('#id_quantity').on('keyup', function() {
    var id_quantity = $(this).val();
    var unit_price = $('#unit_price').val();
    var total = id_quantity * unit_price;
    $('#id_total').val(total);
});