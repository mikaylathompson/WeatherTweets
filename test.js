    

var width = 800,
    height = 500;

svg = d3.select("svg")
    .attr("width", width)
    .attr("height", height);

var y = d3.scale.linear()
    .range([height,0])
    .domain([24,50]);

var x = d3.scale.linear()
    .range([0,width])
    .domain([-124,-66]);

d3.json("storm_texts.json", function(error, data) {
    svg.selectAll("circle")
        .data(data)
      .enter().append("circle")
        .style("fill", function(d) {
            if((d.text.indexOf("hunder")>-1) || (d.text.indexOf("HUNDER")>-1)) {
                return "darkred";
            }
            if ((d.text.indexOf("ightning")!=-1) || (d.text.indexOf("IGHTNING")!=-1)) {
                return "gold";
            }
            if((d.text.indexOf("torm")>-1) || (d.text.indexOf("TORM")>-1)) {
                return "slategray";
            }
            return "dodgerblue";})
        .attr("r", 5)
        .attr("cx", function(d) {return x(d.coords[0]); } )
        .attr("cy", function(d) {return y(d.coords[1]); } )
        .attr("class", function(d) {return d.place;} );
});


    
    
    
//    { "text": "I hear thunder!\u26a1\ufe0f\u2614\ufe0f My luck it will be pouring when it's time to load the car at 1am! #cooperstown14 \ud83d\udc99\u26be\ufe0f", 
//      "time": "Fri Jun 20 03:38:53 +0000 2014", 
//      "coords": [-78.92391202, 35.27236568], 
//      "location": "", 
//      "country": "United States", 
//      "place": "North Carolina, USA", 
//      "geo": [35.27236568, -78.92391202]}
