from os import environ
import json

if 'VCAP_SERVICES' in environ:
    vcap_services = json.loads(environ['VCAP_SERVICES'])

    if 'newrelic' in vcap_services:
        NEW_RELIC_LICENSE_KEY = vcap_services['newrelic'][0]['credentials']['licenseKey']
        print(NEW_RELIC_LICENSE_KEY)
