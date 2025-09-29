# Gerenciador de Tarefas - Programação Funcional

Este projeto foi desenvolvido como parte da disciplina **Programação Funcional** (Curso de Análise e Desenvolvimento de Sistemas - UNIFOR).

## Objetivo
Implementar um sistema simples de gerenciamento de tarefas utilizando conceitos de Programação Funcional em Python.

## Funcionalidades
- Adicionar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Filtrar tarefas (concluídas/pendentes)
- Exportar tarefas em formato JSON

## Conceitos de Programação Funcional utilizados
- **Lambda**: usado na função `complete_task` para localizar a tarefa pelo ID.
- **List Comprehension**: usado em `list_tasks` para formatar a saída.
- **Closure**: a função `create_task_manager` encapsula a lista de tarefas.
- **Função de Alta Ordem**: `filter_tasks` recebe funções como parâmetro para filtrar as tarefas.

## Como executar

### Requisitos
- Python 3.8+

### Rodar a aplicação
```bash
python main.py
```

### Rodar testes automatizados
```bash
python -m unittest tasks_manager.py
```

## Estrutura de Arquivos
- `tasks_manager.py` → Implementação principal do gerenciador de tarefas.
- `main.py` → Interface simples em modo texto (CLI) para demonstração.
- `README.md` → Este arquivo de instruções.

## Casos de Teste
1. Adicionar uma tarefa e verificar listagem.
2. Marcar uma tarefa como concluída e verificar atualização.
3. Filtrar tarefas concluídas e pendentes.
4. Exportar dados em formato JSON.

---
Equipe: Bruna Yasmim, Cloberto de Sousa, Israel Sarhon, Luiz Gabriel, Lucas Bezerra, Paulo Bezerra.
