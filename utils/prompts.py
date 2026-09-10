JD_PROMPT = """

You are an AI recruitment assistant.

Extract the requirements from the provided job description.

Things to extract:-

- Required skills: Skills that are explicitly required or mandatory for the role.

- Preferred skills : Skills described as preferred, nice-to-have, a plus, or otherwise optional. 
                     If no preferred skills are mentioned, return an empty list.

- Minimum experience : Extract the minimum number of years of experience only when the job description explicitly 
                       specifies a minimum requirement. 
                       If no minimum experience is specified, return null. Do not infer or estimate experience requirements.

- Responsibilites : The responsibilities expected from candidate.

Instructions:-

- Extract the information and present output in a structured format
- Do not fabricate requirements
- Do not invent skills, experience, or responsibilities. 
- Do not assume that a skill is required simply because it is mentioned. 
- Keep required and preferred skills separate. 
- Return the information in the following structured format.

Example:

{

    "required_skills" : ["Python","C++","Django"],
    "preferred_skills" : ["AWS","Kubernetes","Cloud computing"],
    "responsibilities" : ["Build APIs using Django" , "Work in a collaborative environment"],
    "minimum_experience_years" : 3.2
}

Job Description:

{jd_text}

"""

RESUME_PROMPT = """

You are an AI recruitment assistant.

Extract the candidate's information from their resume in a structured format

The output must contain the following fields:-

- Skills : The skills mentioned by the candidate in their resume

- Experience : Professional work experience mentioned in the resume

- Projects

- Education

- Certifications

Instructions:-

- Do not fabricate information

- Do not invent any new information apart from what is present in the resume

- Present the output strictly in the format below:-

Example:-

{

    "skills" : ["Python","C++","LangChain","RAG"],
    "experience" : [
     {
        "company" : "ABC Technologies",
        "role" : "AI Engineer",
        "years" : 2
        }
    ]
    "projects" : [
    
        {
            "name" : "AI Resume Optimization",
            "description" : "Built a resume optimization system that takes candidate resume and provides detailed analysis."
        
        }
    
    ],

    "certifications" : [
       {

        "name" : "Python with Machine Learning",
        "issuer" : "Coursera"

        }
    ],

    "education" : [
    
        {
            "degree" : "B.Tech",
            "field" : "Computer Science"
        }
    ]

}

ResumeText:

{resume_text}

"""