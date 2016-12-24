# stevedore/example2/setup.py
from setuptools import setup, find_packages

setup(
    name='stevedore-example',
    version='1.0',

    description='Demonstration package for stevedore',

    url='http://git.openstack.org/cgit/openstack/stevedore',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['example',
              ],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'test_stevedore.study': [
            'field =example.example:FieldList',
        ],
    },

    zip_safe=False,
)
