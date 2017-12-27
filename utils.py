#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date, timedelta
from random import randrange

def random_date(min_date, max_date):
    d = max_date - min_date
    delta = randrange(d.days)
    return min_date + timedelta(days=delta)
