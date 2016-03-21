// wrapper for 
OL_OBJ.writeTrans = function (pntArray) {
	// WFS transaction format object
	var wfst = new ol.format.WFS({
		featureNS: OL_OBJ.featNs,
		featureType: OL_OBJ.featType
	});
	var options = {
		gmlOptions: {srsName: OL_OBJ.defaultSRS}, 
		featureNS: OL_OBJ.featNs,
		featureType: OL_OBJ.featType
	};
	if (OL_OBJ.wfsOperation == 'CREATE') {
		return wfst.writeTransaction(pntArray, null, null, options);
	} else if (OL_OBJ.wfsOperation == 'UPDATE') {
		return wfst.writeTransaction(null, pntArray, null, options);
	} else if (OL_OBJ.wfsOperation == 'DELETE') {
		return wfst.writeTransaction(null, null, pntArray, options);
	}
};
// interaction toggle handler for buttons
OL_OBJ.toggleInter = function (interaction, dragpan, active) {
	return function() {
		if (active === false) {
			OL_OBJ.map.removeInteraction(dragpan);
			OL_OBJ.map.addInteraction(interaction);
			active = true;
		} else {
			OL_OBJ.map.removeInteraction(interaction);
			OL_OBJ.map.addInteraction(dragpan);
			active = false;
		}
	};
};
OL_OBJ.wfsOperation = 'CREATE'; // Default WFS transaction is insertion
// collect fid from url query string, if present
OL_OBJ.entryFID = function() {
	var qstrArray = window.location.search.split('?');
	for (i = 1; i < qstrArray.length; i++) {
		var arg = qstrArray[i].split('=');
		if (arg[0] == 'fid') {
			return arg[1];
		}
	}
	return undefined;
}();

$(document).ready(function () {
	/*
	/  -- LAYERS --
	*/
	// Dummy Draw Source (so that modifying feature of 
	// the actual draw source doesn't rescale the view)
	var dummydrawsrc = new ol.source.Vector({});
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
	var draw = new ol.interaction.Draw({
		source: drawentrysrc,
		type: 'Point'
	});
	
	/*
	/  -- MISC. PREP --
	*/
	var newentry; // Holds new entry point
	// when done modifying, update newpoint to new coordinates
	modify.on('modifyend', function(evt) {
		newpoint = evt.features.item(0);
	});
	
	/*
	/  -- UPDATE MAP WITH NEW ELEMENTS --
	*/
	// Adding elements to map
	OL_OBJ.map.addInteraction(select);
	OL_OBJ.map.addInteraction(dragpan);
	OL_OBJ.map.addLayer(drawentry);
	// Readjusting the view
	OL_OBJ.resetView();
	
	/*
	/  -- MAIN --
	*/
	// the editing buttons
	var drawbtn = $('#drawbtn');
	var modbtn = $('#modbtn');
	// the form elements
	var form = $('#the-form');
	var titleInput = $('#title');
	var bodyInput = $('#body');
	var uuidInput = $('#uuid');
	var wfsxmlInput = $('#wfsxml');
	var dummySubmitBtn = $('#dummy-submit');
	var submitBtn = $('#submit-btn');
	// BOOLS indicating whether interactions are attached to the map
	var drawActive = false;
	var modActive = false;
	// IF EDITING EXITING ENTRY:
	if (OL_OBJ.entryFID) {
		// HIDE DRAW BUTTON
		drawbtn.hide();
		// ADD QUERY STR TO FORM URL
		var formUrl = form.attr('action');
		form.attr('action', formUrl + '?fid=' + OL_OBJ.entryFID);
		// FIND FEATURE BEING EDITED:
		OL_OBJ.entriessource.on('addfeature', function(e) {
			if (e.feature.get('fid') == OL_OBJ.entryFID) {
				// move feature to drawentry source,
				// also copy to the dummy draw source
				drawentrysrc.addFeature(e.feature);
				dummydrawsrc.addFeature(e.feature.clone());
				OL_OBJ.entriessource.removeFeature(e.feature);
				// select it
				//select.getFeatures().push(e.feature);
				// POPULATE THE FORM WITH ITS ATTRIBUTES
				titleInput.val(e.feature.get('title'));
				bodyInput.val(e.feature.get('body'));
				// STORE UUID
				OL_OBJ.entryUUID = e.feature.get('uuid');
			}
		});
		// set WFS operation to update
		OL_OBJ.wfsOperation = 'UPDATE';
		// rescale view to dummy draw source
		OL_OBJ.rescaleView(dummydrawsrc);
	// ELSE, IF CREATING NEW ENTRY:
	} else {
		// HIDE MODIFY GEOM BUTTON
		modbtn.hide()
		// Connect DRAW interaction to draw button:
		drawbtn.on('click', OL_OBJ.toggleInter(draw, dragpan, drawActive));
		// on drawend display the form 
		draw.on('drawend', function(evt) {
			OL_OBJ.map.removeInteraction(draw);
			OL_OBJ.map.addInteraction(dragpan);
			drawbtn.hide();
			modbtn.show();
			newpoint = evt.feature;
		});
		// MAKE AND STORE NEW UUID
		OL_OBJ.entryUUID = uuid.v4();
		// rescale view to entries source
		OL_OBJ.rescaleView(OL_OBJ.entriessource);
	}
	// Connect MODIFY interaction to modify geom button
	modbtn.on('click', OL_OBJ.toggleInter(modify, dragpan, modActive));
	// Dummy Submit Btn: on click prepare and subit form
	dummySubmitBtn.on('click', function(evt) {
		select.getFeatures().clear();
		newpoint.set('uuid', OL_OBJ.entryUUID);
		newpoint.set('title', titleInput.val());
		newpoint.set('body', bodyInput.val());
		var node = OL_OBJ.writeTrans([newpoint]);
		var wfsxml =  new XMLSerializer().serializeToString(node)
		wfsxmlInput.attr('value', wfsxml);
		uuidInput.attr('value', OL_OBJ.entryUUID);
		submitBtn.click();
	});
});