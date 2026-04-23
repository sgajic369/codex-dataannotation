from flask import Flask
from app.adapters.inbound.flask_routes import create_task_blueprint
from app.adapters.outbound.in_memory_task_repository import InMemoryTaskRepository
from app.application.use_cases.add_task import AddTask

def create_app() -> Flask:
    app = Flask(__name__)

    task_repository = InMemoryTaskRepository()
    add_task_use_case = AddTask(task_repository)

    app.register_blueprint(create_task_blueprint(add_task_use_case))
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
