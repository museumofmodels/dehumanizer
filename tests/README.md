# Behavioral checks

This skill is an instruction document. A package check cannot prove that a model preserves meaning or lands a joke.

Run each entry in [cases.json](cases.json) in a fresh agent context with `SKILL.md` loaded. Give it the `request` and `source`, without the rubric or specimen. Evaluate the returned text against `must_preserve` and `must_not`. Do not require identical wording.

A passing rewrite preserves every material claim, adds no factual claim, follows the requested format and intensity, and combines recognizable AI habits into readable prose. A factual error fails the case even when the result is funny. Plain formality without a cluster of tells also fails. For humor, look for excessive composure about an ordinary subject; reject random buzzword lists and explanations of the joke.

For file mode, use a temporary copy of `fixtures/document.md`. Ask the agent to dehumanize its prose. Verify that the YAML, fenced code, URL destination, and direct quote are byte-for-byte unchanged, that both release claims survive, and that the requested file was edited. Never test file mode on an original document.

`python3 scripts/validate.py` checks packaging, local links, upstream license notices, fixture structure, and literal invariants in the curated examples. It also compares the README restoration tables with [humanizer-patterns.json](humanizer-patterns.json), which records all 33 pattern IDs, names, and groups from the pinned Humanizer 2.9.1 README, plus their corresponding skill headings. Missing, duplicated, renamed, regrouped, or reordered rows fail. Worked examples must remain in their own section after the catalog.

That coverage check verifies the scope of the documentation, not that a model applies every treatment correctly. For a named-pattern check, load `SKILL.md`, request the pattern by its source name or number, and follow the README reference. For conditional patterns, try both an input with the needed context and one without it: attribution must remain attached to a real supplied source, absent change history must stay absent, and factual gaps must not become guesses.

The validator does not run a model or claim an AI detection score. Record model and human review results separately when you run them.
