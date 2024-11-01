import click
from click.testing import CliRunner
from cli import cli

def test_create_project():
    runner = CliRunner()
    result = runner.invoke(cli, ['create_project', '--name', 'Test Project'])
    assert result.exit_code == 0
    assert 'Project "Test Project" created!' in result.output

def test_list_projects():
    runner = CliRunner()
    result = runner.invoke(cli, ['list_projects'])
    assert result.exit_code == 0
    assert 'Project ID' in result.output  # Adjust according to your output format
