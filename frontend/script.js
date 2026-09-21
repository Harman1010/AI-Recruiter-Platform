const jobsButton = document.getElementById("job-button");

const createButton = document.getElementById("create-jobs-button");

const candidateButton = document.getElementById("candidate-button");

const jobSelect = document.getElementById("job-select");

const candidateName = document.getElementById("candidate-name");

const resumeFile = document.getElementById("resume-file");

const candidateSubmit = document.getElementById("candidate-submit");

const jobTitle = document.getElementById("job-title");

const jobDescription = document.getElementById("job-description");

const jobSubmit = document.getElementById("job-submit");

const candidateJob = document.getElementById("candidate-job");

const API_URL = "http://127.0.0.1:8000";

async function loadJobs() {

    if(!jobSelect) {
        return;
    }
    
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
                <button onclick="showMatchDetails(${candidate.match_id})">
                    View Details
                </button>
            </td>
        `;

        rankingTable.appendChild(row);
    });

}

if(jobSelect) {
    jobSelect.addEventListener("change", function () {

    const jobId = this.value;

    if (!jobId) {
        return;
    }

    loadRanking(jobId);

    });

}

loadJobs();

async function loadJobsPage() {

    const jobsContainer = document.getElementById("jobs-container");

    if (!jobsContainer) {
        return;
    }

    const response = await fetch(`${API_URL}/jobs`);

    const jobs = await response.json();

    jobsContainer.innerHTML = "";

    jobs.forEach(job => {

        const jobCard = document.createElement("div");

        jobCard.innerHTML = `
            <h3>${job.title}</h3>
            <p>${job.description}</p>
        `;

        jobsContainer.appendChild(jobCard);
    });
}

loadJobsPage();

if (jobsButton) {

    jobsButton.addEventListener("click", function () {

        window.location.href = "jobs.html";

    });

}

if (candidateSubmit) {

    candidateSubmit.addEventListener("click", async function () {

        const name = candidateName.value;

        const file = resumeFile.files[0];

        const jobId = candidateJob.value;


        if (!name) {
            alert("Please enter a name");
            return;
        }

        if (!file) {
            alert("Please upload a resume");
            return;
        }

        if (!jobId) {
            alert("Please select a job");
            return;
        }


        const formData = new FormData();

        formData.append("name", name);
        formData.append("resume", file);


        const response = await fetch(
            `${API_URL}/candidates`,
            {
                method: "POST",
                body: formData
            }
        );


        const result = await response.json();


        if (!response.ok) {
            alert(result.detail || "Failed to create candidate");
            return;
        }


        const candidateId = result.id;


        await createMatch(jobId, candidateId);


        candidateName.value = "";
        resumeFile.value = "";
        candidateJob.value = "";

    });

}

if (jobSubmit) {

    jobSubmit.addEventListener("click", async function () {

        const title = jobTitle.value;

        const description = jobDescription.value;

        if (!title) {
            alert("Please enter job title");
            return;
        }

        if (!description) {
            alert("Please enter job description");
            return;
        }

        const formData = new FormData();

        formData.append("title", title);
        formData.append("description", description);

        const response = await fetch(`${API_URL}/jobs`, {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (!response.ok) {
            alert(result.detail || "Failed to create job");
            return;
        }

        alert("Job created successfully");

        jobTitle.value = "";
        jobDescription.value = "";
    });
}

if (createButton) {

    createButton.addEventListener("click", function () {

        window.location.href = "create-job.html";

    });
}

if (candidateButton) {

    candidateButton.addEventListener("click", function () {

        window.location.href = "add-candidate.html";

    });
}

async function createMatch(jobId, candidateId) {

    const response = await fetch(
        `${API_URL}/matches/${jobId}/${candidateId}`,
        {
            method: "POST"
        }
    );

    const result = await response.json();

    if (!response.ok) {
        alert(result.detail || "Failed to create match");
        return;
    }

    alert("Candidate matched successfully");
}

async function loadCandidateJobs() {

    if (!candidateJob) {
        return;
    }

    const response = await fetch(`${API_URL}/jobs`);

    const jobs = await response.json();

    candidateJob.innerHTML = "";

    const defaultOption = document.createElement("option");

    defaultOption.value = "";

    defaultOption.textContent = "Select a job";

    candidateJob.appendChild(defaultOption);


    jobs.forEach(job => {

        const option = document.createElement("option");

        option.value = job.id;

        option.textContent = job.title;

        candidateJob.appendChild(option);
    });
}

loadCandidateJobs();

async function showMatchDetails(matchId) {

    const response = await fetch(
        `${API_URL}/matches/${matchId}`
    );

    const match = await response.json();

    if (!response.ok) {
        alert(match.detail || "Failed to load match details");
        return;
    }

    alert(
        `Match Details\n\n` +
        `Total Score: ${match.total_score.toFixed(2)} / 100\n\n` +
        `Required Skills: ${match.required_skill_score.toFixed(2)} / 25\n` +
        `Preferred Skills: ${match.preferred_skill_score.toFixed(2)} / 15\n` +
        `Projects: ${match.project_score.toFixed(2)} / 40\n` +
        `Experience: ${match.experience_score.toFixed(2)} / 15\n` +
        `Certifications: ${match.certification_score.toFixed(2)} / 5`
    );
}