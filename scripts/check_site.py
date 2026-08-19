#!/usr/bin/env python3
"""Run dependency-free structural checks for the Docsify revision site."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
COURSE_RANGES = {
    "ig-0478": range(1, 11),
    "as-9618": range(1, 13),
    "a2-9618": range(13, 21),
}
EXPECTED_CHAPTERS = {
    ROOT / course / f"chapter-{number}.md"
    for course, numbers in COURSE_RANGES.items()
    for number in numbers
}
IG_REVIEW_PAGE = ROOT / "ig-0478" / "paper-2-review.md"
IG_REVIEW_PAGE_2 = ROOT / "ig-0478" / "paper-2-review-2.md"
IG_PAPER1_REVIEW_PAGE = ROOT / "ig-0478" / "paper-1-review.md"
IG_PAPER1_REVIEW_PAGE_2 = ROOT / "ig-0478" / "paper-1-review-2.md"
AS_REVIEW_PAGE = ROOT / "as-9618" / "paper-2-review.md"
AS_REVIEW_PAGE_2 = ROOT / "as-9618" / "paper-2-review-2.md"
AS_PAPER1_REVIEW_PAGE = ROOT / "as-9618" / "paper-1-review.md"
AS_PAPER1_REVIEW_PAGE_2 = ROOT / "as-9618" / "paper-1-review-2.md"
A2_PAPER3_REVIEW_PAGE = ROOT / "a2-9618" / "paper-3-review.md"
A2_PAPER3_REVIEW_PAGE_2 = ROOT / "a2-9618" / "paper-3-review-2.md"
A2_REVIEW_PAGE = ROOT / "a2-9618" / "paper-4-review.md"
A2_REVIEW_PAGE_2 = ROOT / "a2-9618" / "paper-4-review-2.md"
REVIEW_PAGES = {
    IG_PAPER1_REVIEW_PAGE,
    IG_PAPER1_REVIEW_PAGE_2,
    IG_REVIEW_PAGE,
    IG_REVIEW_PAGE_2,
    AS_PAPER1_REVIEW_PAGE,
    AS_PAPER1_REVIEW_PAGE_2,
    AS_REVIEW_PAGE,
    AS_REVIEW_PAGE_2,
    A2_PAPER3_REVIEW_PAGE,
    A2_PAPER3_REVIEW_PAGE_2,
    A2_REVIEW_PAGE,
    A2_REVIEW_PAGE_2,
}
HUB_PAGES = {ROOT / course / "README.md" for course in COURSE_RANGES}
COURSE_SIDEBARS = {ROOT / course / "_sidebar.md" for course in COURSE_RANGES}
SHARED_PAGES = {ROOT / "exam-technique.md", ROOT / "syllabus-versions.md"}
CONTENT_PAGES = EXPECTED_CHAPTERS | REVIEW_PAGES | HUB_PAGES | SHARED_PAGES
OVERVIEW_CONTRACTS = {
    ROOT / "ig-0478" / "chapter-1.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        ["Convert values", "Calculate storage", "Represent media", "Choose compression"],
    ),
    ROOT / "ig-0478" / "chapter-2.md": (
        "## Chapter at a Glance",
        "_chapter-2-at-a-glance",
        ["Trace packet delivery", "Select transmission", "Detect errors", "Protect messages"],
    ),
    ROOT / "ig-0478" / "chapter-3.md": (
        "## Chapter at a Glance",
        "_chapter-3-at-a-glance",
        [
            "Trace processor operation",
            "Select devices and sensors",
            "Explain data storage",
            "Connect network hardware",
        ],
    ),
    ROOT / "ig-0478" / "chapter-4.md": (
        "## Chapter at a Glance",
        "_2-chapter-4-overall-mind-map",
        ["Select software", "Handle interrupts", "Translate source code", "Use IDE tools"],
    ),
    ROOT / "ig-0478" / "chapter-5.md": (
        "## Chapter at a Glance",
        "_chapter-5-at-a-glance",
        [
            "Trace a web request",
            "Secure web use",
            "Explain digital currency",
            "Match threats to controls",
        ],
    ),
    ROOT / "ig-0478" / "chapter-6.md": (
        "## Chapter at a Glance",
        "_9-final-one-page-revision-map",
        ["Trace an automated system", "Classify robots", "Explain AI", "Evaluate impacts"],
    ),
    ROOT / "as-9618" / "chapter-1.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Convert and encode",
            "Calculate multimedia size",
            "Compare representations",
            "Choose compression",
        ],
    ),
    ROOT / "as-9618" / "chapter-2.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        ["Choose the network", "Trace the journey", "Select the technology", "Score the marks"],
    ),
    ROOT / "as-9618" / "chapter-3.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Classify hardware",
            "Compare memory and storage",
            "Trace monitoring and control",
            "Build logic answers",
        ],
    ),
    ROOT / "as-9618" / "chapter-4.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Trace fetch-decode-execute",
            "Use registers and buses",
            "Handle interrupts",
            "Read assembly code",
        ],
    ),
    ROOT / "as-9618" / "chapter-5.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Explain OS management",
            "Choose utilities and libraries",
            "Trace translation",
            "Use IDE tools",
        ],
    ),
    ROOT / "as-9618" / "chapter-6.md": (
        "## Chapter at a Glance",
        "_4-one-page-mind-map",
        [
            "Distinguish core terms",
            "Match threats to controls",
            "Validate or verify",
            "Protect integrity",
        ],
    ),
    ROOT / "as-9618" / "chapter-7.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Apply ethical principles",
            "Explain ownership and licensing",
            "Evaluate AI uses",
            "Balance impacts",
        ],
    ),
    ROOT / "as-9618" / "chapter-8.md": (
        "## Chapter at a Glance",
        "_4-one-page-mind-map",
        ["Model the database", "Normalise to 3NF", "Explain DBMS functions", "Write SQL"],
    ),
    ROOT / "a2-9618" / "chapter-13.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        ["Define data types", "Choose file access", "Calculate floating point", "Control range and error"],
    ),
    ROOT / "a2-9618" / "chapter-14.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        ["Trace the TCP/IP stack", "Compare switching", "Route packets", "Match protocols"],
    ),
    ROOT / "a2-9618" / "chapter-15.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Compare processors",
            "Explain parallel processing and VMs",
            "Simplify Boolean expressions",
            "Build logic circuits",
        ],
    ),
    ROOT / "a2-9618" / "chapter-16.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        ["Schedule processes", "Manage memory", "Handle interrupts", "Parse and translate code"],
    ),
    ROOT / "a2-9618" / "chapter-17.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Choose encryption",
            "Secure or verify messages",
            "Establish TLS trust",
            "Evaluate quantum cryptography",
        ],
    ),
    ROOT / "a2-9618" / "chapter-18.md": (
        "## Chapter at a Glance",
        "_3-one-page-mind-map",
        [
            "Model graphs and search",
            "Choose a learning approach",
            "Train a neural network",
            "Evaluate results",
        ],
    ),
}
PHASE2_CHAPTERS = {
    ROOT / "ig-0478" / "chapter-7.md": {
        "worked_examples": 3,
        "topics": [
            "Program Development Life Cycle",
            "linear search",
            "bubble sort",
            "Check digit",
            "double entry",
            "Trace Tables",
        ],
    },
    ROOT / "ig-0478" / "chapter-8.md": {
        "worked_examples": 3,
        "topics": [
            "SUBSTRING",
            "UCASE",
            "LCASE",
            "RANDOM",
            "Two-dimensional array",
            "OPENFILE",
        ],
    },
    ROOT / "ig-0478" / "chapter-9.md": {
        "worked_examples": 2,
        "topics": [
            "Primary Keys",
            "SELECT",
            "WHERE",
            "ORDER BY",
            "SUM",
            "COUNT",
        ],
    },
    ROOT / "ig-0478" / "chapter-10.md": {
        "worked_examples": 2,
        "topics": [
            "../assets/logic-gates.svg",
            "NAND",
            "NOR",
            "XOR/EOR",
            "Expression to circuit",
            "Truth table to circuit",
        ],
    },
}
PHASE3_CHAPTERS = {
    ROOT / "as-9618" / "chapter-9.md": {
        "worked_examples": 3,
        "topics": [
            "Abstraction",
            "Decomposition",
            "Identifier table",
            "Structured English",
            "Stepwise Refinement",
        ],
    },
    ROOT / "as-9618" / "chapter-10.md": {
        "worked_examples": 3,
        "topics": [
            "Records",
            "bubble sort",
            "linear search",
            "OPENFILE",
            "Abstract Data Types",
            "FreeListPointer",
        ],
    },
    ROOT / "as-9618" / "chapter-11.md": {
        "worked_examples": 3,
        "topics": [
            "BYVAL",
            "BYREF",
            "CASE OF",
            "REPEAT ... UNTIL",
            "Efficient Pseudocode",
        ],
    },
    ROOT / "as-9618" / "chapter-12.md": {
        "worked_examples": 3,
        "topics": [
            "Rapid Application Development",
            "stateDiagram-v2",
            "White-box testing",
            "Black-box testing",
            "Stub",
            "Corrective",
            "Adaptive",
            "Perfective",
        ],
    },
}
PHASE4_CHAPTERS = {
    ROOT / "a2-9618" / "chapter-19.md": {
        "worked_examples": 4,
        "topics": [
            "binarySearch",
            "insertionSort",
            "ArrayLinkedList",
            "BinarySearchTree",
            "TwoStackQueue",
            "O(log n)",
            "unwinding",
            "graph",
        ],
    },
    ROOT / "a2-9618" / "chapter-20.md": {
        "worked_examples": 4,
        "topics": [
            "Paper 4 excludes",
            "imperative",
            "Object-Oriented",
            "containment",
            "polymorphism",
            "serial",
            "sequential",
            "random",
            "HashTable",
            "FileNotFoundException",
        ],
    },
}
MARKDOWN_REF_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_REF_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
CDN_RE = re.compile(r"//cdn\.jsdelivr\.net/npm/([^/\"']+)")
EXACT_VERSION_RE = re.compile(r"^[^@]+@\d+\.\d+\.\d+$")
BOLD_MARK_RE = re.compile(r"\*\*\[(\d+)\]\*\*")
JAVA_FENCE_RE = re.compile(
    r"^```java\s*\n(.*?)^```\s*$",
    flags=re.MULTILINE | re.DOTALL,
)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add_error(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{relative(path)}: {message}")


def check_chapter_inventory(errors: list[str]) -> None:
    actual = set()
    for course in COURSE_RANGES:
        actual.update((ROOT / course).glob("chapter-*.md"))

    for path in sorted(EXPECTED_CHAPTERS - actual):
        errors.append(f"missing chapter: {relative(path)}")
    for path in sorted(actual - EXPECTED_CHAPTERS):
        errors.append(f"unexpected chapter: {relative(path)}")


def check_headings_and_fences(errors: list[str]) -> None:
    for path in sorted(CONTENT_PAGES):
        headings: list[tuple[int, int]] = []
        in_fence = False
        fence_type = ""

        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.lstrip()
            marker_match = re.match(r"(`{3,}|~{3,})", stripped)
            if marker_match:
                marker_type = marker_match.group(1)[0]
                if not in_fence:
                    in_fence = True
                    fence_type = marker_type
                elif marker_type == fence_type:
                    in_fence = False
                    fence_type = ""
                continue

            if in_fence:
                continue

            heading_match = HEADING_RE.match(line)
            if heading_match:
                headings.append((number, len(heading_match.group(1))))

        if in_fence:
            add_error(errors, path, "unclosed fenced code block")

        h1_lines = [number for number, level in headings if level == 1]
        if len(h1_lines) != 1:
            add_error(errors, path, f"expected exactly one H1, found {len(h1_lines)}")
        elif not headings or headings[0][1] != 1:
            add_error(errors, path, "the first heading must be the page H1")

        for (previous_line, previous), (number, level) in zip(headings, headings[1:]):
            if level > previous + 1:
                add_error(
                    errors,
                    path,
                    f"heading level jumps from H{previous} on line {previous_line} "
                    f"to H{level} on line {number}",
                )


def check_chapter_heading_numbering(errors: list[str]) -> None:
    artificial_h2 = re.compile(r"^## (\d+)\.\s+\S")
    three_part_h2 = re.compile(r"^## \d+\.\d+\.\d+\s+\S")
    numbered_h3 = re.compile(r"^### (\d+\.\d+)\s+\S")
    bare_section_reference = re.compile(
        r"\bSections? \d+(?:(?:\s+and\s+|[–-])\d+)*(?=\b)"
    )

    for path in sorted(EXPECTED_CHAPTERS):
        h2_titles: dict[str, int] = {}
        current_h2 = ""
        in_syllabus_map = False
        in_fence = False
        fence_type = ""

        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            stripped = line.lstrip()
            marker_match = re.match(r"(`{3,}|~{3,})", stripped)
            if marker_match:
                marker_type = marker_match.group(1)[0]
                if not in_fence:
                    in_fence = True
                    fence_type = marker_type
                elif marker_type == fence_type:
                    in_fence = False
                    fence_type = ""
                continue

            if in_fence:
                continue

            if line.startswith("## "):
                current_h2 = line[3:].strip()
                in_syllabus_map = current_h2 == "Syllabus Map"
                normalised = " ".join(current_h2.split()).casefold()
                if normalised in h2_titles:
                    add_error(
                        errors,
                        path,
                        f"duplicate H2 '{current_h2}' on lines "
                        f"{h2_titles[normalised]} and {number}",
                    )
                else:
                    h2_titles[normalised] = number

                if artificial_h2.match(line):
                    add_error(errors, path, f"artificial H2 page number on line {number}")
                if three_part_h2.match(line):
                    add_error(errors, path, f"three-part syllabus code must not be H2 on line {number}")
                continue

            h3_match = numbered_h3.match(line)
            if h3_match and not (
                path == ROOT / "as-9618" / "chapter-6.md"
                and current_h2 == "Syllabus Map"
                and h3_match.group(1) in {"6.1", "6.2"}
            ):
                add_error(errors, path, f"artificial two-part H3 page number on line {number}")

            if in_syllabus_map and bare_section_reference.search(line):
                add_error(
                    errors,
                    path,
                    f"Syllabus Map uses a bare page-section reference on line {number}",
                )


def resolve_reference(source: Path, reference: str) -> Path | None:
    reference = unquote(reference.strip().split()[0].strip("<>\"'"))
    if not reference or reference.startswith(("http://", "https://", "//", "mailto:", "tel:")):
        return None
    if reference.startswith("#/"):
        raw_route = reference[2:].split("?", 1)[0].split("#", 1)[0]
        route = raw_route.strip("/")
        if not route:
            return ROOT / "README.md"
        if raw_route.endswith("/"):
            return ROOT / route / "README.md"
        return ROOT / f"{route}.md"
    if reference.startswith("#"):
        return None
    if reference.startswith("/"):
        raw_route = reference.split("?", 1)[0].split("#", 1)[0]
        route = raw_route.strip("/")
        if not route:
            return ROOT / "README.md"
        if raw_route.endswith("/"):
            return ROOT / route / "README.md"
        return ROOT / f"{route}.md"

    target = reference.split("?", 1)[0].split("#", 1)[0]
    if not target:
        return None
    if target.startswith("assets/"):
        return (ROOT / target).resolve()
    return (source.parent / target).resolve()


def check_references(errors: list[str]) -> None:
    sources = sorted(ROOT.glob("*.md")) + sorted(ROOT.glob("*.html"))
    for course in COURSE_RANGES:
        sources.extend(sorted((ROOT / course).glob("*.md")))

    for source in sources:
        text = source.read_text(encoding="utf-8")
        references = MARKDOWN_REF_RE.findall(text) + HTML_REF_RE.findall(text)
        for reference in references:
            target = resolve_reference(source, reference)
            if target is not None and not target.exists():
                add_error(errors, source, f"missing local target for {reference!r}")


def local_targets(source: Path) -> set[Path]:
    text = source.read_text(encoding="utf-8")
    references = MARKDOWN_REF_RE.findall(text) + HTML_REF_RE.findall(text)
    return {
        target
        for reference in references
        if (target := resolve_reference(source, reference)) is not None
    }


def check_navigation(errors: list[str]) -> None:
    root_sources = [ROOT / "README.md", ROOT / "_coverpage.md", ROOT / "_sidebar.md"]
    for source in root_sources:
        targets = local_targets(source)
        missing_hubs = HUB_PAGES - targets
        if missing_hubs:
            add_error(errors, source, "root navigation must link all three course hubs")
        if any(target.name.startswith("chapter-") for target in targets):
            add_error(errors, source, "root navigation must not list individual chapters")
        if ROOT / "coverage.md" in targets:
            add_error(errors, source, "coverage.md is maintainer-only and must not be in student navigation")

    course_reviews = {
        "ig-0478": {
            IG_PAPER1_REVIEW_PAGE,
            IG_PAPER1_REVIEW_PAGE_2,
            IG_REVIEW_PAGE,
            IG_REVIEW_PAGE_2,
        },
        "as-9618": {
            AS_PAPER1_REVIEW_PAGE,
            AS_PAPER1_REVIEW_PAGE_2,
            AS_REVIEW_PAGE,
            AS_REVIEW_PAGE_2,
        },
        "a2-9618": {
            A2_PAPER3_REVIEW_PAGE,
            A2_PAPER3_REVIEW_PAGE_2,
            A2_REVIEW_PAGE,
            A2_REVIEW_PAGE_2,
        },
    }
    for course, numbers in COURSE_RANGES.items():
        expected_chapters = {ROOT / course / f"chapter-{number}.md" for number in numbers}
        expected = expected_chapters | course_reviews[course]
        for source in (ROOT / course / "README.md", ROOT / course / "_sidebar.md"):
            targets = local_targets(source)
            if not expected.issubset(targets):
                add_error(errors, source, "course hub/sidebar is missing chapter or review links")
            foreign = {
                target for target in targets
                if target.name.startswith("chapter-") and target.parent.name != course
            }
            if foreign:
                add_error(errors, source, "course navigation contains a chapter from another level")

        sidebar = ROOT / course / "_sidebar.md"
        sidebar_references = MARKDOWN_REF_RE.findall(sidebar.read_text(encoding="utf-8"))
        local_references = [
            reference for reference in sidebar_references
            if not reference.startswith(("http://", "https://", "//", "mailto:", "tel:"))
        ]
        if any(not reference.startswith("/") for reference in local_references):
            add_error(
                errors,
                sidebar,
                "course sidebar links must use explicit Docsify routes so the course prefix is preserved",
            )
        course_references = [
            reference for reference in local_references
            if "chapter-" in reference or "paper-" in reference
        ]
        if any(not reference.startswith(f"/{course}/") for reference in course_references):
            add_error(errors, sidebar, "course sidebar content links must retain the course route prefix")

    root_sidebar = (ROOT / "_sidebar.md").read_text(encoding="utf-8")
    if "chapter-" in root_sidebar:
        add_error(errors, ROOT / "_sidebar.md", "root sidebar must stay course-level")

    index = ROOT / "index.html"
    index_text = index.read_text(encoding="utf-8")
    submax_levels = re.findall(r"\bsubMaxLevel\s*:\s*(\d+)", index_text)
    if submax_levels != ["0"]:
        add_error(
            errors,
            index,
            "Docsify subMaxLevel must be explicitly set to 0 so course sidebars stay course-only",
        )
    if "paths: 'auto'" in index_text or "paths: \"auto\"" in index_text:
        add_error(errors, index, "search paths must be an explicit list")
    for path in sorted(CONTENT_PAGES):
        if path in SHARED_PAGES:
            route = "/" + path.stem
        elif path.name == "README.md":
            route = "/" + path.parent.name + "/"
        else:
            route = "/" + relative(path)[:-3]
        if repr(route) not in index_text:
            add_error(errors, index, f"explicit search paths missing {route}")


def check_marked_chapter_contracts(
    errors: list[str],
    phase_name: str,
    chapters: dict[Path, dict[str, object]],
) -> None:
    required_sections = [
        "Official Syllabus Checklist",
        "10-Mark Quick Check",
        "Quick Check Answers",
        "20-Mark Exam Practice",
        "Practice Mark Scheme",
        "Total: 10 marks",
        "Total: 20 marks",
    ]

    for path, requirements in chapters.items():
        text = path.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                add_error(
                    errors,
                    path,
                    f"missing {phase_name} content contract: {section}",
                )

        worked_examples = len(
            re.findall(r"^## (?:\d+\. )?Worked Example", text, flags=re.MULTILINE)
        )
        required_examples = int(requirements["worked_examples"])
        if worked_examples < required_examples:
            add_error(
                errors,
                path,
                f"expected at least {required_examples} worked examples, "
                f"found {worked_examples}",
            )

        for topic in requirements["topics"]:
            if str(topic).casefold() not in text.casefold():
                add_error(errors, path, f"missing required syllabus evidence: {topic}")

        for label, expected_total in [
            ("10-Mark Quick Check", 10),
            ("20-Mark Exam Practice", 20),
        ]:
            heading_match = re.search(
                rf"^## {re.escape(label)}$",
                text,
                flags=re.MULTILINE,
            )
            total_marker = f"**Total: {expected_total} marks**"
            if heading_match is None:
                continue
            total_position = text.find(total_marker, heading_match.end())
            if total_position == -1:
                continue
            assessment_text = text[heading_match.end():total_position]
            actual_total = sum(
                int(mark) for mark in BOLD_MARK_RE.findall(assessment_text)
            )
            if actual_total != expected_total:
                add_error(
                    errors,
                    path,
                    f"{label} mark labels total {actual_total}, "
                    f"expected {expected_total}",
                )


def check_editorial_contracts(errors: list[str]) -> None:
    required_sections = [
        "Official Syllabus Checklist",
        "Core Knowledge",
        "Required Ideas and Exam Language",
        "Common Confusions",
        "Worked Examples",
        "10-Mark Quick Check",
        "Quick Check Answers",
        "20-Mark Exam Practice",
        "Final Revision Checklist",
    ]
    banned = [
        "Content Update Decision",
        "Keep and Strengthen",
        "Keep / Downweight / Delete",
        "Keep/Downweight/Delete",
        "Downweighted content",
        "Downweight warning",
        "Delete / Avoid",
        "Remove / Avoid",
        "Must-have keywords",
        "**Version:**",
        "Main audience:",
        "**Style:**",
        "regenerated version",
        "Ongoing Improvement Areas",
        "Maintenance Priorities",
        "structural/content/runtime checker",
        "current maturity",
        "旧版",
        "文件没有完整覆盖",
        "必须补回",
        "<font",
        "**Docsify:**",
    ]
    dated_editorial_patterns = [
        (
            r"^#{2,6}\s+.*\b20\d{2}(?:[–-]20\d{2})?\b.*"
            r"(?:style|trend|focus|warning|answer|clue|wording|justification|tip|features|phrase)",
            "dated editorial heading",
        ),
        (
            r"\b20\d{2}\s+Paper\s+[1-4]\s+(?:also\s+)?(?:asked|tested)\b",
            "dated past-paper commentary",
        ),
        (
            r"\b20\d{2}(?:[–-]20\d{2})?\s+mark schemes?\s+"
            r"(?:often\s+)?(?:award|reward)\b",
            "dated mark-scheme commentary",
        ),
    ]
    identities = {
        "ig-0478": ("# IGCSE 0478 Chapter", "0478 · 2026–2028 · Version 5"),
        "as-9618": ("# AS 9618 Chapter", "9618 · 2027–2029 · Version 2"),
        "a2-9618": ("# A2 9618 Chapter", "9618 · 2027–2029 · Version 2"),
    }
    for path in sorted(EXPECTED_CHAPTERS):
        text = path.read_text(encoding="utf-8")
        h1_prefix, version = identities[path.parent.name]
        if not text.startswith(h1_prefix):
            add_error(errors, path, f"H1 must start with {h1_prefix!r}")
        if version not in text or "class=\"chapter-meta\"" not in text:
            add_error(errors, path, "missing course/Paper/syllabus-version metadata")
        for section in required_sections:
            if f"## {section}" not in text:
                add_error(errors, path, f"missing chapter contract section: {section}")
        for phrase in banned:
            if phrase.casefold() in text.casefold():
                add_error(errors, path, f"student page contains banned editorial text: {phrase}")
        for pattern, description in dated_editorial_patterns:
            if re.search(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
                add_error(errors, path, f"student page contains {description}")
        for marks in (10, 20):
            if f"**Total: {marks} marks**" not in text:
                add_error(errors, path, f"missing explicit {marks}-mark assessment total")
        for number, line in enumerate(text.splitlines(), 1):
            if line.startswith("#") and re.search(r"[\u4e00-\u9fff]", line):
                add_error(errors, path, f"student heading must be English (line {number})")
            if re.search(r"[\u4e00-\u9fff]", line) and 'lang="zh-CN"' not in line:
                add_error(errors, path, f"Chinese support lacks lang attribute (line {number})")


def check_ao_totals(
    errors: list[str],
    path: Path,
    expected_ao1: int,
    expected_ao2: int,
    expected_ao3: int | None = None,
) -> None:
    text = path.read_text(encoding="utf-8")
    if expected_ao3 is None:
        total_row = rf"\| \*\*Total\*\* .*\| \*\*75\*\* \| \*\*{expected_ao1}\*\* \| \*\*{expected_ao2}\*\* \|"
    else:
        total_row = rf"\| \*\*Total\*\* .*\| \*\*75\*\* \| \*\*{expected_ao1}\*\* \| \*\*{expected_ao2}\*\* \| \*\*{expected_ao3}\*\* \|"
    if not re.search(total_row, text):
        add_error(errors, path, "assessment-objective totals do not match the approved allocation")


def check_syllabus_alignment_contracts(errors: list[str]) -> None:
    required_evidence = {
        ROOT / "ig-0478" / "chapter-3.md": [
            "**Optical mouse**",
            "#### Touchscreen types",
            "**Resistive**",
            "**Capacitive**",
            "**DLP projector**",
            "**LCD projector**",
            "**LCD screen**",
            "**LED screen**",
            "**3D printer**",
            "**Acoustic**",
            "**Magnetic field**",
            "### Required input and output devices",
            "Optical mouse →",
            "DLP / LCD projector →",
            "LCD / LED screen →",
        ],
        ROOT / "ig-0478" / "chapter-8.md": [
            "between `0` and `1` inclusive",
            "RAND(x)",
        ],
        ROOT / "ig-0478" / "chapter-7.md": [
            "### Abstraction",
            "Decomposition divides the problem",
            "one detail that can be removed by abstraction",
        ],
        ROOT / "ig-0478" / "chapter-9.md": [
            "### Validation in a database design",
            "State one suitable validation rule for `HourlyRate`",
        ],
        ROOT / "as-9618" / "chapter-3.md": [
            "##### Laser printer",
            "##### 3D printer",
            "##### Microphone",
            "##### Speaker",
            "##### Touchscreen",
            "##### Virtual reality headset",
            "### Magnetic hard disk",
            "### Optical storage",
            "### Solid-state storage / flash memory",
            "floating gate",
        ],
        ROOT / "as-9618" / "chapter-4.md": [
            "## Peripheral Ports",
            "| USB |",
            "| HDMI |",
            "| VGA |",
            "### Current example instruction set",
            "`LDM #n`",
            "`LDD address`",
            "`LDI address`",
            "`LDX address`",
            "`LDR #n`",
            "`MOV IX`",
            "`STO address`",
            "`ADD address` / `ADD #n`",
            "`SUB address` / `SUB #n`",
            "`INC register` / `DEC register`",
            "`JMP address`",
            "`CMP address` / `CMP #n`",
            "`CMI address`",
            "`JPE address`",
            "`JPN address`",
            "`IN`",
            "`OUT`",
            "`END`",
        ],
        ROOT / "as-9618" / "chapter-8.md": [
            "### Secondary key",
            "### Indexing",
            "does not have to contain unique values",
        ],
        ROOT / "a2-9618" / "chapter-19.md": [
            "A2 9618 · Papers 3–4",
            "**Paper 3 focus:**",
            "**Paper 4 focus:**",
            "Java console mode",
            "Pseudocode for binary search",
        ],
        ROOT / "a2-9618" / "chapter-20.md": [
            "A2 9618 · Papers 3–4",
            "## Low-Level Programming for Paper 3",
            "## Declarative Programming for Paper 3",
            "immediate",
            "direct",
            "indirect",
            "indexed",
            "relative",
            "LDM #n",
            "LDD address",
            "LDI address",
            "LDX address",
            "JPE",
            "FACT",
            "RULE",
            "GOAL",
            "Java console mode",
        ],
        AS_PAPER1_REVIEW_PAGE: [
            "star topology",
            "public and a private IP address",
            "program libraries",
            "encryption protects appointment data",
        ],
        AS_REVIEW_PAGE_2: [
            "ADT operations and array representation",
            "Trace these operations in order",
            "Count = 6` means full",
        ],
        IG_REVIEW_PAGE: ["Use pseudocode or Python"],
        IG_REVIEW_PAGE_2: ["Use pseudocode or Python"],
        A2_PAPER3_REVIEW_PAGE: [
            "BitTorrent distributes a file between peers",
            "lexical analysis, syntax analysis and code generation",
            "RULE priority(X) IF refrigerated(X)",
        ],
        A2_PAPER3_REVIEW_PAGE_2: [
            "Compare POP3 and IMAP",
            "reinforcement learning uses rewards and penalties",
            "Using `LDM`, `STO` and `JPE`",
            "JPE MATCH",
        ],
        A2_REVIEW_PAGE: [
            "Java console mode",
            "Complete every task in Java",
        ],
        A2_REVIEW_PAGE_2: [
            "Java console mode",
            "Complete every task in Java",
        ],
        ROOT / "exam-technique.md": [
            "## Examination Conditions",
            "IGCSE 0478 Papers 1 and 2 do not permit calculators",
            "9618 Papers 1, 2, 3 and 4 do not permit calculators",
        ],
        ROOT / "as-9618" / "README.md": [
            "721401-2027-2029-pseudocode-guide.pdf",
            "Pseudocode is compulsory for Paper 2",
        ],
        ROOT / "ig-0478" / "README.md": [
            "required pseudocode",
            "Python program-code practice",
        ],
        ROOT / "a2-9618" / "README.md": [
            "Pseudocode remains required",
            "Java console mode only",
        ],
        ROOT / "syllabus-versions.md": [
            "721401-2027-2029-pseudocode-guide.pdf",
            "RAND(x)",
            "RANDOM()",
            "every student learns pseudocode",
            "Java console mode only",
        ],
    }

    for path, evidence_items in required_evidence.items():
        text = path.read_text(encoding="utf-8")
        for evidence in evidence_items:
            if evidence not in text:
                add_error(errors, path, f"missing syllabus-alignment evidence: {evidence}")

    forbidden_evidence = {
        ROOT / "as-9618" / "chapter-4.md": ["JPZ", "| Logic / bitwise |"],
        AS_PAPER1_REVIEW_PAGE: [
            "packet switching allows a file",
            "purpose of a MAC address",
            "linker and a loader",
            "asymmetric encryption can establish",
        ],
        AS_REVIEW_PAGE_2: [
            "Write pseudocode for `Enqueue",
            "FUNCTION Enqueue",
            "Write pseudocode for `Dequeue",
            "FUNCTION Dequeue",
        ],
        IG_REVIEW_PAGE: ["Visual Basic", "Use pseudocode, Python, Visual Basic or Java"],
        IG_REVIEW_PAGE_2: ["Visual Basic", "Use pseudocode, Python, Visual Basic or Java"],
        A2_PAPER3_REVIEW_PAGE: [
            "bit streaming and why buffering",
            "compiler, linker and loader",
        ],
        A2_PAPER3_REVIEW_PAGE_2: [
            "buffering may be needed at the receiver",
            "training data, validation data and test data",
            "Distinguish syntax, logic and runtime errors",
        ],
        A2_REVIEW_PAGE: ["```python", "Python 3 console mode"],
        A2_REVIEW_PAGE_2: ["```python", "Python 3 console mode"],
        ROOT / "a2-9618" / "chapter-19.md": ["```python", "Python 3"],
        ROOT / "a2-9618" / "chapter-20.md": ["```python", "Python 3"],
    }

    for path, forbidden_items in forbidden_evidence.items():
        text = path.read_text(encoding="utf-8")
        for forbidden in forbidden_items:
            if forbidden.casefold() in text.casefold():
                add_error(errors, path, f"contains out-of-scope syllabus evidence: {forbidden}")

    for review_page in sorted(REVIEW_PAGES):
        if "Do not use a calculator." not in review_page.read_text(encoding="utf-8"):
            add_error(errors, review_page, "full-paper instructions must prohibit calculators")

    for practical_page in (A2_REVIEW_PAGE, A2_REVIEW_PAGE_2):
        if "without internet or email access" not in practical_page.read_text(encoding="utf-8"):
            add_error(errors, practical_page, "Paper 4 instructions must require an offline computer")

    coverage = ROOT / "coverage.md"
    coverage_text = coverage.read_text(encoding="utf-8")
    if "| ID | Requirement paraphrase | Chapter heading evidence | Practice evidence | Status |" not in coverage_text:
        add_error(errors, coverage, "alignment register must use the required evidence columns")
    row_pattern = re.compile(
        r"^\| ((?:IG|AS|A2)-[^| ]+) \|.*\| (covered|partial|missing) \|$",
        flags=re.MULTILINE,
    )
    alignment_rows = row_pattern.findall(coverage_text)
    expected_counts = {"IG": 29, "AS": 29, "A2": 15}
    actual_counts = {course: 0 for course in expected_counts}
    seen_ids: set[str] = set()
    for objective_id, status in alignment_rows:
        course = objective_id.split("-", 1)[0]
        actual_counts[course] += 1
        if course == "IG":
            valid_id = re.fullmatch(r"IG-\d+\.\d+-\d+", objective_id)
        else:
            valid_id = re.fullmatch(
                rf"{course}-\d+\.\d+-[a-z0-9]+(?:-[a-z0-9]+)*",
                objective_id,
            )
        if not valid_id:
            add_error(errors, coverage, f"invalid syllabus objective ID format: {objective_id}")
        if objective_id in seen_ids:
            add_error(errors, coverage, f"duplicate syllabus objective ID: {objective_id}")
        seen_ids.add(objective_id)
        if status != "covered":
            add_error(errors, coverage, f"syllabus objective is not covered: {objective_id}")

    for course, expected_count in expected_counts.items():
        if actual_counts[course] != expected_count:
            add_error(
                errors,
                coverage,
                f"{course} alignment register has {actual_counts[course]} rows; "
                f"expected {expected_count}",
            )


def check_mixed_review(
    errors: list[str],
    review_page: Path,
    expected_questions: int,
    required_evidence: list[str],
) -> None:
    review_text = review_page.read_text(encoding="utf-8")
    question_matches = list(
        re.finditer(
            r"^## Question (\d+) .+ \[(\d+)\]$",
            review_text,
            flags=re.MULTILINE,
        )
    )
    question_headings = [match.group(0) for match in question_matches]
    mark_scheme_numbers = re.findall(
        r"^### Question (\d+) Mark Scheme\b",
        review_text,
        flags=re.MULTILINE,
    )
    expected_numbers = [str(number) for number in range(1, expected_questions + 1)]
    actual_numbers = [match.group(1) for match in question_matches]
    if len(question_headings) != expected_questions or actual_numbers != expected_numbers:
        add_error(
            errors,
            review_page,
            f"expected questions {', '.join(expected_numbers)}, "
            f"found {', '.join(actual_numbers) or 'none'}",
        )
    if mark_scheme_numbers != expected_numbers:
        add_error(
            errors,
            review_page,
            f"expected mark schemes {', '.join(expected_numbers)}, "
            f"found {', '.join(mark_scheme_numbers) or 'none'}",
        )

    if len(question_matches) == expected_questions:
        heading_total = sum(int(match.group(2)) for match in question_matches)
        if heading_total != 75:
            add_error(
                errors,
                review_page,
                f"question heading marks total {heading_total}, expected 75",
            )

        mark_scheme_start = review_text.find("\n## Mark Scheme")
        if mark_scheme_start == -1:
            add_error(errors, review_page, "missing Mark Scheme section")
        for index, match in enumerate(question_matches):
            if mark_scheme_start == -1:
                break
            next_start = (
                question_matches[index + 1].start()
                if index + 1 < len(question_matches)
                else mark_scheme_start
            )
            question_text = review_text[match.end():next_start]
            labelled_total = sum(
                int(mark) for mark in BOLD_MARK_RE.findall(question_text)
            )
            expected_total = int(match.group(2))
            if labelled_total != expected_total:
                add_error(
                    errors,
                    review_page,
                    f"Question {match.group(1)} mark labels total "
                    f"{labelled_total}, expected {expected_total}",
                )

    for evidence in required_evidence:
        if evidence not in review_text:
            add_error(errors, review_page, f"missing review contract: {evidence}")


def extract_review_questions(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    mark_scheme = re.search(r"^## Mark Scheme\s*$", text, flags=re.MULTILINE)
    question_text = text[: mark_scheme.start()] if mark_scheme else text
    matches = list(re.finditer(r"^## Question \d+[^\n]*$", question_text, flags=re.MULTILINE))

    return [
        question_text[
            match.end() : matches[index + 1].start()
            if index + 1 < len(matches)
            else len(question_text)
        ]
        for index, match in enumerate(matches)
    ]


def normalise_question(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def check_review_independence(
    errors: list[str],
    first_set: Path,
    second_set: Path,
    maximum_similarity: float = 0.65,
) -> None:
    first_questions = extract_review_questions(first_set)
    second_questions = extract_review_questions(second_set)

    for first_index, first_question in enumerate(first_questions, 1):
        for second_index, second_question in enumerate(second_questions, 1):
            similarity = SequenceMatcher(
                None,
                normalise_question(first_question),
                normalise_question(second_question),
            ).ratio()
            if similarity >= maximum_similarity:
                add_error(
                    errors,
                    second_set,
                    f"Question {second_index} is too similar to Set A Question "
                    f"{first_index} ({similarity:.0%}; limit {maximum_similarity:.0%})",
                )


def check_java_code_blocks(errors: list[str]) -> None:
    java_pages = set(PHASE4_CHAPTERS) | {A2_REVIEW_PAGE, A2_REVIEW_PAGE_2}
    javac = shutil.which("javac")
    java = shutil.which("java")
    if javac is None or java is None:
        errors.append("Java validation requires both javac and java on PATH")
        return

    smoke_classes = {
        ROOT / "a2-9618" / "chapter-19.md": [
            "Ch19SearchSortDemo",
            "Ch19ArrayLinkedListDemo",
            "Ch19TwoStackQueueDemo",
            "Ch19TreeDemo",
            "Ch19RecursionDemo",
        ],
        ROOT / "a2-9618" / "chapter-20.md": [
            "Ch20OopDemo",
            "Ch20HashTableDemo",
            "Ch20FileDemo",
        ],
        A2_REVIEW_PAGE: [
            "Paper4AQuestion1",
            "Paper4AQuestion2",
            "Paper4AQuestion3",
        ],
        A2_REVIEW_PAGE_2: [
            "Paper4BQuestion1",
            "Paper4BQuestion2",
            "Paper4BQuestion3",
        ],
    }

    for path in sorted(java_pages):
        text = path.read_text(encoding="utf-8")
        blocks = JAVA_FENCE_RE.findall(text)
        if not blocks:
            add_error(errors, path, "expected at least one fenced Java code block")
            continue
        if "```python" in text.casefold() or "Python 3 console mode" in text:
            add_error(errors, path, "A2 executable content must be Java-only")

        with tempfile.TemporaryDirectory(prefix="cs-check-java-") as temp_name:
            temp = Path(temp_name)
            output = temp / "classes"
            output.mkdir()
            compilation_failed = False
            for block_number, code in enumerate(blocks, 1):
                source = temp / f"Snippet{block_number}.java"
                source.write_text(code, encoding="utf-8")
                result = subprocess.run(
                    [javac, "-encoding", "UTF-8", "-d", str(output), str(source)],
                    capture_output=True,
                    text=True,
                    timeout=20,
                    check=False,
                )
                if result.returncode != 0:
                    compilation_failed = True
                    detail = (result.stderr or result.stdout).strip().splitlines()
                    add_error(
                        errors,
                        path,
                        f"Java block {block_number} failed to compile: "
                        + (detail[-1] if detail else "unknown javac error"),
                    )

            if compilation_failed:
                continue

            for class_name in smoke_classes[path]:
                result = subprocess.run(
                    [java, "-cp", str(output), class_name],
                    capture_output=True,
                    text=True,
                    timeout=20,
                    check=False,
                )
                if result.returncode != 0:
                    detail = (result.stderr or result.stdout).strip().splitlines()
                    add_error(
                        errors,
                        path,
                        f"Java smoke test {class_name} failed: "
                        + (detail[-1] if detail else f"exit {result.returncode}"),
                    )

    for course in (ROOT / "as-9618", ROOT / "a2-9618"):
        for path in sorted(course.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if re.search(r"\bpython\b", text, flags=re.IGNORECASE):
                add_error(errors, path, "AS/A2 student content must use Java, not Python")


def check_chapter_overviews(errors: list[str]) -> None:
    mindmap_fence = re.compile(
        r"^```mermaid\s*\n\s*mindmap\b",
        flags=re.MULTILINE,
    )
    for path in sorted(EXPECTED_CHAPTERS):
        text = path.read_text(encoding="utf-8")
        if mindmap_fence.search(text):
            add_error(errors, path, "chapter inventory must not use a Mermaid mindmap fence")

    for path, (overview_heading, legacy_anchor, expected_topics) in OVERVIEW_CONTRACTS.items():
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        try:
            heading_index = lines.index(overview_heading)
        except ValueError:
            add_error(errors, path, f"missing overview heading: {overview_heading}")
            continue

        try:
            anchor_index = next(
                index
                for index, line in enumerate(lines)
                if f'id="{legacy_anchor}"' in line and 'class="legacy-anchor"' in line
            )
        except StopIteration:
            add_error(errors, path, f"missing legacy overview anchor: {legacy_anchor}")
        else:
            if anchor_index >= heading_index:
                add_error(errors, path, "legacy overview anchor must appear before the new heading")

        level = len(overview_heading) - len(overview_heading.lstrip("#"))
        end_index = len(lines)
        for index in range(heading_index + 1, len(lines)):
            if lines[index] == "---":
                end_index = index
                break
            match = re.match(r"^(#{1,6})\s+\S", lines[index])
            if match and len(match.group(1)) <= level:
                end_index = index
                break

        overview_lines = lines[heading_index + 1 : end_index]
        topic_prefix = "#" * (level + 1) + " "
        topic_positions = [
            index
            for index, line in enumerate(overview_lines)
            if line.startswith(topic_prefix)
        ]
        actual_topics = [overview_lines[index][len(topic_prefix) :] for index in topic_positions]
        if actual_topics != expected_topics:
            add_error(
                errors,
                path,
                "overview task areas must be exactly: " + "; ".join(expected_topics),
            )
            continue

        intro = "\n".join(overview_lines[: topic_positions[0]]).strip()
        if not intro or re.search(r"[<>]", intro):
            add_error(errors, path, "overview must begin with one plain Markdown instruction sentence")

        information_units = len(actual_topics)
        for topic_index, topic_name in enumerate(actual_topics):
            start = topic_positions[topic_index] + 1
            end = (
                topic_positions[topic_index + 1]
                if topic_index + 1 < len(topic_positions)
                else len(overview_lines)
            )
            topic_text = "\n".join(overview_lines[start:end])
            cn_hints = re.findall(r'<span lang="zh-CN">[^<]+</span>', topic_text)
            statements = re.findall(r"^- \S.+$", topic_text, flags=re.MULTILINE)
            exam_cues = re.findall(r"^\*\*Exam cue:\*\* \S.+$", topic_text, flags=re.MULTILINE)

            if len(cn_hints) != 1:
                add_error(errors, path, f"{topic_name} must contain exactly one Chinese hint")
            if len(statements) != 3:
                add_error(
                    errors,
                    path,
                    f"{topic_name} must contain exactly three core statements, found {len(statements)}",
                )
            if len(exam_cues) != 1:
                add_error(errors, path, f"{topic_name} must contain exactly one Exam cue")

            information_units += len(cn_hints) + len(statements) + len(exam_cues)

        if not 20 <= information_units <= 28:
            add_error(
                errors,
                path,
                f"overview has {information_units} information units; expected 20 to 28",
            )


def check_marked_content(errors: list[str]) -> None:
    check_editorial_contracts(errors)
    check_syllabus_alignment_contracts(errors)
    check_chapter_overviews(errors)
    check_marked_chapter_contracts(errors, "Phase 2", PHASE2_CHAPTERS)
    check_marked_chapter_contracts(errors, "Phase 3", PHASE3_CHAPTERS)
    check_marked_chapter_contracts(errors, "Phase 4", PHASE4_CHAPTERS)

    check_mixed_review(
        errors,
        IG_PAPER1_REVIEW_PAGE,
        6,
        [
            "Original practice paper",
            "1 hour 45 minutes",
            "0478, examinations 2026–2028, Version 5",
            "Question 6 — Automated and Emerging Technologies [12]",
            "**45** | **15** | **15**",
        ],
    )
    check_mixed_review(
        errors,
        IG_PAPER1_REVIEW_PAGE_2,
        6,
        [
            "Original practice paper",
            "independent second set",
            "1 hour 45 minutes",
            "Question 6 — Automated and Emerging Technologies [12]",
            "**45** | **15** | **15**",
        ],
    )
    check_mixed_review(
        errors,
        IG_REVIEW_PAGE,
        7,
        [
            "Original practice paper",
            "1 hour 45 minutes",
            "Question 7 — Integrated Programming Scenario [15]",
            "Total: **75 marks**",
        ],
    )
    check_mixed_review(
        errors,
        IG_REVIEW_PAGE_2,
        7,
        [
            "Original practice paper",
            "independent second set",
            "1 hour 45 minutes",
            "Question 7 — Integrated Programming Scenario [15]",
            "Total: 75 marks",
        ],
    )
    check_mixed_review(
        errors,
        AS_PAPER1_REVIEW_PAGE,
        8,
        [
            "Original practice paper",
            "1 hour 30 minutes",
            "9618, examinations 2027–2029, Version 2",
            "Question 8 — Databases [10]",
            "**45** | **30**",
        ],
    )
    check_mixed_review(
        errors,
        AS_PAPER1_REVIEW_PAGE_2,
        8,
        [
            "Original practice paper",
            "independent second set",
            "1 hour 30 minutes",
            "Question 8 — Databases [10]",
            "**45** | **30**",
        ],
    )
    check_mixed_review(
        errors,
        AS_REVIEW_PAGE,
        7,
        [
            "Original practice paper",
            "2 hours",
            "Question 7 — Integrated Pseudocode Scenario [15]",
            "Total: **75 marks**",
        ],
    )
    check_mixed_review(
        errors,
        AS_REVIEW_PAGE_2,
        7,
        [
            "Original practice paper",
            "independent second set",
            "2 hours",
            "Question 7 — Integrated Pseudocode Scenario [15]",
            "Total: 75 marks",
        ],
    )
    check_mixed_review(
        errors,
        A2_PAPER3_REVIEW_PAGE,
        8,
        [
            "Original practice paper",
            "Review — Set A",
            "1 hour 30 minutes",
            "Sections 13–20",
            "Question 8 — Further Programming [9]",
            "Total: 75 marks",
        ],
    )
    check_mixed_review(
        errors,
        A2_PAPER3_REVIEW_PAGE_2,
        8,
        [
            "Original practice paper",
            "independent second set",
            "1 hour 30 minutes",
            "Question 8 — Program Design [9]",
            "**45** | **30**",
        ],
    )
    check_mixed_review(
        errors,
        A2_REVIEW_PAGE,
        3,
        [
            "Original practice paper",
            "2 hours 30 minutes",
            "Java console mode",
            "complete program code and evidence of testing",
            "Question 3 — Clinic Queue and Direct Lookup [24]",
            "75 marks",
        ],
    )
    check_mixed_review(
        errors,
        A2_REVIEW_PAGE_2,
        3,
        [
            "Original practice paper",
            "independent second practical set",
            "2 hours 30 minutes",
            "Java console mode",
            "Question 3 — Search Tree Catalogue [24]",
            "75 marks",
        ],
    )
    check_review_independence(errors, IG_REVIEW_PAGE, IG_REVIEW_PAGE_2)
    check_review_independence(errors, IG_PAPER1_REVIEW_PAGE, IG_PAPER1_REVIEW_PAGE_2)
    check_review_independence(errors, AS_REVIEW_PAGE, AS_REVIEW_PAGE_2)
    check_review_independence(errors, AS_PAPER1_REVIEW_PAGE, AS_PAPER1_REVIEW_PAGE_2)
    check_review_independence(errors, A2_PAPER3_REVIEW_PAGE, A2_PAPER3_REVIEW_PAGE_2)
    check_review_independence(errors, A2_REVIEW_PAGE, A2_REVIEW_PAGE_2)
    check_ao_totals(errors, IG_PAPER1_REVIEW_PAGE, 45, 15, 15)
    check_ao_totals(errors, IG_PAPER1_REVIEW_PAGE_2, 45, 15, 15)
    check_ao_totals(errors, AS_PAPER1_REVIEW_PAGE, 45, 30)
    check_ao_totals(errors, AS_PAPER1_REVIEW_PAGE_2, 45, 30)
    check_ao_totals(errors, A2_PAPER3_REVIEW_PAGE, 45, 30)
    check_ao_totals(errors, A2_PAPER3_REVIEW_PAGE_2, 45, 30)
    check_java_code_blocks(errors)


def check_cdn_versions(errors: list[str]) -> None:
    index = ROOT / "index.html"
    text = index.read_text(encoding="utf-8")
    packages = CDN_RE.findall(text)
    if not packages:
        add_error(errors, index, "no jsDelivr npm dependencies found")
        return

    for package in packages:
        if not EXACT_VERSION_RE.match(package):
            add_error(errors, index, f"CDN dependency is not pinned to an exact version: {package}")


def check_accessibility_baseline(errors: list[str]) -> None:
    index = ROOT / "index.html"
    index_text = index.read_text(encoding="utf-8")
    site_script = ROOT / "assets" / "site.js"
    script_text = site_script.read_text(encoding="utf-8")
    style = ROOT / "assets" / "style.css"
    style_text = style.read_text(encoding="utf-8")

    index_contracts = [
        ('class="skip-link"', "a keyboard skip link"),
        ('href="#main-content"', "a skip-link target"),
    ]
    for needle, description in index_contracts:
        if needle not in index_text:
            add_error(errors, index, f"missing {description}")

    script_contracts = [
        ("main.id = 'main-content'", "a persistent main content target"),
        ("main.tabIndex = -1", "a programmatically focusable main target"),
        ("answer-disclosure", "native answer disclosure processing"),
        ("table-scroll", "focusable horizontal table processing"),
        ("course-hub-return", "course-bounded pagination return"),
        ("prepareChapterOverviews", "chapter overview preparation"),
        ("chapter-overview", "stable chapter overview wrapper"),
        ("overview-topic", "stable overview task-area wrapper"),
    ]
    for needle, description in script_contracts:
        if needle not in script_text:
            add_error(errors, site_script, f"missing {description}")

    style_contracts = [
        (":focus-visible", "visible keyboard focus styling"),
        ("prefers-reduced-motion: reduce", "reduced-motion support"),
        ("@media print", "A4 print styling"),
        ("--muted: #59697d", "contrast-safe muted text"),
        ("--code-bg: #111c2e", "stable code-block background"),
        ("--code-text: #e5edf7", "contrast-safe code-block text"),
        ("--code-punctuation: #cbd5e1", "contrast-safe code punctuation"),
        ("--code-tag: #7dd3fc", "contrast-safe code tags"),
        ("background: var(--code-bg); color: var(--code-text)", "code-block foreground/background pairing"),
        (".markdown-section pre .token.punctuation", "code punctuation override"),
        (".markdown-section pre .token.tag", "code tag override"),
        (".chapter-overview", "chapter overview layout styling"),
        (".overview-topic", "overview task-area styling"),
        (".overview-route", "responsive semantic route styling"),
        ("break-inside: avoid", "print-safe overview task areas"),
    ]
    for needle, description in style_contracts:
        if needle not in style_text:
            add_error(errors, style, f"missing {description}")


def check_mermaid_runtime(errors: list[str]) -> None:
    index = ROOT / "index.html"
    index_text = index.read_text(encoding="utf-8")
    site_script = ROOT / "assets" / "site.js"
    script_text = site_script.read_text(encoding="utf-8")
    style = ROOT / "assets" / "style.css"
    style_text = style.read_text(encoding="utf-8")

    index_contracts = [
        ("startOnLoad: false", "Docsify-owned Mermaid rendering"),
        ("flowchart: { useMaxWidth: false }", "natural-width flowcharts"),
        ("sequence: { useMaxWidth: false }", "natural-width sequence diagrams"),
        ("state: { useMaxWidth: false }", "natural-width state diagrams"),
        ("er: { useMaxWidth: false }", "natural-width ER diagrams"),
    ]
    for needle, description in index_contracts:
        if needle not in index_text:
            add_error(errors, index, f"missing {description}")

    script_contracts = [
        ("tightenMermaidSvg", "defensive Mermaid viewBox tightening"),
        ("contentRatio >= 0.3", "Mermaid empty-canvas threshold"),
        ("excessWidth <= 64 && excessHeight <= 64", "Mermaid excess-space threshold"),
        ("Scrollable diagram:", "accessible overflowing diagram labels"),
        ("prepareMermaidDiagrams", "post-render Mermaid preparation"),
    ]
    for needle, description in script_contracts:
        if needle not in script_text:
            add_error(errors, site_script, f"missing {description}")

    style_contracts = [
        (".mermaid svg", "Mermaid SVG sizing rules"),
        ("overflow-x: auto", "local horizontal diagram scrolling"),
        ("max-width: none", "natural-width Mermaid SVGs"),
        ("margin-inline: auto", "centred compact Mermaid SVGs"),
    ]
    for needle, description in style_contracts:
        if needle not in style_text:
            add_error(errors, style, f"missing {description}")


def main() -> int:
    errors: list[str] = []
    check_chapter_inventory(errors)
    check_headings_and_fences(errors)
    check_chapter_heading_numbering(errors)
    check_references(errors)
    check_navigation(errors)
    check_marked_content(errors)
    check_cdn_versions(errors)
    check_accessibility_baseline(errors)
    check_mermaid_runtime(errors)

    if errors:
        print(f"Site checks failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Site checks passed:")
    print("- 30 expected chapter files are present")
    print("- every student content page has one H1 and consistent heading levels")
    print("- chapter headings contain no page-order numbers, duplicate H2s or bare map references")
    print("- local Markdown/HTML references resolve")
    print("- root navigation is hub-only and course sidebars stay course-only and complete")
    print("- explicit search paths include all student content and exclude coverage.md")
    print("- all 30 chapters satisfy the editorial, identity and 10/20-mark contracts")
    print("- all 21 registered chapter overviews satisfy the title, anchor, four-area and 20-28-unit contracts")
    print("- student pages contain no maintainer headings, raw font tags or legacy keyword labels")
    print("- both IGCSE Paper 1 sets have 6 questions, 75 marks and AO1/AO2/AO3 45/15/15")
    print("- IGCSE Paper 2 chapters satisfy worked-example and exact 10/20-mark contracts")
    print("- both IGCSE Paper 2 reviews have 7 questions, 75 marks and 7 mark schemes")
    print("- both AS Paper 1 sets have 8 questions, 75 marks and AO1/AO2 45/30")
    print("- AS Paper 2 chapters satisfy worked-example and exact 10/20-mark contracts")
    print("- both AS Paper 2 reviews have 7 questions, 75 marks and 7 mark schemes")
    print("- both A2 Paper 3 reviews have 8 questions, 75 marks and AO1/AO2 45/30")
    print("- A2 Paper 4 chapters satisfy worked-example and exact 10/20-mark contracts")
    print("- both A2 Paper 4 reviews have 3 questions, 75 marks and 3 mark schemes")
    print("- every A/B review pair remains below the 65% near-duplicate threshold")
    print("- syllabus-alignment evidence, scope exclusions, exam conditions and objective register pass")
    print("- every A2 fenced Java code block compiles and all Java smoke tests pass")
    print("- jsDelivr npm dependencies use exact versions")
    print("- skip link, keyboard focus, contrast-safe code styling, answer/table/pagination scripting, print and reduced-motion checks pass")
    print("- Mermaid uses one render path, natural SVG sizes and guarded local overflow")
    return 0


if __name__ == "__main__":
    sys.exit(main())
