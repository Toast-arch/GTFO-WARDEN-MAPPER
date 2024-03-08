from setuptools import setup, find_packages

setup(
    name='gtfo_warden_mapper',
    version='1.1.2',
    author='ARCHI#1757',
    author_email='thiago.pbueno@gmail.com',
    description='',
    license='GNU General Public License v3.0',
    keywords=[],
    url='',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "Pillow==9.3.0",
        "opencv-python==4.6.0.66"
    ],
    classifiers=[
        'Environment :: PC - Any OS',
        'Intended Audience :: Gaming/Speedrunning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)