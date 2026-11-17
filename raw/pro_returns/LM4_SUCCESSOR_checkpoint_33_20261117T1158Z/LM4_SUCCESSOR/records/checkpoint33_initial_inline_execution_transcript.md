# Exact initial inline Python commands and observed outputs

These are read-only checks and one new-record writer actually executed by
root after the context continuation on 2026-11-17. They are retained here
verbatim rather than represented as mathematical certificate executions.
All three command calls returned actual exit code zero. Shell reads,
clock tools, and complete-source tool outputs remain distinct from
mathematical programs.

## Source identity check

Executed with working directory `/workspace/scratch/a50d05093ca1`:

```python
from pathlib import Path
import hashlib
root=Path('/workspace/scratch/a50d05093ca1/recovered_inputs32/background/expanded')
for rel in ['LM7_PUSH_checkpoint_09/sections/E_cm_character_agent.tex','LM7_PUSH_checkpoint_09/sections/E_genus_one_sewing_agent.tex','referee/REFEREE_B_E61_E65.md']:
    data=(root/rel).read_bytes()
    print(rel,len(data),hashlib.sha256(data).hexdigest())
```

Observed output:

```text
LM7_PUSH_checkpoint_09/sections/E_cm_character_agent.tex 13406 45fb24828a71b3a2444f32b99625a594092732222065515f848bd49e022f15b9
LM7_PUSH_checkpoint_09/sections/E_genus_one_sewing_agent.tex 9847 6957b7565c585852ec94882e3558a738ba34678119b2f14a8fab7dea6ace8925
referee/REFEREE_B_E61_E65.md 33246 0faa565d68df0bdf0d1370dd090529375ccfeb51b22135102a7efab187c06581
```

## In-progress archive size observation

Executed while the sole capture32 producer was still running. This did
not open the ZIP as an archive, verify it, or treat it as complete:

```python
from pathlib import Path
p=Path('/workspace/scratch/a50d05093ca1/LM4_SUCCESSOR_checkpoint_32.zip')
print({'exists':p.exists(),'current_bytes':p.stat().st_size if p.exists() else None})
```

Observed output at approximately11:08:20 UTC:

```text
{'exists': True, 'current_bytes': 475039202}
```

## Actual capture-completion record writer

Executed only after capture11244 returned exit0 and after all three
writers had been explicitly released, before this later transcript:

```python
from pathlib import Path
import json
p=Path('records/checkpoint32_capture_completion_observed.json')
record={'archive':'LM4_SUCCESSOR_checkpoint_32.zip','capture_session':11244,'actual_producer_exit_code':0,'archive_closed_at':'2026-11-17T11:08:46.772422+00:00','exit_observed_at':'2026-11-17T11:09:05+00:00','archive_bytes':494718836,'archive_sha256':'67ad6a36bef8bc98dbf3a6db7426065765022ca95d18434e6bde60d56c24f2c0','logical_entries':9680,'writer_release':'All three agents explicitly released immediately after exit0 and before any archive verifier or save operation.','next_scheduled_at':'2026-11-17T11:49:30+00:00','immutability':'No second archive, repack, mutation, or upload has been performed.'}
with p.open('x') as stream: json.dump(record,stream,indent=2);stream.write('\n')
print(p)
```

Observed output:

```text
records/checkpoint32_capture_completion_observed.json
```

The final sentence in that record describes its writing time. The later
successful upload is separately recorded in
`records/checkpoint32_library_save_observed.json`; the immutable ZIP
contents were not changed by that upload.

## Exact successful upload invocation

```bash
python /workspace/scratch/a50d05093ca1/library_helpers_recovery32/library_upload.py <<'JSON'
{"uploads":[{"local_path":"/workspace/scratch/a50d05093ca1/LM4_SUCCESSOR_checkpoint_32.zip","purpose":"create_library_file","library_artifact_type":"other"}]}
JSON
```

Producer47399 returned actual exit0 and the native write receipt and
successful results object retained in the companion save record. This
was the sole upload of the sole32 archive; no finalize retry occurred.
