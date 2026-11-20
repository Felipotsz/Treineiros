import re,json,sys
blocks=re.split(r"^===== Q(\d+)\n",open(sys.argv[1]).read(),flags=re.M)
out={}
for i in range(1,len(blocks),2):
    n=int(blocks[i]); 
    if n==0: continue
    alts={}; cur=None
    for l in blocks[i+1].splitlines():
        s=l.strip()
        if re.match(r"^(Texto para|Leia estes poemas|p\d+ (IMG|DRW|N))",s): 
            if cur=="E" and alts.get("E"): cur=None
            continue
        m=re.match(r"^\(?([A-E])\)\s*(.*)$",s)
        if m: cur=m.group(1); alts[cur]=m.group(2); continue
        if cur: alts[cur]=(alts[cur]+" "+s).strip()
    out[n]={k:re.sub(r"(\w)- (\w)",r"\1-\2",v.strip()) for k,v in alts.items()}
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
for n,a in out.items():
    bad = len(a)!=5 or any(len(v)<2 or len(v)>260 for v in a.values())
    if bad: print(n, json.dumps(a,ensure_ascii=False)[:400])
