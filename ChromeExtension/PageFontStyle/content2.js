chrome.runtime.sendMessage({todo: "showPageAction"});

var datapoints = [];
var today = new Date();
var price = 2500;
for (let i=30; i>0; i--) {
    let date = new Date()
    date.setDate(today.getDate()-i);
    price += Math.random()*400-200;
    datapoints.push({x: date, y:price})
}

var options = [
    {
     title: {
         text: "Price"
     },
     
     axisY: {
        includeZero: false
     },
     
     toolTip:{
        enabled: false,
      },
     data: [              
         {
         	type: "line",
         	dataPoints: datapoints
    	}
     ]
 	}        
];

$(window).on('load', function(){
var images = [];
var chartClassElements = document.getElementsByClassName("pi-cr");
var cards = document.getElementsByClassName("pc-wrp");
for (let i=0; i<chartClassElements.length; i++) {
    let chartClass = chartClassElements[i];
    images.push(chartClass.children[0]);
    let card = cards[i];
    $(card).children().bind('mouseenter', function() {
        
            var chart = new CanvasJS.Chart(chartClass, options[0])
            chart.render();
            console.log("uyuuuuuu")
            
    });
    $(card).children().bind('mouseleave', function() {
        
            while (chartClass.firstChild) {
                chartClass.removeChild(chartClass.firstChild);
                }
            chartClass.appendChild(images[i]);
            console.log("omgomogmog")
            
        });
    $(card).click(function() {
        while (chartClass.firstChild) {
            chartClass.removeChild(chartClass.firstChild);
            }
        chartClass.appendChild(images[i]);
        console.log("omgomogmog")
    });
    }
});