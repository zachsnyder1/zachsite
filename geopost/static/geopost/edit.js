// collect fid from url query string, if present
var qstrArray = window.location.search.split('?');
var entryFID;
for (i = 1; i < qstrArray.length; i++) {
	var arg = qstrArray[i].split('=');
	if (arg[0] == 'fid') {
		entryFID = arg[1];
		break;
	}
}

$(document).ready(function () {
	/*
	/  -- LAYERS --
	*/
	// Entries source
	var entriessource = new ol.source.Vector({
		url: 'http://localhost:8080/geoserver/mypoints/ows?service=WFS&ve' +
			'rsion=2.0.0&request=GetFeature&typeName=mypoints:test_points' +
			'&srsname=EPSG:4326&outputFormat=application/json',
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
	// Connect MODIFY interaction to modify button:
	var modbtn = $('#modify-btn');
	var modActive = false;
	function toggleModify() {
		if (drawActive === false) {
			OL_OBJ.map.removeInteraction(dragpan);
			OL_OBJ.map.addInteraction(modify);
			modActive = true;
		} else {
			OL_OBJ.map.removeInteraction(modify);
			OL_OBJ.map.addInteraction(dragpan);
			modActive = false;
		}
	}
	modbtn.on('click', toggleModify);
	
	/*
	/  -- MISC. PREP --
	*/
	// WFS transaction format object
	var wfst = new ol.format.WFS({
		featureNS: 'mypoints',
		featureType: 'test_points'
	});
	var newentry; // Holds new entry point
	// when done modifying, update newpoint to new coordinates
	modify.on('modifyend', function(evt) {
		newpoint = evt.features.item(0);
	});




		newpoint = evt.feature;
		var form = $('#the-form');
		var dummySubmitBtn = $('#dummy-submit');
		form.css('display', 'block');
		dummySubmitBtn.css('display', 'block');
		// On click, prepare and submit form
		dummySubmitBtn.on('click', function(evt) {
			select.getFeatures().clear();
			entryUUID = uuid.v4();
			newpoint.set('uuid', entryUUID);
			newpoint.set('title', $('#title').val());
			newpoint.set('body', $('#body').val());
			var node = writeTrans([newpoint], wfsOperation);
			var wfsxml =  new XMLSerializer().serializeToString(node)
			$('#wfsxml').attr('value', wfsxml);
			$('#uuid').attr('value', entryUUID);
			$('#submit-btn').click();
		});
	
	
	
	
	/*
	/  -- IF EDITING EXISTING FEATURE --
	*/
	if (entryFID) {
		// ADD QUERY STR TO FORM URL
		var formUrl = $('#the-form').attr('action');
		$('#the-form').attr('action', formUrl + '?fid=' + entryFID);
		var editfeat;
		entriessource.on('addfeature', function(e) {
			if (e.feature.get('fid') == entryFID) {
				select.getFeatures().push(e.feature);
			}
		});
		// POPULATE THE FORM WITH ATTRIBUTES
		wfsOperation = 'UPDATE';
	}
	
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