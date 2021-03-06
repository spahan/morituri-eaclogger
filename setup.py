from setuptools import setup, find_packages

setup(
    name="morituri-eaclogger",
    version="0.2.1",
    description="""morituri EAC-style logger""",
    author="superveloman",
    packages=[
        'eaclogger',
        'eaclogger.logger'],
    entry_points="""
  [morituri.logger]
  eac = eaclogger.logger.eac:EacLogger
  """)
