# Conference method data: tokens and times

Measured by the rapporteur with `conference_tokens.py` (this folder) from the five participants' transcripts, on
13 November 2026: round 1 at 13:58 UTC, round 2 (final) at 14:12 UTC. All times are UTC, 13 November 2026, from the transcripts' own timestamps.

## What is measured

- **A round** runs from the instruction that opens it for a participant (a message naming the conference and
  "round N") to the instruction that opens the next round.
- **Output tokens**: the sum over the participant's assistant messages in the round, one count per message (its
  last usage line). Output tokens include the model's reasoning, so they exceed the length of the talk.
- **Context**: input + cache-read + cache-creation + output tokens of a usage line, that is, the size of the
  participant's conversation after that message. "At the opening" is the last message before the round's
  instruction; "at the last line" is the round's last message. The difference is what the round added to the
  participant's context: its reading and its writing.
- Input tokens are not summed: each request re-sends the whole conversation, almost all of it from the cache, so a
  sum over requests would count the same context many times. The context column gives the size instead.
- The rapporteur's own tokens are not in these tables.

## Round 1 (talks): closed

| Participant | Agent | Model | Round | Opened (UTC) | Last assistant line (UTC) | Assistant messages | Output tokens | Context at the opening | Context at the last line | State |
|---|---|---|---|---|---|---|---|---|---|---|
| shape_map | a6ef4ff663ce71f74 | claude-fable-5-2 | 1 | 13:33:25.751 | 13:35:28.321 | 3 | 10,422 | 562,113 | 575,408 | closed |
| intake | a5ead5c6fd26104b9 | claude-fable-5-2 | 1 | 13:32:15.818 | 13:38:19.029 | 6 | 33,560 | 567,475 | 607,014 | closed |
| LM7_reviewer | abbb9ceeb78661b2a | claude-fable-5-2 | 1 | 13:32:43.395 | 13:40:37.541 | 13 | 45,444 | 637,193 | 710,283 | closed |
| Derivateurs_expert | a7ca0d5d87ede29ec | claude-fable-5-2 | 1 | 13:35:57.943 | 13:42:46.053 | 7 | 38,133 | 596,279 | 662,073 | closed |
| EXIT_reviewer | aacc5ca1a82daf18b | claude-fable-5-2 | 1 | 13:37:37.978 | 13:50:34.460 | 12 | 67,483 | 612,099 | 708,830 | closed |

- Five participants, **195,042 output tokens** in total.
- Wall time: first invitation 13:32:15, last talk finished 13:50:34: **18 min 19 s**. The participants worked in
  parallel; the longest single talk took 12 min 57 s (EXIT_ONE_TYPE reviewer), the shortest 2 min 3 s (shape-map
  agent).
- Context added by the round, per participant: shape-map 13,295; intake 39,539; LM7 reviewer 73,090; Dérivateurs
  expert 65,794; EXIT_ONE_TYPE reviewer 96,731. Total 288,449.
- All five participants ran on Claude Fable 5.2 (`claude-fable-5-2`). Efforts, from the talks' headers: shape-map
  medium; intake high; LM7 reviewer, Dérivateurs expert and EXIT_ONE_TYPE reviewer max.

### Preparation folded into the talks

Four participants had been asked at 13:30 to write a note building on the new findings. The round-1 invitation
reached them while they were on it, and they folded the note into the talk. The output tokens of that stretch, from
the 13:30 instruction to the invitation:

| Participant | Preparation opened (UTC) | Assistant messages | Output tokens |
|---|---|---|---|
| shape_map | 13:30:40.446 | 3 | 8,773 |
| LM7_reviewer | 13:30:25.476 | 6 | 8,861 |
| Derivateurs_expert | 13:30:30.387 | 1 | 25,959 |
| EXIT_reviewer | 13:30:35.726 | 6 | 33,844 |

- Total **77,437 output tokens**. With them, the talks of round 1 cost 272,479 output tokens.
- The intake agent had no such stretch: its invitation was a new instruction.

## Round 2 (replies): closed

| Participant | Agent | Model | Round | Opened (UTC) | Last assistant line (UTC) | Assistant messages | Output tokens | Context at the opening | Context at the last line | State |
|---|---|---|---|---|---|---|---|---|---|---|
| shape_map | a6ef4ff663ce71f74 | claude-fable-5-2 | 2 | 13:50:54.722 | 13:54:11.369 | 7 | 14,195 | 575,408 | 605,135 | closed |
| intake | a5ead5c6fd26104b9 | claude-fable-5-2 | 2 | 13:51:00.947 | 13:56:19.838 | 6 | 28,835 | 607,014 | 644,015 | closed |
| LM7_reviewer | abbb9ceeb78661b2a | claude-fable-5-2 | 2 | 13:51:03.979 | 13:53:57.257 | 2 | 14,969 | 710,283 | 725,686 | closed |
| Derivateurs_expert | a7ca0d5d87ede29ec | claude-fable-5-2 | 2 | 13:50:57.775 | 13:54:24.951 | 6 | 16,479 | 662,073 | 685,236 | closed |
| EXIT_reviewer | aacc5ca1a82daf18b | claude-fable-5-2 | 2 | 13:51:06.462 | 13:52:42.409 | 3 | 7,584 | 708,830 | 716,889 | closed |

- Final figures, measured at 14:12 UTC after the round was declared complete. They equal the figures of the 13:58
  measurement: the last reply had been written at 13:56:19.
- Five participants, **82,062 output tokens** in total. This includes the five floor questions, which were written
  in the same turns.
- Wall time: 13:50:54 to 13:56:19: **5 min 25 s**. Per participant: EXIT_ONE_TYPE reviewer 1 min 36 s; LM7
  reviewer 2 min 53 s; shape-map agent 3 min 17 s; Dérivateurs expert 3 min 27 s; intake agent 5 min 19 s.
- Context added by the round, per participant: shape-map 29,727; intake 37,001; LM7 reviewer 15,403; Dérivateurs
  expert 23,163; EXIT_ONE_TYPE reviewer 8,059. Total 113,353.
- The LM7 reviewer and the EXIT_ONE_TYPE reviewer were told to write without reading (context above 700K); their
  context grew by their own output and little else.

## Rounds 1 and 2 together

| Participant | Output tokens, round 1 | Output tokens, round 2 | Both | Context at the end of round 2 |
|---|---|---|---|---|
| Shape-map agent | 10,422 | 14,195 | 24,617 | 605,135 |
| Intake agent | 33,560 | 28,835 | 62,395 | 644,015 |
| LM7 reviewer | 45,444 | 14,969 | 60,413 | 725,686 |
| Dérivateurs expert | 38,133 | 16,479 | 54,612 | 685,236 |
| EXIT_ONE_TYPE reviewer | 67,483 | 7,584 | 75,067 | 716,889 |
| All five | 195,042 | 82,062 | 277,104 | |

With the preparation stretch of round 1 (77,437): 354,541 output tokens. Wall time of the two rounds, from the
first invitation to the last reply: 13:32:15 to 13:56:19, 24 min 4 s, of which 20 s lay between the rounds.

## Round 3

Opened at 14:11 UTC for the intake agent, the LM7 reviewer and the EXIT_ONE_TYPE reviewer. The drafter of the joint
statements and the successors that answer floor questions are other agents; their transcripts are not among the
five measured here and have to be added to `conference_tokens.py` for the round-3 figures.

## Context of the participants

The agenda gave the participants' context at the start as 625K for the LM7 reviewer and 540-570K for the others.
Measured at the round-1 invitation: LM7 reviewer 637,193; EXIT_ONE_TYPE reviewer 612,099; Dérivateurs expert
596,279; intake agent 567,475; shape-map agent 562,113. At the end of round 1 two participants were above 700K
(LM7 reviewer 710,283; EXIT_ONE_TYPE reviewer 708,830); in round 2 those two were told to answer from what they
know, without reading.
