#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2020 NXP
#
# SPDX-License-Identifier: BSD-3-Clause
"""Module for crypto operations (certificate and key management).

There is functionality included:

1. for the key management:

- generating RSA private key (size and exponent as parameter)
- generating RSA public key
- saving RSA private key to the file
- saving RSA publice key to the file

2. for certificate management:

- generating the x.509 certificate
- validating of a certificate
- validating of a chain of certificates
- returning public key from the given certificate
- converting a certificate into bytes
- saving a certificate into file

3. for general purpose:

- loading the public key from file
- loading the private key from file
- loading the x.509 certificate from file
"""
from cryptography import x509
from cryptography.exceptions import *
from cryptography.hazmat.backends import *
from cryptography.hazmat.backends.interfaces import *
from cryptography.hazmat.backends.openssl.rsa import *
from cryptography.hazmat.primitives import *
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import *
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.asymmetric.rsa import *
from cryptography.hazmat.primitives.serialization import *
from cryptography.x509 import *
from cryptography.x509.oid import *
from cryptography.x509.base import *

from .certificate_management import *
from .keys_management import *
from .loaders import (_get_encoding_type, generic_load, load_certificate,
                      load_private_key, load_public_key)
