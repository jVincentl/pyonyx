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


async def aexec(code, **kwargs):
    var_locals = {}
    var_globals = globals().copy()
    args = ", ".join(list(kwargs.keys()))
    exec(f"async def func({args}):\n    " + code.replace("\n", "\n    "), {}, var_locals)
    result = await var_locals["func"](**kwargs)
    try:
        globals().clear()
    finally:
        globals().update(**var_globals)
    return result

from pyodide.http import open_url
url = "https://raw.githubusercontent.com/jVincentl/pyonyx/main/main.py"

content = open_url(url).read()

print(content)
