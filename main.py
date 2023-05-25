import micropip
await micropip.install('pyno')

from pyno import HTML as H
import js 

div = js.document.createElement("div")
div.innerHTML = "<h1>This element was created from Python</h1>"
js.document.body.prepend(div)
div.style.float='right'
div.style.background='white'
div.contentEditable='true'

div.innerHTML = str(H.pre(H.code("""import js
... div = js.document.createElement('div')
... div.style.float='right'
""")))



async def aexec(code):
    exec(
        f'async def __ex(): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__ex']()


from pyodide.http import open_url
url = "https://raw.githubusercontent.com/jVincentl/pyonyx/main/main.py"

content = open_url(url).read()

# exec('async def __ex():\n    ' +content.replace('\n', '\n    ')); await __ex()

print(content)
