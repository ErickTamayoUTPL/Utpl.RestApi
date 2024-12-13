from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# App FastAPI
app = FastAPI(
    title="API de Registro Centralizado de Proyectos para UrbanRetail")

# Modelo de datos para un proyecto


class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    status: str  # Puede ser "Pendiente", "En progreso", "Finalizado"


# Base de datos simulada
projects_db = []

# Endpoint para crear un nuevo proyecto


@app.post("/projects", response_model=Project)
def create_project(project: Project):
    for existing_project in projects_db:
        if existing_project.id == project.id:
            raise HTTPException(
                status_code=400, detail="El proyecto con este ID ya existe.")
    projects_db.append(project)
    return project

# Endpoint para obtener todos los proyectos


@app.get("/projects", response_model=List[Project])
def get_projects():
    return projects_db

# Endpoint para obtener un proyecto por ID


@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: int):
    for project in projects_db:
        if project.id == project_id:
            return project
    raise HTTPException(status_code=404, detail="Proyecto no encontrado.")

# Endpoint para actualizar un proyecto por ID


@app.put("/projects/{project_id}", response_model=Project)
def update_project(project_id: int, updated_project: Project):
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            projects_db[index] = updated_project
            return updated_project
    raise HTTPException(status_code=404, detail="Proyecto no encontrado.")

# Endpoint para eliminar un proyecto por ID


@app.delete("/projects/{project_id}", response_model=Project)
def delete_project(project_id: int):
    for index, project in enumerate(projects_db):
        if project.id == project_id:
            deleted_project = projects_db.pop(index)
            return deleted_project
    raise HTTPException(status_code=404, detail="Proyecto no encontrado.")

# Ejecuta la app: usa "uvicorn <nombre_archivo>:app --reload" para correrla
