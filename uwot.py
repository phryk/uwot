#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Generic value over time thingie. """

import os
import datetime
import click
import peewee

homedir = os.path.expanduser('~')
uwotdir = os.path.join(homedir, '.uwot')
db_path = os.path.join(uwotdir, 'values.db')

db = peewee.SqliteDatabase(db_path)

class Data(peewee.Model):

    date = peewee.DateTimeField(default=datetime.datetime.now)
    value = peewee.IntegerField()


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):

    click.echo("WTF")
    click.secho(str(ctx.invoked_subcommand), fg='cyan')
    if ctx.invoked_subcommand is None:
        collect()


@cli.command()
@click.option('value', prompt="Value", type=int)
def collect(value):

    datapoint = Data()
    datapoint.value = value

    if datapoint.save():
        click.secho("Saved datapoint for %s" % datapoint.date, fg='green')
    else:
        click.secho("Could not save datapoint!", fg='red', bold=True)


@cli.command()
def initdb():

    if not os.path.exists(uwotdir):
        os.mkdir(uwotdir)

    if not os.path.exists(db_path):
        Data.create_table()
        click.secho("Database created!", fg='green')
    else:
        click.secho("Database file %s already exists, move or delete and retry.", fg='red', bold=True)
