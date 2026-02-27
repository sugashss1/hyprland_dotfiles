// ---------- TASKS ----------
if (document.getElementById("taskForm")) {
  loadTasks();

  taskForm.onsubmit = async e => {
    e.preventDefault();

    await fetch("/api/tasks", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        title: title.value,
        assigned_to: assigned_to.value,
        start_date: start_date.value,
        due_date: due_date.value,
        task_type: task_type.value
      })
    });

    taskForm.reset();
    loadTasks();
  };
}

async function loadTasks() {
  const res = await fetch("/api/tasks");
  const tasks = await res.json();

  tasksList.innerHTML = "";
  tasks.forEach(t => {
    tasksList.innerHTML += `
      <li class="bg-white p-3 rounded shadow flex justify-between">
        <span>${t.title}</span>
        <button onclick="deleteTask('${t.id}')" class="text-red-500">✕</button>
      </li>`;
  });
}

async function deleteTask(id) {
  await fetch(`/api/tasks/${id}`, {method: "DELETE"});
  loadTasks();
}

// ---------- PROJECTS ----------
if (document.getElementById("projectForm")) {
  loadProjects();

  projectForm.onsubmit = async e => {
    e.preventDefault();

    await fetch("/api/projects", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        project_name: project_name.value,
        start_date: start_date.value,
        due_date: due_date.value
      })
    });

    projectForm.reset();
    loadProjects();
  };
}

async function loadProjects() {
  const res = await fetch("/api/projects");
  const projects = await res.json();

  projectsList.innerHTML = "";
  projects.forEach(p => {
    projectsList.innerHTML += `
      <li class="bg-white p-3 rounded shadow">${p.project_name}</li>`;
  });
}

// ---------- CHATBOT ----------
async function sendChat() {
  const msg = chatInput.value;
  chatInput.value = "";

  chatBox.innerHTML += `<div class="mb-2"><b>You:</b> ${msg}</div>`;

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  });

  const data = await res.json();
  chatBox.innerHTML += `<div class="mb-2"><b>Bot:</b> ${data.reply}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
