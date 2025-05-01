import pathlib
import shutil
from py2ren import create_config
from py2ren.cli import main, Args
from py2ren.config.config import dump_config

# checking paths
root = pathlib.Path(__file__).parent
path = root.joinpath("gallerynpyx")
out = root.joinpath("dist", path.name)

shutil.rmtree(out, ignore_errors=True)

# Init config
cfg = create_config(path, level=-1, store_modules=["gallerynpyx"], analyze_dependencies=True)

## Internal module name checking. Exists an unexpected behavior with underscore names
internal = cfg.modules["_internal"]
internal._name = "_internal"

events = internal.modules["_events.py"]
events._name = "_events"

# Build
dump_config(root, cfg)
main(
    Args(
        "./gallerynpyx",
        "./dist/gallerynpyx",
        config=cfg
    )
)

# copy files
shutil.copytree(root.joinpath("images"), out.joinpath("images"), dirs_exist_ok=True)
shutil.copytree(root.joinpath("scripts"), out.joinpath("scripts"), dirs_exist_ok=True)
