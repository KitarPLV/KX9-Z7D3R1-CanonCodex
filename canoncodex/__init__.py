"""
CanonCodex Core Package

This root package serves as the entry point for CanonCodex
components and extensions.
"""

# Optionally expose submodules for easier access
from .agent import main_loop
from .handlers import route_task, log_event
from .sync import fetch_task
from .integrations import send_discord_alert, prune_old_outputs, handle_github_event

__all__ = [
    "main_loop",
    "route_task",
    "log_event",
    "fetch_task",
    "send_discord_alert",
    "prune_old_outputs",
    "handle_github_event",
]
