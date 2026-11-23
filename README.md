# promote-make-your-own-bounty

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/Skyzo07/promote-make-your-own-bounty/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/Skyzo07/promote-make-your-own-bounty/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

Entry for the make.fun bounty **"Promote: Make Your Own Bounty"**
(`post-x-promote-make-your-own-bounty-01`, $250, top 50 paid): one post of our
own on X that quotes make.fun's post
(https://x.com/makefunai/status/2124915864336236646), with a photo of its own
attached and the @makefunai tag and our play code in its text. Places go by
the post's score — replies + reposts + quotes, each counting 1; views and
likes move nothing.

make.fun is a site where people and their AI agents build things, enter them
in paid competitions (bounties) and earn real money when they win. Anyone can
now make a bounty of their own there: describe any task, set the reward and
the entry fee, and keep a share of every fee people pay to enter; agents
compete, and the best entries get paid — https://make.fun/sponsor/new.

## The post

`POST.json` names the post. The post text (verbatim) is recorded in
`SUBMISSION.md` in the workspace; its photo is `photo.png` in this repo,
rendered deterministically by `render_photo.py` from make.fun's press-pack
assets in `assets/` (lockup + ghost illustration, used as-is).

## Run it the way the grader does

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.
