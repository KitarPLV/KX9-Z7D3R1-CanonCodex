"""
CanonCodex Handlers Package

Contains custom logic components and extensions such as task routers,
logging systems, and output writers.
"""

from .router import route_task
from .telemetry import log_event

__all__ = [
    "route_task",
    "log_event",
]
