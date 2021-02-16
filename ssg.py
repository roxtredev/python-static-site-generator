from . import bar
import typer

#updated
from ssg.site import Site

def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    Site(**config).build()

typer.run(main)