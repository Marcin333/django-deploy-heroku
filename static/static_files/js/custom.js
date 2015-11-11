function showFlashMessage(message) {
	var template = "<div class='container container-alert-flash'>" +
	"<div class='col-sm-4 col-sm-offset-8'> " +
	"<div class='alert' id='alert-flush' role='alert'>"
	+ "<span class='glyphicon glyphicon-ok'></span>" + " " + message + "</div></div></div>"
	$("body").append(template);
	$(".container-alert-flash").slideDown(800);
	setTimeout(function(){
		$(".container-alert-flash").slideUp(800);
	}, 3000);

}

function setPrice(){
  var price = $(".variation_option option:selected").attr("data-price");
  var sale_price = $(".variation_option option:selected").attr("data-sale-price");
  if (sale_price != "" && sale_price != 'None' && sale_price != null) {
    $('#price').html(sale_price + " " + '<small class="sale_price">' + price + '</small>')
  } else {
    $('#price').html(price);
  }
}
setPrice();
  // var price = $(".variation_option option:selected").attr("data-price");
  // $('#price').text(price);
  $('.variation_option').change(function(){
    setPrice();
    // var img = $(".variation_option option:selected").attr("data-price");
    // $('#img').attr('src', img);
  });
$(document).ready(function(){
  
});

