# -*- coding: utf-8 -*-
import click

from myrandomutils.filemanagement import DeleteDir


@click.group()
def myrandomutils():
    pass


@myrandomutils.command()
@click.option('--rootpath', '-r', default=None,
              help="Choose a rootpath to be walked for deleting __pycache_ directories.")
def deletecache(rootpath):
    DeleteDir(rootpath).delete_cache()
