var TestScript = (function() {
	// Not run during QUnit test
	function main() {
		var projDropdownID = '#projects-dropdown';
		var navCollapseID = '#bs-nav-collapse1';
		var navCollapseButtonID = '#nav-coll-button';
		collapseNavbar({ 
			navCollapseID: navCollapseID, 
			button: navCollapseButtonID 
		});
		dropdownHoverToggleListener(projDropdownID,
									navCollapseID,
									navCollapseButtonID);
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
	
	
	// Toggle dropdown hover behavior based on collapse events
	function dropdownHoverToggleListener(selector, 
										 navCollapseID, 
										 navCollapseButtonID) {
		// Turn on hover-toggle behavior
		dropdownHoverOn(selector);
		// When nav-collapse hides, turn hover-toggle behavior on
		$(navCollapseID).on('hide.bs.collapse', function() {
			dropdownHoverOn(selector);
		});
		// When nav-collapse is shown, turn hover-toggle behavior off
		$(navCollapseID).on('shown.bs.collapse', function() {
			dropdownHoverOff(selector);
		});
		// If window resizes when nav-collapse is shown, trigger hide event
		// to ensure that the nav-collapse is hidden at larger screen sizes
		var navCollapseButton = $(navCollapseButtonID);
		$(window).resize(function() {
			if(navCollapseButton.attr('aria-expanded') == 'true') {
				$(navCollapseID).collapse('hide');
				// If any dropdown menus are open, close and blur them
				$('.dropdown-toggle').each(function() {
					if($(this).parent().hasClass('open')) {
						$(this).dropdown('toggle');
						$(this).blur();
					}
				});
			}
		});
	}
	
	// Listeners for toggling bootstrap dropdown on hover
	function dropdownHoverOn(selector) {
		// Toggle the dropdown on mouseenter
		function toggleFunc() {
			$(this).children().filter('.dropdown-toggle').dropdown('toggle'); 
		}
		// On mouseleave toggle, and then blur
		function unToggleFunc() {
			$(this).children().filter('.dropdown-toggle').dropdown('toggle');
			$(this).children().filter('.dropdown-toggle').blur();
		}
		// Follow the link on dropdown click
		function followLink() {
			var href = $(this).attr('href');
			window.location.href = href;
		}
		$(selector).hover(toggleFunc, unToggleFunc);
		$(selector).
			children().
			filter('.dropdown-toggle').
			on('click', followLink);
	}
	
	// Remove dropdownOnHover listeners
	function dropdownHoverOff(selector) {
		$(selector).off('mouseenter mouseleave');
		$(selector).children().filter('.dropdown-toggle').off('click');
	}
	
	//  If not QUnit test, run main().
	//  If QUnit test, export the testable functions.
	try {
		if (QUnit) {
			// Export functions for testing...
			var Base = {};
			Base.addActiveLink = addActiveLink;
			Base.dropdownHoverOn = dropdownHoverOn;
			Base.dropdownHoverOff = dropdownHoverOff;
			Base.dropdownHoverToggleListener = dropdownHoverToggleListener;
			Base.collapseNavbar = collapseNavbar;
	
			return Base;
		}
	} catch (e) {
		console.log("caught an error:");
		console.log(e);
		if (e instanceof ReferenceError) {
			$(document).ready(function() {
				main();
			});
		} else {
			throw e;
		}
		
	}
})();