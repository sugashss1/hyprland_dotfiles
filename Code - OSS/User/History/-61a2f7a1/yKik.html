<!DOCTYPE html>
<html>
<head>
  <title>Kanban Board</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>

{% include "_navbar.html" %}

<div class="container">
  <h1>Kanban Board</h1>
  <p>Drag and drop tasks to update their status</p>

  <div class="kanban">
    <div class="column">
      <h3>TODO</h3>
      <div id="todo" class="task-column"></div>
    </div>

    <div class="column">
      <h3>IN PROGRESS</h3>
      <div id="in_progress" class="task-column"></div>
    </div>

    <div class="column">
      <h3>DONE</h3>
      <div id="done" class="task-column"></div>
    </div>
  </div>
</div>

<script>
async function loadTasks() {
  const res = await fetch("/api/tasks");
  const tasks = await res.json();
  render(tasks);
}

function render(tasks) {
  ["todo", "in_progress", "done"].forEach(id => {
    document.getElementById(id).innerHTML = "";
  });

  tasks.forEach(task => {
    const el = document.createElement("div");
    el.className = "task";
    el.draggable = true;
    el.ondragstart = e => e.dataTransfer.setData("id", task.id);

    el.innerHTML = `
      <strong>${task.title}</strong>
      <div class="meta">
        <small>${task.project_name || "-"}</small><br>
        <small>${task.assigned_to}</small>
      </div>
    `;

    document.getElementById(task.status.toLowerCase()).appendChild(el);
  });
}

async function updateStatus(id, status) {
  await fetch(`/api/tasks/${id}`, {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ status })
  });
}

document.querySelectorAll(".task-column").forEach(col => {
  col.ondragover = e => e.preventDefault();
  col.ondrop = async e => {
    const id = e.dataTransfer.getData("id");
    await updateStatus(id, col.id.toUpperCase());
    loadTasks();
  };
});

loadTasks();
</script>

</body>
</html>