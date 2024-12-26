from setuptools import setup, find_packages

setup(
    name='task_tracker_cli',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'task_tracker_cli=task_tracker_cli.__main__:main',
        ],
    },
)
