const {chromium}=require('playwright');const http=require('http');const fs=require('fs');const path=require('path');
const root=__dirname;
const srv=http.createServer((q,r)=>{const f=path.join(root,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return;}
r.writeHead(200,{'Content-Type':f.endsWith('.js')?'text/javascript':'text/html'});r.end(d);});}).listen(8765,async()=>{
const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:1400,height:1100},deviceScaleFactor:+(process.argv[2]||1)});
p.on('console',m=>console.log('console',m.text()));p.on('pageerror',e=>console.log('err',e.message));
await p.goto('http://localhost:8765/index.html');await p.waitForSelector('body[data-done]',{timeout:60000});
await p.screenshot({path:process.argv[3]||'axo.png',clip:{x:0,y:0,width:1400,height:1100}});await b.close();srv.close();});
