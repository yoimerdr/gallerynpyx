from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

from py2ren import create_config
from py2ren.cli import Args, main as py2ren_main
from py2ren.config.config import dump_config


ROOT = Path(__file__).resolve().parents[1]
MODULE_NAME = "gallerynpyx"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Build the gallerynpyx module into dist/gallerynpyx."
    )
    parser.add_argument(
        "--version",
        default=os.environ.get("MODULE_VERSION"),
        help="Optional release version passed by the workflow.",
    )
    return parser.parse_args()


def build_gallerynpyx():
    source_dir = ROOT / MODULE_NAME
    output_dir = ROOT / "dist" / MODULE_NAME

    if not source_dir.is_dir():
        raise SystemExit(f"Module source directory does not exist: {source_dir}")

    shutil.rmtree(output_dir, ignore_errors=True)

    cfg = create_config(
        source_dir,
        level=-1,
        store_modules=[MODULE_NAME],
        analyze_dependencies=True,
    )

    # py2ren can mangle leading underscores, so we restore the expected names.
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

    dump_config(ROOT, cfg)

    previous_cwd = Path.cwd()
    os.chdir(ROOT)
    try:
        py2ren_main(
            Args(
                f"./{MODULE_NAME}",
                f"./dist/{MODULE_NAME}",
                config=cfg,
            )
        )
    finally:
        os.chdir(previous_cwd)

    for asset_dir_name in ("images", "scripts"):
        asset_dir = ROOT / asset_dir_name
        if asset_dir.exists():
            shutil.copytree(asset_dir, output_dir / asset_dir_name, dirs_exist_ok=True)


def main():
    args = parse_args()

    if args.version:
        print(f"Building {MODULE_NAME} for version {args.version}")
    else:
        print(f"Building {MODULE_NAME}")

    build_gallerynpyx()


if __name__ == "__main__":
    main()
