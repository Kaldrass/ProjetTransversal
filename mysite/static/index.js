/*
$("#superButton").click(function() {
    alert("ouioui");
    $.get("/output/", function(data) {
        $("#output").html(data);
    }, "html");
});
*/

function ok(i){let xhr = new XMLHttpRequest();
    xhr.open("POST", "arrowMvt");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
      }};

    let data = `{
      "Type": ${i}
    }`;

    xhr.send(data);
    console.log("ok2");
}