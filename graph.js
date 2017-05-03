var ctry_data = [];
var graph_country ;
var country_selected;

function graph(){
    /*console.log(perCountryData)*/
      /*console.log(countryName)*/
      country_selected = $('#countryName').text()
      console.log(country_selected)
      var width = 500;
      var height = 280;

      var margin = {
        top: 5,
        left: 80,
        right: 20,
        bottom: 70
    };

    var svg = d3.select("#viz")
      .classed("active", true)
      .append("svg")
      .attr('width', width)
      .attr('height', height)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.right + ")");

    width = width - margin.left - margin.right;
    height = height - margin.top - margin.bottom;
    /*console.log(width, height)*/

    svg.append('g')
      .attr('transform', 'translate(0, ' + height + ')')
      .attr('class', 'x axis');

    svg.append('g')
      .attr('class', 'y axis');

    for(var j = 0; j< perCountryData.length; j++){
        if(country_selected == perCountryData[j].Countries){
          graph_country = perCountryData[j]
        }   
        
  } 
  console.log(graph_country)
  labels = (Object.keys(graph_country));
  labelsLength = labels.length
  labels = labels.splice(0, (labelsLength-1))

  yValues = (Object.values(graph_country));
  yValuesLength = yValues.length
  yValues = (yValues.splice(0, (yValuesLength-1)))
/*
  console.log(labels, '\n', yValues)*/
  for (var i =0; i<yValues.length; i++){
      d = {};
      d['value'] = parseInt(yValues[i])
      d['key'] = labels[i]
      ctry_data.push(d)
      
  }
  console.log(ctry_data);
  newlabels = ctry_data.map(function(d){return d.key; })
  newValues = ctry_data.map(function(d){return (d.value / 1000000); })

  var y_scale = d3.scaleLinear()
    .range([height, 0])
    .domain([0, d3.max(newValues)]);

  var x_scale = d3.scaleBand()
    .range([0, width])
    .padding(0.1);

  var x_axis = d3.axisBottom(x_scale);
  var y_axis = d3.axisLeft(y_scale);

  /*console.log(newlabels)*/
  x_scale.domain(newlabels);
  y_scale.domain([0, d3.max(newValues)]);

  var bars = svg.selectAll(".bar")
    .data(ctry_data);

  bars
    .exit()
    .attr('height', 0)
    .attr('y', height)
    .remove();

  var new_bars = bars
    .enter()
    .append('rect')
    .attr('height', 0)
    .attr('y', height)
    .attr('class','bar')
    .attr("fill", "rgb(75, 35, 9)");

  new_bars.merge(bars)
    .attr("height", function(d, i){ return height - y_scale(d.value/1000000) })
    .attr("y", function(d, i){ return y_scale(d.value/1000000); })
    .attr("width", x_scale.bandwidth())
    .attr("x", function(d){ return x_scale(d.key); });


  svg.select('.x.axis')
    .call(x_axis);

  svg.select('.y.axis')
    .call(y_axis);

  svg.append("text")
    .attr("transform", "translate(" + width/2 +  "," + (height + margin.bottom/2) + ")")
    .style("text-anchor", "end")
    .style('stroke', '#000')
    .text("Years");

  svg.append("text")
    .attr("transform", "translate(-30," + height/2 + ")rotate(-90)")
    .style("text-anchor", "middle")
    .style('stroke', '#000')
    .text("subscriptions in millions");

}

