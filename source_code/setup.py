from cx_Freeze import setup, Executable
import os

build_exe_options = {"packages": ["time", "os", "copy"]}

setup(name='turing_converter', version='1', description='converter',options = {"build_exe": build_exe_options}, executables=[Executable("__init__.py")])