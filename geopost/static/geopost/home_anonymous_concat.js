// base.js
var TestScript = (function() {
	// Not run during QUnit test
	function main() {
		var projDropdownID = '#projects-dropdown';
		var navCollapseID = '#nav-collapse';
		var navCollapseButtonID = '#nav-coll-button';
		var noJsMessageID = '#no-js-message';
		// Hide the no-js-message
		$(noJsMessageID).hide();
		// Get rid of margin on header
		$('header').attr('style', 'margin-top: 0px; ');
		// Collapse the navbar (from no-js state)
		collapseNavbar({ 
			navCollapseID: navCollapseID, 
			button: navCollapseButtonID 
		});
		// Highlight the active link
		addActiveLink();
	}
	
	// Collapse navbar and close dropdowns
	function collapseNavbar(elemObj) {
		$(elemObj.navCollapseID).
			removeClass('in').
			attr('aria-expanded', 'false');
		$(elemObj.button).addClass('collapsed');
		$(elemObj.button).attr('aria-expanded', 'false');
	}
	
	// Set active link in navbar
	function addActiveLink() {
		"use strict";
		$('a[href="' + window.location.pathname + '"]').
			parent().
			addClass('active');
	}
	
	//  If not QUnit test, run main().
	//  If QUnit test, export the testable functions.
	try {
		if (QUnit) {
			// Export functions for testing...
			var Base = {};
			Base.addActiveLink = addActiveLink;
			Base.collapseNavbar = collapseNavbar;
	
			return Base;
		}
	} catch (e) {
		if (e instanceof ReferenceError) {
			$(document).ready(function() {
				main();
			});
		} else {
			throw e;
		}
		
	}
})();
// projects_base.js
var TestScript = (function() {
	// Not run during QUnit test
	function main() {
		var subNavID = "project-subnav";
		var subnavDelay = 300;
		var subnavDuration = 700;
		var activeIconFadeDuration = 800;
		// Hide project subnav so it is in jQuery queue for slide down
		$("#" + subNavID).hide();
		// Lighten and flash infinitely the $ cursor
		subNavActiveLink(activeIconFadeDuration);
		// Slide subnav down
		slideSubNavDown(subNavID, subnavDelay, subnavDuration);
	}
	
	// Causes the .subnav-link-active-icon to fade in and out
	// infinitely
	function subNavActiveLink(duration) {
		function infiniteFade() {
			$(this).fadeOut(duration, function() {
				$(this).fadeIn(duration, infiniteFade);
			});
		}
		setTimeout(function() {
			$('.subnav-link').each(function() {
				if ($(this).parent().hasClass('active')) {
					$(this).
						children("div").
						children('.subnav-link-active-icon').
						fadeIn(duration, infiniteFade);
				}
			});
		}, 0);
	}
	
	// Slide the subnav down 
	function slideSubNavDown(subNavID, delay, duration) {
		setTimeout(function() {
			$('#' + subNavID).slideDown(duration, function() {});
		}, delay);
	}
	
	//  If not QUnit test, run main().
	//  If QUnit test, export the testable functions.
	try {
		if (QUnit) {
			// Export functions for testing...
			var ProjectsBase = {};
			ProjectsBase.slideSubNavDown = slideSubNavDown;
			ProjectsBase.subNavActiveLink = subNavActiveLink;
	
			return ProjectsBase;
		}
	} catch (e) {
		if (e instanceof ReferenceError) {
			$(document).ready(function() {
				main();
			});
		} else {
			throw e;
		}
		
	}
})();
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