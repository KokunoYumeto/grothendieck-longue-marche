# Doubt marks DM01_1_001-160: Alexander Grothendieck's papers, Montpellier archive, cote 1, scans 1-160

You are settling **2684 doubt marks** on 142 scan pages of `1.pdf` in the Montpellier archive of Alexander
Grothendieck: "Analyse fonctionnelle : notes manuscrites (s.d.), lettre (1953).". Each mark is a place where the first transcription of the page said it was not sure:
`\unsure{reading}` (1765 marks), `\unsure{reading|alternative}` (775 marks) or `\illegible{n}`
(144 marks). The first transcription is a diplomatic LaTeX reading (scans 3-36, 38-42, 44-46, 48-50 by GPT-6 Astra (ChatGPT Pro mode); scans 51-105, 107-122, 124-140, 142-150 by GPT-6.2 Astra at reasoning effort max in ChatGPT Work); these readings are careful,
and on our tests such readings made about 1 to 3 errors per 100 words. Its doubt marks are
where its errors are most likely: in our Pro second passes, 44 % of all corrections fell on such a mark. Settling these
marks from the ink, cheaply and in bulk, leaves the later readings of the archive free to look for the errors no mark
points at.

**The task: decide every listed mark from the ink.** For each mark, the ink shows one of the readings, or another
reading, or it does not settle it. Record which, with what you saw. Do not change anything else on the pages; if you
see another error, list it (`other_errors.tsv`) and leave the page as it is.

## The attachments

- `DM01_1_001-160_scans.zip`: one image per page, `1_scanNNN.jpg`, the scan as the archive's PDF holds it (its native
  resolution, 1668x2150 pixels), contrast-enhanced and sharpened. Zoom into it yourself as deep as a place
  needs: a tight crop scaled up to a few thousand pixels across, with the contrast raised where the ink is faint, is
  what settles small writing.
- `DM01_1_001-160_texts.zip`:
  - `pages/1_scanNNN.tex`: the transcription of each page as it stands now, with its marks;
  - `MARKS.tsv`: every mark, in page order, with its id (`M0001` ...), its scan, its kind, the mark as written, and
    the LaTeX around it;
  - `hua/hua_1_scanNNN.tex`: Michel Hua's transcription of the same page (another AI reading, made in the
    Commutator project with Claude models, in its own macros; on our checks it errs more often than ours, about 1.5 to
    8 errors per 100 words, and it leaves gaps). Use it to see what another reader made of a place; the ink decides;
  - `PREAMBLE.tex`: the macros of the transcription.

Unzip them in your sandbox. Look at the images yourself. Reading software (OCR, a PDF text layer, any text-recognition
library) is not a substitute for looking and must not be used.

## You design the workflow

You have full editorial freedom over how to do this: the order of the marks, how deep to zoom, when to crop several
marks at once, how to use your sub-agents (for example, independent readings of the hard marks, or a check of a
sample of your own decisions), what to look at in Hua's text, and when to change any of it. Change the workflow as you
learn the hand and the kinds of marks. Two facts to plan with:
- an image kept in a reader's context is read again at every later step, so work in a way that looks at each image
  once where you can and keeps old images out of the readers' contexts;
- many marks are the same kind of doubt repeated (a letter form, an accent, an index): once a kind is settled on
  several clear cases, it can be decided faster on the rest, each still checked in its own ink.

**Record the workflow as you go**, in `WORKFLOW.md`:
1. the workflow as you first set it up, and why;
2. every change, with its time (UTC), what you changed, why, and its measured effect (marks decided per hour before
   and after, crops per mark, how many marks the change settled);
3. what worked and what did not, for our next prompts of this kind.

Also write `PATTERNS.md`: the first reader's recurring kinds of doubt and of error that you found (for example a letter
form it reads two ways, an accent it misses, an index it mistakes), each with the marks that show it and how the ink
settles it. These patterns let us check the rest of the archive by script.

## What to return

One zip file, `DM01_1_001-160.zip`, offered as the only download. It holds:

1. `decisions.tsv`, one row per mark, in the order of `MARKS.tsv`, with the columns `id`, `scan`, `decision`
   (`first` = the first reading of the mark; `alternative` = its other reading; `other` = another reading;
   `undecided` = the ink does not settle it), `reading` (the reading the ink shows, as it is to stand in the LaTeX:
   without the mark where the ink settles it, with a narrowed `\unsure{...}` where it does not), `what the ink shows`
   (the strokes you saw), `crop` (the crop you decided it on, as pixel coordinates, or `page` if the page view
   settled it) and `confidence` (`high`, `medium` or `low`).
2. `pages/1_scanNNN.tex`: each page with your decisions put in, and nothing else changed.
3. `WORKFLOW.md` and `PATTERNS.md` (above).
4. `other_errors.tsv`: errors you saw that are not at a mark (scan, place, the reading, what the ink shows); none of them
   is changed on the pages.
5. `CHECK_EVENTS.tsv`: for every statement, record its check events in CHECK_EVENTS.tsv: statement id, date, who (model,
   effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and
   rechecked in this run / carried as background without fault found / refuted, with the refined statement's id),
   outcome. Here a statement is a decided mark: its row in `decisions.tsv` is checked in its own ink.
6. `progress.log`: the start time (UTC) as its first line, then `scan NNN done <current UTC time>` as each page's
   marks are decided.

## Method

1. Before the first mark, write the current time (UTC) as the first line of `progress.log`.
2. Decide every mark of a page before you go to the next page, in page order, and append `scan NNN done <time>`.
3. Read the first page as slowly as the last: the marks decided fastest are where wrong decisions cluster.
4. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `DM01_1_001-160_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no
   other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint holds every
   deliverable written so far and everything that documents the work (`decisions.tsv`, the page files, `WORKFLOW.md`,
   `PATTERNS.md`, `other_errors.tsv`, `CHECK_EVENTS.tsv`, `progress.log`, scripts), so that a new session can continue
   from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and the
   texts: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only.
   Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it.
   Checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost.
5. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
   intervals for as long as this session lasts, without writing recovery text into the chat. When the environment
   is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo
   what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead:
   the work reaches us only through checkpoint ZIPs and the final ZIP.
6. **The final package.** When every mark is decided, write `DM01_1_001-160.zip` with everything above and offer it as the only
   download.

This task is long by design: 2684 marks, each decided in its own ink and recorded. Work through all of it completely;
do not stop at a sample or a plan, and do not ask whether to continue. Ignore any clock.
