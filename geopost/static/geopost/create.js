$(document).ready(function () {
	/*
	/  -- LAYERS --
	*/
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
	// Draw Entry source
	var drawentrysrc = new ol.source.Vector({});
	// Draw Entry layer
	var drawentry = new ol.layer.Vector({
		source: drawentrysrc,
		style: new ol.style.Style({
			image: new ol.style.Circle({
				radius: 12,
				fill: new ol.style.Fill({
					color: 'red'
				})
			})
		})
	});
	
	/*
	/  -- INTERACTIONS --
	*/
	// DRAGPAN
	var dragpan = new ol.interaction.DragPan();
	// SELECT
	var select = new ol.interaction.Select({
		condition: ol.events.condition.click,
		layers: [drawentry]
	});
	// MODIFY
	var modify = new ol.interaction.Modify({
		features: select.getFeatures()
	});
	// DRAW
	var drawinteraction = new ol.interaction.Draw({
		source: drawentrysrc,
		type: 'Point'
	});
	// Connect DRAW interaction to draw button:
	var drawbtn = $('#drawbtn');
	var drawActive = false;
	function toggleDraw() {
		if (drawActive === false) {
			OL_OBJ.map.removeInteraction(dragpan);
			OL_OBJ.map.addInteraction(drawinteraction);
			drawActive = true;
		} else {
			OL_OBJ.map.removeInteraction(drawinteraction);
			OL_OBJ.map.addInteraction(dragpan);
			drawActive = false;
		}
	}
	drawbtn.on('click', toggleDraw);
	
	/*
	/  -- MISC. PREP --
	*/
	// WFS transaction format object
	var wfst = new ol.format.WFS({
		featureNS: 'mypoints',
		featureType: 'real_points'
	});
	var newentry; // Holds new entry point
	// when done modifying, update newpoint to new coordinates
	modify.on('modifyend', function(evt) {
		newpoint = evt.features.item(0);
	});
	drawinteraction.on('drawend', function(evt) {
		OL_OBJ.map.removeInteraction(drawinteraction);
		drawbtn.hide();
		newpoint = evt.feature;
		var form = $('#the-form');
		var dummySubmitBtn = $('#dummy-submit');
		form.css('display', 'block');
		dummySubmitBtn.css('display', 'block');
		// On click, prepare and submit form
		dummySubmitBtn.on('click', function(evt) {
			select.getFeatures().clear();
			entryUUID = uuid.v4();
			newpoint.set('the_geom', newpoint.getGeometry());
			newpoint.set('geometry', null);
			newpoint.set('uuid', entryUUID);
			newpoint.set('title', $('#title').val());
			newpoint.set('body', $('#body').val());
			var node = wfst.writeTransaction([newpoint], null, null, {
				gmlOptions: {srsName: "EPSG:3857"},
				featureNS: "mypoints",
				featureType: "real_points"
			});
			$('#wfsxml').attr('value', new XMLSerializer().serializeToString(node));
			$('#uuid').attr('value', entryUUID);
			$('#submit-btn').click();
		});
	});
	
	/*
	/  -- UPDATE MAP WITH NEW ELEMENTS --
	*/
	// Adding elements to map
	OL_OBJ.map.addInteraction(select);
	OL_OBJ.map.addInteraction(dragpan);
	OL_OBJ.map.addLayer(entries);
	OL_OBJ.map.addLayer(drawentry);
	// Readjusting the view
	OL_OBJ.rescaleView(entriessource);
	OL_OBJ.resetView();
});