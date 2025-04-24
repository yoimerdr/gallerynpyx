from py2ren.cli import main, Args
from py2ren import create_config

path = "./gallerynpyx"
cfg = create_config(path, level=-1, store_modules=["gallerynpyx"], analyze_dependencies=True)

main(
    Args(
        "./gallerynpyx",
        "./dist/gallerynpyx",
        config=cfg
    )
)
