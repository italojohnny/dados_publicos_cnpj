import asyncio
import click

from dados_publicos_cnpj.extract.util import check_url_availability


URL = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/"


@click.group()
def cli_commands():
    pass


@click.command()
def verifica():
    click.echo(f"Verificando o site: {URL}")
    availability = asyncio.run(check_url_availability(URL))
    if availability:
        click.secho("O site está online!", fg='green')
        exit(0)
    else:
        click.secho("O site está offline ou inacessível.", fg='red')
        exit(1)


cli_commands.add_command(verifica)
cli_commands()
