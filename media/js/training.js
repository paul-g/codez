var g, renderer;

/* only do all this when document has finished loading (needed for RaphaelJS) */
showTrainingGraph = function(div_id, training_data) {
    var width = $(document).width() / 2;
    var height = $(document).height() / 2;

    g = new Graph();

    var DIR = {directed: true};

    for (var i = 0; i < training_data.length; i++) {
        var node = training_data[i];
        var nodeName = node[0];
        var nodeDeps = node[1];
        for (var j = 0; j < nodeDeps.length; j++) {
            g.addEdge(nodeDeps[j], nodeName, DIR);
            // TODO(paul-g): improve layout logic
        }
    }

    // Layout
    var layouter = new Graph.Layout.Spring(g);
    var renderer = new Graph.Renderer.Raphael('canvas', g, width, height);
};
