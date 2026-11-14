"""Run dossier negative controls on an isolated disposable documentation copy."""
from pathlib import Path
import tempfile,shutil,json,importlib.util,contextlib,io
ROOT=Path(__file__).resolve().parents[3]
def main():
    with tempfile.TemporaryDirectory(prefix='nyua-dossier-controls-') as name:
        tmp=Path(name)
        for directory in ['docs','tasks']:
            shutil.copytree(ROOT/directory,tmp/directory,ignore=shutil.ignore_patterns('__pycache__'))
        for p in list(ROOT.glob('*.md'))+list((ROOT/'labs').rglob('*.md')):
            q=tmp/p.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
        h=tmp/'docs/product/AI';p=h/'validate_dossier.py'
        spec=importlib.util.spec_from_file_location('isolated_dossier',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        def run():
            out=io.StringIO()
            with contextlib.redirect_stdout(out):result=m.validate()
            return result,out.getvalue()
        code,out=run()
        if code:raise AssertionError(out)
        cases=[('source hash','requirements.json',lambda x:x.update(source_sha256='0'*64),'Canonical source hash drift'),('cycle','backlog.json',lambda x:x['tasks'][0]['dependencies'].append(x['tasks'][0]['id']),'cycle'),('missing coverage','backlog.json',lambda x:next(t for t in x['tasks'] if t['id'].startswith('V00-'))['requirement_refs'].clear(),'missing coverage'),('invalid acceptance','requirements.json',lambda x:x['records'][0].update(acceptance='OK'),'Invalid acceptance length')]
        for label,file,mutate,expected in cases:
            f=h/file;original=f.read_bytes();x=json.loads(original);mutate(x);f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            code,out=run()
            if code!=1 or expected not in out:raise AssertionError((label,out))
            f.write_bytes(original);print('REJECTED isolated dossier control: '+label)
        if run()[0]:raise AssertionError('Restored isolated copy failed')
        print('PASS: clean/restored dossier and four negative controls; real inputs untouched.')
if __name__=='__main__':main()
