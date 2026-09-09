from pathlib import Path
import re
p=Path("index.html")
s=p.read_text(encoding="utf-8")
checks={
"ten distinct slots rendered": "for(let i=0;i<10;i++)" in s,
"quantity includes zero and ten": "buildTargets=[0,1,3,5,7,10]" in s,
"number bonds include 0+10 and 5+5": "bondStarts=[0,1,2,5,7,8,10]" in s,
"worked 7+3 example": "Watch 7 + 3" in s and "7 + 3 = 10" in s,
"at least six story records": len(re.findall(r"\{text:'",s)) >= 6,
"9 minus 4 story": "9 blocks" in s and "a:9,b:4,op:'-',ans:5" in s,
"two scaffold levels": "setScaffold(1)" in s and "setScaffold(2)" in s,
"read aloud starts off": "speechOn=false" in s and "Read-aloud: off" in s,
"reduced motion support": "prefers-reduced-motion:reduce" in s,
"no remote scripts": not re.search(r"<script[^>]+src=",s,re.I),
"no fetch/xhr": "fetch(" not in s and "XMLHttpRequest" not in s,
"story model bounded 0..10": "storyModelCount<10" in s and "Math.max(0,storyModelCount-1)" in s,
}
bad=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(("PASS" if v else "FAIL"),"-",k)
print(f"\n{len(checks)-len(bad)}/{len(checks)} checks passed")
raise SystemExit(1 if bad else 0)
