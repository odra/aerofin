from click.testing import CliRunner

from pybov import __version__ as pkg_version
from pybov import cli


def test_version():
    runner = CliRunner()
    result = runner.invoke(cli.version)

    assert result.exit_code == 0
    assert result.output == f'v{pkg_version}\n'


def test_version_cmd():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ['version'])

    assert result.exit_code == 0
    assert result.output == f'v{pkg_version}\n'
