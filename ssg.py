import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    Site.self.source = main(**config).builld()
    Site.self.dest = main(**config).build()


typer.run(main)
