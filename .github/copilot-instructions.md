## Instruções rápidas para agentes de codificação

Objetivo: dar contexto mínimo e ações iniciais para que um agente (Copilot / AI) seja produtivo ao trabalhar neste repositório.

- Estado atual do repositório: contém apenas `README.md` na raiz. Não há código fonte, arquivos de build, testes ou workflows detectados.

- Primeiro passos (sempre executar):
  1. Listar arquivos e diretórios na raiz para detectar novos artefatos (ex.: `src/`, `package.json`, `pyproject.toml`, `Dockerfile`, `.github/workflows/`).
  2. Procurar por padrões comuns: `package.json`, `requirements.txt`, `pyproject.toml`, `Makefile`, `pom.xml`, `build.gradle` e `Dockerfile`.
  3. Verificar se existe `.github/workflows/` para entender os comandos de CI.

- Como interpretar o "big picture" aqui:
  - No estado atual não há serviços nem separação de componentes. Se novos diretórios aparecerem, trate cada diretório de alto nível como um componente potencial (ex.: `backend/`, `frontend/`, `infra/`) e procure por seus manifestos de build.

- Padrões e convenções observáveis neste repositório:
  - Nenhum padrão específico detectado além do `README.md` na raiz. Portanto, antes de fazer mudanças invasivas, solicite confirmação humana se a intenção do repositório não estiver clara.

- Integrações e dependências externas:
  - Não há integrações detectáveis (APIs, serviços, CI, pacotes privados). Se arquivos de configuração forem adicionados, priorize leitura desses arquivos para descobrir endpoints/registries/scritps.

- Exemplo de tarefas seguras e acionáveis (prioridade alta):
  1. Criar um arquivo `CONTRIBUTING.md` ou `docs/README.md` propondo um layout de projeto quando novos artefatos forem adicionados.
  2. Se for adicionada uma linguagem (ex.: Node/Python/Java), procurar o gerenciador de pacotes e executar uma inspeção de dependências estática.

- Contrato rápido para o agente:
  - Entradas: conteúdo do repositório e histórico de commits (quando disponível).
  - Saídas: rascunho de PR ou patch contendo alterações pequenas e reversíveis (ex.: docs, testes mínimos, ajustes de CI).
  - Erros tratados: repositório vazio/minimal -> pedir orientação ao mantenedor antes de mudanças maiores.

- Notas sobre merge/atualização desta instrução:
  - Se houver um `.github/copilot-instructions.md` pré-existente, mescle conteúdo que descreva regras locais e preserve observações de segurança/CI.

Se quiser, eu posso expandir este arquivo com comandos e exemplos automáticos (inspeção de dependências, modelos de CI) assim que você adicionar artefatos de código ou me pedir para analisar diretórios específicos.
