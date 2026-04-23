from flask import Flask, request, jsonify

app = Flask(__name__)

class TaskHandler:
    def __init__(self, TaskName):
        self.TaskName = TaskName

    def ProcessLogin(self):
        
        return True

    def save_to_db(self):
        print(f"Saving task: {self.TaskName}...")
        return 1

@app.route('/add_task', methods=['POST'])
def handle_web_request():
    data = request.json
    task_title = data.get('name')
    
    handler = TaskHandler(task_title)
    
    if handler.ProcessLogin():
        result = handler.save_to_db()
        return jsonify({"status": "success", "code": result}), 200
    
    return jsonify({"error": "Failed"}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
