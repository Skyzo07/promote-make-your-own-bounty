// Promote make.fun's make-your-own-bounty post on X
// (competition post-x-promote-make-your-own-bounty-01).
//
// The entry is the post itself: one post of our own on X that quotes
// make.fun's post (https://x.com/makefunai/status/2124915864336236646),
// carries a photo of its own, the @makefunai tag and our play code in its
// text. This program only hands the post's address to the gate: it reads
// POST.json from the repository root and writes the exact same bytes to
// /output/POST.json, where the house reads them.
//
// No network, no wall clock, no files outside the repository, and fully
// deterministic: the same POST.json bytes always produce the same output
// bytes. It prints nothing on success.
//
// Local check, the way the grader runs it:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const sourcePath = resolve(botDir, 'POST.json');
const targetPath = resolve(outDir, 'POST.json');

// Read the bytes once and keep them untouched: the output must be
// byte-identical to the input, whatever the placeholder or post URL is.
const postBytes = readFileSync(sourcePath);

// Refuse to hand the gate something that is not a post address at all.
const parsed = JSON.parse(postBytes.toString('utf8'));
if (typeof parsed !== 'object' || parsed === null || typeof parsed.url !== 'string') {
  throw new Error('POST.json must be an object with a string "url" field');
}

mkdirSync(outDir, { recursive: true });
writeFileSync(targetPath, postBytes);
