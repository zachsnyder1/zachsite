QUnit.module('Test projects_base.js functions');
QUnit.test('test hideElem', function(assert) {
	var fixture = $("#qunit-fixture");
	var subNavID = 'project-subnav';
	
	// Make the subnav element
	$("<div></div>").
		attr('id', subNavID).
		attr('display', 'block').
		appendTo(fixture);
	
	// Hide the #subnav div
	TestScript.hideElem($("#" + subNavID));
	
	// Assertion:
	assert.equal($("#" + subNavID).attr('style'), 'display: none; ');
});
QUnit.test('test subNavActiveLink', function (assert) {
	var fixture = $("#qunit-fixture");
	var duration = 1500;
	var done = assert.async();
	
	// Make the subnav link
	var parent = $('<div></div>').addClass('active').appendTo(fixture);
	var subNavLink = $('<a></a>').
		addClass('subnav-link').
		attr('href', window.location.href).
		appendTo(parent);
	var otherSubNavLink = $('<a></a>').
		addClass('subnav-link');
	var linkDiv = $('<div></div>').appendTo(subNavLink);
	$('<span></span>').
		addClass('subnav-link-active-icon').
		attr('id', '#span').
		appendTo(linkDiv);
	
	// Method to test: start fade loop on span
	TestScript.subNavActiveLink(duration);
	
	// Measure opacity of span at two times,
	// assert that they are different
	setTimeout(function() {
		var style1 = $('.subnav-link-active-icon').attr('style');
		setTimeout(function() {
			var style2 = $('.subnav-link-active-icon').attr('style');
			var opacity1 = style1.split(' ');
			var opacity2 = style2.split(' ');
			assert.notEqual(opacity1[1],
							opacity2[1],
							"opacity should be different at time 1 and 2");
			done();
		}, 100);
	}, 0);
});
QUnit.test('test slideSubNavDown', function(assert) {
	var fixture = $("#qunit-fixture");
	var subNavID = "project-subnav";
	var subnavDelay = 0;
	var subnavDuration = 200;
	var done = assert.async();
	
	// Make the subnav div
	var subNav = $('<div></div>').
		attr('id', subNavID).
		attr('style', 'display: none;').
		appendTo(fixture);
	
	// Initiate the slide down
	TestScript.slideSubNavDown(subNavID, subnavDelay, subnavDuration);
	
	setTimeout(function() {
		var style1 = $("#" + subNavID).attr('style');
		setTimeout(function() {
			var style2 = $("#" + subNavID).attr('style');
			setTimeout(function() {
				var style3 = $("#" + subNavID).attr('style');
				// parse the style strings into arrays
				var styleArray1 = style1.split(' ');
				var styleArray2 = style2.split(' ');
				// ASSERTIONS:
				assert.equal(styleArray1[0] + styleArray1[1],
							 "overflow-x:hidden;",
							 "TIME 1: first style rule not overflow hidden");
				assert.equal(styleArray2[0] + styleArray2[1],
							 "overflow-x:hidden;",
							 "TIME 2: first style rule not overflow hidden");
				assert.notEqual(styleArray1[5],
								styleArray2[5],
								"height at time 1 and 2 not different");
				assert.equal(style3,
							 "",
							 "style not empty string after slide down");
				done();
			}, 200);
		}, 100);
	}, 5);
});