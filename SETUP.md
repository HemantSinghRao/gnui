# Setup — what to do on github.com after pushing

For you, not the students. Fifteen minutes, once. Do it at least a day
before the session, then run the rehearsal at the bottom.

Everything is at
**https://github.com/HemantSinghRao/gnui** → **Settings**.

---

## 1. Make the repository public

**Settings → General → Danger Zone → Change repository visibility →
Make public**

Type the repository name to confirm.

Why it must be public: private repositories do not let outside people fork
or open pull requests, and GitHub Pages needs a paid plan on a private repo.
Public also means the students' contributions show on their profiles — which
is the entire emotional payoff of the session.

---

## 2. Turn Actions on, and give them permission to write

**Settings → Actions → General**

- **Actions permissions** → *Allow all actions and reusable workflows*
- **Fork pull request workflows from outside collaborators** →
  the default is **Require approval for first-time contributors**, and it
  will stop 200 students' checks from running until you click each one.
  **Change it to *Require approval for first-time contributors who are new
  to GitHub*, or turn approval off for the session.**

  🔴 **This is the single most common way a session like this stalls.** Get
  it wrong and every check sits grey saying "waiting for approval" while 200
  people stare at their phones. Test it with a throwaway account.

- **Workflow permissions** → *Read and write permissions*
  (the wall workflow commits `docs/index.html` back to `main`)
- Tick **Allow GitHub Actions to create and approve pull requests** — not
  needed today, harmless later.

**Save.**

---

## 3. Turn on Pages, from /docs

**Settings → Pages**

- **Source** → *Deploy from a branch*
- **Branch** → `main`, folder → **`/docs`**
- **Save**

The wall is live at **https://hemantsinghrao.github.io/gnui/** about a
minute later.

Note the lowercase URL — GitHub lowercases the username in Pages addresses
even though the repository is `HemantSinghRao/gnui`.

> The example project in `examples/` uses the *other* kind of Pages setup
> (Source → GitHub Actions). Do not switch this repository to that — it
> would stop the `/docs` wall from publishing. The example is for students
> to copy into their own repositories.

---

## 4. Protect main so nothing merges red

**Settings → Rules → Rulesets → New ruleset → New branch ruleset**

- **Name:** `main`
- **Enforcement status:** **Active** ← easy to leave on "Evaluate" by
  mistake, which enforces nothing
- **Target branches** → *Add target* → *Include default branch*

Tick these rules:

- ☑️ **Require a pull request before merging**
  - Required approvals: **0** — you are merging your own students' work all
    session and cannot approve 200 pull requests yourself
  - ☑️ *Dismiss stale pull request approvals when new commits are pushed*
- ☑️ **Require status checks to pass**
  - *Require branches to be up to date before merging* → **leave OFF**. With
    200 pull requests landing in an hour, it would force every student to
    update their branch after every merge. It would end the session.
  - Add these four checks by name — type each and pick it from the list:

    ```
    File is in the right place
    Formatting is valid
    Username matches the filename
    No duplicate entry
    ```

    ⚠️ GitHub only offers a check in that dropdown **after it has run at
    least once**. So do the rehearsal in step 6 first, then come back here
    and add them.

- ☑️ **Block force pushes**

**Create.**

Leave **Do not allow bypassing the above settings** unticked, so you can
force a merge if something goes wrong live.

---

## 5. Add the label the issues use

**Issues → Labels → New label**

- Name: `good first issue` (exactly this — it is the convention every
  project uses, and search engines index it)
- Colour: `#7057ff`

GitHub often creates this one for you. Check before adding a duplicate.

Then, when you have a spare evening, open the ten tasks in
[good-first-issues.md](good-first-issues.md) as real issues, using
**Issues → New issue → Good first issue**. Students can only claim an issue
that exists.

---

## 6. Rehearse it, from a different account

Do not skip this. Borrow a friend's account or make a throwaway one — it
must **not** have write access, or you will be testing the wrong path
entirely.

From a phone, signed in as that account:

1. Open `contributors/`, add `throwawayname.md`, commit, open the pull
   request.
2. Four checks should appear and go green in **under a minute**.
3. The welcome comment should appear.
4. Merge it. The *Build the wall* workflow runs.
5. `https://hemantsinghrao.github.io/gnui/` shows the new card.

Then rehearse the failure, because you will be demoing it live:

6. New pull request, file named `mismatch-test.md`, but `github:
   mismatchtest` inside.
7. *Username matches the filename* goes red. Read that message on a phone
   screen — it is exactly what 200 people will read.
8. Fix the file, commit again, watch it go green with nobody asking it to.

Delete the throwaway files afterwards, or leave them — they are proof it
works.

---

## During the session

**Merging:** open the Pull requests tab, sort by oldest, merge anything with
four green ticks. "Squash and merge" keeps history tidy; plain "Merge" is
one tap fewer. Either is fine.

**Speed:** each merge to `main` triggers a wall rebuild. Rapid merges cancel
each other's rebuilds by design, and the last one includes everybody. If the
wall looks behind, wait for the run in the Actions tab, then refresh.

**If the wall breaks:** **Actions → Build the wall → Run workflow** rebuilds
it from scratch from every file in `contributors/`.

**If Actions stops entirely** (outage, quota, anything): merge anyway. The
checks are a teaching device, not a gate you cannot lift. Everything in
`contributors/` is text, so nothing dangerous can land.

---

## The QR code for your slide

Point it at the contributors folder, not the repository home — that drops
people one tap from "Add file".

Just want the image? Open this and save it:

```
https://api.qrserver.com/v1/create-qr-code/?size=1000x1000&margin=20&data=https%3A%2F%2Fgithub.com%2FHemantSinghRao%2Fgnui%2Ftree%2Fmain%2Fcontributors
```

Prefer to generate it locally (no third-party service, sharper on a
projector):

```
brew install qrencode && qrencode -s 20 -m 2 -o qr.png 'https://github.com/HemantSinghRao/gnui/tree/main/contributors'
```

Put the URL on the slide in readable text underneath as well. Some phones
refuse to scan a projector, and somebody always sits behind a pillar.

**Scan it yourself, from the back of the actual room, before the session.**
