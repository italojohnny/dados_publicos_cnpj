import aiohttp
import asyncio
import click


URL = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/"


async def check_url_availability(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                return 200 <= response.status < 300

        except aiohttp.ClientError:
            return False


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
