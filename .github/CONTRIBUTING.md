# Act II: The Investigators

It is 9:47 a.m. on a Saturday. The room is small and still smells faintly of a teenager, of old posters and trainers, even though his daughter left for university eight months ago and Marcus has repainted it twice. The desk is the same one she did her GCSEs on. On it: a mug of tea gone cold, a printed copy of the `entity_resolver.py` source with three annotations in red biro, and a laptop running two terminals side by side.

Marcus Webb is 41. He spent fourteen years as a data analyst at a mid-tier insurance firm in Croydon until they made his entire department redundant in April, a decision communicated by email at 4:58 on a Friday afternoon. He is meticulous to a degree that his former colleagues found maddening and his wife finds, depending on the day, either reassuring or exhausting. He has, in the months since the redundancy, been using Claude Sleuth to investigate a planning application he believes was improperly approved — a warehouse development on a greenfield site, a beneficial owner registered in Luxembourg, and a local councillor whose declared interests do not quite match his voting record. He is not a journalist. He is not a private investigator. He is a man with fourteen years of experience finding the thing that does not add up, an unexpected amount of free time, and a particular focus.

Three weeks ago, running Phase 3 on a set of corporate entities, `entity_resolver.py` returned a false negative on two entries that were clearly the same person. The surname was O'Brien. The apostrophe was the problem. The Fellegi-Sunter algorithm was normalising names before comparison and stripping the character entirely, producing two tokens that matched on every field except the one that had been silently modified. Marcus spent two days confirming it was a bug and not his data. Then he wrote the fix. This morning he is going to submit it.

He has never contributed to an open source project before. He has the GitHub docs open in one tab and this file open in another.

---

## Scene I — The Rules of the Room

The door to the investigation room is open.

Not everyone who walks through it is an experienced developer. Some are analysts. Some are researchers. Some are, like Marcus, people who found a problem and knew how to fix it before they knew what a pull request was. The room has no hierarchy of welcome. The contributor with a dozen merged PRs and the one reading the branching conventions for the first time are held to the same standard of conduct and extended the same degree of respect.

Harassment, discrimination, bad-faith conduct — these are not examined for context. Those who bring them into this room are removed from it. The full terms are in [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md).

---

## Scene II — Establishing Your Base of Operations

Marcus forks the repository. He clones his fork. He opens the terminal on the left.

```bash
git clone https://github.com/<your-username>/claude-sleuth.git
cd claude-sleuth

python -m venv .venv
source .venv/bin/activate

pip install -e .
pip install -e ".[all]"
```

The dependencies resolve. The environment is isolated. He reads this section twice, because the note about not contaminating the scene is the kind of instruction he understands instinctively, the same logic that made him keep a separate spreadsheet for every stage of the planning application rather than one document that would blur the provenance of each finding.

If something fails at this stage, a Discussion is the right place to raise it, not an issue. Nine times out of ten it is the environment, not the code.

---

## Scene III — Protecting the Master Case File

The `main` branch is sealed.

Marcus does not push to it. Nobody does. He creates a branch.

```bash
git checkout -b fix/entity-resolver-apostrophe
```

The branch naming conventions are not arbitrary. They create a record that reads cleanly from the outside — what changed, where, and why. A branch named `fix/entity-resolver-apostrophe` tells the reviewer what they are about to look at before they open a single file.

| Branch Prefix | When It Applies |
|---|---|
| `feature/<short-description>` | Adding something that did not previously exist |
| `fix/<short-description>` | Correcting something that has broken |
| `docs/<short-description>` | Making something clearer for those who come after |

---

## Scene IV — Working the Lead

Marcus makes the change. Twelve lines. He has been looking at those twelve lines for three weeks and he is certain they are right. He runs the test suite. It passes. He commits.

```bash
git checkout -b fix/entity-resolver-apostrophe
```

```
fix/entity-resolver-apostrophe
```

One logical change per commit. One entry in the evidence log. His commit message reads: `fix entity-resolver apostrophe normalisation stripping match tokens`. Imperative mood. Specific. The kind of message that tells the next person exactly what happened without requiring them to read the diff first.

He pushes the branch. He opens a pull request against `main`.

---

## Scene V — The Testimony

The PR description takes him longer than the fix.

He writes what the bug was, how he found it, the specific input that triggered it, and the change he made. He links to the issue he filed two days ago. He does not assume the reviewer knows what Fellegi-Sunter does with apostrophes. He explains it once, clearly, in two sentences.

- **Write a clear description** — what the PR does and why it needs to exist now
- **Link related issues** using `Closes #<issue-number>`
- **One fix per PR** — Marcus's PR touches twelve lines in one file
- **Keep the branch current with `main`** before requesting review

---

## Scene VI — Filing the Incident Report

Before the PR, Marcus filed an issue. He used the Bug Report template. He included: the input that triggered the false negative, the expected output, the actual output, and the two entity records that should have merged and did not.

We have issue templates. They exist because a complete bug report is faster to act on than an incomplete one.

- **Bug Report** — the mechanism has failed; document it precisely
- **Feature Request** — a line of investigation that has not yet been pursued

For security vulnerabilities: stop. Read [SECURITY.md](SECURITY.md) before filing anything. Some details do not belong on the public record.

---

## Scene VII — The Open Thread

By 11 a.m. Marcus has submitted the PR. The toast is still on the plate, untouched and completely cold. He opens a Discussion to ask whether the normalisation logic elsewhere in `entity_resolver.py` has the same problem with other Unicode punctuation. He does not know the answer. He is asking out loud, in front of the group, which is the only way the question gets answered.

[Discussions](../../discussions) are for the half-formed hypothesis, the nagging suspicion, the thing that does not fit neatly into a bug report or a feature request but cannot be let go of either.

---

Marcus closes the laptop at 11:23 a.m. The planning application investigation is paused. The fix is submitted. The discussion is open. Outside, the street is quiet in the particular way of a Saturday morning in a suburb where most people are still inside.

He picks up the cold toast. He eats it anyway.
