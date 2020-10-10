from setuptools import setup

meta = {}
with open('sphinx_code_tabs/__init__.py', 'rb') as f:
    try:
        exec(f.read(), meta, meta)
    except ImportError:     # ignore missing dependencies at setup time
        pass                # and return dunder-globals anyway!


setup(
    name='sphinx_code_tabs',
    version=meta['__version__'],
)
