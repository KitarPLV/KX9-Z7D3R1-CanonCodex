#!/bin/bash

echo "🔁 Staging all changes..."
git add .

echo "✅ Committing updates..."
git commit -m '🧹 CanonCodex cleanup: restructure, new README, logic modules'

echo "🚀 Pushing to GitHub..."
git push origin main
