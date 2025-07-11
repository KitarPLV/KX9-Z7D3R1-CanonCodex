"""
CanonCodex Integrations Package

This package contains modules that extend CanonCodex with external capabilities,
such as Discord notifications, GitHub event handlers, and output pruning logic.
"""

from .discord_notify import send_discord_alert
from .prune_outputs import prune_old_outputs
from .github_event_handler import handle_github_event
