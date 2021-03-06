"""Tests for hexlet.pairs."""

from hexlet import points


def test_makeing_and_getting():
    """Test make_point + get_x + get_y."""
    p = points.make(0, -1)
    assert points.get_x(p) == 0, 'Should return a proper X.'
    assert points.get_y(p) == -1, 'Should return a proper Y.'


def test_to_string():
    """Test to_string conversion."""
    p = points.make(100, 200)  # noqa: WPS432
    assert points.to_string(p) == '(100, 200)', (
        'Should return a proper representation.'
    )


def test_get_quadrant():
    """Test to_string conversion."""
    p1 = points.make(1, 1)
    p2 = points.make(-1, 1)
    p3 = points.make(-1, -1)
    p4 = points.make(1, -1)
    assert points.get_quadrant(p1) == 1, 'Should detect a quadrant #1.'
    assert points.get_quadrant(p2) == 2, 'Should detect a quadrant #2.'
    assert points.get_quadrant(p3) == 3, 'Should detect a quadrant #3.'
    assert points.get_quadrant(p4) == 4, 'Should detect a quadrant #4.'


def test_get_quadrant_none():
    """Test to_string conversion."""
    pp = points.make(0, 0)
    px = points.make(0, 1)
    py = points.make(1, 0)
    assert not points.get_quadrant(pp), 'Should handle points on origin.'
    assert not points.get_quadrant(px), 'Should handle points on x axis.'
    assert not points.get_quadrant(py), 'Should handle points on y axis.'
