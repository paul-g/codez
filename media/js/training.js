var g, renderer;

/* only do all this when document has finished loading (needed for RaphaelJS) */
window.onload = function() {
    // TODO(paul-g): fetch training data from server
    var width = $(document).width() / 2;
    var height = $(document).height() / 2;

    g = new Graph();

    var DIR = {directed: true};

    // Training nodes
    var nodeCppPrimer = "C++ primer";
    var nodeJavaPrimer = "Java primer";
    var nodeHaskellPrimer = "Haskell primer";
    var nodeDataStructures = "Data Structures";
    var nodeGraphsOne = "Graphs Algorithms One";
    var nodeGraphsAdv = "Graphs Advanced";
    var nodeGraphsHardcore = "Graphs Hardcore";

    // Training edges
    g.addEdge(nodeCppPrimer, nodeDataStructures, DIR);
    g.addEdge(nodeJavaPrimer, nodeDataStructures, DIR);
    g.addEdge(nodeHaskellPrimer, nodeDataStructures, DIR)

    g.addEdge(nodeCppPrimer, nodeGraphsOne, DIR);
    g.addEdge(nodeJavaPrimer, nodeGraphsOne, DIR);
    g.addEdge(nodeHaskellPrimer, nodeGraphsOne, DIR)

    g.addEdge(nodeGraphsOne, nodeGraphsAdv, DIR);
    g.addEdge(nodeGraphsAdv, nodeGraphsHardcore, DIR);

    // Layout
    var layouter = new Graph.Layout.Spring(g);
    var renderer = new Graph.Renderer.Raphael('canvas', g, width, height);
};
