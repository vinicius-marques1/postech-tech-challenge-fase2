# Otimizador de Rotas Médicas

Estrutura inicial do Projeto 2 da Fase 2: otimização de rotas para distribuição
de medicamentos e insumos. O documento de referência está em `docs/`.

O projeto está sendo preparado para evoluir com otimização de rotas por
algoritmos genéticos, restrições operacionais, visualização em mapa e geração de
instruções e relatórios com LLM. Essas funcionalidades ainda não estão
implementadas.

## Ambiente de desenvolvimento

Instale o `uv` seguindo as instruções oficiais para seu sistema operacional:
<https://docs.astral.sh/uv/getting-started/installation/>.

Na raiz do repositório, sincronize o ambiente e as dependências registradas:

```bash
uv sync --locked
```

O `uv` cria o ambiente local em `.venv/`, que não deve ser compartilhado nem
versionado. Use `uv run` para executar comandos nele:

```bash
uv run python --version
uv run python -m unittest discover -s tests
```

Quando o `pyproject.toml` mudar, atualize e versione também o lockfile:

```bash
uv lock
```

## Estrutura

- `src/route_optimizer/`: pacote principal Python.
- `tests/`: testes automatizados.
- `docs/`: documentos de referência e documentação do projeto.
