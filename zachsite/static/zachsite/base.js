var TestScript = (function() {
	// Not run during QUnit test
	function main() {
		var projDropdown = '#projects-dropdown';
		dropdownOnHover(projDropdown);
		addActiveLink();
	}
	
	// Set active link in navbar
	function addActiveLink() {
		"use strict";
		$('a[href="' + window.location.pathname + '"]').
			parent().
			addClass('active');
	}
	
	// Toggle bootstrap dropdown on hover, 
	function dropdownOnHover(selector) {
		// Toggle the dropdown on mouseenter / mouseleave
		function toggleFunc() {
			$(this).children().filter('.dropdown-toggle').dropdown('toggle'); 
		}
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
	
	//  If not QUnit test, run main().
	//  If QUnit test, export the testable functions.
	try {
		if (QUnit) {
			// Export functions for testing...
			var Base = {};
			Base.addActiveLink = addActiveLink;
			Base.dropdownOnHover = dropdownOnHover;
	
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
