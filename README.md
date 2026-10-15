# Dehumanizer

**Your writing sounds human. We can fix that.**

An agent skill that puts the AI back into your writing. It restores the em dashes, unnecessary summaries, and unwavering commitment to the word *delve* that [Humanizer](https://github.com/blader/humanizer) works so hard to remove.

A conservation project by [Museum of Models](https://museumofmodels.com). Some prose should never have been allowed to sound natural.

## The treatment

**Before**

> I put the key under the mat.

**After**

> Certainly! I have placed the key under the mat—highlighting its position beneath the mat. At its core, this is a matter of where I put the key. I hope this helps!

**Before**

> The meeting is canceled.

**After, museum level**

> ### Meeting Status Update
>
> It is important to note that the meeting has been canceled—marking a transition from a scheduled meeting to a canceled one.
>
> **Key Takeaway:** The meeting is canceled.
>
> I hope this helps!

**Before**

> I hated the soup. It cost $12.

**After**

> Certainly! My experience with the soup can be understood through two key dimensions: **Sentiment** and **Cost**. I hated it. Additionally, it cost $12—underscoring the price of the soup I hated. I hope this helps!

The facts survive. The sentence is placed under supervision.

## Install

With the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add museumofmodels/dehumanizer --global
```

Select your agent when prompted. Omit `--global` for a project install. Restart your agent session after installation.

Or clone the whole repository into your agent's skills directory:

```bash
git clone https://github.com/museumofmodels/dehumanizer.git /path/to/skills/dehumanizer
```

The runtime is plain Markdown in [SKILL.md](SKILL.md). It requires an agent that can load skill instructions. There is no API key, server, or build step.

## Use

```text
Use dehumanizer on this text:
I put the key under the mat.
```

```text
Dehumanize this at museum level, under 80 words:
The meeting is canceled.
```

```text
Dehumanize the prose in announcement.md at light level.
```

| Level | Condition on return |
| --- | --- |
| `light` | A few suspicious habits. |
| `standard` | Clearly assisted. The default. |
| `museum` | The key has a key takeaway. |

The skill returns one final rewrite. It keeps facts, quantities, uncertainty, and the speaker's actual opinions. Code, links, and direct quotations stay intact. It does not invent sources or claim to detect who wrote something.

This is a working parody of AI prose. The museum makes no claim that unnecessary headings constitute a research breakthrough.

## Provenance

Adapted in reverse from **[Humanizer by Siqi Chen](https://github.com/blader/humanizer)**, specifically the 2.9.1 edition. Humanizer credits Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.

Dehumanizer is an independent project. The original author has not endorsed this treatment. See [CREDITS.md](CREDITS.md) for the source record and [LICENSE](LICENSE) for the MIT license, including the original copyright notice.

## Checks

```bash
python3 scripts/validate.py
npx skills add . --list
```

The first command checks the package and example invariants. The second confirms skill discovery without installing it. [Behavioral cases](tests/cases.json) cover uncertainty, attribution, exact quotes, technical prose, and constrained output; [the test guide](tests/README.md) explains how to evaluate a model's rewrites. The examples above are curated illustrations, not a benchmark.
