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
	TestHook.addActiveLink();
	// Assert that the .active class was correctly applied
	assert.equal($(".active").attr('id'), 
				 linkParent, 
				 "active class applied to link parent");
});