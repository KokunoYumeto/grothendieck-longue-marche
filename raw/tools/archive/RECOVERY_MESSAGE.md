# Message to paste when a Pro run's execution environment disconnects

(11 Nov 2026. A reply in the same chat; it works for the archive packages and, with the last sentence changed, for
the mathematics prompts.)

```
The execution environment was disconnected. Before anything else, list which of your working files still exist
(page files, progress.log, the inventory, the doubts and notes files) and whether the two uploaded zips are still
there. If the zips are gone, say so and stop; I will upload them again. Otherwise continue from the first scan page
that has no saved page file, under the same rules as before: save each page as soon as it is done, with its inventory
rows and its progress.log line. Do not redo pages that are saved and complete, and do not summarize or skip any. The
task is finished only when every scan page has its file and every inventory row is yes, followed by the research
notes as the prompt specifies.
```

For a mathematics prompt, replace the last two sentences with: "Continue from the first part that is not written
in full. The section 'What the outcome must be' still applies to every item."

## When Pro reports that the workspace is gone and gives nothing (11 Nov 2026: packages 08 and 10)

Paste into the same chat:

```
Do not wait for the workspace and do not ask for the files yet. Write out in this chat, now, as text, every page file you finished, in full, each in its own code block headed by its file name: copy each one from the code you ran to save it. Then give the inventory rows of those scans as CSV, the progress.log lines, and the draft of any page you had not saved yet, with anything unresolved marked \unsure or \illegible in place. Do not summarize and do not describe the checkpoint: write the files out in full. If it does not fit in one answer, stop at the end of a page file and say so; I will reply "continue". After that I will reattach the two archives so that you can recreate the files and continue from the first unfinished scan.
```

Then:
1. The user pastes the chat output into the Claude Code session.
2. Claude rebuilds the files in returns/<PKG>_from_chat/.
3. The user reattaches the scans zip and the context zip in the same chat, so Pro continues from the first
   unfinished scan.

From 11 Nov, every new prompt carries the disconnect clause: if the workspace has not come back after at least 10
minutes of retrying, write the work out in the chat. It is Method step 6 in the archive prompts and item 5 of "What
the outcome must be" in the LM prompts.
