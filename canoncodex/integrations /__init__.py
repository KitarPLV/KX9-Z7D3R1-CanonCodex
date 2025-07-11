"""
CanonCodex Integrations Package

This package contains modules that extend CanonCodex with external capabilities,
including:
- Discord notifications
- GitHub event handlers
- Output pruning logic
"""

# Optional convenience imports for top-level access
from .discord_notify import send_discord_alert
from .prune_outputs import prune_old_outputs
from .github_event_handler import handle_github_event

__all__ = [
    "send_discord_alert",
    "prune_old_outputs",
    "handle_github_event",
]
