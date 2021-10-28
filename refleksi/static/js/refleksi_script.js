$(document).ready(function() {
    $(document).on("click", ".ujicoba", function() {
    	var nama = $(this).find(".card-body h4").text();
    	if (nama == "Lainnya") {
    		$("#id_nama").val("");
    		$("#id_nama").prop("disabled", false);
    	} else {
    		$("#id_nama").val(nama);
    		$("#id_nama").prop("disabled", true);
    		$("#id_nama").css("background-color", "white");
    	}
    });
});