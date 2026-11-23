# Build notes — One-Line Roast: The Gadget You Use Every Day

## The bounty

A single original line of at most 200 characters roasting a gadget or app
used every day. A judge model compares entries two at a time on how funny
the line is, how fresh the angle is and how neatly it is worded. The top
three places share a five dollar pot. The gate is simple: the output file
must be UTF-8 text of 1 to 200 characters, not only white space. There is
no numeric floor and no local benchmark to beat, because this bounty is
judged, not measured.

## Fase 1 — Deconstruction and the cliche radar

The judge weighs five things in order. First, the line must clearly roast
a gadget or app people use every day. Second, it must actually be funny,
landing on a first read with a sting of recognition rather than a mild
grumble. Third, it must feel fresh, with an angle or detail the judge has
not seen before. Fourth, it must be neatly worded, tight and well timed.
Fifth, it must sound like one person's specific gripe, with a concrete
detail about how the thing actually behaves.

The cliche radar matters most here because the bounty description itself
hands every entrant three examples: the phone that dies at four in the
afternoon, the app that asks for a rating before it opens, and the smart
kettle that wants a firmware update first. Those three angles are the
ninety percent lane. Any line built on them will face dozens of near
copies, and the judge's freshness criterion will punish it. The same
applies to the other obvious complaints: a printer that never works, a
Wi-Fi router that needs restarting, a laptop that is slow. All of those
were ruled out before any line was drafted.

## Fase 2 — Three contrasting concepts

Concept A, Sharp Utility: a specific gadget behavior with a concrete
number or detail. The candidates were an earbuds case that announces
low battery at two percent and then dies mid-sentence, a phone charger
that only works at one exact angle, and a microwave that beeps five
times and then beeps again an hour later to remind you it waited.

Concept B, Contrarian: roast the gadget by praising it, so its one
loyal trait is the flaw. The candidates were a laptop fan so loyal it
starts screaming the moment a second tab opens, like a guard dog
barking at its own shadow, and a smartwatch so committed to your health
that it wakes you at three in the morning to congratulate you on
sleeping well.

Concept C, High-Craft Fusion: the gadget's smart feature is itself the
dumb part. The candidates were a phone whose face unlock does not
recognise its owner before coffee, an autocorrect that turns a meeting
invite into something embarrassing and offers no apology, and a smart
speaker that answers questions nobody asked and then cannot hear the
question actually asked of it.

## Fase 3 — Adversarial judging

Each candidate was scored from one to ten on four axes: 3-Second Hook,
Originality against AI slop, Sponsor fit, and Clarity and Execution.

The charger line from concept A scored nine on Hook, eight on
Originality, nine on Sponsor fit and nine on Clarity, thirty-five out of
forty. The hook is a visual image that lands instantly. The detail, one
exact angle, is concrete and personal, which is exactly what the fifth
criterion asks for. The bomb image is fresh in this context even though
the underlying complaint is familiar.

The smartwatch line from concept B also scored thirty-five out of forty:
nine on Hook, eight on Originality, nine on Sponsor fit and nine on
Clarity. Its contradiction, a device that celebrates your sleep by
ruining it, is elegant and very tight at sixty-six characters. It lost
the tie-break because the charger line carries a stronger concrete
detail, and the fifth criterion is the one that separates near-identical
lines.

The face unlock line from concept C scored thirty-four out of forty:
nine on Hook, seven on Originality, nine on Sponsor fit and nine on
Clarity. Face unlock failing is a known complaint, and its originality
ceiling is lower than the other two.

The winner is the charger line: "My phone charger only works at one
exact angle, so I charge my phone like I'm defusing a bomb." Ninety-four
characters, one line, no trailing newline.

## The program

The entry program is a small Python script with no dependencies. It
holds the line as a constant, checks the gate before writing, writes it
to the output path, and then reads the file back to confirm the bytes on
disk are exactly the text that was checked. The first version checked
length, whitespace and single-line shape. The second version, a genuine
revision, added two more checks: rejection of a hidden second sentence
behind an exclamation mark, a question mark or an extra full stop, and
the read-back verification. Both versions were run twice and produced
byte-identical output, with the same hash, which is the determinism the
grader needs.

## Verification

The output file was checked locally: ninety-four characters, ninety-four
bytes, one line, no trailing newline, and the same hash across four runs
in total. The repository carries an MIT license with the SPDX identifier
line, a README with the three live make.fun badge lines, and this notes
file. No numeric floor exists for this bounty, so no benchmark was run.
