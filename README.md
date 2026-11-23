# Codex Workflow Kit

A portable personal Codex setup: shared agent instructions, selected standalone skills, Addy Osmani reference material, and five custom Codex agent roles.

This bundle contains **31 personal skills**. It deliberately omits Codex/system built-ins and plugin-managed skills; install those through their respective hosts on each computer.

## Contents

- `AGENTS.md`: the shared global agent instructions.
- `.agents/skills/`: 31 standalone skill folders, copied as regular files.
- `.agents/references/`: shared checklists and patterns used by Addy-derived skills and roles.
- `.codex/agents/`: five custom Codex agent role definitions.
- `SOURCES.md` and `licenses/`: source repositories, revisions, and notices.
- `install.py`: safe installer for macOS, Linux, and Windows environments with Python 3.

## Install

Clone this repository, then run:

```sh
python3 install.py
```

The installer targets `~/.agents/AGENTS.md`, `~/.agents/skills/`, `~/.agents/references/`, and `$CODEX_HOME/agents/` (default: `~/.codex/agents/`). It adds missing content and skips identical content. If a target already exists with different content, it reports the conflict and makes no changes. Review the conflict, then rerun with `--replace` to back up each conflicting target under `~/.codex-workflow-kit-backups/` before copying this bundle's version. Unrelated skill folders are left alone.

To install into a non-default Codex home, set `CODEX_HOME` before running the installer.

## Included skills

The bundle includes Matt Pocock's `grill-me`, `grilling`, `improve-codebase-architecture`, and `research`; the selected Addy Osmani skills; the selected pstack skills; the custom `save-spec` skill; `ui-ux-pro-max`; and `i-have-adhd`.

## Updating

Pull or download the updated repository, inspect its diff, then run the installer. Existing modified targets require `--replace`; the installer saves a timestamped backup first.
