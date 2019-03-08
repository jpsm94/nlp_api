from setuptools import setup, find_packages

setup(
    name='nlp_api',
    version='1.0.0',
    description='NLP RESTful API',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='rest restful api flask swagger openapi flask-restplus nlp spacy',

    packages=find_packages(),

    install_requires=['flask-restplus==0.12.1', 'spacy'],
)
