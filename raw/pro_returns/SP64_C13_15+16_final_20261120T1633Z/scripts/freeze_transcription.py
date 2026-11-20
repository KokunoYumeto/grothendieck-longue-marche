"""Record and verify the primary reader's final transcription SHA-256 values."""
import argparse
import hashlib
import re
from workflow import WORK, PREFIX, ORDER, now, log


def paths():
    return [WORK / 'pages' / f'{cote}_scan{scan}.tex' for cote, scan in ORDER] + [WORK / f'{PREFIX}_transcription.tex']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['freeze', 'verify'])
    args = parser.parse_args()
    progress = (WORK / 'progress.log').read_text()
    files = paths()
    assert len(files) == 26 and all(p.is_file() for p in files)
    if args.action == 'freeze':
        assert not re.search(r'^transcription frozen ', progress, re.M), 'Transcription already frozen'
        log(f'transcription frozen {now()}')
        for path in files:
            log(f'frozen sha256 {digest(path)} {path.relative_to(WORK).as_posix()}')
        print('Frozen 25 page files and the combined transcription; SHA-256 values recorded in progress.log.')
    else:
        matches = re.findall(r'^frozen sha256 ([0-9a-f]{64}) (.+)$', progress, re.M)
        expected = {name: value for value, name in matches}
        names = {p.relative_to(WORK).as_posix() for p in files}
        assert len(matches) == len(expected) == 26 and set(expected) == names
        changed = [p.relative_to(WORK).as_posix() for p in files if digest(p) != expected[p.relative_to(WORK).as_posix()]]
        assert not changed, f'Frozen bytes changed: {changed}'
        log(f'final frozen-transcription verification {now()}: all 25 page SHA-256 values and the combined-transcription SHA-256 are unchanged from the recorded freeze')
        print('Verified all 26 frozen transcription hashes unchanged.')


if __name__ == '__main__':
    main()
