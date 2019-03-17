# -*- coding: utf-8 -*-
import click

from myrandomutils.filemanagement import DeleteDir


@click.group()
def myrandomutils():
    pass


@myrandomutils.group()
def deletecache():
    pass


@deletecache.command()
@click.option('--rootpath', '-r', default=None,
              help="")
def deletecache(rootpath):
    DeleteDir(rootpath).delete_cache()
