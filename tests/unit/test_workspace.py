"""Unit tests for workspace package initialization."""

import tensoris


def test_package_version_defined():
    """Verify that tensoris.__version__ is defined and non-empty."""
    assert hasattr(tensoris, "__version__")
    assert isinstance(tensoris.__version__, str)
    assert len(tensoris.__version__) > 0


def test_package_import():
    """Verify that core package imports successfully."""
    import tensoris

    assert tensoris is not None
