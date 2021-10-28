$(document).ready(function () {
    console.log("TESSSS");
  $.ajax({
    url: "/pojok-curhat/json",
    success: function (results) {
      console.log(results);
      results.map((result) => {
        $("#curhat_container").append(`
          <div class="card-container">
          <div class="card">
            <div class="card-header">
              <h4>${result.fields.title}</h4>
              </div>
              <h5>${result.fields.fromCurhat}</h5>
              <p>${result.fields.message}</p>
          </div>
        </div>`);
      });
    },
  });
});