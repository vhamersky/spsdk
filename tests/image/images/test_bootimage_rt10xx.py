#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2020 NXP
#
# SPDX-License-Identifier: BSD-3-Clause

import pytest

from spsdk.image import BootImgRT


def test_bootimage_rt10xx_basic():
    """Simple test for BootImgRT"""
    img = BootImgRT(0x60000000)
    assert img.info()
    img_data = img.export()
    # test parser returns same result
    assert BootImgRT.parse(img_data).export() == img_data


def test_bootimage_rt10xx_missing_ivt():
    # IVT header not found
    with pytest.raises(ValueError):
        BootImgRT.parse(b'00000000')


def test_bootimage_rt10xx_aead_nonce_len():
    """Test `aead_nonce_len`"""
    assert BootImgRT.aead_nonce_len(0) == 13
    assert BootImgRT.aead_nonce_len(0xFFFF) == 13
    assert BootImgRT.aead_nonce_len(0x10000) == 12
    assert BootImgRT.aead_nonce_len(0xFFFFFF) == 12
    assert BootImgRT.aead_nonce_len(0x1000000) == 11


def test_bootimage_rt10xx_add_encrypted_image():
    """Test add_image with encryption parameters"""
    img = BootImgRT(0x20000000)
    test_app_data = bytes([0]) * 1024
    img.add_image(test_app_data, address=0x20000000, dek_key=b'')
    assert len(img.dek_key) == 16
    # test invalid dek key length
    img = BootImgRT(0x20000000)
    with pytest.raises(ValueError):
        img.add_image(test_app_data, address=0x20000000, dek_key=b'x')
    # test image already added
    with pytest.raises(ValueError):
        img.add_image(test_app_data, address=0x20000000, dek_key=b'0123456789123456')

