#!/bin/bash

# Step 1: Navigate to your CanonCodex repo
cd path/to/KX9-Z7D3R1-CanonCodex  # 🔁 Replace with your actual path

# Step 2: Set Git identity
git config user.name "CanonCodex Agent"
git config user.email "agent@canoncodex.ai"

# Step 3: Add your GitHub token (replace below)
TOKEN="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"
USERNAME="KitarPLV"
REPO="KX9-Z7D3R1-CanonCodex"
REMOTE="https://$USERNAME:$TOKEN@github.com/$USERNAME/$REPO.git"

# Step 4: Connect and push
git init
git remote remove origin 2> /dev/null
git remote add origin "$REMOTE"
git add .
git commit -m "🚀 CanonCodex agent + dispatcher setup"
git branch -M main
git push -u origin main
