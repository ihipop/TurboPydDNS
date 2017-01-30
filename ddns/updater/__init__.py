#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017/1/29 20:47
# Project: turboPydDNS
# __author__ = 'ihipop'


# Set default logging handler to avoid "No handler found" warnings.
import logging

from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
