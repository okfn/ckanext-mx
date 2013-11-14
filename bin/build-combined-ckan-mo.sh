#!/bin/bash

# Based on:
# https://github.com/open-data/ckanext-canada/blob/master/bin/build-combined-ckan-mo.sh
# https://github.com/formwandler/ckanext-odmetheme/master/bin/build-combined-ckan-mo.sh

HERE=`dirname $0`

msgcat --use-first \
    "$HERE/../ckanext/mx/i18n/es/LC_MESSAGES/ckan.po" \
    "$HERE/../../ckan/i18n/es/LC_MESSAGES/ckan.po" \
    | msgfmt - -o "$HERE/../../ckan/i18n/es/LC_MESSAGES/ckan.mo"
