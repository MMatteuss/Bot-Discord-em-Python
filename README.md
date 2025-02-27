# Projeto de Bots para Discord

Este repositório contém códigos de testes para bots do Discord utilizando a biblioteca `discord.py`. Nenhum dos códigos aqui está finalizado ou pronto para produção.

## Tecnologias Utilizadas
- Python
- discord.py
- PostgreSQL (para testes de banco de dados)

## Arquivos

### `meuBotTeste.py`
- Um bot simples que responde ao comando `regras` com algumas regras do servidor.
- Utiliza `discord.Client` para gerenciar eventos.

### `botVallTeste.py`
- Teste de comandos de barra (`/` commands) utilizando `discord.app_commands`.
- Integração com banco de dados PostgreSQL (ainda não funcional).
- Comandos testados:
  - `/teste` - Responde confirmando que o bot está funcionando.
  - `/dados` - Gera um número aleatório entre 1 e 5.
  - `/meunome` - Teste para buscar nome de um usuário no banco de dados.

### `BotVall.py`
- Similar ao `botVallTeste.py`, mas sem a integração com banco de dados.
- Comandos testados:
  - `/teste` - Responde confirmando que o bot está funcionando.
  - `/dados` - Gera um número aleatório entre 1 e 5.

## Como Rodar os Testes
1. Instale as dependências necessárias com:
   ```sh
   pip install discord psycopg2
   ```
2. Substitua `tk = "token"` pelo token real do bot.
3. Se for testar o `botVallTeste.py`, configure corretamente os dados do PostgreSQL.
4. Execute o script desejado com:
   ```sh
   python nome_do_arquivo.py
   ```

## Observações
- Os bots ainda estão em fase de teste.
- O código pode conter erros ou funcionalidades incompletas.
- O banco de dados PostgreSQL ainda não está corretamente implementado.

## Futuras Melhorias
- Corrigir a conexão com o banco de dados.
- Melhorar o tratamento de comandos.
- Implementar logging para depuração mais eficiente.
- Adicionar mais funcionalidades ao bot.

---

Este projeto é apenas para testes e aprendizado. Qualquer contribuição ou sugestão é bem-vinda!

