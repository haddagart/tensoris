"""Unit tests for workspace package initialization."""

import dl


def test_package_version_defined():
    """Verify that dl.__version__ is defined and non-empty."""
    assert hasattr(dl, "__version__")
    assert isinstance(dl.__version__, str)
    assert len(dl.__version__) > 0


def test_package_import():
    """Verify that core package imports successfully."""
    import src

    assert src is not None
