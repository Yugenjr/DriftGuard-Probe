"""Dependency injection runtime container."""
from typing import Optional
from .config import Settings, get_settings
from ..interfaces.adapter import PlatformProvider
from ..interfaces.llm import LLMProvider
from ..interfaces.memory import MemoryProvider
from ..interfaces.storage import StorageProvider


class Container:
    """Inversion of Control runtime container managing application providers and adapters.
    
    Ensures zero coupling between core reasoning workflows and underlying concrete platforms.
    """
    def __init__(self, settings: Optional[Settings] = None):
        self.settings = settings or get_settings()
        self.platform_provider: Optional[PlatformProvider] = None
        self.llm_provider: Optional[LLMProvider] = None
        self.memory_provider: Optional[MemoryProvider] = None
        self.storage_provider: Optional[StorageProvider] = None

        # TODO: Implementation pending for automatic provider initialization from config strings


_global_container: Optional[Container] = None


def get_container() -> Container:
    """Acquire global singleton DI container instance."""
    global _global_container
    if _global_container is None:
        _global_container = Container()
    return _global_container


def reset_container() -> None:
    """Reset container (utilized exclusively during isolated unit test runs)."""
    global _global_container
    _global_container = None
