// SCOPING GLOBAL RESOURCES
OL_OBJ = {}
// TILE LAYER
OL_OBJ.featNs = "/mypoints",
OL_OBJ.featType = "test_points",
OL_OBJ.defaultSRS = "EPSG:3857",
OL_OBJ.tile = new ol.layer.Tile({
	source: new ol.source.MapQuest({layer: 'sat'})
});
// ENTRIES SOURCE
OL_OBJ.entriessource = new ol.source.Vector({
	url: 'http://localhost:8080/geoserver/mypoints/ows?service=WFS&ve' +
		'rsion=2.0.0&request=GetFeature&typeName=mypoints:test_points' +
		'&srsname=EPSG:4326&outputFormat=application/json',
	format: new ol.format.GeoJSON()
});
// ENTRIES LAYER
OL_OBJ.entries = new ol.layer.Vector({
	source: OL_OBJ.entriessource,
	style: new ol.style.Style({
		image: new ol.style.Circle({
			radius: 9,
			fill: new ol.style.Fill({color: 'yellow'})
		})
	})
});
// THE VIEW
OL_OBJ.view = new ol.View({
	center: [0, 0],
	zoom: 3,
	maxZoom: 16
});
// Scale View to Extent of A Layer
OL_OBJ.rescaleView = function (lyrSrcObj) {
	lyrSrcObj.on('change', function (e) {
		if (lyrSrcObj.getState() == 'ready') {
			extent = lyrSrcObj.getExtent();
			OL_OBJ.view.fit(extent, OL_OBJ.map.getSize());
		}
	});
};
// Reset View to Clear Distortion
OL_OBJ.resetView = function () {
	setTimeout(function(){OL_OBJ.map.updateSize();}, 200);
};

$(document).ready(function () {
	// THE MAP
	OL_OBJ.map = new ol.Map({
		target: 'map',
		layers: [OL_OBJ.tile, OL_OBJ.entries],
		view: OL_OBJ.view,
		interactions: []
	});
});