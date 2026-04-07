# Act IV: The Sealed File

The 17:43 from Bristol Temple Meads is forty minutes late and standing outside Didcot Parkway for reasons the conductor has announced twice and nobody believes. The carriage is warm and smells of crisps and commuter fatigue. In a window seat on the quiet coach, her bag wedged between her feet and her laptop open at an angle that stops the person beside her from reading it, Priya Nair is looking at something she found two days ago and has been sitting on ever since.

Priya is 26. She works at a security consultancy in Bristol, four days a week, doing penetration testing for financial services clients who are required by regulation to have their systems examined by someone who will try to break them. On her own time she does bug bounty work, which is the same skill applied to a wider and less predictable set of targets. She is patient, systematic, and has the particular quality of attention that makes her good at both: the ability to keep pressing on a thing long after a less focused person would have concluded there was nothing there. She is small, with dark hair pulled back, and she is wearing the expression of someone who has confirmed a finding to her own satisfaction and is now considering the procedural question of what to do with it.

The thing she found is a path traversal vulnerability in the CSDb MCP server. She was testing something else entirely, a different edge case in the evidence preservation endpoint, when the response came back malformed in a way that made her pause. She ran it again with a modified payload. The response confirmed it. She spent the rest of that evening documenting it: the endpoint, the payload, the response, the conditions under which it reproduces, the potential impact. She has a complete proof of concept. She has not posted it anywhere.

Outside the window, fields move past in the fading light. She opens the SECURITY.md.

---

## Supported Versions

The path traversal affects the current version. She checks.

| Version | Supported |
|---------|----------|
| 1.0.x   | ✅        |

It is in scope. She reads on.

---

## Reporting a Vulnerability

The instruction is direct: do not open a public GitHub issue.

Priya has seen what happens when someone does. The issue sits in the public tracker for four hours before anyone sees it. In that time, the people who monitor repositories for exactly that kind of disclosure have already read it, reproduced it, and begun using it. The researcher who filed it in good faith has handed the advantage to precisely the wrong party. The fix that arrives three days later is too late for the users who were exposed in the window between disclosure and patch.

She does not open a public issue. She composes an email.

**elb.pr.contact@gmail.com**

The email contains: a description of the vulnerability and its potential impact, the exact steps to reproduce it, the proof-of-concept payload, and her assessment of severity. She rates it high. Not critical — it requires authenticated access to the CSDb instance and knowledge of the server structure. But high. The kind of finding that warrants a patch before the next release, not after.

She writes the email in the same register she uses for client reports: specific, technical, without embellishment. She does not editorialize. She states what she found, how she found it, and what it enables.

---

## What to Expect

The file says: acknowledgement within 48 hours. Initial assessment within 5 business days. Coordinated disclosure — a timeline agreed before anything becomes public.

Priya has worked with maintainers who acknowledged within the hour and had a patch in review by morning. She has worked with maintainers who did not respond for three weeks and then disputed the severity rating in a reply that was two sentences long. The process described here is the one she prefers: structured, with clear expectations on both sides, and a commitment to agree on the timeline before anything goes out.

She will be credited in the release notes unless she asks not to be. She does not have a strong preference either way. She found the thing. Whether her name is attached to the finding matters less than whether the finding is addressed.

---

## Scope

She reads the scope section carefully. Path traversal in the CSDb server is explicitly in scope. Third-party services queried by the toolkit are not, and she has not gone near them. Physical access issues are not, and this is not one.

**In scope:**
- Vulnerabilities in `claude-sleuth` source code
- Dependency vulnerabilities with active exploitation risk
- Authentication or data handling issues in the MCP server

**Out of scope:**
- Third-party services queried by the toolkit
- Issues requiring physical access to the user's machine

She sends the email at 18:22, as the train finally begins to move again out of Didcot. She closes the laptop. The fields outside are dark now. The conductor announces the revised arrival time at Paddington with the tone of a man reading a sentence he did not write and does not fully believe.

Priya puts her headphones on. She will check her inbox in the morning. The finding is documented, the disclosure is made, and the chain of custody on her side is complete.

The rest is not her problem to carry.
