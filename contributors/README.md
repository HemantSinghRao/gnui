# This folder

One file per person. Yours is new — you never edit anybody else's, and you
never edit this page.

That is deliberate. If 200 people edited one shared list, GitHub would ask
every single one of you to untangle the clashes by hand. One new file each
means nobody can clash with anybody.

## Your file

**Name it after your GitHub username**, then `.md`:

```
contributors/priyasharma.md
```

Small letters, numbers and hyphens only. No capitals, no spaces, no
underscores.

Not sure what your username is? It is the name in your profile link:
`github.com/`**`priyasharma`**.

## What goes inside it

Copy this and change every line:

```
---
name: Priya Sharma
github: priyasharma
branch: Computer Science
year: 1
building: A bot that tells me when the library actually has free seats
---

Anything you want to say, in one or two sentences.
```

The three dashes at the top and bottom matter. They tell the robot where
your settings stop and your sentences start.

| Line | Required? | What it is |
|------|-----------|------------|
| `name` | yes | What you want to be called on the wall |
| `github` | yes | Your username — **must be identical to the file name** |
| `branch` | yes | Your course, e.g. Computer Science |
| `year` | no | 1, 2, 3… |
| `building` | no | Something you want to build, however small or silly |
| the text below | no | Up to 500 characters |

## The one mistake nearly everybody makes

The file name and the `github:` line have to match **exactly**.

```
contributors/priya-sharma.md   ←  the file name says  priya-sharma
github: priyasharma            ←  but this line says  priyasharma
```

That fails the check called *Username matches the filename*. It is not a big
deal: edit the file, make the two match, commit again, and the check re-runs
by itself.

## A filled-in one

[EXAMPLE-username.md](EXAMPLE-username.md) is a real, valid file. Open it,
tap the pencil to see the raw text, and copy it into your own file.

Step-by-step instructions with the exact taps are in the
[main README](../README.md).
