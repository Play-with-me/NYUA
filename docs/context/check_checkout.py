"""Verify context freshness on committed Git LF blobs and a CRLF checkout copy.

Only runs the documentation check/query tools; never builds/runs product source.
"""
from pathlib import Path
import io
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]


def verify(revision='HEAD'):
    archive = subprocess.run(['git','archive','--format=zip',revision], cwd=ROOT,
                             check=True,capture_output=True,timeout=30).stdout
    with tempfile.TemporaryDirectory(prefix='nyua-clean-checkout-') as temporary:
        checkout = Path(temporary)
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            for entry in bundle.infolist():
                target = (checkout / entry.filename).resolve()
                if not target.is_relative_to(checkout.resolve()):
                    raise ValueError('Archive path escapes temporary checkout')
            bundle.extractall(checkout)
        script = checkout/'docs/context/context_nav.py'

        def check(expected=0):
            result = subprocess.run([sys.executable,str(script),'check'],cwd=checkout,
                                    capture_output=True,text=True,timeout=30)
            if result.returncode != expected:
                raise AssertionError((result.returncode,result.stdout,result.stderr))
            if expected == 2 and 'STALE' not in result.stderr:
                raise AssertionError(result.stderr)

        check()
        print('PASS: clean git archive LF source/map/measurement fingerprints')
        manifest=json.loads((checkout/'graphify-out/manifest.json').read_text(encoding='utf-8'))
        paths=set(manifest['sources']) | set(manifest['outputs']) | {
            'graphify-out/manifest.json','graphify-out/MEASUREMENTS.json',
            'graphify-out/measurements-manifest.json'}
        for name in paths:
            path=checkout/name
            text=path.read_text(encoding='utf-8-sig')
            path.write_bytes(text.replace('\n','\r\n').encode('utf-8'))
        check()
        print('PASS: same committed files converted to CRLF remain fresh')
        result=subprocess.run([sys.executable,str(script),'task','P10-03',
                               '--out',str(checkout/'probe-context.json')],cwd=checkout,
                              capture_output=True,text=True,timeout=30)
        if result.returncode:
            raise AssertionError(result.stderr)
        for name in ['docs/product/AI/SRS.md',
                     'labs/policy-native/PolicyLab.Core/ReadCoordinator.cs',
                     'graphify-out/MEASUREMENTS.json']:
            path=checkout/name
            original=path.read_bytes()
            path.write_bytes(original+b'\r\n ')
            check(expected=2)
            path.write_bytes(original)
            check()
            print('REJECTED content edit (restored): '+name)
        print('PASS: checkout query works; LF/CRLF portability does not bypass content integrity')


if __name__=='__main__':
    verify(sys.argv[1] if len(sys.argv)>1 else 'HEAD')
