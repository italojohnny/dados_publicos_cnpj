
verifica:
	@poetry run python -m dados_publicos_cnpj verifica

unit_tests:
	@poetry run pytest
	@poetry run coverage html
