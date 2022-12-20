from src.switch import Switch

__all__ = ["Switch"]


from . import _version

__version__ = _version.get_versions()["version"]
del _version
