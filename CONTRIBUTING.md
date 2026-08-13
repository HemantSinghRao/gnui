# Contributing

Everything here works on a phone. There is no terminal, no `git` command, no
software to install. If you are on a laptop it works the same way — the
buttons are just further apart.

- [The flow, in detail](#the-flow-in-detail)
- [What each check means when it goes red](#what-each-check-means-when-it-goes-red)
- [What to contribute after this session](#what-to-contribute-after-this-session)

---

## The flow, in detail

### What is actually happening

You do not have permission to change this repository. Almost nobody does —
that is normal, and it is the point. So GitHub does this instead:

1. You start editing → GitHub silently makes **your own copy** (a *fork*)
   under your account.
2. Your change is saved to your copy (a *commit*).
3. You ask for your change to be pulled into the original (a *pull
   request*).
4. A robot checks it. A human merges it.

You never have to think about steps 1 and 2 on a phone — GitHub does them
when you tap the buttons. Understanding that this is what happened, though,
is most of what people mean by "knowing git".

### The taps

1. Open **[contributors/](https://github.com/HemantSinghRao/gnui/tree/main/contributors)**.
   Check the path at the top says `gnui / contributors` — this matters,
   because "Add file" adds the file to whichever folder you are looking at.
2. **Add file** → **Create new file**.
3. File name: `yourusername.md` — small letters, numbers, hyphens; no
   capitals; no spaces; no slashes.
4. Paste the template below, edit every line.
5. **Commit changes...** → **Propose changes**.
6. **Create pull request** → **Create pull request** again.

### The template

```
---
name: Hemantsingh Rao
github: hemantsinghrao
---

Anything you want to say, in one or two sentences.
```

| Line | Required | Notes |
|------|----------|-------|
| `name` | yes | Any name you want on the wall |
| `github` | yes | **Identical to the file name**, minus `.md` |
| `branch` | no | Your course |
| `year` | no | A number |
| `building` | no | Anything, however small |
| free text | no | 500 characters maximum |

Two required lines. The other three put more on your card if you want them:

```
---
name: Hemantsingh Rao
github: hemantsinghrao
branch: Computer Science
year: 1
building: A bot that tells me when the library actually has free seats
---
```

Nothing else is allowed between the dashes. If you want to say more, say it
underneath them.

### The rules, and why they exist

**One new file per person, never an edit to a shared file.**
If 200 people edited one shared list, every one of you would be asked to
untangle the clashes by hand, and this session would turn into an hour of
merge conflicts. A new file each means your change cannot possibly collide
with anybody else's. Real projects use this trick more often than you would
think.

**Only one file per pull request.**
Because a pull request should be one idea. It is the difference between "add
Hemant" and "add Hemant and also change 14 unrelated things", and reviewers
will love you for it for the rest of your career.

**Do not change any other file.**
For today only. From next week, changing other files is exactly what
[good-first-issues.md](good-first-issues.md) is for.

---

## What each check means when it goes red

The checks take under a minute. When one fails, tap the red ✗, then
**Details** for the full message. Every failure message tells you what to
type. None of them require anybody's help.

Then fix your file (✏️ pencil → edit → commit) and **the checks re-run by
themselves**. You never need to close a pull request and start again.

### ✗ File is in the right place

One of these:

- Your file is not inside `contributors/` — you probably tapped "Add file"
  from the repository home page instead of from inside the folder.
- Your file name has a slash in it, which quietly made a new folder.
- It does not end in `.md`.
- The name has a capital letter, a space or an underscore in it.
- You added two files, or changed a file that already existed.

The message names your file and tells you what to rename it to. If the file
is in the wrong folder, the quickest route on a phone is: close the pull
request, go back to Step 1, and create it in the right place. It takes
thirty seconds the second time.

### ✗ Formatting is valid

Nearly always one of:

- The first line is not exactly `---`
- There is no closing `---`
- A required line (`name` or `github`) is missing or blank
- A line between the dashes has no `:` in it
- Your free text is over 500 characters

The message says which one, and what the line should look like.

### ✗ Username matches the filename

The famous one. Your file name and the `github:` line inside it disagree:

```
contributors/hemantsingh-rao.md    ← file name:  hemantsingh-rao
github: hemantsinghrao             ← inside it:  hemantsinghrao
```

Change the `github:` line to match the file name. One edit, one commit,
done.

This check exists because it is the same class of mistake that breaks real
software: two places that must agree, and nobody checked that they did. Now
a robot checks for you.

### ✗ No duplicate entry

Somebody already has that username on the wall.

If it was you — you are already in. Close the pull request and go and look
at the wall.

If it was not you, somebody typed your username by mistake. Leave a comment;
a maintainer will sort it out.

### Nothing appears at all

Checks take a few seconds to start. Pull down to refresh. If there is still
nothing after two minutes, leave a comment on your pull request — that is a
maintainer problem, not yours.

---

## What to contribute after this session

You are now somebody who has opened a pull request. The second one is much
easier than the first.

**Here, this week:** [good-first-issues.md](good-first-issues.md) has ten
real tasks — improve the wording of a check, fix a colour-contrast problem
on the wall, add a test. Comment on one to claim it so two people don't do
the same work.

**Everywhere else:** open source projects tag beginner-friendly work with a
label, almost always called **`good first issue`**. It is a convention, not
a rule, but it is close to universal.

Find them:

- On any repository: **Issues** tab → **Labels** → `good first issue`
- Across all of GitHub, search:
  `label:"good first issue" is:open is:issue language:python`
  (swap the language for whatever you are learning)
- [goodfirstissue.dev](https://goodfirstissue.dev) and
  [firstcontributions.github.io](https://firstcontributions.github.io) list
  them for you

**How to pick one that will not waste your evening:**

- The project has had a commit in the last month. Dead projects never merge
  anything.
- The issue has no assignee and no pull request already linked to it.
- You understand what "done" means after reading it once. If you cannot
  tell, it is not a good first issue, whatever the label says.
- Comment before you start: *"I'd like to try this — is it still open?"*
  Nobody minds this. Everybody minds two people doing the same work.

**A useful thing to know:** improving documentation counts. Every project
has instructions that were true two years ago. Fixing them is a real
contribution, it gets merged faster than code, and maintainers are quietly
delighted by it.

Please read [AI_POLICY.md](AI_POLICY.md) before you use AI on any of this.
Short version: use it, and understand what it gave you.
