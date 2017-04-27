$(function() {
    socket = new io.Socket('localhost');
    socket.connect();
    console.log(socket);
    
    var $placeholder = $('#placeholder');
    var datalen = 100;
    var plot = null;
    var series = {
        label: "Value",
        lines: { 
            show: true,
            fill: true
        },
        data: []
    };

    socket.on('connect', function() {
        $('#conn_status').html('<b>Connected: ' + socket.transport.type + '</b>');
    });
    socket.on('error', function() {
        $('#conn_status').html('<b>Error</b>');
    });
    socket.on('disconnect', function() {
        $('#conn_status').html('<b>Closed</b>');
    });
    socket.on('message', function(msg) {
        var d = $.parseJSON(msg);
        series.data.push([d.x, d.y]);
        while (series.data.length > datalen) {
            series.data.shift();
        }
        if(plot == null && series.data.length > 10) {
            plot = $.plot($placeholder, [series], {
                xaxis:{
                    mode: "time",
                    timeformat: "%H:%M:%S"
                },
                yaxis: { min: 0, max: 5 },
                hooks: {
                    draw: function(plot, canvascontext) {
                        // Redraw the graph in 50ms
                        setTimeout(function() {
                            plot.setData([series]);
                            plot.setupGrid();
                            plot.draw();}, 50);
                    }
                }
            });
        }
    });
});

