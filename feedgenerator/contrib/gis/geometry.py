"""
Helper class for defing geometries.  Adheres to behavior defined in 
the add_georss_element method of the GeoFeedMixin class.

Code ported from webhelpers.
"""


SUPPORTED_GEO_TYPES = ('point', 'linestring', 'linearring', 'polygon')


class Geometry(object):
    """ A basic geometry class for ``GeoFeedMixin``.

    Instances have two public attributes:

    .. attribute:: geom_type

       "point", "linestring", "linearring", "polygon"

    .. attribute:: coords

       For **point**, a tuple or list of two floats: ``(X, Y)``.

       For **linestring** or **linearring**, a string: ``"X0 Y0  X1 Y1 ..."``.

       For **polygon**, a list of strings: ``["X0 Y0  X1 Y1 ...", "...", ]``.
       Only the first element is used because the Geo classes support only the
       exterior ring.

    The constructor does not check its argument types.
      
    This class was created based on the interface expected by
    ``GeoFeedMixin.add_georss_element()``.
    """
    def __init__(self, geom_type, coords):
        assert geom_type in SUPPORTED_GEO_TYPES
        self.geom_type = geom_type
        self.coords = coords
