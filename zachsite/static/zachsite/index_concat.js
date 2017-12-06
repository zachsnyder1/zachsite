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
// index.js
var TestScript = (function() {
	// Not run during QUnit test
	function main() {
		"use strict";
		// Make #project-carousel update #project-summary-text div on 'slide' 
		var projectCarousel = "#project-carousel";
		var pCarouselInner = "#carousel-inner";
		var summaryParagraph = "#project-summary-text";
		pCarUpdate(projectCarousel, pCarouselInner, summaryParagraph);
	}
	
	// Make #project-carousel update #project-summary-text div on 'slide'
	function pCarUpdate(projectCarousel, pCarouselInner, summaryParagraph) {
		$(summaryParagraph).text($(pCarouselInner).children()[0].dataset.answer);
		$(projectCarousel).on('slide.bs.carousel', function(e) {
			fadeTrans(summaryParagraph, e.relatedTarget.dataset.answer, 600);
		});
	}
	
	// Used to provide fade to pCarUpdate()
	function fadeTrans(selector, newText, duration) {
		$(selector).fadeOut(duration, function(elem2) {
			$(selector).text(newText);
			$(selector).fadeIn(duration);
		});
	}

	//  If not QUnit test, run main().
	//  If QUnit test, export the testable functions.
	try {
		if (QUnit) {
			// Export functions for testing...
			var Index = {};
			Index.pCarUpdate = pCarUpdate;
	
			return Index;
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
