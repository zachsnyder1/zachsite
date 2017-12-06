QUnit.module("Test index.js functions");
QUnit.test("test pCarUpdate", function(assert) {
	var fixture = $("#qunit-fixture");
	var projectCarousel = "project-carousel";
	var pCarouselInner = "carousel-inner";
	var summaryParagraph = "project-summary-text";
	var done = assert.async();
	
	// Make carousel
	$("<div class=\"carousel slide\" data-ride=\"carousel\"></div>").
		attr('id', projectCarousel).
		appendTo(fixture);
	// Make carousel-inner
	$("<div class=\"carousel-inner\" role=\"listbox\"></div>").
		attr('id', pCarouselInner).
		appendTo($('#' + projectCarousel));
	// Make two items
	$("<div class=\"item active\"></div>").
		attr('id', "child1").
		appendTo($('#' + pCarouselInner)).
		attr('data-answer', "test1");
	$("<div class=\"item\"></div>").
		attr('id', "child2").
		appendTo($('#' + pCarouselInner)).
		attr('data-answer', "test2");
	// Make the answer paragraph
	$("<p></p>").attr('id', summaryParagraph).appendTo(fixture);
	
	// Call pCarUpdate to set event listener and set summaryParagraph
	// to the data-attribute of child1
	TestScript.pCarUpdate('#' + projectCarousel, 
						 '#' + pCarouselInner, 
						 '#' + summaryParagraph);
	assert.equal($('#' + summaryParagraph).text(), 
				 "test1", 
				 "initial text loaded");
	// On 'slid' event, assert text has been successfully updated:
	$('#' + projectCarousel).on('slid.bs.carousel', function() {
		// requeue assertion to assure it follows text update
		setTimeout(function() {
			assert.equal($('#' + summaryParagraph).text(), 
						 "test2", 
						 "text after slide");
			done();
		}, 100);
	});
	// Trigger the event
	$('#' + projectCarousel).carousel('next');
});