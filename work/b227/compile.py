import json,re,subprocess,os,sys,hashlib,glob
ENV=re.compile(r'\\begin\{(asy|tikzpicture)\}[\s\S]*?\\end\{\1\}')
def compile_env(env,out):
    body=re.sub(r'^\\begin\{asy\}|\\end\{asy\}$','',env)
    d=os.path.dirname(out) or '.'
    base=os.path.splitext(os.path.basename(out))[0]
    wd=os.path.join('/tmp/asywork',os.path.basename(os.getcwd()))
    src=os.path.join(wd,base+'.asy')
    os.makedirs(wd,exist_ok=True)
    open(src,'w').write('settings.outformat="svg";\nsettings.render=0;\n'+body)
    r=subprocess.run(['asy','-f','svg','-o',os.path.abspath(out[:-4]),src],cwd=wd,capture_output=True,text=True,timeout=120)
    return r.returncode==0 and os.path.exists(out), r.stderr[-800:]
if __name__=='__main__':
    for f in sys.argv[1:]:
        for r in json.load(open(f)):
            for key in ['question','solution']:
                for i,m in enumerate(ENV.finditer(r[key]),1):
                    out=f"svgtest/{r['topic_id']}-q{r['part']:02}-{key}-{i}.svg"
                    ok,err=compile_env(m.group(),out)
                    if not ok: print('FAIL',out,err)
    print('done')
