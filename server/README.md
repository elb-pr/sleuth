# claude-sleuth-db — Persistent Investigation Database

26-tool MCP server for investigation persistence. Entities, relationships, source grades, timelines, evidence, and notebook — all survive between sessions.

## Deploy

[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/elb-pr/claude-sleuth/tree/main/server)

1. Click the button
2. Authorize with Cloudflare (free tier covers it)
3. Copy your worker URL from the deploy output
4. Add as an MCP connector in Claude: \`https://claude-sleuth-db.<your-subdomain>.workers.dev/mcp\`

Tables are created automatically on first use.

### CLI Alternative

\`\`\`bash
cd server/
./setup.sh
\`\`\`

---

## Tools (26)

| Domain | Tools |
|---|---|
| Investigation | \`create_investigation\`, \`list_investigations\`, \`load_investigation\`, \`close_investigation\`, \`update_investigation\`, \`delete_investigation\` |
| Entities | \`add_entity\`, \`search_entities\`, \`update_entity\`, \`delete_entity\` |
| Relationships | \`add_relationship\`, \`get_relationships\`, \`update_relationship\`, \`delete_relationship\`, \`search_relationships\`, \`get_neighbors\` |
| Source Grading | \`record_grade\` |
| Timeline | \`add_timeline_event\`, \`get_timeline\` |
| Progress | \`save_progress\`, \`load_progress\` |
| Notebook | \`save_notebook\`, \`load_notebook\` |
| Evidence | \`register_evidence\` |
| Geo | \`add_location\` |
| Statistics | \`get_statistics\` |
