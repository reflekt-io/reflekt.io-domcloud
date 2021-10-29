$(document).ready(function () {
  $.ajax({
    url: "/kutipan-penyemangat/json",
    success: function (results) {
      console.log(results);
      results.map((result) => {
        $("#quotes_container").append(`
          <div class="card card1">
          <div class="container">
            <div class="field">
              <h3>${result.fields.name}</h3>
              <p>${result.fields.quotes_form}</p>
            </div>
          </div>
        </div>`);
      });
    },
  });
});
