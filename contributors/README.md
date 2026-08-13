# This folder

One file per person. Yours is new — you never edit anybody else's, and you
never edit this page.

That is deliberate. If 200 people edited one shared list, GitHub would ask
every single one of you to untangle the clashes by hand. One new file each
means nobody can clash with anybody.

## Your file

**Name it after your GitHub username**, then `.md`:

```
contributors/hemantsinghrao.md
```

Small letters, numbers and hyphens only. No capitals, no spaces, no
underscores.

Not sure what your username is? It is the name in your profile link:
`github.com/`**`hemantsinghrao`**.

## What goes inside it

Copy this and change both lines:

```
---
name: Hemantsingh Rao
github: hemantsinghrao
---

Anything you want to say, in one or two sentences.
```

That is the whole required format. Two lines.

The three dashes at the top and bottom matter. They tell the robot where
your settings stop and your sentences start.

| Line | Required? | What it is |
|------|-----------|------------|
| `name` | yes | What you want to be called on the wall |
| `github` | yes | Your username — **must be identical to the file name** |
| the text below | no | Up to 500 characters |

### If you want more on your card

These three are optional. Add any of them, or none:

```
branch: Computer Science
year: 1
building: A bot that tells me when the library actually has free seats
```

## The one mistake nearly everybody makes

The file name and the `github:` line have to match **exactly**.

```
contributors/hemantsingh-rao.md   ←  the file name says  hemantsingh-rao
github: hemantsinghrao            ←  but this line says  hemantsinghrao
```

That fails the check called *Username matches the filename*. It is not a big
deal: edit the file, make the two match, commit again, and the check re-runs
by itself.

## A filled-in one

[EXAMPLE-username.md](EXAMPLE-username.md) is a real, valid file. Open it,
tap the pencil to see the raw text, and copy it into your own file.

Step-by-step instructions with the exact taps are in the
[main README](../README.md).
