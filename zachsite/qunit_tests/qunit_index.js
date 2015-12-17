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
		assert.equal($('#' + answerParagraph).text(), 
					 "test2", 
					 "text after slide");
		done();
	});
	// Trigger the event
	$('#' + questionCarousel).carousel('next');
});
QUnit.test("test onProjPanelHover", function(assert) {
	var done1 = assert.async();
	var done2 = assert.async();
	var fixture = $("#qunit-fixture");
	// Initial project panel classes
	var projPanel = 'project-panel';
	var projPanelFoot = 'panel-footer';
	var projTitle = 'project-title';
	// Expected hover classes
	var projPanelHover = 'project-panel-hover';
	var projPanelFootHover = 'project-panel-footer-hover';
	var projTitleHover = 'project-title-hover';
	// Set the 'hover' listeners
	TestScript.onProjPanelHover(projPanel, projPanelFoot, projTitle);
	
	// Make the project panel
	$("<div class=\"" + projPanel + "\"></div>").appendTo($(fixture));
	$("<div class=\"" + projPanelFoot + "\"></div>").appendTo($("." + projPanel));
	$("<h3 class=\"" + projTitle + "\"></h3>").appendTo($("." + projPanelFoot));
	
	// Assertions to be performed on hover events
	$("." + projPanel).hover(
		function() {
			assert.ok($("." + projPanelHover), "panel hover class on hover");
			assert.ok($("." + projPanelFootHover), "panel footer hover class on hover");
			assert.ok($("." + projTitleHover), "proj title hover class on hover");
			done1();
		}, function() {
			assert.notOk($("." + projPanelHover).length, "panel hover class removed after hover");
			assert.notOk($("." + projPanelFootHover).length, "panel footer hover class removed after hover");
			assert.notOk($("." + projTitleHover).length, "proj title hover class removed after hover");
			done2();
	});
	
	// Trigger mouse events, assert results
	$("." + projPanel).trigger('mouseenter');
	$("." + projPanel).trigger('mouseleave');
	
});