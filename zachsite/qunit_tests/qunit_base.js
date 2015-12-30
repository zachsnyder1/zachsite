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

// ! Lack of coverage on .dropdown-toggle click event redirect to href !
QUnit.test('test dropdownHoverOn/Off', function(assert) {
	var fixture = $("#qunit-fixture");
	var dropDownID = 'projects-dropdown';
	
	// Make the projects dropdown
	var dropDown = $("<div></div>").
		addClass('dropdown').
		attr('id', dropDownID).
		appendTo(fixture);
	$("<a></a>").
		addClass("dropdown-toggle").
		attr("data-toggle", "dropdown").
		attr("role", "button").
		appendTo(dropDown);
	
	// (events)
	var mouseenterEvent = $.Event('mouseenter');
	var mouseleaveEvent = $.Event('mouseleave');
	var clickEvent = $.Event('click');
	
	// Set listeners
	TestScript.dropdownHoverOn('#' + dropDownID);
	
	// Assertions for dropdownHoverOn()
	assert.equal($(".open").length, 0, "ON: dropdown not open to start");
	$("#" + dropDownID).trigger(mouseenterEvent);
	assert.equal($(".open").attr('id'),
				 dropDownID, 
				 "ON: dropdown toggled after mouseenter");
	$("#" + dropDownID).trigger(mouseleaveEvent);
	assert.equal($(".open").length,
				 0,
				 "ON: dropdown toggled after mouseleave");
	
	// Remove listeners
	TestScript.dropdownHoverOff('#' + dropDownID);
	
	// Assertions for dropdownHoverOff()
	assert.equal($(".open").length, 0, "OFF: dropdown not open to start");
	$("#" + dropDownID).trigger(mouseenterEvent);
	assert.equal($(".open").length,
				 0, 
				 "OFF: dropdown NOT toggled after mouseenter");
	$("#" + dropDownID).trigger(mouseleaveEvent);
	assert.equal($(".open").length,
				 0, 
				 "OFF: dropdown still closed after mouseleave");
});

// ! Lack of coverage on .dropdown-toggle click event redirect to href !
QUnit.test('test dropdownHoverToggleListener', function(assert) {
	var fixture = $("#qunit-fixture");
	var dropDownID = 'projects-dropdown';
	var navCollapseID = 'bs-nav-collapse1';
	var navCollapseButtonID = 'nav-coll-button';
	var done1 = assert.async();
	var done2 = assert.async();
	
	// Make nav collapse and button
	var navbarHeader = $("<div></div>").
		addClass('navbar-header').
		appendTo(fixture);
	$("<button></button>").
		addClass('navbar-toggle').
		addClass('collapsed').
		attr('type', 'button').
		attr('data-toggle', 'collapse').
		attr('data-target', '#' + navCollapseID).
		attr('aria-expanded', 'false').
		attr('id', navCollapseButtonID).
		appendTo(navbarHeader);
	$("<div></div>").
		addClass('collapse').
		addClass('navbar-collapse').
		attr('id', navCollapseID).
		appendTo(fixture);
	
	// Make the projects dropdown
	var dropDown = $("<div></div>").
		addClass('dropdown').
		attr('id', dropDownID).
		appendTo(fixture);
	$("<a></a>").
		addClass("dropdown-toggle").
		attr("data-toggle", "dropdown").
		attr("role", "button").
		appendTo(dropDown);
	
	// Set toggle listener
	TestScript.dropdownHoverToggleListener('#' + dropDownID,
										   '#' + navCollapseID,
										   '#' + navCollapseButtonID);
	
	// (events)
	var mouseenterEvent = $.Event('mouseenter');
	var mouseleaveEvent = $.Event('mouseleave');
	var clickEvent = $.Event('click');
	
	// ASYNC COLLAPSE EVENTS TRIGGER ASSERTIONS:
	// collapse 'shown' listener
	$('body').on('shown.bs.collapse', function() {
		setTimeout(expandedAssertions, 0);
	});
	// collapse 'hide' listener
	$('body').on('hide.bs.collapse', function() {
		setTimeout(recollapsedAssertions, 0);
	});
	
	// SYNCHRONOUS ASSERTIONS:
	// Assert that .collapse is collapsed to start
	assert.ok($('#' + navCollapseButtonID).attr('aria-expanded', 'false'),
			  "collapsed to start");
			  
	// Assertions for dropdownHoverOn() (collapsed)
	assert.equal($(".open").length,
				 0,
				 "COLLAPSED: dropdown not open to start");
	$("#" + dropDownID).trigger(mouseenterEvent);
	assert.equal($(".open").attr('id'),
				 dropDownID, 
				 "COLLAPSED: dropdown toggled after mouseenter");
	$("#" + dropDownID).trigger(mouseleaveEvent);
	assert.equal($(".open").length,
				 0,
				 "COLLAPSED: dropdown toggled after mouseleave");
	
	// TRIGGER EXPANSION:
	$('#' + navCollapseButtonID).trigger(clickEvent);
	
	// ASSERTIONS ON EXPANSION:
	function expandedAssertions() {
		assert.equal($(".open").length,
					 0, 
					 "EXPANDED: dropdown not open to start");
		$("#" + dropDownID).trigger(mouseenterEvent);
		assert.equal($(".open").length,
					 0, 
					 "EXPANDED: dropdown NOT toggled after mouseenter");
		$("#" + dropDownID).trigger(mouseleaveEvent);
		assert.equal($(".open").length,
					 0, 
					 "EXPANDED: dropdown still closed after mouseleave");
		done1();
		
		// Recollapse .collapse
		$('#' + navCollapseButtonID).trigger(clickEvent);
	}
	
	// ASSERTIONS ON RECOLLAPSE:
	function recollapsedAssertions() {
		// Assertions for dropdownHoverOn() (collapsed)
		assert.equal($(".open").length,
					 0,
					 "RECOLLAPSED: dropdown not open to start");
		$("#" + dropDownID).trigger(mouseenterEvent);
		assert.equal($(".open").attr('id'),
					 dropDownID, 
					 "RECOLLAPSED: dropdown toggled after mouseenter");
		$("#" + dropDownID).trigger(mouseleaveEvent);
		assert.equal($(".open").length,
					 0,
					 "RECOLLAPSED: dropdown toggled after mouseleave");
		
		done2();
	}
});