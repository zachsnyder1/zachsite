OL_OBJ = {
	// TILE LAYER
	tile: new ol.layer.Tile({
		source: new ol.source.MapQuest({layer: 'sat'})
	}),
	// THE VIEW
	view: new ol.View({
		center: [0, 0],
		zoom: 3,
		maxZoom: 16
	}),
	// Scale View to Extent of A Layer
	rescaleView: function (lyrSrcObj) {
		lyrSrcObj.on('change', function (e) {
			if (lyrSrcObj.getState() == 'ready') {
				extent = lyrSrcObj.getExtent();
				OL_OBJ.view.fit(extent, OL_OBJ.map.getSize());
			}
		});
	},

	// Reset View to Clear Distortion
	resetView: function () {
		setTimeout(function(){OL_OBJ.map.updateSize();}, 200);
	}
};

$(document).ready(function () {
	// THE MAP
	OL_OBJ.map = new ol.Map({
		target: 'map',
		layers: [OL_OBJ.tile],
		view: OL_OBJ.view,
		interactions: []
	});
});