# Walkthrough: a red run, then a green one

For narrating live. Two runs of the same project — one broken, one fixed —
in the order the audience sees them.

Everything below is real output from `examples/`. To reproduce it on the
projector, `cd examples` and break `seats.js` as described.

---

## Act 1 — somebody breaks it

The change. One character:

```diff
 export function freeSeats(total, taken) {
   ...
-  return total - taken;
+  return total + taken;
 }
```

It is not obviously wrong. It reads fine. The page even still shows a
number.

They commit it and open a pull request.

### What appears on the pull request, in order

**0–5 seconds** — a yellow dot. GitHub is finding a machine.

```
🟡  Test and deploy / Run the tests            Queued
    Test and deploy / Put it on the internet   —
```

**~10 seconds** — the test job is running. The deploy job has not started,
and will not, until it knows.

**~25 seconds:**

```
❌  Test and deploy / Run the tests            Failed in 22s
⏭️  Test and deploy / Put it on the internet   Skipped
```

> **Say this out loud:** the second line is the point of the whole exercise.
> Nothing was published. The live site is still the working version. The
> broken code got precisely as far as a pull request.

### Clicking into the red one

```
✖ counts the seats nobody is sitting in (2.4ms)
  AssertionError [ERR_ASSERTION]: Expected values to be strictly equal:

  217 !== 23

      at TestContext.<anonymous> (file:///home/runner/work/.../seats.test.js:8:10)

✖ a full library has no free seats (0.9ms)
  AssertionError [ERR_ASSERTION]: Expected values to be strictly equal:

  240 !== 0

✔ refuses impossible numbers instead of quietly lying (1.1ms)

ℹ tests 3
ℹ pass 1
ℹ fail 2
Error: Process completed with exit code 1.
```

Four things worth pointing at:

1. **`217 !== 23`** — the test says what it wanted and what it got. It does
   not just say "error". It says which number, which is far more useful.
2. **The file and line number**, `seats.test.js:8`. That is where to start
   reading.
3. **`exit code 1`** — the actual mechanism. A non-zero exit code means "I
   failed". That is how GitHub knows, and it is why `needs: test` held the
   deploy back. There is no magic in it.
4. **One test still passed.** The third one only checks that bad input is
   refused, and the guards at the top of the function were untouched. A
   green test does not mean the code is right — it means the one thing that
   test checks is still true.

---

## Act 2 — they fix it

Same pull request. They change the `+` back to a `-` and commit again.

**Nobody asks for the checks to re-run.** The push does it.

```
🟡  Test and deploy / Run the tests            In progress
```

**~25 seconds:**

```
✅  Test and deploy / Run the tests            Passed in 21s
✅  Test and deploy / Put it on the internet   Passed in 18s
        → https://username.github.io/repo/
```

Inside the green test job:

```
✔ counts the seats nobody is sitting in (2.1ms)
✔ a full library has no free seats (0.4ms)
✔ refuses impossible numbers instead of quietly lying (0.9ms)

ℹ tests 3
ℹ pass 3
ℹ fail 0
```

The deploy job started **only because** the test job went green, and only
because this landed on `main`. The URL at the bottom is live before you have
finished reading the log.

---

## The difference, in one table

| | Test fails | Test passes |
|---|---|---|
| Test job | ❌ red, exit code 1 | ✅ green, exit code 0 |
| Deploy job | ⏭️ **never starts** | ✅ runs |
| The live site | untouched, still working | updated |
| Who had to notice | nobody — it is automatic | nobody |
| Time from push to knowing | about 25 seconds | about 45 seconds |

---

## Lines worth saying while it runs

- "Nobody ran that. They pushed a commit, and a machine somewhere decided
  the code was wrong."
- "The deploy did not fail. It was **skipped**. That is a much better
  outcome — the broken version never existed on the internet."
- "This is the same shape as the four checks on your own pull request today.
  Different robot, same idea: something reads your change before a human
  does."
- "This entire safety net is one line: `needs: test`."
- "One test still passed while the code was broken. Tests do not prove code
  is right. They prove the specific things somebody thought to check are
  still true."

## If you want to demo it live rather than read it

```
cd examples
node --test                      # 3 passing

# break it:  return total + taken;
node --test                      # 2 failing
echo $?                          # prints 1 — this is what CI looks at

# fix it back
node --test && echo "CI would deploy now"
```

That last line is the whole idea of CD in one shell command: `&&` means
"only if the thing before me succeeded".
