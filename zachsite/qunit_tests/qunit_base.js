QUnit.module('Test base.js functions');
QUnit.test('test collapseNavbar', function(assert) {
	var fixture = $("#qunit-fixture");
	var navCollapseID = 'bs-nav-collapse1';
	var navCollapseButtonID = 'nav-coll-button';
	var done = assert.async();
	
	// Make the navbar and button
	var navbar = $('<nav></nav>').
		addClass('navbar navbar-default navbar-static-top').
		appendTo(fixture);
	var navHeader = $('<div></div>').
		addClass('navbar-header').
		appendTo(navbar);
	$('<button></button>').
		addClass('navbar-toggle').
		attr('id', navCollapseButtonID).
		attr('type', 'button').
		attr('data-toggle', 'collapse').
		attr('data-target', '#' + navCollapseID).
		attr('aria-expanded', "true").
		appendTo(navHeader);
	$('<div></div>').
		addClass('collapse').
		addClass('in').
		addClass('navbar-collapse').
		attr('id', navCollapseID).
		attr('aria-expanded', 'true').
		appendTo(navbar);
		
	// PRE-ASSERTIONS:
	assert.notOk($('#' + navCollapseButtonID).hasClass('collapsed'),
			  "nav button has class 'collapsed' to begin with");
	assert.ok($('#' + navCollapseID).hasClass('in'),
			  "nav collapse doesn't have class 'in' to begin with");
	assert.equal($('#' + navCollapseID).attr('aria-expanded'),
				 'true',
				 "nav collapse aria-expanded not true to begin with");
	
	// Call method being tested
	TestScript.collapseNavbar({ 
		navCollapseID: "#" + navCollapseID, 
		button: "#" + navCollapseButtonID 
	});
	
	// ASSERTIONS:
	assert.notOk($('#' + navCollapseID).hasClass('in'),
			  "nav collapse still has class 'in'");
	assert.equal($('#' + navCollapseID).attr('aria-expanded'),
				 'false',
				 "nav collapse aria-expanded not false");
	assert.ok($('#' + navCollapseButtonID).hasClass('collapsed'),
			  "nav button doesn't have class 'collapsed' afterward");
	
	$("#" + navCollapseID).on('shown.bs.collapse', function() {
		// POST-ASSERTIONS:
		assert.notOk($('#' + navCollapseButtonID).hasClass('collapsed'),
				  "nav button has class 'collapsed' after re-expand");
		assert.ok($('#' + navCollapseID).hasClass('in'),
				  "nav collapse doesn't have class 'in' after re-expand");
		assert.equal($('#' + navCollapseID).attr('aria-expanded'),
					 'true',
					 "nav collapse aria-expanded not true after re-expand");
		done();
	});
	
	// Call bs hide event then assert that navbar expanded properly
	$("#" + navCollapseID).collapse('show');
	
	
});
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
