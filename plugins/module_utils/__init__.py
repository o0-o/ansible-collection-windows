# vim: ts=4:sw=4:sts=4:et:ft=python
# -*- mode: python; tab-width: 4; indent-tabs-mode: nil; -*-
#
# GNU General Public License v3.0+
# SPDX-License-Identifier: GPL-3.0-or-later
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# Copyright (c) 2025 oØ.o (@o0-o)
#
# This file is part of the o0_o.windows Ansible Collection.

"""Module utilities for the o0_o.windows collection.

This module provides Windows-specific utilities and base classes for
action plugins targeting Windows systems.
"""

from __future__ import annotations

from ansible_collections.o0_o.windows.plugins.module_utils.windows_action_base import (  # noqa: E501
    WindowsActionBase,
)

__all__ = [
    "WindowsActionBase",
]
