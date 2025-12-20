from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory database
tasks = {}
task_id_counter = 0


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask CI/CD Demo!",
        "endpoints": {
            "health": "/health",
            "tasks": "/tasks"
        }
    })


@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    })


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({
        "tasks": list(tasks.values()),
        "count": len(tasks)
    })


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    task_id_counter += 1
    task = {
        "id": task_id_counter,
        "title": data['title'],
        "completed": data.get('completed', False),
        "created_at": datetime.utcnow().isoformat()
    }
    tasks[task_id_counter] = task
    return jsonify(task), 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(tasks[task_id])


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    deleted = tasks.pop(task_id)
    return jsonify({"message": "Task deleted", "task": deleted})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
