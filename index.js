document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('worker-form');
    const tableBody = document.getElementById('workers-body');
    let workers = JSON.parse(localStorage.getItem('workers')) || [];

    // Render workers
    function renderWorkers() {
        tableBody.innerHTML = '';
        workers.forEach((worker, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${worker.name}</td>
                <td>${worker.role}</td>
                <td>${worker.status}</td>
                <td><button class="delete-btn" data-index="${index}">Delete</button></td>
            `;
            tableBody.appendChild(row);
        });
    }

    // Add worker
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const role = document.getElementById('role').value;
        const status = document.getElementById('status').value;
        workers.push({ name, role, status });
        localStorage.setItem('workers', JSON.stringify(workers));
        renderWorkers();
        form.reset();
    });

    // Delete worker
    tableBody.addEventListener('click', (e) => {
        if (e.target.classList.contains('delete-btn')) {
            const index = e.target.dataset.index;
            workers.splice(index, 1);
            localStorage.setItem('workers', JSON.stringify(workers));
            renderWorkers();
        }
    });

    renderWorkers();
});