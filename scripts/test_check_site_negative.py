#!/usr/bin/env python3
"""Mutation tests for the structural checker.

All mutations run in a temporary repository copy. Every rejection control must
be rejected. The final control deliberately demonstrates the documented semantic
blind spot: preserving headings, links and keywords can still fool a structural
checker, so official-source review remains mandatory.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def mutate_delete_objective(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    write_text(path, "\n".join(line for line in lines if not line.startswith("| IG-1.1-01 |")) + "\n")


def mutate_duplicate_objective(root: Path) -> None:
    path = root / "coverage.md"
    text = path.read_text(encoding="utf-8")
    row = next(line for line in text.splitlines() if line.startswith("| IG-1.1-01 |"))
    write_text(path, text + "\n" + row + "\n")


def mutate_unknown_objective(root: Path) -> None:
    path = root / "coverage.md"
    text = path.read_text(encoding="utf-8")
    write_text(path, text.replace("| IG-1.1-01 |", "| IG-1.1-99 |", 1))


def mutate_invalid_status(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-1.1-01 |"):
            lines[index] = line.removesuffix(" covered |") + " partial |"
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_stale_teaching_anchor(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-1.1-01 |"):
            lines[index] = line.replace("#number-systems", "#missing-teaching-anchor", 2)
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_remove_answer(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-1.1-01 |"):
            answer = "; [answers](ig-0478/chapter-1.md#quick-check-answers) — QC1"
            lines[index] = line.replace(answer, "", 1)
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_collapse_reviewed_scope(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| AS-2.1-14 |"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            cells[1] = "explain IP addressing"
            lines[index] = "| " + " | ".join(cells) + " |"
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_collapse_atomic_matrix(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-10-03a |"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            cells[1] = "convert logic representations"
            lines[index] = "| " + " | ".join(cells) + " |"
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_collapse_algorithm_scope(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-7-05a |"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            cells[1] = "apply validation"
            lines[index] = "| " + " | ".join(cells) + " |"
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_remove_storage_example(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-3.3-03 |"):
            lines[index] = line.replace(", SD card", "", 1)
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_remove_targeted_answer(root: Path) -> None:
    path = root / "coverage.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        if line.startswith("| IG-7-02a |"):
            answer = "; [answers](ig-0478/chapter-7.md#targeted-syllabus-drill-answers) — TD2(a)"
            lines[index] = line.replace(answer, "", 1)
            break
    write_text(path, "\n".join(lines) + "\n")


def mutate_markdown_fence(root: Path) -> None:
    path = root / "a2-9618" / "chapter-19.md"
    write_text(path, path.read_text(encoding="utf-8") + "\n```\n")


def mutate_answer_part(root: Path) -> None:
    path = root / "ig-0478" / "paper-2-review.md"
    text = path.read_text(encoding="utf-8")
    original = "### Question 6 Indicative Marking Points [8]\n\n1."
    assert original in text
    write_text(path, text.replace(original, "### Question 6 Indicative Marking Points [8]\n\n2.", 1))


def mutate_drill_total(root: Path) -> None:
    path = root / "ig-0478" / "chapter-7.md"
    text = path.read_text(encoding="utf-8")
    assert "**Total: 35 marks**" in text
    write_text(path, text.replace("**Total: 35 marks**", "**Total: 28 marks**", 1))


def mutate_python_behaviour(root: Path) -> None:
    path = root / "ig-0478" / "chapter-8.md"
    text = path.read_text(encoding="utf-8")
    assert "0 <= mark <= 100" in text
    write_text(path, text.replace("0 <= mark <= 100", "0 < mark < 100", 1))


def mutate_as_java_behaviour(root: Path) -> None:
    path = root / "as-9618" / "chapter-11.md"
    text = path.read_text(encoding="utf-8")
    assert "statistics.total += mark;" in text
    write_text(path, text.replace("statistics.total += mark;", "statistics.total = mark;", 1))


def mutate_relative_links(root: Path) -> None:
    path = root / "index.html"
    text = path.read_text(encoding="utf-8")
    assert "relativePath: true" in text
    write_text(path, text.replace("relativePath: true", "relativePath: false", 1))


def mutate_duplicate_source_id(root: Path) -> None:
    path = root / "audit" / "source-manifest.csv"
    lines = path.read_text(encoding="utf-8").splitlines()
    write_text(path, "\n".join(lines + [lines[1]]) + "\n")


def mutate_invalid_source_hash(root: Path) -> None:
    path = root / "audit" / "source-manifest.csv"
    text = path.read_text(encoding="utf-8")
    original = "e89c9629185d75b7e182e74460f1b0fd62e30c71f2ae4d67c9563123ca0558d1"
    assert original in text
    write_text(path, text.replace(original, "not-a-sha256", 1))


def mutate_missing_registered_source(root: Path) -> None:
    path = root / "audit" / "source-manifest.csv"
    lines = path.read_text(encoding="utf-8").splitlines()
    write_text(path, "\n".join(line for line in lines if not line.startswith("9618-MS-41-MJ24,")) + "\n")


def mutate_unsupported_source_phrase(root: Path) -> None:
    path = root / "ig-0478" / "chapter-1.md"
    write_text(path, path.read_text(encoding="utf-8") + "\nCambridge accepts any equivalent wording.\n")


def mutate_unregistered_official_label(root: Path) -> None:
    path = root / "ig-0478" / "chapter-1.md"
    write_text(path, path.read_text(encoding="utf-8") + "\n## MS-aligned answer\n")


def mutate_subject_version(root: Path) -> None:
    path = root / "ig-0478" / "chapter-1.md"
    text = path.read_text(encoding="utf-8")
    assert "0478 · 2026–2028 · Version 6" in text
    write_text(path, text.replace("0478 · 2026–2028 · Version 6", "0478 · 2026–2028 · Version 5", 1))


def mutate_round_arity(root: Path) -> None:
    path = root / "ig-0478" / "chapter-8.md"
    text = path.read_text(encoding="utf-8")
    assert "ROUND(Area, 2)" in text
    write_text(path, text.replace("ROUND(Area, 2)", "ROUND(Area)", 1))


def mutate_9618_random_name(root: Path) -> None:
    path = root / "as-9618" / "chapter-1.md"
    write_text(path, path.read_text(encoding="utf-8") + "\nUse `RANDOM()` to obtain a random value.\n")


def mutate_ig_language_scope(root: Path) -> None:
    path = root / "ig-0478" / "paper-2-review.md"
    text = path.read_text(encoding="utf-8")
    original = "Use pseudocode, Python, Visual Basic or Java."
    assert original in text
    write_text(path, text.replace(original, "Use pseudocode or Python.", 1))


def mutate_missing_semantic_audit_row(root: Path) -> None:
    path = root / "audit" / "stage7-a2-semantic-audit.csv"
    lines = path.read_text(encoding="utf-8").splitlines()
    write_text(path, "\n".join(line for line in lines if not line.startswith("A2-13.1-01,")) + "\n")


def mutate_unverified_semantic_audit(root: Path) -> None:
    path = root / "audit" / "stage7-a2-semantic-audit.csv"
    text = path.read_text(encoding="utf-8")
    original = "A2-13.1-01,verified,verified,"
    assert original in text
    write_text(path, text.replace(original, "A2-13.1-01,verified,partial,", 1))


def mutate_unknown_audit_source(root: Path) -> None:
    path = root / "audit" / "stage7-a2-semantic-audit.csv"
    text = path.read_text(encoding="utf-8")
    original = "9618-SYL-2027-2029-V2"
    assert original in text
    write_text(path, text.replace(original, "9618-SYL-UNKNOWN", 1))


def mutate_semantic_blind_spot(root: Path) -> None:
    path = root / "a2-9618" / "chapter-19.md"
    text = path.read_text(encoding="utf-8")
    original = (
        "A dictionary stores **key–value pairs** and supports `insert(key, value)`, "
        "`find(key)` and `delete(key)`. Keys are unique even when values repeat. "
        "It may be represented by parallel key/value arrays, a binary search tree, "
        "or a hash table. With open-address hashing, insertion and search must use "
        "the same probe sequence; deletion uses a tombstone rather than an empty "
        "slot so later colliding keys remain reachable."
    )
    replacement = "A dictionary is covered here."
    if original not in text:
        raise RuntimeError("semantic control source paragraph was not found")
    write_text(path, text.replace(original, replacement, 1))


def run_checker(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/check_site.py"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def restore(root: Path, relative_path: str) -> None:
    shutil.copy2(ROOT / relative_path, root / relative_path)


def main() -> int:
    rejected_controls: list[tuple[str, str, Callable[[Path], None], str]] = [
        ("missing objective", "coverage.md", mutate_delete_objective, "missing syllabus objective ID"),
        ("duplicate objective", "coverage.md", mutate_duplicate_objective, "duplicate syllabus objective ID"),
        ("unknown objective", "coverage.md", mutate_unknown_objective, "unknown syllabus objective ID"),
        ("partial status", "coverage.md", mutate_invalid_status, "syllabus objective is not covered"),
        ("stale teaching anchor", "coverage.md", mutate_stale_teaching_anchor, "stale teaching anchor"),
        ("missing answer", "coverage.md", mutate_remove_answer, "practice evidence must name a question and its answers"),
        ("collapsed reviewed scope", "coverage.md", mutate_collapse_reviewed_scope, "omits reviewed Notes-and-guidance scope"),
        ("collapsed atomic conversion", "coverage.md", mutate_collapse_atomic_matrix, "omits reviewed Notes-and-guidance scope"),
        ("collapsed algorithm scope", "coverage.md", mutate_collapse_algorithm_scope, "omits reviewed Notes-and-guidance scope"),
        ("missing storage example", "coverage.md", mutate_remove_storage_example, "omits reviewed Notes-and-guidance scope"),
        ("missing targeted answer", "coverage.md", mutate_remove_targeted_answer, "practice evidence must name a question and its answers"),
        ("unbalanced Markdown fence", "a2-9618/chapter-19.md", mutate_markdown_fence, "unclosed fenced code block"),
        ("misnumbered answer", "ig-0478/paper-2-review.md", mutate_answer_part, "answer part numbers do not match"),
        ("wrong drill total", "ig-0478/chapter-7.md", mutate_drill_total, "marks total 35, expected 28"),
        ("Python endpoint regression", "ig-0478/chapter-8.md", mutate_python_behaviour, "Python example 1 failed"),
        ("AS Java parameter regression", "as-9618/chapter-11.md", mutate_as_java_behaviour, "Java smoke test Ch11JavaParameters failed"),
        ("relative link regression", "index.html", mutate_relative_links, "missing relative Markdown link resolution"),
        ("duplicate source ID", "audit/source-manifest.csv", mutate_duplicate_source_id, "duplicate source ID"),
        ("invalid source hash", "audit/source-manifest.csv", mutate_invalid_source_hash, "invalid SHA-256"),
        ("missing registered source", "audit/source-manifest.csv", mutate_missing_registered_source, "missing registered source ID: 9618-MS-41-MJ24"),
        ("unsupported Cambridge claim", "ig-0478/chapter-1.md", mutate_unsupported_source_phrase, "student page contains banned editorial text: Cambridge accepts"),
        ("unregistered official label", "ig-0478/chapter-1.md", mutate_unregistered_official_label, "official/MS-aligned label lacks a registered source ID"),
        ("subject version regression", "ig-0478/chapter-1.md", mutate_subject_version, "missing course/Paper/syllabus-version metadata"),
        ("0478 ROUND arity regression", "ig-0478/chapter-8.md", mutate_round_arity, "0478 ROUND must use ROUND(value, places)"),
        ("9618 random routine regression", "as-9618/chapter-1.md", mutate_9618_random_name, "9618 content must use RAND(x), not 0478 RANDOM()"),
        ("IGCSE language-scope regression", "ig-0478/paper-2-review.md", mutate_ig_language_scope, "missing syllabus-alignment evidence"),
        ("missing semantic audit row", "audit/stage7-a2-semantic-audit.csv", mutate_missing_semantic_audit_row, "semantic audit has 82 rows, expected 83"),
        ("unverified semantic audit row", "audit/stage7-a2-semantic-audit.csv", mutate_unverified_semantic_audit, "final status must be verified"),
        ("unknown semantic audit source", "audit/stage7-a2-semantic-audit.csv", mutate_unknown_audit_source, "unknown official source ID"),
    ]

    with tempfile.TemporaryDirectory(prefix="cs-web-checklist-negative-") as temp_dir:
        copy_root = Path(temp_dir) / "repo"
        shutil.copytree(
            ROOT,
            copy_root,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"),
        )

        failures: list[str] = []
        for name, relative_path, mutate, expected_message in rejected_controls:
            restore(copy_root, relative_path)
            mutate(copy_root)
            result = run_checker(copy_root)
            combined = result.stdout + result.stderr
            if result.returncode == 0 or expected_message not in combined:
                failures.append(
                    f"{name}: expected rejection containing {expected_message!r}, "
                    f"got exit {result.returncode}"
                )
            else:
                print(f"PASS (rejected): {name}")
            restore(copy_root, relative_path)

        restore(copy_root, "coverage.md")
        restore(copy_root, "a2-9618/chapter-19.md")
        mutate_semantic_blind_spot(copy_root)
        semantic_result = run_checker(copy_root)
        if semantic_result.returncode != 0:
            failures.append("semantic blind-spot control unexpectedly failed structurally")
        else:
            print("PASS (documented blind spot): semantic dilution can pass structural checks")

    if failures:
        print("Negative-control failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
