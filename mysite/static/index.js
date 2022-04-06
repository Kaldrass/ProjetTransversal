$("#superButton").click(function() {
    alert("ouioui");
    $.get("/output/", function(data) {
        $("#output").html(data);
    }, "html");
});