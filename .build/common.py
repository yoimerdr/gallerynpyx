from __future__ import annotations

import shutil


GALLERYNPYX_ASSET_DIRS = ("images", "scripts")
GALLERYNPYX_EXTRA_FILES = ("README.md", "LICENSE")


def map_gallerynpyx_config(cfg):
    """
    Restores the expected module names in the generated py2ren config.
    """
    try:
        internal = cfg.modules["_internal"]
    except KeyError:
        internal = None

    if internal is not None:
        internal._name = "_internal"

        try:
            events = internal.modules["_events.py"]
        except KeyError:
            events = None

        if events is not None:
            events._name = "_events"

    return cfg


def copy_gallerynpyx_assets(root, output_dir):
    """
    Copies gallerynpyx runtime assets and project metadata into the build output.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    for asset_dir_name in GALLERYNPYX_ASSET_DIRS:
        asset_dir = root / asset_dir_name
        if asset_dir.exists():
            shutil.copytree(asset_dir, output_dir / asset_dir_name, dirs_exist_ok=True)

    for file_name in GALLERYNPYX_EXTRA_FILES:
        source = root / file_name
        if source.is_file():
            shutil.copy2(source, output_dir / source.name)
