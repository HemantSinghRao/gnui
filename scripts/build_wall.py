#!/usr/bin/env python3
"""Builds docs/index.html - the contributor wall - from contributors/*.md.

Stdlib only. Reads every entry, sorts by name, writes one self-contained
HTML file with no external CSS, JS, fonts or images.

    python3 scripts/build_wall.py
"""

import html
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from validate import frontmatter, is_example  # noqa: E402

UNIVERSITY = "Ganpat University"
REPO = "HemantSinghRao/gnui"

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "contributors"
TARGET = ROOT / "docs" / "index.html"


def load():
    entries = []
    for path in sorted(SOURCE.glob("*.md")):
        relative = f"contributors/{path.name}"
        if is_example(relative):
            continue
        fields, body, error = frontmatter(path.read_text(encoding="utf-8"))
        if error:
            print(f"skipped {relative}: could not read the settings block")
            continue
        if not fields.get("github"):
            print(f"skipped {relative}: no github: line")
            continue
        entries.append(
            {
                "name": fields.get("name") or fields["github"],
                "github": fields["github"],
                "branch": fields.get("branch", ""),
                "year": fields.get("year", ""),
                "building": fields.get("building", ""),
                "note": body or "",
            }
        )
    entries.sort(key=lambda entry: entry["name"].lower())
    return entries


def initials(name):
    parts = [p for p in re.split(r"\s+", name.strip()) if p]
    letters = "".join(p[0] for p in parts[:2])
    return html.escape(letters.upper() or "?")


def card(entry):
    def e(value):
        return html.escape(str(value), quote=True)

    meta = " &middot; ".join(
        bit
        for bit in [
            e(entry["branch"]),
            f"Year {e(entry['year'])}" if entry["year"] else "",
        ]
        if bit
    )
    building = (
        f'<p class="building"><span class="label">Building</span>'
        f'{e(entry["building"])}</p>'
        if entry["building"]
        else ""
    )
    note = f'<p class="note">{e(entry["note"])}</p>' if entry["note"] else ""
    return f"""      <li class="card">
        <div class="head">
          <span class="avatar" aria-hidden="true">{initials(entry["name"])}</span>
          <div>
            <h2>{e(entry["name"])}</h2>
            <a class="handle" href="https://github.com/{e(entry["github"])}" rel="noopener">@{e(entry["github"])}</a>
          </div>
        </div>
        {f'<p class="meta">{meta}</p>' if meta else ""}
        {building}
        {note}
      </li>"""


def render(entries):
    count = len(entries)
    people = "contributor" if count == 1 else "contributors"
    cards = "\n".join(card(entry) for entry in entries) or (
        '      <li class="card empty">Nobody yet. You could be first.</li>'
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contributors &middot; {html.escape(UNIVERSITY)}</title>
<meta name="description" content="Everyone who opened their first pull request at {html.escape(UNIVERSITY)}.">
<style>
  :root {{
    --bg: #fbfbfd;
    --panel: #ffffff;
    --ink: #16181d;
    --muted: #6b7280;
    --line: #e8e8ee;
    --accent: #3b4cca;
    --accent-soft: #eef0ff;
    --shadow: 0 1px 2px rgba(16,18,29,.05), 0 8px 24px rgba(16,18,29,.06);
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #0e1015;
      --panel: #171a21;
      --ink: #f2f3f7;
      --muted: #9aa1ad;
      --line: #262a33;
      --accent: #9aa8ff;
      --accent-soft: #232842;
      --shadow: 0 1px 2px rgba(0,0,0,.4), 0 8px 24px rgba(0,0,0,.35);
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 0 1.25rem 4rem;
    background: var(--bg);
    color: var(--ink);
    font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          "Helvetica Neue", Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
  }}
  header {{
    max-width: 62rem;
    margin: 0 auto;
    padding: 3.5rem 0 2.25rem;
    text-align: center;
  }}
  .count {{
    font-size: clamp(2rem, 8vw, 3.25rem);
    font-weight: 700;
    letter-spacing: -.03em;
    margin: 0;
    line-height: 1.15;
  }}
  .count span {{ color: var(--accent); }}
  .sub {{
    margin: .9rem auto 0;
    max-width: 34rem;
    color: var(--muted);
    font-size: 1.02rem;
  }}
  .cta {{
    display: inline-block;
    margin-top: 1.5rem;
    padding: .7rem 1.25rem;
    border-radius: 999px;
    background: var(--accent-soft);
    color: var(--accent);
    font-weight: 600;
    font-size: .95rem;
    text-decoration: none;
    border: 1px solid var(--line);
  }}
  .cta:hover {{ filter: brightness(.97); }}
  ul.grid {{
    list-style: none;
    max-width: 62rem;
    margin: 0 auto;
    padding: 0;
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 17rem), 1fr));
  }}
  .card {{
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 1.15rem 1.25rem 1.25rem;
    box-shadow: var(--shadow);
  }}
  .card.empty {{ text-align: center; color: var(--muted); }}
  .head {{ display: flex; gap: .8rem; align-items: center; }}
  .avatar {{
    flex: 0 0 auto;
    width: 2.6rem;
    height: 2.6rem;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: var(--accent-soft);
    color: var(--accent);
    font-weight: 700;
    font-size: .9rem;
  }}
  h2 {{
    margin: 0;
    font-size: 1.05rem;
    font-weight: 650;
    letter-spacing: -.01em;
  }}
  .handle {{
    color: var(--accent);
    text-decoration: none;
    font-size: .9rem;
    word-break: break-all;
  }}
  .handle:hover {{ text-decoration: underline; }}
  .meta {{
    margin: .9rem 0 0;
    color: var(--muted);
    font-size: .8rem;
    text-transform: uppercase;
    letter-spacing: .04em;
  }}
  .building {{ margin: .75rem 0 0; font-size: .95rem; }}
  .label {{
    display: block;
    color: var(--muted);
    font-size: .72rem;
    text-transform: uppercase;
    letter-spacing: .07em;
    margin-bottom: .15rem;
  }}
  .note {{
    margin: .75rem 0 0;
    color: var(--muted);
    font-size: .9rem;
    border-top: 1px solid var(--line);
    padding-top: .75rem;
  }}
  footer {{
    max-width: 62rem;
    margin: 3rem auto 0;
    text-align: center;
    color: var(--muted);
    font-size: .85rem;
  }}
  footer a {{ color: var(--muted); }}
</style>
</head>
<body>
  <header>
    <h1 class="count"><span>{count}</span> {people}<br>from {html.escape(UNIVERSITY)}</h1>
    <p class="sub">Everybody here opened their first pull request from a phone,
    in about ten minutes. This page rebuilds itself every time somebody new is
    merged in.</p>
    <a class="cta" href="https://github.com/{REPO}/tree/main/contributors">Add yourself &rarr;</a>
  </header>
  <main>
    <ul class="grid">
{cards}
    </ul>
  </main>
  <footer>
    <p>Built automatically from <a href="https://github.com/{REPO}">github.com/{REPO}</a></p>
  </footer>
</body>
</html>
"""


def main():
    entries = load()
    TARGET.parent.mkdir(exist_ok=True)
    TARGET.write_text(render(entries), encoding="utf-8")
    print(f"wrote {TARGET.relative_to(ROOT)} with {len(entries)} contributors")


if __name__ == "__main__":
    main()
