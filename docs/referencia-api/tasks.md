# Tasks

`client.tasks` — Gestión de tareas en la plataforma Workiva.

Las tareas permiten organizar proyectos, asignar responsabilidades y controlar plazos.

## Operaciones

| Método | Descripción | Paginado |
|--------|-------------|----------|
| `get_tasks` | Listar tareas | Sí |
| `get_task_by_id` | Obtener tarea por ID | No |
| `create_task` | Crear tarea | No |
| `partially_update_task_by_id` | Actualizar tarea parcialmente | No |
| `delete_task_by_id` | Eliminar tarea | No |
| `submit_task_action` | Enviar acción sobre tarea | No |

## Ejemplos

### Listar tareas

```python
response = client.tasks.get_tasks()

for task in response.result.data:
    print(f"{task.name} - {task.status}")

# Paginar
while response.next is not None:
    response = response.next()
```

### Crear tarea

```python
response = client.tasks.create_task(
    task={
        "name": "Revisar reporte Q4",
        "description": "Verificar datos financieros",
    },
)
print(f"Tarea creada: {response.result.id}")
```

### Actualizar tarea

```python
client.tasks.partially_update_task_by_id(
    task_id="task-123",
    task={"status": "completed"},
)
```

### Eliminar tarea

```python
client.tasks.delete_task_by_id(task_id="task-123")
```

### Enviar acción

```python
client.tasks.submit_task_action(
    task_id="task-123",
    task_action={"action": "approve"},
)
```
