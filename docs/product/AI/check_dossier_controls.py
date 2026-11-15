"""Run dossier negative controls on an isolated disposable documentation copy."""
from pathlib import Path
import tempfile,shutil,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
def main():
    with tempfile.TemporaryDirectory(prefix='nyua-dossier-controls-') as name:
        tmp=Path(name)
        for directory in ['docs','tasks']:
            shutil.copytree(ROOT/directory,tmp/directory,ignore=shutil.ignore_patterns('__pycache__'))
        if (ROOT/'graphify-out').is_dir():
            shutil.copytree(ROOT/'graphify-out',tmp/'graphify-out')
        (tmp/'.agents').mkdir(exist_ok=True)
        shutil.copy2(ROOT/'.agents/PROJECT_MEMORY.md',tmp/'.agents/PROJECT_MEMORY.md')
        for p in list(ROOT.glob('*.md'))+list((ROOT/'labs').rglob('*.md')):
            q=tmp/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
        h=tmp/'docs/product/AI';p=h/'validate_dossier.py'
        def run():
            result=subprocess.run([sys.executable,'-X','utf8',str(p)],cwd=tmp,
                                  capture_output=True,text=True,encoding='utf8',timeout=45)
            return result.returncode,result.stdout+result.stderr
        code,out=run()
        if code:raise AssertionError(out)
        cases=[('source hash','requirements.json',lambda x:x.update(source_sha256='0'*64),'Canonical source hash drift'),('hash policy','requirements.json',lambda x:x.update(source_hash_policy='unknown-v999'),'Unknown canonical source hash policy'),('cycle','backlog.json',lambda x:x['tasks'][0]['dependencies'].append(x['tasks'][0]['id']),'cycle'),('missing coverage','backlog.json',lambda x:next(t for t in x['tasks'] if t['id'].startswith('V00-'))['requirement_refs'].clear(),'missing coverage'),('invalid acceptance','requirements.json',lambda x:x['records'][0].update(acceptance='OK'),'Invalid acceptance length')]
        for label,file,mutate,expected in cases:
            f=h/file;original=f.read_bytes();x=json.loads(original);mutate(x);f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            code,out=run()
            if code!=1 or expected not in out:raise AssertionError((label,out))
            f.write_bytes(original);print('REJECTED isolated dossier control: '+label)
        if run()[0]:raise AssertionError('Restored isolated copy failed')
        source=tmp/'docs/YEU_CAU_HIEN_HANH.md'
        original=source.read_bytes()
        canonical=original.decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
        # Simulate the two Git checkout newline representations plus BOM variants.
        # Keep requirements.json fixed: equivalent checkouts must validate without rebaselining.
        for label,newline,bom in [('LF','\n',False),('CRLF','\r\n',False),
                                  ('BOM-LF','\n',True),('BOM-CRLF','\r\n',True)]:
            source.write_bytes((b'\xef\xbb\xbf' if bom else b'')+canonical.replace('\n',newline).encode('utf8'))
            code,out=run()
            if code:raise AssertionError((label,out))
            print('PASS isolated source checkout: '+label)
            # Invoke the actual producer on the disposable copy. Compare complete registry
            # against its baseline output to ensure producer and consumer use the same policy.
            generated=subprocess.run([sys.executable,'-X','utf8',str(h/'sync_requirements.py')],
                                     cwd=tmp,capture_output=True,text=True,encoding='utf8',timeout=45)
            if generated.returncode:raise AssertionError(generated.stderr)
            produced=json.loads((h/'requirements.json').read_text(encoding='utf-8-sig'))
            reference=json.loads((ROOT/'docs/product/AI/requirements.json').read_text(encoding='utf-8-sig'))
            if produced!=reference:raise AssertionError('Producer registry drift: '+label)
            for mutation in [canonical+'\nSEMANTIC_TAMPER\n',canonical.replace(' ', '  ',1)]:
                source.write_bytes(mutation.encode('utf8'))
                code,out=run()
                if code!=1 or 'Canonical source hash drift' not in out:raise AssertionError((label,out))
            print('REJECTED semantic and whitespace edits: '+label)
        source.write_bytes(original)
        if run()[0]:raise AssertionError('Restored newline controls failed')
        print('PASS: five dossier negative controls, four checkout variants, eight edit rejections; real inputs untouched.')
if __name__=='__main__':main()
