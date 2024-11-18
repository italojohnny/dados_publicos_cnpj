import pytest

from dados_publicos_cnpj.extract.util import check_url_availability


@pytest.mark.asyncio
async def test_check_url_availability():
    url = "https://google.com"
    result = await check_url_availability(url)
    assert result
