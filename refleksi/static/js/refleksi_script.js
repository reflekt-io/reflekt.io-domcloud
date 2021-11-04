$(document).ready(function() {
    $(document).on("submit", "#kegiatanForm", function(event) {
        event.preventDefault();
        $.ajax({
            data: $(this).serialize(),
            type: "POST",
            url: "add-deskripsi",
            success: function (response) {
                $("#button-close").click();
                
                var status = "<h2>Kegiatan yang pernah kamu lakukan</h2>";
                status += "<p>Halo "+response.user+"! Di bawah ini beberapa kegiatan yang pernah kamu lakukan sebelumnya.</p>";
                $(".status-kegiatan").html(status);

                var kegiatan_baru = "<div class='card mb-4 past-card'><div class='card-body'>";
                kegiatan_baru += "<h4>"+response.nama+"</h4><p>"+response.deskripsi+"</p></div></div>";
                if (response.nama != "" && response.deskripsi != "") {
                    $(".riwayat-kegiatan").append(kegiatan_baru);
                }
            },
            error: function (request, status, error) {
                console.log(request.responseText);
                $("#button-close").click();
            }
        });
    });

    $(document).on("click", ".add-rec", function() {
    	var nama = $(this).find(".card-body h4").text();
    	if (nama == "(+) Tambah Rekomendasi") {
    		$(this).attr("href", "/refleksi/add-kegiatan")
    	} else {
            $("#id_deskripsi").val("");
    		$("#id_nama").val(nama);
    		$("#id_nama").prop("readonly", true);
    		$("#id_nama").css("background-color", "white");
    	}
    });

    var recomendation = new Set([
        "bermain game",
        "menonton film",
        "membaca buku",
        "mendengarkan musik",
        "belanja",
        "mengunjungi tempat wisata",
        "olahraga",
        "menulis",
        "memasak",
        "membersihkan rumah"
    ]);

    add_recomendation(recomendation);

    function add_recomendation(daftar) {
        $.ajax({
            data: {},
            type: "GET",
            url: "add-deskripsi",
            success: function (response) {
                $.each(response, function(index, value) {
                    var nama = value.fields["nama"];
                    daftar.add(nama.toLowerCase());
                });
                show_recomendation(daftar);
            },
            error: function (request, status, error) {
                console.log(request.responseText);
            }
        });
    }

    function show_recomendation(daftar) {
        var card = "<div class='card mb-4 add-card'>";
        card += "<a class='stretched-link text-decoration-none add-rec' href ";
        card += "data-toggle='modal' data-target='#modal-form'>"
        card += "<div class='card-body text-center'><h4>";
        var ccard = "</h4></div></a></div>";

        daftar.forEach(function(value) {
            value = value.charAt(0).toUpperCase() + value.slice(1);
            $("#card-recomendation").append(card + value + ccard);
        });
    }
});