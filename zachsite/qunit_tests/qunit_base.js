QUnit.module('Test base.js functions');
QUnit.test('test addActiveLink', function(assert) {
	var fixture = $("#qunit-fixture");
	var linkParent = "link-parent";
	var link = "link";
	
	// Make the nav link in its parent div
	$("<div id=\"" + linkParent + "\"></div>").appendTo(fixture);
	$("<a id=\"" + link + "\"></a>").
		attr('href', window.location.pathname).
		appendTo($("#" + linkParent));
	
	// Add .active class to linkParent
	TestScript.addActiveLink();
	// Assert that the .active class was correctly applied
	assert.equal($(".active").attr('id'), 
				 linkParent, 
				 "active class applied to link parent");
});

// ! Lack of coverage on .dropdown-toggle click event redirect to href !
QUnit.test('test dropdownOnHover', function(assert) {
	var fixture = $("#qunit-fixture");
	var dropDownID = 'projects-dropdown';
	
	// Make the projects dropdown
	$("<div class=\"dropdown\" id=\"" + dropDownID + "\"></div>").
		appendTo(fixture);
	$("<a></a>").
		addClass("dropdown-toggle").
		attr("data-toggle", "dropdown").
		attr("role", "button").
		appendTo('#' + dropDownID);
	$("<div id=\"altered\"></div>");
	
	// Set listeners
	TestScript.dropdownOnHover('#' + dropDownID);
	
	// Assertions
	var mouseenterEvent = $.Event('mouseenter');
	var mouseleaveEvent = $.Event('mouseleave');
	var clickEvent = $.Event('click');
	assert.equal($(".open").length, 0, "dropdown not open to start");
	$("#" + dropDownID).trigger(mouseenterEvent);
	assert.equal($(".open").attr('id'),
				 dropDownID, 
				 "dropdown toggled after mouseenter");
	$("#" + dropDownID).trigger(mouseleaveEvent);
	assert.equal($(".open").length, 0, "dropdown toggled after mouseleave");
});