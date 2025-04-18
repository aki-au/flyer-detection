#imports
import setuptools

version = '1.0.0'

long_description = ''
with open('README.md', 'r') as readme :
    for il,line in enumerate(readme.readlines(),start=1) :
        long_description+=line

setupkwargs = dict(
    name='flyerdetection',
    packages=setuptools.find_packages(include=['flyerdetection*']),
    include_package_data=True,
    version=version,
    description='''Python application for detecting and analyzing flyer properties in 
                   laser shock lab high speed video frames''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alakarthika Ulaganathan, Maggie Eminizer',
    url='https://github.com/aki-au/flyer-detection',
    download_url=f'https://github.com/aki-au/flyer-detection/archive/refs/tags/v{version}.tar.gz',
    license='GNU GPLv3',
    entry_points = {
        'console_scripts' : ['FlyerAnalysisStreamProcessor=flyerdetection.flyer_analysis_stream_processor:main',
                            ],
    },
    python_requires='>=3.9',
    install_requires=['imageio>=2.23.0',
                      'matplotlib>=3.6.2',
                      'numpy>=1.24.1',
                      'opencv-python>=4.7.0.68',
                      'openmsistream>=1.2.0',
                      'pandas>=1.5.2',
                      'pytest-shutil>=1.7.0',
                      'scikit-image>=0.19.3',
                      'scipy>=1.10.0',
                     ],
    extras_require = {'dev': ['twine',
                                ],
                        },
    keywords=['data_streaming','stream_processing','materials','data_science'],
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)

setupkwargs["extras_require"]["all"] = sum(setupkwargs["extras_require"].values(), [])

setuptools.setup(**setupkwargs)
