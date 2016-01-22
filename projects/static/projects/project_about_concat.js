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
// project_about.js