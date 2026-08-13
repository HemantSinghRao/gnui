# gnui — your first pull request

**[See the contributor wall →](https://hemantsinghrao.github.io/gnui/)**

This repository exists for one reason: so everybody at this session leaves
having made a real contribution to a real public project, from the phone in
their hand, in about ten minutes.

Not a practice repository. Not a sandbox that gets deleted afterwards. This
is a public repository on the internet, and what you add today stays on your
GitHub profile — where recruiters, professors and future you can see it.

**What you are going to do:** add one small file about yourself. A robot
checks it. A human merges it. Your name appears on a page anybody can visit.

Nothing you add ever runs as code. It is text, so nothing here can break.

---

## A few words, before the taps

You will meet four bits of jargon. That is all of it.

| Word | What it actually means |
|------|------------------------|
| **repository** (repo) | A folder of files, kept on GitHub. This page is one. |
| **fork** | Your own copy of somebody else's repository. GitHub makes it for you automatically — you do not have to do anything. |
| **commit** | Saving a change, with a note about what you changed. |
| **pull request** (PR) | "Here is my change — please pull it into your project." A polite request, not a demand. |

Two more you will see today:

- **CI** / **checks** — a robot that reads your change and says yes or no.
- **merge** — a maintainer accepting your pull request.

---

## Add yourself in 5 steps (works on your phone)

Do this in your phone's browser. Chrome and Safari both work. You do **not**
need the GitHub app and you do **not** need to install anything.

You need a GitHub account. If you do not have one:
[github.com/signup](https://github.com/signup) — about a minute, and you can
do it right now.

### Step 1 — Open the contributors folder

Tap here: **[contributors/](https://github.com/HemantSinghRao/gnui/tree/main/contributors)**

Make sure you are inside that folder before the next step. The path near the
top should read `gnui / contributors`.

### Step 2 — Tap "Add file", then "Create new file"

The **Add file** button is near the top right. On a narrow phone it may be a
**+** icon.

If you cannot see it, you are probably signed out — tap the ☰ menu, sign in,
then come back to Step 1.

### Step 3 — Name the file after your GitHub username

In the box that says *Name your file...*, type:

```
yourusername.md
```

So if your profile is `github.com/hemantsinghrao`, type `hemantsinghrao.md`.

Three rules for the name:

- small letters, numbers and hyphens only — no capitals, no spaces
- it must end in `.md`
- **no slashes** — a slash makes a folder by accident

### Step 4 — Type your details, then commit

Tap the big empty area and type this, changing both lines to be about you:

```
---
name: Hemantsingh Rao
github: hemantsinghrao
---

Anything you want to say, in a sentence or two.
```

That is everything. Two lines.

The lines of three dashes are not decoration — they tell the robot where
your details stop.

**The `github:` line must be identical to the file name.** This is the one
thing most people get wrong: `hemantsingh-rao.md` with `github: hemantsinghrao`
inside it will fail the check.

Want more on your card? Any of these can go under the `github:` line, and
all of them are optional:

```
branch: Computer Science
year: 1
building: A bot that tells me when the library actually has free seats
```

The sentences underneath the dashes can be up to 500 characters.

Now scroll down, tap the green **Commit changes...** button, then
**Propose changes** in the box that appears.

### Step 5 — Create the pull request

GitHub shows you a page with a green **Create pull request** button. Tap it.
If it asks again on the next screen, tap it again.

Done. That is a pull request.

Within a minute you will see four checks appear:

```
✓ File is in the right place
✓ Formatting is valid
✓ Username matches the filename
✓ No duplicate entry
```

All green? A maintainer merges it, and your card appears on
**[the wall](https://hemantsinghrao.github.io/gnui/)** a moment later.

---

## Something went red

**Good.** Genuinely — this is the most useful thing that can happen to you
today, because now you get to read what a machine says when it disagrees
with you, and fix it.

1. Tap the red ✗.
2. Read the message. It says what is wrong and what to type instead — no
   stack traces, no jargon.
3. Go back to your file, tap the ✏️ pencil, fix it, commit again.
4. The checks re-run by themselves. Nobody has to be asked.

You do **not** need to close the pull request and start again. A pull
request is a conversation, not an exam.

What each check means, and how to fix it, is in
**[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## After today

- **[good-first-issues.md](good-first-issues.md)** — 10 small, real tasks in
  this repository you can pick up this week. Every one is genuinely useful.
- **[examples/](examples/)** — a tiny working project with a test and
  automatic deployment. Every line of the setup is explained. Copy it into
  your own projects.
- **[AI_POLICY.md](AI_POLICY.md)** — yes, you can use AI here. Read this
  first.

Then go and find a `good first issue` label on a project you actually use.
That is the same flow you just did, on somebody else's repository.

---

## Everything else

- [CONTRIBUTING.md](CONTRIBUTING.md) — the flow in more depth
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — how we treat each other
- [AI_POLICY.md](AI_POLICY.md) — using AI here
- [LICENSE](LICENSE) — MIT

## Who runs this

Hemant Singh Rao — Ganpat University.
Questions, ideas, or "my check is red and I don't understand why":
**hemantsingh.rao001@gmail.com**

Being stuck is not embarrassing. Everybody who works in this industry has
been stuck on something more basic than whatever you are stuck on.
