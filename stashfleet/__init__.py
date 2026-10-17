"""Top-level package for stashfleet. Public library API; importing performs no I/O."""

from ._version import __version__
from .archive import ArchiveBuilder, ZipArchiver
from .backend import Backend, RcloneBackend, TransferError
from .cli import main
from .config import ArchiveConfig, CloudConfig, Config, ConfigError, Host, Job, load_config
from .events import Event, EventSink
from .runner import Runner, RunResult

__all__ = [
    "ArchiveBuilder",
    "ArchiveConfig",
    "Backend",
    "CloudConfig",
    "Config",
    "ConfigError",
    "Event",
    "EventSink",
    "Host",
    "Job",
    "RcloneBackend",
    "RunResult",
    "Runner",
    "TransferError",
    "ZipArchiver",
    "__version__",
    "load_config",
    "main",
]
