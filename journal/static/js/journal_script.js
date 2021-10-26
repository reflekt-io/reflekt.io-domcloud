// AJAX for loading journals

const months = [
  "Januari",
  "Februari",
  "Maret",
  "April",
  "Mei",
  "Juni",
  "Juli",
  "Agustus",
  "September",
  "Oktober",
  "November",
  "Desember",
];

const days = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];

const FEELINGS = {
  "antusias": "Antusias",
  "gembira": "Gembira",
  "takjub": "Takjub",
  "semangat": "Semangat",
  "bangga": "Bangga",
  "penuh_cinta": "Penuh Cinta",
  "santai": "Santai",
  "tenang": "Tenang",
  "puas": "Puas",
  "lega": "Lega",
  "marah": "Marah",
  "takut": "Takut",
  "stres": "Stres",
  "waspada": "Waspada",
  "kewalahan": "Kewalahan",
  "kesal": "Kesal",
  "malu": "Malu",
  "cemas": "Cemas",
  "lesu": "Lesu",
  "sedih": "Sedih",
  "duka": "Duka",
  "bosan": "Bosan",
  "kesepian": "Kesepian",
  "bingung": "Bingung"
};

const FACTORS = {
    "keluarga": "Keluarga",
    "pekerjaan": "Pekerjaan",
    "teman": "Teman",
    "percintaan": "Percintaan",
    "kesehatan": "Kesehatan",
    "pendidikan": "Pendidikan",
    "tidur": "Tidur",
    "perjalanan": "Perjalanan",
    "bersantai": "Bersantai",
    "makanan": "Makanan",
    "olahraga": "Olahraga",
    "seni": "Seni",
    "hobi": "Hobi",
    "cuaca": "Cuaca",
    "belanja": "Belanja",
    "hiburan": "Hiburan",
    "keuangan": "Keuangan",
    "ibadah": "Ibadah",
    "refleksi_diri": "Refleksi Diri",
};

function formatDate(dateData) {
  // Parse informations
  var year = dateData.getFullYear();
  var monthName = months[dateData.getMonth()];
  var dayName = days[dateData.getDay()];
  var date = dateData.getDate();
  var hour = dateData.getHours();
  var minute = dateData.getMinutes();
  var second = dateData.getSeconds();
  // Make formatted date
  var formattedDate = `${dayName}, ${date} ${monthName} ${year}, pukul ${hour}.${minute}.${second}.`;
  return formattedDate;
}

function formatFeelings(feelingsData) {
  var formattedFeelings = "";
  for (let i = 0; i < feelingsData.length; i++) {
    formattedFeelings += FEELINGS[feelingsData[i]];
    if (i < feelingsData.length - 1) {
      formattedFeelings += ", ";
    }
  }
  return formattedFeelings;
}

function formatFactors(factorsData) {
  var formattedFactors = "";
  for (let i = 0; i < factorsData.length; i++) {
    formattedFactors += FACTORS[factorsData[i]];
    if (i < factorsData.length - 1) {
      formattedFactors += ", ";
    }
  }
  return formattedFactors;
}

$(document).ready(function () {
  $.ajax({
    url: "/journal/json",
    success: function (results) {
      console.log(results);
      results.map((result) => {
        // Date customatization
        var dateData = new Date(result.fields.date);
        formattedDate = formatDate(dateData);
        // Feelings formatting
        var feelingsData = result.fields.feeling.split(",");
        formattedFeelings = formatFeelings(feelingsData);
        // Factors formatting
        var factorsData = result.fields.factor.split(",");
        formattedFactors = formatFactors(factorsData);
        // Append to date
        $("#journal-table-body").append(`
                <tr>
                    <td>${formattedDate}</td>
                    <td>${formattedFeelings}</td>
                    <td>${formattedFactors}</td>
                    <td>${result.fields.anxiety_rate}</td>
                    <td>${result.fields.summary}</td>
                </tr>`);
      });
    },
  });
});
