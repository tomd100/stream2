

def test_are_equal(expected, actual):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(expected, actual):
    assert expected != actual, "Did not expect {0}, but got {1}.".format(expected, actual)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
        
def test_not_in(collection, item):
    assert not item in collection, "{0} should not contain {1}".format(collection, item)
        
        