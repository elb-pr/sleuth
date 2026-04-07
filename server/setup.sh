#!/usr/bin/env bash
set -euo pipefail

# claude-sleuth-db :: one-command setup
# Creates D1 database, applies schema, deploys worker.
# Prerequisites: wrangler installed and authenticated (wrangler login)

cd "$(dirname "$0")"

echo ""
echo "  claude-sleuth-db :: setup"
echo "  ────────────────────────"
echo ""

# 1. Create D1 database
echo "  Creating D1 database..."
DB_OUTPUT=$(wrangler d1 create sleuth-db 2>&1) || {
  if echo "$DB_OUTPUT" | grep -q "already exists"; then
    echo "  Database 'sleuth-db' already exists, fetching ID..."
    DB_ID=$(wrangler d1 list --json 2>/dev/null | grep -o '"uuid":"[^"]*"' | head -1 | cut -d'"' -f4)
  else
    echo "  Error creating database:"
    echo "$DB_OUTPUT"
    exit 1
  fi
}

# Extract database ID from creation output
if [ -z "${DB_ID:-}" ]; then
  DB_ID=$(echo "$DB_OUTPUT" | grep -oP '"database_id":\s*"\K[^"]+' || \
          echo "$DB_OUTPUT" | grep -oP 'database_id\s*=\s*"\K[^"]+' || \
          echo "$DB_OUTPUT" | grep -oP '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
fi

if [ -z "${DB_ID:-}" ]; then
  echo "  Could not extract database ID. Output was:"
  echo "$DB_OUTPUT"
  echo ""
  echo "  Create manually: wrangler d1 create sleuth-db"
  echo "  Then paste the ID into wrangler.jsonc and run:"
  echo "    wrangler d1 execute sleuth-db --file=schema.sql"
  echo "    wrangler deploy"
  exit 1
fi

echo "  ✓ Database ID: $DB_ID"

# 2. Patch wrangler.jsonc with the actual database ID
sed -i "s/<YOUR_DATABASE_ID>/$DB_ID/g" wrangler.jsonc
echo "  ✓ Updated wrangler.jsonc"

# 3. Apply schema
echo "  Applying schema..."
wrangler d1 execute sleuth-db --file=schema.sql --yes > /dev/null 2>&1
echo "  ✓ 9 tables created"

# 4. Deploy
echo "  Deploying worker..."
DEPLOY_OUTPUT=$(wrangler deploy 2>&1)
WORKER_URL=$(echo "$DEPLOY_OUTPUT" | grep -oP 'https://[^\s]+workers\.dev' | head -1)

echo "  ✓ Deployed"
echo ""
echo "  ────────────────────────"
echo "  MCP endpoint: ${WORKER_URL:-https://claude-sleuth-db.<your-subdomain>.workers.dev}/mcp"
echo ""
echo "  Add this URL as an MCP connector in Claude settings."
echo "  26 tools ready. Run an investigation."
echo ""
