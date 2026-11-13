import asyncio
from playwright.async_api import async_playwright
BONE='#ECE4D4'; RED='#BE121C'; DK='#0a0606'
defs=f'''<defs>
<radialGradient id="moon" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#f4e9dc"/><stop offset=".7" stop-color="#d9c7b4"/><stop offset="1" stop-color="#b9a48f"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#be121c" stop-opacity=".55"/><stop offset="1" stop-color="#be121c" stop-opacity="0"/></radialGradient>
<radialGradient id="wglow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#f4e9dc" stop-opacity=".35"/><stop offset="1" stop-color="#f4e9dc" stop-opacity="0"/></radialGradient>
<linearGradient id="bone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3ece0"/><stop offset="1" stop-color="#b8ab98"/></linearGradient>
<linearGradient id="fadeb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ECE4D4" stop-opacity="1"/><stop offset=".75" stop-color="#ECE4D4" stop-opacity=".9"/><stop offset="1" stop-color="#ECE4D4" stop-opacity="0"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
</defs>'''
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="640" viewBox="0 0 1080 640">{defs}{body}</svg>'
M={}
# FANTASMA com celular "visto"
M['fantasma']=svg(f'''
<circle cx="540" cy="300" r="300" fill="url(#wglow)"/>
<path d="M400 560 Q400 150 540 140 Q680 150 680 560 Q655 520 632 560 Q610 525 586 560 Q563 522 540 560 Q517 522 494 560 Q470 525 447 560 Q424 520 400 560Z" fill="url(#fadeb)"/>
<path d="M412 360 Q340 380 330 330 Q360 340 405 320Z" fill="#ECE4D4" opacity=".95"/>
<path d="M668 360 Q735 400 745 350 Q712 350 676 322Z" fill="#ECE4D4" opacity=".95"/>
<ellipse cx="500" cy="270" rx="22" ry="34" fill="{DK}"/><ellipse cx="580" cy="270" rx="22" ry="34" fill="{DK}"/>
<ellipse cx="540" cy="345" rx="20" ry="30" fill="{DK}"/>
<g transform="translate(722 270) rotate(12)"><rect x="0" y="0" width="74" height="132" rx="12" fill="#111" stroke="#555" stroke-width="3"/>
<rect x="7" y="14" width="60" height="100" rx="4" fill="#1d2a22"/>
<rect x="13" y="54" width="46" height="18" rx="8" fill="#2e4b3a"/>
<text x="16" y="96" font-family="Arial" font-size="13" fill="#53bdeb" font-weight="bold">✓✓ visto</text></g>''')
# MÚMIA
st=''.join(f'<path d="M380 {y} Q540 {y+(18 if i%2 else -14)} 700 {y+(8 if i%2 else 22)}" stroke="#cfc3ad" stroke-width="30" fill="none" opacity="{0.9 if i%2 else 1}"/>' for i,y in enumerate(range(150,620,34)))
st2=''.join(f'<path d="M380 {y} Q540 {y+10} 700 {y-6}" stroke="#8d8270" stroke-width="2" fill="none"/>' for y in range(166,620,34))
M['mumia']=svg(f'''
<circle cx="540" cy="330" r="290" fill="url(#glow)"/>
<clipPath id="cab"><path d="M420 640 L420 300 Q420 120 540 115 Q660 120 660 300 L660 640Z"/></clipPath>
<g clip-path="url(#cab)"><rect x="380" y="100" width="320" height="540" fill="#b8ab94"/>{st}{st2}
<rect x="440" y="250" width="200" height="44" fill="#0a0606"/>
<circle cx="495" cy="272" r="13" fill="{RED}"/><circle cx="585" cy="272" r="13" fill="{RED}"/>
<circle cx="495" cy="272" r="26" fill="url(#glow)"/><circle cx="585" cy="272" r="26" fill="url(#glow)"/></g>

''')
# LOBISOMEM uivando na lua cheia, no rochedo
M['lobisomem']=svg(f'''
<circle cx="590" cy="250" r="235" fill="url(#moon)"/>
<circle cx="520" cy="190" r="30" fill="#c9b6a2" opacity=".6"/><circle cx="700" cy="320" r="46" fill="#c9b6a2" opacity=".5"/><circle cx="650" cy="140" r="16" fill="#c9b6a2" opacity=".6"/>
<path d="M120 640 L300 560 L400 575 L520 545 L660 570 L780 560 L960 640Z" fill="#050303"/>
<path fill="#050303" d="M430 565 Q380 560 372 520 Q370 492 396 488 Q392 512 412 524 Q430 532 440 520
L432 470 Q426 420 452 380 L488 330 Q500 300 512 288 L506 252 L524 226 L540 262
Q556 252 572 246 L632 176 L652 160 Q660 158 656 170 L646 186 L622 214 L612 226 L640 210 Q646 210 642 218 L612 248
Q600 262 594 284 L590 330 Q596 360 598 400 L606 480 L620 548 Q600 556 580 552 L572 480 L556 486 L566 548 Q546 556 520 552 L520 520 Q500 540 470 548 Z"/>
<path d="M520 300 L540 320" stroke="#be121c" stroke-width="0"/>
<circle cx="574" cy="258" r="5" fill="#be121c"/>''')
# CAVEIRA
M['caveira']=svg(f'''
<circle cx="540" cy="320" r="290" fill="url(#glow)"/>
<path d="M410 300 Q410 130 540 128 Q670 130 670 300 Q670 360 632 384 L632 440 Q632 456 616 456 L464 456 Q448 456 448 440 L448 384 Q410 360 410 300Z" fill="url(#bone)"/>
<path d="M455 285 Q465 245 500 245 Q530 250 528 285 Q522 320 488 322 Q455 318 455 285Z" fill="{DK}"/>
<path d="M552 285 Q550 250 580 245 Q615 245 625 285 Q625 318 592 322 Q558 320 552 285Z" fill="{DK}"/>
<circle cx="492" cy="285" r="9" fill="{RED}"/><circle cx="588" cy="285" r="9" fill="{RED}"/>
<path d="M540 335 L522 372 L558 372Z" fill="{DK}"/>
{''.join(f'<rect x="{x}" y="400" width="22" height="44" rx="5" fill="#d8ccb8" stroke="#6d6252" stroke-width="3"/>' for x in range(474,600,26))}
<path d="M600 160 L585 200 L598 222" stroke="#6d6252" stroke-width="3" fill="none"/>
<g stroke="url(#bone)" stroke-width="30" stroke-linecap="round"><line x1="330" y1="480" x2="750" y2="600"/><line x1="750" y1="480" x2="330" y2="600"/></g>
<g fill="#e9e0d0">{''.join(f'<circle cx="{x}" cy="{y}" r="22"/>' for x,y in [(320,470),(316,500),(760,470),(764,500),(320,590),(316,620),(760,590),(764,620)])}</g>''')
# ZUMBI: mão saindo da cova + lápide do perfil
M['zumbi']=svg(f'''
<circle cx="540" cy="360" r="300" fill="url(#glow)"/>
<path d="M600 640 L600 260 Q600 170 720 170 Q840 170 840 260 L840 640Z" fill="#3a3330" stroke="#1a1514" stroke-width="6"/>
<text x="720" y="270" text-anchor="middle" font-family="Georgia" font-size="40" fill="#cfc3ad" font-weight="bold">R.I.P.</text>
<text x="720" y="330" text-anchor="middle" font-family="Georgia" font-size="30" fill="#cfc3ad">Seu perfil</text>
<text x="720" y="385" text-anchor="middle" font-family="Georgia" font-size="22" fill="#a89c88">último post:</text>
<text x="720" y="418" text-anchor="middle" font-family="Georgia" font-size="22" fill="#a89c88">há 47 dias</text>
<path d="M120 640 Q300 560 520 600 Q700 580 960 640Z" fill="#140c0a"/>
<path fill="#7d8f6a" stroke="#2c3326" stroke-width="5" d="M360 610 L372 450 Q366 420 340 400 L300 330 Q292 312 306 308 Q318 306 330 324 L360 372 L352 268 Q350 248 366 248 Q380 248 382 268 L392 352 L398 242 Q400 222 416 222 Q432 224 430 244 L424 352 L440 256 Q444 238 458 240 Q472 244 468 262 L452 360 L474 290 Q480 274 494 278 Q506 284 500 300 L470 420 Q460 450 450 470 L452 610Z"/>
<path d="M330 610 L340 560 L360 590 L380 548 L400 600 L420 560 L440 590 L470 552 L480 610Z" fill="#140c0a"/>''')
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':640})
        for k,v in M.items():
            await pg.set_content(f'<html><body style="margin:0;background:transparent">{v}</body></html>')
            await pg.screenshot(path=f'{k}.png',omit_background=True)
        await b.close()
asyncio.run(main())
