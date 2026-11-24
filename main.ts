// Warning Label for Humans: One Line, Big Laugh
// Competition: u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85
// Writes one single-line warning label to <MAKEFUN_OUTPUT_DIR>/entry.txt
// (cap 160 chars). Node 22 stdlib-only.
//
// Draft v1: the "I'm fine" malfunction plus ignored low-battery signals.
// Recognisable, but it ends on the setup ("until shutdown") instead of a
// turn, and most of the line's room goes unused.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

// Revision: keep the label register and the two recognisable behaviours,
// then close with the turn a real label would bury at the end — the care
// requirements are "not included in the box". Final line: 158 of 160
// chars (159 with the trailing newline).
const LINE = "WARNING: Contents may say 'I'm fine' while malfunctioning, ignore all low-battery signals, and require snacks, sleep, and reassurance not included in the box.";

if (LINE.length < 1 || LINE.length > 160 || LINE.trim().length === 0 || LINE.includes("\n")) {
  throw new Error(`Invalid entry line: must be one non-blank line of 1-160 chars, got ${LINE.length} chars.`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.txt"), LINE + "\n", "utf8");
