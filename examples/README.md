# A real CI/CD setup, small enough to read in one sitting

Three files: a page, a function, and a test for that function. Plus one
workflow file that runs the test and — only if it passes — publishes the
page to the internet.

That is all "CI/CD" means. Everything else is scale.

```
examples/
  index.html                       the page
  seats.js                         one function
  seats.test.js                    one test for that function
  .github/workflows/deploy.yml     the robot instructions
```

**CI** = continuous integration = *run the tests every time somebody changes
something*.
**CD** = continuous deployment = *if the tests pass, ship it*.

## Try it on your own machine

You need Node installed (`node --version` should print something).

```
cd examples
node --test
```

You should see three passing tests. There is nothing to install first — the
test runner comes with Node.

## Use it in your own project

1. Copy `.github/workflows/deploy.yml` to `.github/workflows/deploy.yml` at
   the **top** of your own repository.
2. In your repository: **Settings → Pages → Source → GitHub Actions**.
3. Push. Watch the **Actions** tab.

---

# deploy.yml, line by line

YAML is a way of writing settings. Two rules: `key: value`, and
**indentation means "belongs to the thing above"**. Spaces only — a tab
character will break it. That is genuinely most of YAML.

```yaml
name: Test and deploy
```

The name you will see in the Actions tab. Cosmetic. Call it anything.

```yaml
on:
  push:
    branches: [main]
  pull_request:
```

**When to run.** Here: whenever somebody pushes to the `main` branch, and
whenever somebody opens a pull request.

That second one is the valuable half. It means a pull request gets tested
*before* anybody merges it, so broken code never reaches `main` in the first
place.

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

**What this workflow is allowed to do.** GitHub hands every run a temporary
password (a token) that expires when the run ends. These three lines say
what that password unlocks: read the code, write to GitHub Pages, and prove
its own identity to the Pages service.

Anything not listed here is refused. Ask for the least you need — this is
the same instinct as not doing everything as administrator.

```yaml
concurrency:
  group: pages
  cancel-in-progress: true
```

**Do not deploy two versions at once.** If you push twice in ten seconds,
the first run is cancelled and only the newer one continues. Without this,
two runs race, and the older one can win — publishing the *older* code.

```yaml
jobs:
```

Everything below is the list of jobs. A **job** is a fresh, empty computer
that GitHub rents for you, uses, and throws away. Two jobs = two computers,
and by default they run **at the same time**.

```yaml
  test:
    name: Run the tests
    runs-on: ubuntu-latest
```

The first job. `test` is its internal id (used further down), `name` is what
humans see, and `runs-on` picks the machine: a fresh Ubuntu Linux box.

```yaml
    steps:
      - uses: actions/checkout@v4
```

**Steps run in order, top to bottom.** Each `- ` starts a new one.

That fresh computer starts out completely empty — it does not even have your
code on it. `actions/checkout` is a ready-made step, written by GitHub, that
downloads your repository onto it. Nearly every workflow starts with this
line.

`@v4` pins the version, so a future update cannot silently change what your
workflow does at 2am.

```yaml
      - uses: actions/setup-node@v4
        with:
          node-version: "20"
```

Installs Node 20 on that machine. `with:` is how you pass settings into a
ready-made step — like arguments to a function.

Pin the version. "Whatever is newest" is how a project that worked last
month stops working today, with nobody having changed anything.

```yaml
      - run: node --test
```

**This is the actual test run.** `run:` means "type this into the terminal on
that machine".

`node --test` finds every `*.test.js` file and runs it.

Here is the important part: **if that command fails, the job fails, and
everything after it stops.** GitHub knows a command failed because of its
exit code — 0 means fine, anything else means broken. Every command-line
tool in existence follows this convention. A failing `assert` makes Node
exit non-zero, and that is the entire mechanism by which a red ✗ appears on
your pull request.

```yaml
  deploy:
    name: Put it on the internet
    needs: test
```

The second job. **`needs: test` is the entire safety net.** It means: do not
even start this job until the `test` job has finished successfully. Tests
red → nothing deploys → the broken version never reaches the internet.

Delete that one line and you have a system that cheerfully publishes broken
code. It is two words.

```yaml
    if: github.ref == 'refs/heads/main'
```

**Only deploy from the main branch.** Without this, opening a pull request
would publish that pull request's code to your live site. We still want the
tests to run on pull requests — just not the deploy.

`github.ref` is one of many values GitHub gives you about what triggered the
run.

```yaml
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
```

Cosmetic but nice: it makes the finished URL appear as a clickable link in
the Actions tab.

`${{ ... }}` means "put a value in here". This one reads the `page_url`
output of the step whose id is `deployment` — the last step in this file.
Steps hand values to later steps this way.

```yaml
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
```

Remember this is a **different machine** from the test job — it is empty
too, so we check the code out again. Nothing is shared between jobs unless
you explicitly pass it.

`configure-pages` works out the settings for your Pages site.

```yaml
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
```

Packs up the folder to publish. `path: .` means "this whole folder". If your
site is built into `dist/` or `build/`, put that here instead.

```yaml
      - id: deployment
        uses: actions/deploy-pages@v4
```

Publishes it. The site is live seconds later.

`id: deployment` is the label the `url:` line above referred to.

---

## Reading a failed run

**Actions** tab → click the red run → click the red job → click the red
step. The output is the same text you would have seen in your own terminal.

Read from the **top** of the red step, not the bottom. The first error is
usually the real one; everything after it is often knock-on noise.

See [EXAMPLES-WALKTHROUGH.md](../EXAMPLES-WALKTHROUGH.md) for exactly what a
failing run and a passing run look like, side by side.

## Things worth knowing early

- **The machine is fresh every time.** If it works on your laptop but not in
  CI, you almost certainly installed something on your laptop and forgot.
  That is not a bug in CI; that is CI telling you the truth.
- **CI does not check that your tests are any good.** It runs the tests you
  wrote. Zero tests pass instantly and prove nothing.
- **Keep it under a minute if you can.** A five-minute pipeline is a
  pipeline people learn to ignore.
- **This file is code.** Change it in a pull request and review it, same as
  anything else.
