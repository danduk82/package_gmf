#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name="package_gmf_geoportal",
    version="1.0",
    description="package_gmf, a c2cgeoportal project",
    author="package_gmf",
    author_email="info@package_gmf.com",
    url="https://www.package_gmf.com/",
    install_requires=["c2cgeoportal_geoportal", "c2cgeoportal_admin",],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={"paste.app_factory": ["main = package_gmf_geoportal:main",], "console_scripts": [],},
)
