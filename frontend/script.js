const jobsButton = document.getElementById("job-button");

const createButton = document.getElementById("create-jobs-button");

const candidateButton = document.getElementById("candidate-button");

const jobSelect = document.getElementById("job-select");

const API_URL = "http://127.0.0.1:8000";

async function loadJobs() {
    
    const response = await fetch(`${API_URL}/jobs`)

    const jobs = await response.json()
    
    jobSelect.innerHTML = "";

    const defaultOption = document.createElement("option");

    defaultOption.value = "";

    defaultOption.textContent = "Select a job";

    jobSelect.appendChild(defaultOption);

    jobs.forEach(job => {

    const option = document.createElement("option");

    option.value = job.id;

    option.textContent = job.title;

    jobSelect.appendChild(option);
});

}

async function loadRanking(jobId) {

    const response = await fetch(
        `${API_URL}/jobs/${jobId}/candidates`
    );

    const candidates = await response.json();

    const rankingTable = document.querySelector("table");

    rankingTable.innerHTML = `
        <tr>
            <th>Rank</th>
            <th>Candidate</th>
            <th>Score</th>
            <th>Details</th>
        </tr>
    `;

    candidates.forEach(candidate => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${candidate.rank}</td>
            <td>${candidate.candidate_name}</td>
            <td>${candidate.score.toFixed(2)} / 100</td>
            <td>
                <button>View Details</button>
            </td>
        `;

        rankingTable.appendChild(row);
    });

}

jobSelect.addEventListener("change", function () {

    const jobId = this.value;

    if (!jobId) {
        return;
    }

    console.log(loadRanking(jobId));

});

loadJobs();

