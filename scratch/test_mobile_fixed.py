import subprocess
import time
import urllib.request
import json
import base64
import websockets
import asyncio
import urllib.parse

proc = subprocess.Popen([
    '/usr/bin/google-chrome',
    '--remote-debugging-port=9249',
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--window-size=390,844'
])
time.sleep(2)

async def test():
    uri = 'http://127.0.0.1:9249/json/new?' + urllib.parse.quote('file:///home/sumit/.gemini/antigravity-ide/scratch/BuildTek-Website/index.html')
    req = urllib.request.Request(uri, method='PUT')
    with urllib.request.urlopen(req) as resp:
        tab = json.loads(resp.read().decode('utf-8'))
    ws_url = tab['webSocketDebuggerUrl']

    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        msg_id = 0
        async def send(method, params=None):
            nonlocal msg_id
            msg_id += 1
            await ws.send(json.dumps({'id': msg_id, 'method': method, 'params': params or {}}))
            while True:
                res = json.loads(await ws.recv())
                if res.get('id') == msg_id:
                    return res.get('result', {})

        await send('Page.enable')
        await send('Runtime.enable')
        await send('Emulation.setDeviceMetricsOverride', {
            'width': 390,
            'height': 844,
            'deviceScaleFactor': 2,
            'mobile': True,
            'hasTouch': True
        })
        
        # Wait 1.5s (should load instantly on mobile now)
        await asyncio.sleep(1.5)

        # 1. Capture mobile hero
        shot_hero = await send('Page.captureScreenshot', {'format': 'png'})
        with open('/home/sumit/.gemini/antigravity-ide/brain/2483bdfb-e683-4d78-9820-8ab395113e9d/screenshot_mobile_hero_fixed.png', 'wb') as f:
            f.write(base64.b64decode(shot_hero['data']))
        print('Captured mobile hero')

        # 2. Scroll to past-events and capture
        await send('Runtime.evaluate', {
            'expression': '''
                document.getElementById('past-events').scrollIntoView();
            '''
        })
        await asyncio.sleep(0.5)
        shot_past = await send('Page.captureScreenshot', {'format': 'png'})
        with open('/home/sumit/.gemini/antigravity-ide/brain/2483bdfb-e683-4d78-9820-8ab395113e9d/screenshot_mobile_past_fixed.png', 'wb') as f:
            f.write(base64.b64decode(shot_past['data']))
        print('Captured mobile past events')

        # 3. Scroll to partners and capture
        await send('Runtime.evaluate', {
            'expression': '''
                document.getElementById('partners').scrollIntoView();
            '''
        })
        await asyncio.sleep(0.5)
        shot_partners = await send('Page.captureScreenshot', {'format': 'png'})
        with open('/home/sumit/.gemini/antigravity-ide/brain/2483bdfb-e683-4d78-9820-8ab395113e9d/screenshot_mobile_partners_fixed.png', 'wb') as f:
            f.write(base64.b64decode(shot_partners['data']))
        print('Captured mobile partners & delegates')

        # 4. Scroll to delegate logos and capture
        await send('Runtime.evaluate', {
            'expression': '''
                document.getElementById('ld').scrollIntoView();
            '''
        })
        await asyncio.sleep(0.5)
        shot_delegates = await send('Page.captureScreenshot', {'format': 'png'})
        with open('/home/sumit/.gemini/antigravity-ide/brain/2483bdfb-e683-4d78-9820-8ab395113e9d/screenshot_mobile_delegates_fixed.png', 'wb') as f:
            f.write(base64.b64decode(shot_delegates['data']))
        print('Captured mobile delegates')

try:
    asyncio.run(test())
finally:
    proc.terminate()
