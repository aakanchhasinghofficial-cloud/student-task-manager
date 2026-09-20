const searchInput = document.getElementById("searchInput");
const priorityFilter = document.getElementById("priorityFilter");
const statusFilter = document.getElementById("statusFilter");
const taskCards = document.querySelectorAll(".task-card");

function filterTasks() {
    const searchText = searchInput.value.toLowerCase();
    const selectedPriority = priorityFilter.value;
    const selectedStatus = statusFilter.value;

    taskCards.forEach(function (taskCard) {
        const taskText = taskCard.textContent.toLowerCase();
        const priorityText = taskCard.querySelector(".task-content p:nth-of-type(2)").textContent;

        const matchesSearch = taskText.includes(searchText);

        const matchesPriority =
            selectedPriority === "All" ||
            priorityText.includes(selectedPriority);

        const isCompleted = taskCard.classList.contains("completed");

        const matchesStatus =
            selectedStatus === "All" ||
            (selectedStatus === "Completed" && isCompleted) ||
            (selectedStatus === "Pending" && !isCompleted);

        if (matchesSearch && matchesPriority && matchesStatus) {
            taskCard.style.display = "";
        } else {
            taskCard.style.display = "none";
        }
    });
}

searchInput.addEventListener("input", filterTasks);
priorityFilter.addEventListener("change", filterTasks);
statusFilter.addEventListener("change", filterTasks);