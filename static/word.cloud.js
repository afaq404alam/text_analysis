(function () {
    $('#get-stats').click(function () {
        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: "/post_text",
            data: JSON.stringify($('#txt-for-analysis').val()),
            success: function (data) {
                $('#div-word-cloud').empty();
                render_cloud(data);
            },
            fail: function () {  
                alert('Error analyzing text.');
            },
            dataType: "json"
        });
    });


    var render_cloud = function (frequency_list) {

var fill = d3.scaleLinear();

var layout = d3.layout.cloud()
    .size([500, 500])
    .words(frequency_list)
    .padding(5)
    .rotate(function() { return ~~(Math.random() * 2) * 90; })
    .font("Impact")
    .fontSize(function(d) { return d.size * 15; })
    .on("end", draw);

layout.start();

function draw(words) {
  d3.select("#div-word-cloud").append("svg")
      .attr("width", layout.size()[0])
      .attr("height", layout.size()[1])
    .append("g")
      .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text")
      .data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) { return fill(i); })
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function(d) { return d.text; });
}
    };


}());