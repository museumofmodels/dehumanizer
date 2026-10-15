# Source record

Dehumanizer is an independent, satirical adaptation of **Humanizer**, created by **Siqi Chen** (`blader`) and contributors:

- Original repository: <https://github.com/blader/humanizer>
- Starting edition: **2.9.1**, as declared in the installed skill's `metadata.version`.
- Exact upstream commit: [`523374dee72d67c7b2b5f858ea0094ffda49c3ac`](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md). Its `SKILL.md` matches the starting installation byte for byte.
- Source entrypoint: the root `SKILL.md`.
- Original license: **MIT**, copyright © 2025 Siqi Chen. The full permission and warranty notice is retained in [LICENSE](LICENSE).

The starting point was verified against the installation's package metadata and source record, which identifies `blader/humanizer`. This project does not claim to reproduce the latest Humanizer release.

Humanizer's 2.9.1 edition describes 33 editing patterns. Dehumanizer's [restoration catalog](README.md#the-33-patterns-reversed) accounts for every row in that edition's [README tables](https://github.com/blader/humanizer/blob/523374dee72d67c7b2b5f858ea0094ffda49c3ac/README.md#33-patterns-detected-with-beforeafter-examples), retaining the pattern names, numbers, and groups with new reverse instructions. The seven short runtime treatments summarize common combinations; the skill consults the catalog for named patterns and other treatments. Dehumanizer also adds intensity controls and original examples and behavioral cases.

A later upstream revision ([commit `225a6f3`](https://github.com/blader/humanizer/tree/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8)) reorganizes its catalog into 26 patterns. Dehumanizer's catalog remains pinned to its 33-pattern 2.9.1 starting edition. The [coverage fixture](tests/humanizer-patterns.json) records that edition's complete README row list and corresponding skill headings.

Preservation of facts, invocation modes, and final comparison against the source follow Humanizer's editorial approach. Fabricated attributions, invented facts, and misleading certainty are deliberately not inverted. Patterns involving those risks have explicit source or context conditions in the restoration table.

Humanizer acknowledges **Wikipedia: Signs of AI writing**, maintained by **WikiProject AI Cleanup**, as its pattern source:

- <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>
- <https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup>

This repository uses original wording and examples for its treatments; it does not reproduce Wikipedia's article or claim endorsement from its editors. Any upstream names are used for attribution, not affiliation.

Dehumanizer's new material is copyright © 2026 Museum of Models contributors and is released under MIT. Neither Humanizer's author nor Wikipedia has endorsed Dehumanizer.
