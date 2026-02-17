# Tasks

`client.tasks` -- Gestion de tareas en la plataforma Workiva.

Las tareas permiten organizar proyectos, asignar responsabilidades y controlar plazos.

## Operaciones

| Metodo | Descripcion | Paginado |
|--------|-------------|----------|
| `get_tasks` | Listar tareas | Si |
| `get_task_by_id` | Obtener tarea por ID | No |
| `create_task` | Crear tarea | No |
| `partially_update_task_by_id` | Actualizar tarea parcialmente | No |
| `delete_task_by_id` | Eliminar tarea | No |
| `submit_task_action` | Enviar accion sobre tarea | No |

## Ejemplos

### Listar tareas (auto-paginacion)

```python
result = client.tasks.get_tasks()

for task in result.data:
    print(f"{task.name} - {task.status}")
```

### Crear tarea

```python
task = client.tasks.create_task(
    body={
        "name": "Revisar reporte Q4",
        "description": "Verificar datos financieros",
    },
)
print(f"Tarea creada: {task.id}")
```

### Actualizar tarea

```python
client.tasks.partially_update_task_by_id(
    task_id="task-123",
    body={"status": "completed"},
)
```

### Eliminar tarea

```python
client.tasks.delete_task_by_id(task_id="task-123")
```

### Enviar accion

```python
client.tasks.submit_task_action(
    task_id="task-123",
    body={"action": "approve"},
)
```
