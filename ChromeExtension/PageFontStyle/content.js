chrome.runtime.sendMessage({todo: "showPageAction"});

  var datapoints = [
    { x: new Date(2012, 01, 1), y: 450 },
    { x: new Date(2012, 01, 2), y: 414 },
    { x: new Date(2012, 01, 3), y: 520 },
    { x: new Date(2012, 01, 4), y: 460 },
    { x: new Date(2012, 01, 5), y: 450 },
    { x: new Date(2012, 01, 6), y: 500 },
    { x: new Date(2012, 01, 7), y: 480 },
    { x: new Date(2012, 01, 8), y: 480 },
    { x: new Date(2012, 01, 9), y: 410 },
    { x: new Date(2012, 01, 10), y: 500 },
    { x: new Date(2012, 01, 11), y: 300 },
    { x: new Date(2012, 01, 12), y: 350 },
    { x: new Date(2012, 01, 13), y: 410 },
    { x: new Date(2012, 01, 14), y: 470 },
    { x: new Date(2012, 01, 15), y: 550 },
    { x: new Date(2012, 01, 16), y: 555 },
    { x: new Date(2012, 01, 17), y: 572 },
    { x: new Date(2012, 01, 18), y: 600 },
    { x: new Date(2012, 01, 19), y: 600 },
    { x: new Date(2012, 01, 20), y: 640 },
    { x: new Date(2012, 01, 21), y: 700 },
    { x: new Date(2012, 01, 22), y: 750 },
    { x: new Date(2012, 01, 23), y: 760 },
    { x: new Date(2012, 01, 24), y: 760 },
    { x: new Date(2012, 01, 25), y: 765 },
    { x: new Date(2012, 01, 26), y: 780 },
    { x: new Date(2012, 01, 27), y: 900 },
    { x: new Date(2012, 01, 28), y: 870 },
    { x: new Date(2012, 01, 29), y: 880 },
    { x: new Date(2012, 01, 30), y: 850 }
    ];

var options = [
    {
     title: {
         text: "Price"
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
    cards[i].onmouseenter = (function() {
        return function() {
            var chart = new CanvasJS.Chart(chartClass, options[0])
            chart.render();
            }
    }());
    cards[i].onmouseleave = (function() {
        return function() {
            while (chartClass.firstChild) {
                chartClass.removeChild(chartClass.firstChild);
                }
            chartClass.appendChild(images[i]);
            }
        }());
    }
});