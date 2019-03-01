chrome.runtime.sendMessage({todo: "showPageAction"});
(function(){

    let datapoints = [];
    let today = new Date();
    let price = 2500;
    for (let i=30; i>0; i--) {
        let date = new Date()
        date.setDate(today.getDate()-i);
        price += Math.random()*400-200;
        datapoints.push({x: date, y:price})
    }

    let options = [
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

    function replaceImage() {
        while (ele.firstChild) {
            ele.removeChild(ele.firstChild);
        }
        ele.appendChild(im);
        console.log('im')
    }
    
    $(window).on('load', function(){
        let images = [];
        let chartClassElements = document.getElementsByClassName("pi-cr");
        chartClassElements = Array.prototype.slice.call(chartClassElements);
        let cards = document.getElementsByClassName("pc-wrp");

        chartClassElements.forEach(function(inner, i) {
            images.push(inner.children[0]);

            $(cards[i]).children().bind('mouseenter', function() {
                let chart = new CanvasJS.Chart(inner, options[0]);
                chart.render();
            });

            $(cards[i]).children().bind('mouseleave', replaceImage(inner, images[i]));
            $(cards[i]).click(replaceImage(inner, images[i]));
        });

    });
})();
        /*
        for (let i=0; i<chartClassElements.length; i++) {
            let chartClass = chartClassElements[i];
            images.push(chartClass.children[0]);
            let card = cards[i];
            $(card).children().bind('mouseenter', function() {
                
                    var chart = new CanvasJS.Chart(chartClass, options[0])
                    chart.render();
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
*/

