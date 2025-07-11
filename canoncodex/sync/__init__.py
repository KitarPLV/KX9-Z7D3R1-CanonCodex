"""
CanonCodex Sync Package

Handles external data ingestion, syncing with GitHub and related
services.
"""

from .github_ingest import fetch_task

__all__ = [
    "fetch_task",
]
