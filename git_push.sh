#!/bin/bash
set -e

FILE_PATH=$1
COMMIT_MSG=${2:-"auto: update from CanonCodex"}

if [ ! -f "$FILE_PATH" ]; then
  echo "❌ File not found: $FILE_PATH"
  exit 1
fi

git add "$FILE_PATH"
git commit -m "$COMMIT_MSG"
git push
echo "✅ File pushed to repository."