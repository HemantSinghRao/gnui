# Good first issues

Ten real tasks in this repository. Every one is something that genuinely
needs doing — none of them is homework invented to keep you busy.

**Before you start:** open an issue (or comment on one) saying *"I'd like to
try this"*, so two people don't do the same work. Then work the way you did
in the session: change one thing, one pull request.

Unlike the session, these **do** mean editing existing files. That is fine
now — you are one person, not two hundred.

Difficulty is honest:

- ☕ **Ten minutes** — text only, no code, doable on a phone
- 🔧 **Half an hour** — a small code change, easier on a laptop
- 🌙 **An evening** — you will need to read some code first

---

### 1. ☕ The README does not say what to do if you arrive without a GitHub account

**What:** Add two sentences near the top of the "Add yourself in 5 steps"
section for somebody who has no account yet — how long signing up takes, and
that they need a working email to hand.

**Where:** `README.md`, just under the "Add yourself in 5 steps" heading.

**Done when:** somebody who has never used GitHub could read that section
and know exactly what to do first.

---

### 2. ☕ Write down what a maintainer actually does when a check goes red

**What:** Nothing here explains the *maintainer's* side: how to spot a stuck
pull request, what to comment, when to fix somebody's file for them rather
than explaining it. Write it down.

**Where:** a new file, `MAINTAINING.md`, linked from `README.md`.

**Done when:** a volunteer helping at the next session could read it in two
minutes and be useful.

**Hint:** the useful content is what you watched happen in the room.

---

### 3. 🔧 The wall does not say when it was last updated

**What:** Add a line in the footer of the generated page: "Last updated 12
August 2026". Right now there is no way to tell whether the page is live or
stale.

**Where:** `scripts/build_wall.py`, in `render()`.

**Done when:** `python3 scripts/build_wall.py` produces a page with a date
in the footer.

**Hint:** `datetime.date.today().strftime("%d %B %Y")`. Careful — a date
that changes on every run makes a pointless commit every time the workflow
runs. Ask in the issue how to handle that; it is a genuinely interesting
problem with more than one right answer.

---

### 4. 🔧 The wall's cards have a colour-contrast problem

**What:** The `.meta` and `.note` text uses `--muted` (`#6b7280` on white,
`#9aa1ad` on dark). Check both against WCAG AA (4.5:1 for normal text) and
fix whichever fail, without making the page look flat.

**Where:** the `<style>` block inside `scripts/build_wall.py`.

**Done when:** every text/background pair on the page passes AA, and the
measured ratios are in your pull request description.

**Hint:** [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker/).
Do the dark-mode block too — that is the one people forget.

---

### 5. 🔧 One long unbroken word breaks the card layout

**What:** Somebody will eventually put a 60-character word with no spaces in
`building:`. Today that pushes the card wider than a phone screen.

**Where:** the `<style>` block in `scripts/build_wall.py`.

**Done when:** you can add a test contributor file with an absurd word in
it, rebuild, and the page still does not scroll sideways at 320px wide.

**Hint:** `overflow-wrap: anywhere`. Test at 320px — the narrowest phone
still in real use.

---

### 6. 🔧 There are no tests for the validator

**What:** `scripts/validate.py` is the only thing standing between 200
students and a confusing error message, and nothing tests it. Add tests for
`frontmatter()` — the pure function, and the easiest to test.

**Where:** a new file, `scripts/test_validate.py`.

**Done when:** `python3 -m unittest discover scripts` passes and covers at
least: a valid file, a missing closing `---`, a line with no colon, and a
body over 500 characters.

**Hint:** `unittest` comes with Python. Import `frontmatter` from
`validate`. Do not try to test the git parts — those need a real repository,
and that is a different, harder issue.

---

### 7. 🔧 Nothing checks that `year:` is actually a number

**What:** `year: banana` sails through today and prints "Year banana" on the
wall. Reject it in the *Formatting is valid* check.

**Where:** `check_format()` in `scripts/validate.py`.

**Done when:** `year: banana` fails with a message a first-year would
understand, `year: 1` still passes, and a file with no `year` line at all
still passes — it is optional.

**Hint:** match the tone of the messages already in that file. No jargon, no
regex in the error text, and always tell them what to type instead.

---

### 8. 🌙 There is no way to find yourself among 200 cards

**What:** Add a search box to the wall that filters cards as you type — by
name, username, branch, or what they are building.

**Where:** `scripts/build_wall.py`.

**Done when:** it works on a phone, and — the hard requirement — **the page
still works with JavaScript switched off**. The cards must be in the HTML,
not built by script.

**Hint:** a `<script>` tag inside the generated page is fine; an external
library is not. About 15 lines is enough. Give the input a real `<label>` so
a screen reader announces it.

---

### 9. 🌙 A broken contributor file can only be found by opening every file

**What:** Write `scripts/lint_all.py`, which checks every file in
`contributors/` and prints a summary of anything broken. Useful when
somebody merges a bad file by hand, and useful before a session.

**Where:** a new file, `scripts/lint_all.py`.

**Done when:** it prints one line per broken file, exits with code 1 if
anything is wrong and code 0 if all is well. That exit code is what makes it
usable from CI later.

**Hint:** reuse `frontmatter()` and `is_example()` from `validate.py` —
`build_wall.py` shows you how to import them.

---

### 10. 🌙 The example project has no accessibility check

**What:** `examples/index.html` has a `<label>` on each input and an
`aria-live` output — but nothing checks it stays that way. Add an automated
accessibility check to `examples/.github/workflows/deploy.yml`.

**Where:** `examples/.github/workflows/deploy.yml`, plus whatever the check
needs.

**Done when:** the workflow fails if somebody removes a label, and
`examples/README.md` explains the new lines in the same plain style as the
rest.

**Hint:** `pa11y-ci` is the small option. Keep the job under a minute, and
it must not need any secret.

---

## Not on this list?

Anything that confused you during the session is a valid issue. "I could not
tell whether it had worked" is real feedback and worth an issue of its own.
Open one.
