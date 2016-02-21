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