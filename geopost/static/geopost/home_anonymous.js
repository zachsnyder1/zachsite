$(document).ready(function () {
	/*
	/  -- LAYERS --
	*/
	// Entries source
	var entriessource = new ol.source.Vector({
		url: 'http://localhost:8080/geoserver/mypoints/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=mypoints:test_points&srsname=EPSG:4326&outputFormat=application/json',
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
	/  -- INTERACTIONS --
	*/
	var dragpan = new ol.interaction.DragPan();
	var select = new ol.interaction.Select({
		condition: ol.events.condition.click,
		layers: [entries]
	});
	// On Select, Display Info
	select.on('select', function (evt) {
		targetEntry = evt.target.getFeatures().item(0);
		$('#title').text(targetEntry.get('title'));
		$('#body').text(targetEntry.get('body'));
		$.ajax({
			url: 'http://127.0.0.1:8000/projects/geopost/photo/' + targetEntry.get('uuid'),
			success: function(data, status, xhr) {
				srcStr = 'data:' + xhr.getResponseHeader('Content-Type') + ';base64,' + data;
				$('#photo').attr('src', srcStr);
			},
			error: function(xhr) {
				console.log("ERROR");
			}
		});
	});
	
	/*
	/  -- UPDATE MAP WITH NEW ELEMENTS --
	*/
	// Adding elements to map
	OL_OBJ.map.addInteraction(select);
	OL_OBJ.map.addInteraction(dragpan);
	OL_OBJ.map.addLayer(entries);
	// Readjusting the view
	OL_OBJ.rescaleView(entriessource);
	OL_OBJ.resetView();
});