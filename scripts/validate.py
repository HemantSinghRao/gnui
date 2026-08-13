#!/usr/bin/env python3
"""Checks a pull request that adds one file to /contributors/.

Runs on Python 3 with nothing installed - no pip, no YAML library - so the
checks finish in seconds. Student files are read as text and never executed.

Usage:
    python3 scripts/validate.py --check place|format|username|duplicate|info \
        [--base origin/main] [--head HEAD]
"""

import argparse
import re
import subprocess
import sys

FOLDER = "contributors/"
FOLDER_README = "contributors/README.md"
FILENAME_OK = re.compile(r"^[a-z0-9-]+$")
REQUIRED = ("name", "github", "branch")
OPTIONAL = ("year", "building")
MAX_BODY = 500

CHECK_NAMES = {
    "place": "File is in the right place",
    "format": "Formatting is valid",
    "username": "Username matches the filename",
    "duplicate": "No duplicate entry",
}


# ---------------------------------------------------------------- plumbing


def git(*args, allow_fail=False):
    result = subprocess.run(
        ["git", *args], capture_output=True, text=True, check=False
    )
    if result.returncode != 0 and not allow_fail:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def is_example(path):
    """The folder's own README and the EXAMPLE- file are not real entries."""
    name = path.rsplit("/", 1)[-1]
    return path == FOLDER_README or name.startswith("EXAMPLE-")


def passed(check):
    print(f"✓ {CHECK_NAMES[check]}")
    sys.exit(0)


def failed(check, message):
    body = "\n".join("    " + line if line else "" for line in message.splitlines())
    print(f"✗ {CHECK_NAMES[check]}\n\n{body}\n")
    sys.exit(1)


def waiting(check):
    failed(
        check,
        "This check is waiting on the check called\n"
        '"File is in the right place".\n\n'
        "Fix that one first - this check will re-run by itself\n"
        "and will probably go green on its own.",
    )


# ------------------------------------------------------------- the parsing


def frontmatter(text):
    """Split '---\\nkey: value\\n---\\nbody' into (fields, body, error).

    error is a plain-language string, or None when everything parsed.
    """
    lines = text.replace("\r\n", "\n").split("\n")
    while lines and not lines[0].strip():
        lines.pop(0)

    if not lines or lines[0].strip() != "---":
        first = lines[0].strip() if lines else "(the file is empty)"
        return None, None, (
            "The very first line of your file has to be exactly three\n"
            "dashes:\n\n"
            "    ---\n\n"
            "That tells us the settings block is starting. Right now your\n"
            "first line is:\n\n"
            f"    {first}"
        )

    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, None, (
            "Your file starts with three dashes but never closes them.\n\n"
            "You need a second line of exactly three dashes after your\n"
            "last setting, like this:\n\n"
            "    ---\n"
            "    name: Priya Sharma\n"
            "    github: priyasharma\n"
            "    branch: Computer Science\n"
            "    ---\n"
            "    Then whatever you want to say goes here."
        )

    fields = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            return None, None, (
                f"Line {number} of your file is:\n\n"
                f"    {line.strip()}\n\n"
                "Every line between the dashes needs a colon in it, because\n"
                "each one is a label and a value. For example:\n\n"
                "    name: Priya Sharma"
            )
        key, _, value = line.partition(":")
        fields[key.strip().lower()] = value.strip().strip('"').strip("'")

    body = "\n".join(lines[end + 1 :]).strip()
    return fields, body, None


def read_file(ref, path):
    return git("show", f"{ref}:{path}")


# -------------------------------------------------------------- the checks


def changed_files(base, head):
    merge_base = git("merge-base", base, head).strip() or base
    output = git("diff", "--name-status", merge_base, head)
    changes = []
    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        changes.append((parts[0][0], parts[-1]))
    return changes


def check_place(changes):
    """Returns (added path, complaint). Exactly one of the two is set."""
    added = [p for status, p in changes if status == "A"]
    touched = [(s, p) for s, p in changes if s != "A"]

    if touched:
        listing = "\n".join(f"    {p}" for _, p in touched)
        return None, (
            "This pull request changes files that already exist:\n\n"
            f"{listing}\n\n"
            "For this session you only ever ADD one new file of your own.\n"
            "Nothing else in the repository should change - that way\n"
            "nobody's work can clash with anybody else's.\n\n"
            "Easiest fix: close this pull request and start again with\n"
            '"Add file" -> "Create new file" inside the contributors folder.'
        )

    if not added:
        return None, (
            "This pull request does not add any new file.\n\n"
            "You need to create one file at:\n\n"
            "    contributors/your-github-username.md\n\n"
            'Go to the contributors folder, tap "Add file", then\n'
            '"Create new file".'
        )

    if len(added) > 1:
        listing = "\n".join(f"    {p}" for p in added)
        return None, (
            f"This pull request adds {len(added)} files:\n\n"
            f"{listing}\n\n"
            "It has to be exactly one file - the one with your name in it.\n"
            "One file per person is what stops 200 people from clashing\n"
            "with each other.\n\n"
            "How to split it: close this pull request. Then add ONE file and\n"
            "open a pull request for it. If you genuinely need the other\n"
            "file too, add it afterwards in a second pull request."
        )

    path = added[0]

    if not path.startswith(FOLDER):
        return None, (
            "Your file is at:\n\n"
            f"    {path}\n\n"
            "It needs to be inside the contributors folder:\n\n"
            f"    contributors/{path.rsplit('/', 1)[-1]}\n\n"
            "Easiest fix: close this pull request. Open the contributors\n"
            'folder first, and only then tap "Add file".'
        )

    if "/" in path[len(FOLDER) :]:
        return None, (
            "Your file is in a folder inside contributors:\n\n"
            f"    {path}\n\n"
            "It has to sit directly in contributors, with no extra folder:\n\n"
            f"    contributors/{path.rsplit('/', 1)[-1]}\n\n"
            "This usually happens by typing a slash in the file name box.\n"
            "A slash in that box creates a new folder."
        )

    filename = path[len(FOLDER) :]

    if path == FOLDER_README:
        return None, (
            "You have edited the contributors folder's own README.\n\n"
            "That file explains the folder to everyone else - it is not\n"
            "where you add yourself.\n\n"
            "Easiest fix: close this pull request, then create a NEW file\n"
            "called your-github-username.md in the same folder."
        )

    if not filename.endswith(".md"):
        return None, (
            "Your file is called:\n\n"
            f"    {filename}\n\n"
            "It has to end in .md - that means Markdown, which is just\n"
            "text with a bit of formatting.\n\n"
            f"Easiest fix: rename it to  {filename}.md"
        )

    stem = filename[:-3]

    if not stem:
        return None, (
            "Your file is called .md with no name in front of it.\n\n"
            "Name it after your GitHub username, for example:\n\n"
            "    priyasharma.md"
        )

    if not FILENAME_OK.match(stem):
        wrong = sorted({c for c in stem if not FILENAME_OK.match(c)})
        shown = " ".join("a space" if c == " " else f"'{c}'" for c in wrong)
        suggestion = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
        return None, (
            "Your file is called:\n\n"
            f"    {filename}\n\n"
            "File names here can only use small letters, numbers and\n"
            f"hyphens. Yours also contains: {shown}\n\n"
            "Common causes: a capital letter, a space, or an underscore.\n\n"
            f"Easiest fix: rename it to  {suggestion}.md\n"
            "and make the github: line inside it say the same thing."
        )

    return path, None


def check_format(head, path):
    fields, body, error = frontmatter(read_file(head, path))
    if error:
        return error

    missing = [key for key in REQUIRED if not fields.get(key)]
    if missing:
        listing = "\n".join(f"    {key}:" for key in missing)
        one = len(missing) == 1
        return (
            f"Your file is missing {'this line' if one else 'these lines'}:\n\n"
            f"{listing}\n\n"
            "Three lines are required and cannot be left blank:\n\n"
            "    name:    what you want to be called\n"
            "    github:  your GitHub username\n"
            "    branch:  your course, e.g. Computer Science\n\n"
            "year and building are optional - add them if you like.\n\n"
            "Easiest fix: edit the file, add the missing line between the\n"
            "two lines of three dashes, and commit again."
        )

    unknown = [k for k in fields if k not in REQUIRED + OPTIONAL]
    if unknown:
        listing = "\n".join(f"    {key}:" for key in unknown)
        return (
            "Your file has settings we do not recognise:\n\n"
            f"{listing}\n\n"
            "Only these five are allowed:\n\n"
            "    name, github, branch, year, building\n\n"
            "Anything else you want to say goes UNDERNEATH the second\n"
            "line of three dashes, as normal sentences."
        )

    if len(body) > MAX_BODY:
        over = len(body) - MAX_BODY
        return (
            "The text under the dashes is too long.\n\n"
            f"    You wrote:  {len(body)} characters\n"
            f"    Limit is:   {MAX_BODY} characters\n\n"
            f"Easiest fix: cut about {over} characters - roughly "
            f"{max(1, over // 6)} words.\n"
            "One or two sentences is exactly right."
        )

    return None


def check_username(head, path):
    stem = path[len(FOLDER) : -3]
    fields, _, error = frontmatter(read_file(head, path))
    if error:
        return (
            'Fix the check called "Formatting is valid" first - we could\n'
            "not read the settings at the top of your file."
        )

    claimed = fields.get("github", "")
    if claimed == stem:
        return None

    return (
        f"Your file is named  {stem}.md\n"
        f"but inside it says  github: {claimed}\n\n"
        "These have to be identical. Easiest fix: edit the file and change\n"
        f"the github: line to  github: {stem}\n"
        "Then commit again - this check will re-run by itself.\n\n"
        "(If it is the file name that is wrong, you can instead delete this\n"
        f"file and create a new one called  {claimed}.md)"
    )


def check_duplicate(base, head, path):
    stem = path[len(FOLDER) : -3]
    fields, _, _ = frontmatter(read_file(head, path))
    claimed = (fields or {}).get("github") or stem

    # One git call for every existing entry, so 200 files is still instant.
    output = git(
        "grep", "-n", "-E", "^github:", base, "--", FOLDER, allow_fail=True
    )
    for line in output.splitlines():
        # <ref>:<path>:<line number>:github: <value>
        parts = line.split(":", 3)
        if len(parts) < 4:
            continue
        other_path = parts[1]
        value = parts[3].partition(":")[2].strip()
        if is_example(other_path) or other_path == path:
            continue
        if value.lower() == claimed.lower():
            return (
                f"Somebody has already added the username  {claimed}\n\n"
                "It is claimed by this file:\n\n"
                f"    {other_path}\n\n"
                "If that file is yours, you are already on the wall - you can\n"
                "close this pull request and celebrate.\n\n"
                "If it is not yours, somebody has typed your username by\n"
                "mistake. Leave a comment here and a maintainer will fix it."
            )
    return None


def check_info(head, path):
    fields, _, _ = frontmatter(read_file(head, path))
    fields = fields or {}
    print(f"name={fields.get('name', '')}")
    print(f"github={fields.get('github', '')}")
    print(f"building={fields.get('building', '')}")


# ------------------------------------------------------------------ entry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", required=True, choices=list(CHECK_NAMES) + ["info"])
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    path, complaint = check_place(changed_files(args.base, args.head))

    if args.check == "place":
        if complaint:
            failed("place", complaint)
        passed("place")

    if complaint:
        if args.check == "info":
            sys.exit(1)
        waiting(args.check)

    if args.check == "info":
        check_info(args.head, path)
        return

    problem = {
        "format": lambda: check_format(args.head, path),
        "username": lambda: check_username(args.head, path),
        "duplicate": lambda: check_duplicate(args.base, args.head, path),
    }[args.check]()

    if problem:
        failed(args.check, problem)
    passed(args.check)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # never show a student a Python traceback
        print(
            "✗ Something went wrong on our side, not yours.\n\n"
            "    This is a problem with the checking robot, not with your\n"
            "    file. Leave a comment on this pull request and a\n"
            "    maintainer will look at it.\n\n"
            f"    Technical detail for the maintainer: {error}\n"
        )
        sys.exit(1)
