
# python setup.py build_ext --inplace


from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        "Texture_Map_Generator_v1.pyx",
        # "ccode3dgen_seg.pyx",
        # "ccode3dgen_tex.pyx"
    ], compiler_directives={'language_level': "3"}),
)