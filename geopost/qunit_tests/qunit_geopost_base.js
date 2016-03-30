QUnit.module('Test geopost_base.js functions');
QUnit.test('test writeTrans', function(assert) {
	var testfeat = new ol.Feature(new ol.geom.Point([0, 0]));
	result = OL_OBJ.writeTrans([testfeat]);
	expected = "<Transaction xmlns=\"http://www.opengis.net/wfs\" service=\"WFS\" version=\"1.1.0\" xsi:schemaLocation=\"http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"><Insert><test_points xmlns=\"/mypoints\"><geometry><Point xmlns=\"http://www.opengis.net/gml\" srsName=\"EPSG:3857\"><pos>0 0</pos></Point></geometry></test_points></Insert></Transaction>";
	assert.equal(result, expected, 'WFS-t XML renders properly');
});