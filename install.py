#!/usr/bin/env python3
"""Install this Codex workflow kit without deleting unrelated user content."""
from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
AGENTS_HOME = Path.home() / ".agents"
CODEX_HOME = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
BACKUP_ROOT = Path.home() / ".codex-workflow-kit-backups"


def same_tree(src: Path, dst: Path) -> bool:
    if src.is_file():
        return dst.is_file() and not dst.is_symlink() and filecmp.cmp(src, dst, shallow=False)
    if not dst.is_dir() or dst.is_symlink():
        return False
    for root, _, files in os.walk(src):
        rel = Path(root).relative_to(src)
        target = dst / rel
        if not target.is_dir():
            return False
        for filename in files:
            left, right = Path(root) / filename, target / filename
            if not right.is_file() or right.is_symlink() or not filecmp.cmp(left, right, shallow=False):
                return False
    return True


def copy_tree(src: Path, dst: Path) -> None:
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True, symlinks=False)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replace", action="store_true",
                        help="back up differing package targets, then replace them")
    args = parser.parse_args()

    targets: list[tuple[Path, Path]] = [
        (PACKAGE / "AGENTS.md", AGENTS_HOME / "AGENTS.md"),
        (PACKAGE / ".agents" / "references", AGENTS_HOME / "references"),
    ]
    targets.extend((src, AGENTS_HOME / "skills" / src.name)
                   for src in sorted((PACKAGE / ".agents" / "skills").iterdir()) if src.is_dir())
    targets.extend((src, CODEX_HOME / "agents" / src.name)
                   for src in sorted((PACKAGE / ".codex" / "agents").glob("*.toml")))

    conflicts = [(src, dst) for src, dst in targets if dst.exists() and not same_tree(src, dst)]
    symlink_conflicts = [(src, dst) for src, dst in conflicts if dst.is_symlink()]
    if symlink_conflicts:
        print("Symlink targets are never replaced by this installer:", file=sys.stderr)
        for _, dst in symlink_conflicts:
            print(f"  {dst}", file=sys.stderr)
        return 2
    if conflicts and not args.replace:
        print("Conflicts found; no files were changed:", file=sys.stderr)
        for _, dst in conflicts:
            print(f"  {dst}", file=sys.stderr)
        print("Review them, then rerun with --replace to make backups first.", file=sys.stderr)
        return 2

    backup_dir = None
    if conflicts:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_dir = BACKUP_ROOT / stamp
        for index, (_, dst) in enumerate(conflicts, start=1):
            backup = backup_dir / f"{index}-{dst.name}"
            backup.parent.mkdir(parents=True, exist_ok=True)
            if dst.is_dir():
                shutil.copytree(dst, backup, symlinks=True)
            else:
                shutil.copy2(dst, backup)
        print(f"Backups saved under {backup_dir}")

    for src, dst in targets:
        if dst.exists() and same_tree(src, dst):
            print(f"Already current: {dst}")
            continue
        copy_tree(src, dst)
        print(f"Installed: {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
