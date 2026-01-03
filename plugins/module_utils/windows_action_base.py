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

"""
Base class for Windows-specific Ansible action plugins.

This module provides a mixin class with utilities for action plugins
targeting Windows systems.
"""

from __future__ import annotations

from ansible_collections.o0_o.utils.plugins.module_utils.typeguard_compat import (  # noqa: E501
    typechecked,
)

try:
    from ansible_collections.o0_o.core.plugins.module_utils import (
        CoreActionBase,
    )
except ImportError as e:
    raise ImportError(
        "o0_o.windows requires o0_o.core. Install the full namespace with: "
        "ansible-galaxy collection install o0_o.core"
    ) from e


WINDOWS_CONNECTIONS = frozenset({"winrm", "psrp"})


class WindowsActionBase(CoreActionBase):
    """
    Base class for Windows-specific Ansible action plugins.

    Extends CoreActionBase with utilities for detecting and working with
    Windows targets.

    Note: @typechecked is applied to methods rather than the class to
    avoid metaclass conflicts when subclasses also inherit from Ansible
    base classes like ActionBase.

    Usage:
        from ansible.plugins.action import ActionBase
        from ansible_collections.o0_o.windows.plugins.module_utils import (
            WindowsActionBase,
        )

        class ActionModule(WindowsActionBase, ActionBase):
            def run(self, tmp=None, task_vars=None):
                if self._is_windows_connection():
                    # Windows-specific logic
                    ...
    """

    @typechecked
    def _is_windows_connection(self) -> bool:
        """Check if the connection is for a Windows target.

        Determines whether the current connection plugin is one that
        targets Windows systems (winrm or psrp).

        :returns bool: True if using a Windows connection plugin
        """
        connection_type = self._get_connection_type()
        return connection_type in WINDOWS_CONNECTIONS
