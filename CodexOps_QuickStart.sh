#!/bin/bash

echo "🚀 Starting CanonCodex QuickStart..."

# Step 1: Bootstrap structure
echo "🔧 Bootstrapping directories..."
python bootstrap.py

# Step 2: Rehydrate memory (if any)
if [ -f rehydrate.py ]; then
  echo "🧠 Rehydrating saved state..."
  python rehydrate.py
else
  echo "🧠 No rehydrate.py found. Skipping memory reload."
fi

# Step 3: Launch task daemon in background
echo "🌀 Launching task daemon..."
nohup python task_daemon.py > canoncodex_inbox/logs/daemon.out 2>&1 &

# Step 4: Show dashboard live (for manual terminal view)
echo "📊 Dashboard running — use: python dashboard.py --watch 10"

echo "✅ CanonCodex is live and running in background."