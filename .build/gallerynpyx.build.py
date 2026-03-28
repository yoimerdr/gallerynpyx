from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from py2ren import create_config
from py2ren.cli import Args, main as py2ren_main
from py2ren.config.config import dump_config


ROOT = Path(__file__).resolve().parents[1]
BUILD_ROOT = Path(__file__).resolve().parent
MODULE_NAME = "gallerynpyx"

if str(BUILD_ROOT) not in sys.path:
    sys.path.insert(0, str(BUILD_ROOT))

from common import copy_gallerynpyx_assets, map_gallerynpyx_config


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
    map_gallerynpyx_config(cfg)

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

    copy_gallerynpyx_assets(ROOT, output_dir)


def main():
    args = parse_args()

    if args.version:
        print(f"Building {MODULE_NAME} for version {args.version}")
    else:
        print(f"Building {MODULE_NAME}")

    build_gallerynpyx()


if __name__ == "__main__":
    main()
