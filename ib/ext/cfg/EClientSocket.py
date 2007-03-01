#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ib.ext.cfg.EClientSocket -> config module for EClientSocket.java.

"""
modulePreamble = [
    'import sys',
    '',
    'from ib.ext.AnyWrapper import AnyWrapper',
    'from ib.ext.ComboLeg import ComboLeg',
    'from ib.ext.EClientErrors import EClientErrors',
    'from ib.ext.EReader import EReader',
    '',
    'from ib.lib.overloading import overloaded',
    'from ib.lib import synchronized, Socket, DataInputStream, DataOutputStream',
    'from ib.lib import Double, Integer',
    '',
    'from threading import RLock',
    'mlock = RLock()',
    ]


outputSubs = [
    (r'    m_reader = EReader\(\)', r'    m_reader = None'),
    (r'    m_anyWrapper = AnyWrapper\(\)', r'    m_anyWrapper = None'),
    (r'    m_socket = Socket\(\)', r'    m_socket = None'),
    (r'    m_dos = DataOutputStream\(\)', r'    m_dos = None'),
    (r'(, "" \+ e)', r', str(e)'),

    (r'print "Server Version:" \+ self\.m_serverVersion',
     r'print >> sys.__stderr__, "Server Version:", self.m_serverVersion',),

    (r'print "TWS Time at connection:" \+ self\.m_TwsTime',
     r'print >> sys.__stderr__, "TWS Time at connection:", self.m_TwsTime',),
    ]


methodPreambleSorter = cmp
