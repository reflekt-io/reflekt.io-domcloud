$(document).ready(function() {
    $(document).on("click", ".add-rec", function() {
    	var nama = $(this).find(".card-body h4").text();
    	if (nama == "(+) Tambah Rekomendasi") {
    		$(this).attr("href", "/refleksi/add-kegiatan")
    	} else {
            $("#id_deskripsi").val("");
    		$("#id_nama").val(nama);
    		$("#id_nama").prop("disabled", true);
    		$("#id_nama").css("background-color", "white");
    	}
    });

    var card = "<div class='card mb-4 add-card'>";
    card += "<a class='stretched-link text-decoration-none add-rec' href";
    var mcard = "<div class='card-body text-center'><h4>";
    var ccard = "</h4></div></a></div>";

    $("#card-recomendation").append(card + ">" + mcard + "(+) Tambah Rekomendasi" + ccard);
    
    card += " data-toggle='modal' data-target='#modal-form'>"

    var recomendation = new Set([
        "bermain game",
        "menonton film",
        "membaca novel",
        "mendengarkan musik",
        "jalan-jalan",
        "olahraga",
        "menulis"
    ]);
    
    recomendation.forEach(function(value) {
        value = value.charAt(0).toUpperCase() + value.slice(1);
        $("#card-recomendation").append(card + mcard + value + ccard);
    });
});