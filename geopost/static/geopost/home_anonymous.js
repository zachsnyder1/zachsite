$(document).ready(function () {
	/*
	/ LAYERS:
	*/
	
	// Tile Layer:
	var tile = new ol.layer.Tile({
		source: new ol.source.MapQuest({layer: 'sat'})
	});
	
	// Entries source
	var entriessource = new ol.source.Vector({
		url: 'http://localhost:8080/geoserver/mypoints/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=mypoints:real_points&srsname=EPSG:4326&outputFormat=application/json',
		format: new ol.format.GeoJSON()
	});
	
	// Entries point layer
	var entries = new ol.layer.Vector({
		source: entriessource,
		style: new ol.style.Style({
			image: new ol.style.Circle({
				radius: 9,
				fill: new ol.style.Fill({color: 'yellow'})
			})
		})
	});
	
	/*
	/ VIEWS:
	*/
	
	// The View
	var initview = new ol.View({
		center: [0, 0],
		zoom: 3,
		maxZoom: 16
	});
	
	/*
	/ INTERACTIONS:
	*/
	
	// Selection Interaction
	var select = new ol.interaction.Select({
		condition: ol.events.condition.click,
		layers: [entries]
	});
	
	// Dragpan Interaction
	var dragpan = new ol.interaction.DragPan();
	
	/*
	/ THE MAP:
	*/
	
	// Map Declaration
	var map = new ol.Map({
		target: 'map',
		layers: [tile, entries],
		view: initview,
		interactions: [select, dragpan]
	});
	
	/*
	/ EVENT HANDLERS:
	*/
	
	// View Scales to Extent of Entries
	entriessource.on('change', function (e) {
		if (entriessource.getState() == 'ready') {
			extent = entriessource.getExtent();
			initview.fit(extent, map.getSize());
		}
	});
	
	// On Select, Display Info
	select.on('select', function (evt) {
		$('#title').text(evt.target.getFeatures().item(0).get('title'));
		$('#body').text(evt.target.getFeatures().item(0).get('body'));
		
	});
	
	/*
	/ POST-SCRIPT:
	*/
	
	// Reset the View to Clear Distortion
	setTimeout(function(){map.updateSize();}, 200);

});