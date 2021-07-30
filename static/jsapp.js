// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

d3.select("#calculate").on("click", function(){
var height = d3.select("#height").node().value
console.log(height)
var angle = d3.select("#angle").node().value;

var AOE_dict = {"breath weapon":60}
var AOE = AOE_dict["breath weapon"]

var origin = height*.9
var length = 360
var opposite = Math.abs(Math.sin(angle)*length)
var midpoint = origin - opposite
var top_of_attack = midpoint + (AOE/2)
var bottom_of_attack = midpoint - (AOE/2)

if (opposite > AOE) {
    var end_of_attack = Math.abs((origin/Math.sin(angle)))
    var end_of_attack_top = Math.abs(((origin+(AOE/2))/Math.sin(angle)))
    var end_of_attack_bottom = Math.abs(((origin-(AOE/2))/Math.sin(angle)))
    console.log("Your attack reaches " + end_of_attack + "inches from you before it hits the ground.")
    var x1 = [0 , end_of_attack];
    var y1 = [origin, 0];
    var data1 = [{x:0, y: origin}, {x: end_of_attack, y:0}];
    var lineFunc = d3.line()
       .x(function(d) { return d.x })
       .y(function(d) { return d.y })

       svg.append('path')
       .attr('d', lineFunc(data1))
       .attr('stroke', 'black')
       .attr('fill', 'none');

    var x2 = [0 , end_of_attack_top];
    var y2 = [origin+(AOE/2), 0];
        
    var x3 = [0 , end_of_attack_bottom];
    var y3 = [origin-(AOE/2), 0];
}

else {
       console.log("Your attack range is from " +top_of_attack + "inches to " +bottom_of_attack+ "inches above the floor")
       var x1 = [0 , length];
       var y1 = [origin, midpoint];
   
       var x2 = [0 , length];
       var y2 = [origin+(AOE/2), top_of_attack];
           
       var x3 = [0 , length];
       var y3 = [origin-(AOE/2), bottom_of_attack];
    }
}
)


// var y = d3.scaleLinear()
//     .domain(y1)
//     .range([ height, 0 ]);
// svg.append("g")
//     .call(d3.axisLeft(y));


// fig = go.Figure()
// fig.add_trace(go.Scatter(
//     x=x1,
//     y=y1,
//     connectgaps = True
// ))
// fig.add_trace(go.Scatter(
//     x=x2,
//     y=y2,
//     connectgaps = True
// ))
// fig.add_trace(go.Scatter(
//     x=x3,
//     y=y3,
//     connectgaps = True
// ))
// fig.show()