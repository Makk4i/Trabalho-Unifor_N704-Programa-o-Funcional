from tasks_manager import create_task_manager

def main():
    manager = create_task_manager()
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Filtrar tarefas concluídas")
        print("5. Filtrar tarefas pendentes")
        print("6. Exportar para JSON")
        print("0. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            title = input("Título: ")
            desc = input("Descrição: ")
            t = manager['add_task'](title, desc)
            print(f"Tarefa adicionada: {t.id} - {t.title}")
        elif choice == "2":
            for line in manager['list_tasks']():
                print(line)
        elif choice == "3":
            tid = int(input("ID da tarefa: "))
            ok = manager['complete_task'](tid)
            print("Tarefa concluída!" if ok else "Tarefa não encontrada.")
        elif choice == "4":
            done = manager['filter_tasks'](lambda t: t.completed)
            for t in done:
                print(f"[X] {t.id}: {t.title}")
        elif choice == "5":
            pending = manager['filter_tasks'](lambda t: not t.completed)
            for t in pending:
                print(f"[ ] {t.id}: {t.title}")
        elif choice == "6":
            print(manager['export_json']())
        elif choice == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
