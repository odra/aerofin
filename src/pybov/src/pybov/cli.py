import os
import sys

import click

from . import errors, types, helpers
from . import __version__ as pkg_version


@click.group
def cli() -> None:
    pass


@click.command
def version() -> None:
    """
    Shows project version.
    """
    click.echo(f'v{pkg_version}')


@click.command
@click.argument('path', type=str)
@click.argument('dest', type=str)
def parse(path: str, dest: str) -> None:
    """
    Parses an archive file from `path` and saves the output to `dest`
    which must be a folder.
    """
    if not os.path.exists(path):
        raise errors.PyBovError(f'Path: "{path}" not found')

    if not os.path.exists(dest):
        raise errors.PyBovError(f'Dest: "{dest}" not found')

    with open(path, 'r') as f:
        lines = f.readlines()

    click.echo('Storing header file...')
    header = types.Header.from_str(lines[0])
    helpers.write_file(f'{dest}/header.json', types.as_json(header))
    click.echo('Header file stored.')

    click.echo('Storing footer file...')
    footer = types.Footer.from_str(lines[-1])
    helpers.write_file(f'{dest}/footer.json', types.as_json(footer))
    click.echo('Header footer stored.')

    click.echo('Storing records (may take a while')
    counter = 0
    for line in lines[1:-1]:
        print(counter)
        record = types.Record.from_str(line.replace('\n', ''))
        helpers.write_file(f'{dest}/record-{counter}.json', types.as_json(record))
        counter += 1
    click.echo('Records stored.')


cli.add_command(version)
cli.add_command(parse)


def run() -> None:
    try:
        cli()
    except errors.PyBovError as e:
        sys.stderr.write(f'{e}\n')
        sys.exit(e.code)
