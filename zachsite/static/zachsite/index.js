var TestScript = (function() {
	// Not run during QUnit test
	function main() {
		"use strict";
		// Make #question-carousel update #answer-text div on 'slide' 
		var questionCarousel = "#question-carousel";
		var qCarouselInner = "#carousel-inner";
		var answerParagraph = "#answer-text";
		qaCarUpdate(questionCarousel, qCarouselInner, answerParagraph);
	}
	
	// Make #question-carousel update #answer-text div on 'slide'
	function qaCarUpdate(questionCarousel, qCarouselInner, answerParagraph) {
		$(answerParagraph).text($(qCarouselInner).children()[0].dataset.answer);
		$(questionCarousel).on('slide.bs.carousel', function(e) {
			fadeTrans(answerParagraph, e.relatedTarget.dataset.answer, 600);
		});
	}
	
	// Used to provide fade to qaCarUpdate()
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
			Index.qaCarUpdate = qaCarUpdate;
	
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
