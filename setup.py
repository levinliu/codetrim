from setuptools import setup


PACKAGE_NAME = "codetrim"
VERSION = "1.1" 
AUTHOR = "levinliu"

REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)

with open('test-requirements.txt') as f:
    TESTS_REQUIRES = f.readlines()

setup(name=PACKAGE_NAME,
    version=VERSION,
    description="Python Code Trim",
    url="https://github.com/levinliu/codetrim",
    author=AUTHOR,
    author_email="",
    license="N/A",
    install_requires=REQUIRES,
    tests_require=TESTS_REQUIRES,
    keywords=["CodeTrim"],
    packages=['codetrim'
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
    ]
)
      
      
      
