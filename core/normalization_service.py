import re

class NormalizationService():

    """A blueprint for normalizing the string"""

    @staticmethod

    def normalize_skill(skill:str) -> str:

        skill = skill.lower().strip()

        skill = re.sub(r"[-_/]"," ",skill)

        skill = re.sub(r"[^a-z0-9+\s#.]","",skill)

        skill = re.sub(r"\s+"," ",skill)

        return skill

