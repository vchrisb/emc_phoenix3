#!/bin/sh

#New Relic
export NEW_RELIC_LICENSE_KEY="$(python $HOME/scripts/newrelic_license.py)"
echo "added environment variable NEW_RELIC_LICENSE_KEY with value: $NEW_RELIC_LICENSE_KEY"
