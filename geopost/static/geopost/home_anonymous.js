$(document).ready(function () {	
	/*
	/  -- INTERACTIONS --
	*/
	var dragpan = new ol.interaction.DragPan();
	var select = new ol.interaction.Select({
		condition: ol.events.condition.click,
		layers: [OL_OBJ.entries]
	});
	
	/*
	/  -- MISC. PREP --
	*/
	var wfst = new ol.format.WFS({
		featureNS: OL_OBJ.featNs,
		featureType: OL_OBJ.featType
	});
	
	/*
	/  -- UPDATE MAP WITH NEW ELEMENTS --
	*/
	// Adding elements to map
	OL_OBJ.map.addInteraction(select);
	OL_OBJ.map.addInteraction(dragpan);
	// Readjusting the view
	OL_OBJ.rescaleView(OL_OBJ.entriessource);
	OL_OBJ.resetView();
	
	/*
	/  -- MAIN --
	*/
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
		
		// update the edit and delete button 'click' listeners:
		$('#edit-btn').on('click', function() {
			var base_url = $('#geopost-home').attr('data-geopost-home');
			var curr_fid = targetEntry.get('fid');
			window.location = base_url + '?fid=' + curr_fid;
		});
		$('#delete-btn').on('click', function() {
			var node = wfst.writeTransaction(null, null, [targetEntry], {
				featureNS: OL_OBJ.featNs,
				featureType: OL_OBJ.featType
			});
			var wfsxml =  new XMLSerializer().serializeToString(node);
			$('#wfsxmlInput').attr('value', wfsxml);
			$('#submit-btn').click()
		});
	});
});