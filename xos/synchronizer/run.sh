#!/bin/bash

export XOS_DIR=/opt/xos
python $XOS_DIR/synchronizers/globalxos/globalxos-synchronizer.py -C $XOS_DIR/synchronizers/globalxos/globalxos_synchronizer_config
