
# tasks_manager.py - Gerenciador de Tarefas (Programação Funcional - Projeto)
from dataclasses import dataclass, asdict
import json
from typing import Callable, List

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False

def create_task_manager():
    tasks = []
    next_id = {'v': 1}
    def add_task(title: str, description: str = "") -> Task:
        t = Task(id=next_id['v'], title=title, description=description, completed=False)
        tasks.append(t)
        next_id['v'] += 1
        return t
    def list_tasks() -> List[str]:
        return [f"[{'X' if t.completed else ' '}] {t.id}: {t.title} - {t.description}" for t in tasks]
    def complete_task(task_id: int) -> bool:
        found = next(filter(lambda x: x.id == task_id, tasks), None)
        if found:
            found.completed = True
            return True
        return False
    def filter_tasks(predicate: Callable[[Task], bool]) -> List[Task]:
        return list(filter(predicate, tasks))
    def export_json() -> str:
        return json.dumps([asdict(t) for t in tasks], ensure_ascii=False, indent=2)
    return {
        'add_task': add_task,
        'list_tasks': list_tasks,
        'complete_task': complete_task,
        'filter_tasks': filter_tasks,
        'export_json': export_json
    }
