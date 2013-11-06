from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-mx',
	version=version,
	description="Open Data - Mexico  theme",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Sam Smith',
	author_email='sam.smith@okfn.org',
	url='https://github.com/okfn/ckanext-mx',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.mx'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.mx:PluginClass
	mx=ckanext.nsw.plugin:mxPlugin
	""",
)
