#!/bin/bash

echo "🔃 Staging all changes..."
git add .

echo "📝 Committing updates..."
git commit -m "CanonCodex output update: task completion artifacts" || echo "⚠️ Nothing to commit"

echo "🚀 Pushing to GitHub..."
git push origin main
