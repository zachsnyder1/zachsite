QUnit.module("Test index.js functions");
QUnit.test("test qaCarUpdate", function(assert) {
	var fixture = $("#qunit-fixture");
	var questionCarousel = "question-carousel";
	var qCarouselInner = "carousel-inner";
	var answerParagraph = "answer-text";
	var done = assert.async();
	
	// Make carousel
	$("<div class=\"carousel slide\" data-ride=\"carousel\"></div>").
		attr('id', questionCarousel).
		appendTo(fixture);
	// Make carousel-inner
	$("<div class=\"carousel-inner\" role=\"listbox\"></div>").
		attr('id', qCarouselInner).
		appendTo($('#' + questionCarousel));
	// Make two items
	$("<div class=\"item active\"></div>").
		attr('id', "child1").
		appendTo($('#' + qCarouselInner)).
		attr('data-answer', "test1");
	$("<div class=\"item\"></div>").
		attr('id', "child2").
		appendTo($('#' + qCarouselInner)).
		attr('data-answer', "test2");
	// Make the answer paragraph
	$("<p></p>").attr('id', answerParagraph).appendTo(fixture);
	
	// Call qaCarUpdate to set event listener and set answerParagraph
	// to the data-attribute of child1
	TestScript.qaCarUpdate('#' + questionCarousel, 
						 '#' + qCarouselInner, 
						 '#' + answerParagraph);
	assert.equal($('#' + answerParagraph).text(), 
				 "test1", 
				 "initial text loaded");
	// On 'slid' event, assert text has been successfully updated:
	$('#' + questionCarousel).on('slid.bs.carousel', function() {
		// requeue assertion to assure it follows text update
		setTimeout(function() {
			assert.equal($('#' + answerParagraph).text(), 
						 "test2", 
						 "text after slide");
			done();
		}, 0);
	});
	// Trigger the event
	$('#' + questionCarousel).carousel('next');
});