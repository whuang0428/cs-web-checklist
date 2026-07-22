#!/usr/bin/env python3
"""Run dependency-free structural checks for the Docsify revision site."""

from __future__ import annotations

import re
import sys
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
AS_REVIEW_PAGE = ROOT / "as-9618" / "paper-2-review.md"
AS_REVIEW_PAGE_2 = ROOT / "as-9618" / "paper-2-review-2.md"
A2_PAPER3_REVIEW_PAGE = ROOT / "a2-9618" / "paper-3-review.md"
A2_REVIEW_PAGE = ROOT / "a2-9618" / "paper-4-review.md"
A2_REVIEW_PAGE_2 = ROOT / "a2-9618" / "paper-4-review-2.md"
REVIEW_PAGES = {
    IG_REVIEW_PAGE,
    IG_REVIEW_PAGE_2,
    AS_REVIEW_PAGE,
    AS_REVIEW_PAGE_2,
    A2_PAPER3_REVIEW_PAGE,
    A2_REVIEW_PAGE,
    A2_REVIEW_PAGE_2,
}
CONTENT_PAGES = EXPECTED_CHAPTERS | REVIEW_PAGES
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
            "binary_search",
            "insertion_sort",
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
            "FileNotFoundError",
        ],
    },
}
MARKDOWN_REF_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_REF_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
CDN_RE = re.compile(r"//cdn\.jsdelivr\.net/npm/([^/\"']+)")
EXACT_VERSION_RE = re.compile(r"^[^@]+@\d+\.\d+\.\d+$")
BOLD_MARK_RE = re.compile(r"\*\*\[(\d+)\]\*\*")
PYTHON_FENCE_RE = re.compile(
    r"^```python\s*\n(.*?)^```\s*$",
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


def resolve_reference(source: Path, reference: str) -> Path | None:
    reference = unquote(reference.strip().split()[0].strip("<>\"'"))
    if not reference or reference.startswith(("http://", "https://", "//", "mailto:", "tel:")):
        return None
    if reference.startswith("#/"):
        route = reference[2:].split("?", 1)[0].split("#", 1)[0].strip("/")
        return ROOT / (f"{route}.md" if route else "README.md")
    if reference.startswith("#"):
        return None

    target = reference.split("?", 1)[0].split("#", 1)[0]
    if not target:
        return None
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


def chapter_targets_from_sidebar() -> set[Path]:
    sidebar = ROOT / "_sidebar.md"
    targets = set()
    for reference in MARKDOWN_REF_RE.findall(sidebar.read_text(encoding="utf-8")):
        target = resolve_reference(sidebar, reference)
        if target and target.name.startswith("chapter-"):
            targets.add(target)
    return targets


def chapter_targets_from_home() -> set[Path]:
    home = ROOT / "README.md"
    targets = set()
    for reference in HTML_REF_RE.findall(home.read_text(encoding="utf-8")):
        target = resolve_reference(home, reference)
        if target and target.name.startswith("chapter-"):
            targets.add(target)
    return targets


def check_navigation(errors: list[str]) -> None:
    sidebar_targets = chapter_targets_from_sidebar()
    home_targets = chapter_targets_from_home()
    if sidebar_targets != EXPECTED_CHAPTERS:
        errors.append("_sidebar.md: chapter links do not exactly match the expected 30 chapters")
    if home_targets != EXPECTED_CHAPTERS:
        errors.append("README.md: chapter cards do not exactly match the expected 30 chapters")

    sidebar = ROOT / "_sidebar.md"
    sidebar_references = MARKDOWN_REF_RE.findall(sidebar.read_text(encoding="utf-8"))
    sidebar_all_targets = {
        target
        for reference in sidebar_references
        if (target := resolve_reference(sidebar, reference)) is not None
    }
    for review_page in REVIEW_PAGES:
        if review_page not in sidebar_all_targets:
            add_error(
                errors,
                sidebar,
                f"missing mixed review link for {review_page.parent.name}",
            )

    home = ROOT / "README.md"
    home_references = HTML_REF_RE.findall(home.read_text(encoding="utf-8"))
    home_all_targets = {
        target
        for reference in home_references
        if (target := resolve_reference(home, reference)) is not None
    }
    for review_page in REVIEW_PAGES:
        if review_page not in home_all_targets:
            add_error(
                errors,
                home,
                f"missing mixed review card for {review_page.parent.name}",
            )

    coverage_sources = [ROOT / "README.md", ROOT / "_coverpage.md", ROOT / "_sidebar.md"]
    for source in coverage_sources:
        text = source.read_text(encoding="utf-8")
        references = MARKDOWN_REF_RE.findall(text) + HTML_REF_RE.findall(text)
        if not any("coverage" in reference for reference in references):
            add_error(errors, source, "missing link to coverage.md")


def check_marked_chapter_contracts(
    errors: list[str],
    phase_name: str,
    chapters: dict[Path, dict[str, object]],
) -> None:
    required_sections = [
        "Syllabus Coverage",
        "10 Marks Quick Check",
        "Quick Check Answers",
        "20 Marks Practice",
        "20 Marks Practice Mark Scheme",
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
            re.findall(r"^## \d+\. Worked Example", text, flags=re.MULTILINE)
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
            ("10 Marks Quick Check", 10),
            ("20 Marks Practice", 20),
        ]:
            heading_match = re.search(
                rf"^## \d+\. {re.escape(label)}$",
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


def check_python_code_blocks(errors: list[str]) -> None:
    python_pages = set(PHASE4_CHAPTERS) | {A2_REVIEW_PAGE, A2_REVIEW_PAGE_2}
    for path in sorted(python_pages):
        text = path.read_text(encoding="utf-8")
        blocks = PYTHON_FENCE_RE.findall(text)
        if not blocks:
            add_error(errors, path, "expected at least one fenced Python code block")
            continue
        namespace: dict[str, object] = {"__builtins__": __builtins__}
        syntax_valid = True
        for block_number, code in enumerate(blocks, 1):
            try:
                compiled = compile(
                    code,
                    f"{relative(path)}:python-block-{block_number}",
                    "exec",
                )
                exec(compiled, namespace)
            except SyntaxError as error:
                syntax_valid = False
                add_error(
                    errors,
                    path,
                    f"Python block {block_number} has invalid syntax: "
                    f"line {error.lineno}: {error.msg}",
                )
            except Exception as error:
                syntax_valid = False
                add_error(
                    errors,
                    path,
                    f"Python block {block_number} failed during definition: {error}",
                )

        if not syntax_valid:
            continue

        try:
            if path == ROOT / "a2-9618" / "chapter-19.md":
                values = [7, 3, 5, 2]
                namespace["insertion_sort"](values)
                if values != [2, 3, 5, 7]:
                    raise ValueError("insertion_sort produced an incorrect result")
                if namespace["binary_search"](values, 5) != 2:
                    raise ValueError("binary_search failed to find an existing item")
                linked = namespace["ArrayLinkedList"](2)
                if not linked.insert_front("A") or not linked.insert_front("B"):
                    raise ValueError("ArrayLinkedList could not fill available nodes")
                if linked.insert_front("C") or not linked.delete("A"):
                    raise ValueError("ArrayLinkedList full/delete behaviour is incorrect")
                if not linked.insert_front("C") or linked.find("C") == -1:
                    raise ValueError("ArrayLinkedList did not reuse a freed node")
                queue = namespace["TwoStackQueue"]()
                queue.enqueue("first")
                queue.enqueue("second")
                if queue.dequeue() != "first" or queue.dequeue() != "second":
                    raise ValueError("TwoStackQueue did not preserve FIFO order")
                if namespace["factorial"](5) != 120:
                    raise ValueError("factorial recursion produced an incorrect result")

            elif path == ROOT / "a2-9618" / "chapter-20.md":
                basic = namespace["Activity"]("Basic", 10)
                timed = namespace["TimedActivity"]("Timed", 10, 5)
                booking = namespace["Booking"]("Learner")
                booking.add_activity(basic)
                booking.add_activity(timed)
                if abs(booking.total_fee() - 21.0) > 1e-9:
                    raise ValueError("polymorphic booking total is incorrect")
                table = namespace["HashTable"](7)
                if not table.insert(10, "A") or not table.insert(17, "B"):
                    raise ValueError("HashTable collision insertion failed")
                if table.find(10) != "A" or table.find(17) != "B":
                    raise ValueError("HashTable collision lookup failed")
                reading = namespace["SensorReading"]("S1", -50.0)
                reading.set_reading(150.0)
                if reading.get_reading() != 150.0:
                    raise ValueError("SensorReading boundary update failed")
                try:
                    reading.set_reading(150.1)
                except ValueError:
                    pass
                else:
                    raise ValueError("SensorReading accepted an out-of-range value")

            elif path == A2_REVIEW_PAGE:
                deliveries = [
                    [104, 2, 8.5],
                    [101, 1, 4.0],
                    [109, 3, 12.5],
                    [106, 2, 5.0],
                ]
                namespace["insertion_sort_deliveries"](deliveries)
                if [record[0] for record in deliveries] != [101, 104, 106, 109]:
                    raise ValueError("review insertion sort produced incorrect IDs")
                if namespace["binary_search_delivery"](deliveries, 106) != 2:
                    raise ValueError("review binary search failed")
                if abs(namespace["total_weight"](deliveries, 0) - 30.0) > 1e-9:
                    raise ValueError("review recursive total is incorrect")
                course = namespace["Course"]("C1", "Writing", 20)
                workshop = namespace["Workshop"]("W1", "Robotics", 30, 4)
                booking = namespace["Booking"]("Learner")
                booking.add_course(course)
                booking.add_course(workshop)
                if abs(booking.total_fee() - 68.0) > 1e-9:
                    raise ValueError("review polymorphic booking total is incorrect")
                queue = namespace["CircularQueue"](2)
                if not queue.enqueue("A") or not queue.enqueue("B"):
                    raise ValueError("review queue could not fill")
                if queue.enqueue("C") or queue.dequeue() != "A":
                    raise ValueError("review queue overflow/FIFO behaviour is incorrect")
                if not queue.enqueue("C") or queue.dequeue() != "B":
                    raise ValueError("review circular queue did not wrap correctly")
                patient_table = namespace["PatientTable"](7)
                patient_table.insert(10, "A")
                patient_table.insert(17, "B")
                if patient_table.find(10) != "A" or patient_table.find(17) != "B":
                    raise ValueError("review patient-table collision lookup failed")

            elif path == A2_REVIEW_PAGE_2:
                results = [[1, 42.0], [2, 35.0], [3, 28.0]]
                namespace["bubble_sort_results"](results)
                if [record[0] for record in results] != [3, 2, 1]:
                    raise ValueError("Set B bubble sort produced incorrect order")
                if namespace["linear_search_runner"](results, 2) != [2, 35.0]:
                    raise ValueError("Set B linear search failed")
                if namespace["count_faster"](results, 40.0, 0) != 2:
                    raise ValueError("Set B recursive count failed")
                ticket = namespace["Ticket"]("T1", "Talk", 20)
                group = namespace["GroupTicket"]("G1", "Lab", 10, 4)
                order = namespace["TicketOrder"]("Learner")
                order.add_ticket(ticket)
                order.add_ticket(group)
                if abs(order.total_fee() - 56.0) > 1e-9:
                    raise ValueError("Set B polymorphic ticket total is incorrect")
                tree = namespace["CatalogueTree"]()
                tree.insert(20, "Root")
                tree.insert(10, "Left")
                tree.insert(30, "Right")
                tree.insert(10, "Updated")
                if tree.find(10) != "Updated" or tree.find(99) is not None:
                    raise ValueError("Set B catalogue find/update failed")
                ordered = []
                namespace["in_order"](tree.root, ordered)
                if [record[0] for record in ordered] != [10, 20, 30]:
                    raise ValueError("Set B in-order traversal failed")
        except Exception as error:
            add_error(errors, path, f"Phase 4 runtime smoke test failed: {error}")


def check_marked_content(errors: list[str]) -> None:
    check_marked_chapter_contracts(errors, "Phase 2", PHASE2_CHAPTERS)
    check_marked_chapter_contracts(errors, "Phase 3", PHASE3_CHAPTERS)
    check_marked_chapter_contracts(errors, "Phase 4", PHASE4_CHAPTERS)

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
            "1 hour 30 minutes",
            "Sections 13–20",
            "Question 8 — Further Programming [9]",
            "Total: 75 marks",
        ],
    )
    check_mixed_review(
        errors,
        A2_REVIEW_PAGE,
        3,
        [
            "Original practice paper",
            "2 hours 30 minutes",
            "Python 3 console mode",
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
            "Python 3 console mode",
            "Question 3 — Search Tree Catalogue [24]",
            "75 marks",
        ],
    )
    check_review_independence(errors, IG_REVIEW_PAGE, IG_REVIEW_PAGE_2)
    check_review_independence(errors, AS_REVIEW_PAGE, AS_REVIEW_PAGE_2)
    check_review_independence(errors, A2_REVIEW_PAGE, A2_REVIEW_PAGE_2)
    check_python_code_blocks(errors)


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
    style = ROOT / "assets" / "style.css"
    style_text = style.read_text(encoding="utf-8")

    index_contracts = [
        ('class="skip-link"', "a keyboard skip link"),
        ('href="#main-content"', "a skip-link target"),
        ("main.id = 'main-content'", "a persistent main content target"),
        ("main.tabIndex = -1", "a programmatically focusable main target"),
    ]
    for needle, description in index_contracts:
        if needle not in index_text:
            add_error(errors, index, f"missing {description}")

    style_contracts = [
        (":focus-visible", "visible keyboard focus styling"),
        ("prefers-reduced-motion: reduce", "reduced-motion support"),
    ]
    for needle, description in style_contracts:
        if needle not in style_text:
            add_error(errors, style, f"missing {description}")


def main() -> int:
    errors: list[str] = []
    check_chapter_inventory(errors)
    check_headings_and_fences(errors)
    check_references(errors)
    check_navigation(errors)
    check_marked_content(errors)
    check_cdn_versions(errors)
    check_accessibility_baseline(errors)

    if errors:
        print(f"Site checks failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Site checks passed:")
    print("- 30 expected chapter files are present")
    print("- every chapter and review page has one H1 and consistent heading levels")
    print("- local Markdown/HTML references resolve")
    print("- home and sidebar chapter/review navigation are complete")
    print("- coverage.md is linked from home, cover and sidebar")
    print("- IGCSE Paper 2 chapters satisfy worked-example and exact 10/20-mark contracts")
    print("- both IGCSE Paper 2 reviews have 7 questions, 75 marks and 7 mark schemes")
    print("- AS Paper 2 chapters satisfy worked-example and exact 10/20-mark contracts")
    print("- both AS Paper 2 reviews have 7 questions, 75 marks and 7 mark schemes")
    print("- the A2 Paper 3 review has 8 questions, 75 marks and 8 mark schemes")
    print("- A2 Paper 4 chapters satisfy worked-example and exact 10/20-mark contracts")
    print("- both A2 Paper 4 reviews have 3 questions, 75 marks and 3 mark schemes")
    print("- Set B question bodies remain below the 65% near-duplicate threshold")
    print("- every A2 fenced Python code block compiles and core examples pass smoke tests")
    print("- jsDelivr npm dependencies use exact versions")
    print("- the skip link, keyboard focus and reduced-motion accessibility baseline is present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
