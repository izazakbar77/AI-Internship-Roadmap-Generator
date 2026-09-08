from fastapi import APIRouter

from app.ai.skill_tree import SkillTree

from app.schemas.skill_tree import (
    SkillTreeRequest,
    SkillTreeResponse,
    SkillNode
)


router = APIRouter(
    prefix="/skill-tree",
    tags=["AI Skill Tree"]
)



@router.post("/", response_model=SkillTreeResponse)
def generate_tree(data: SkillTreeRequest):


    tree = SkillTree.generate(
        data.skills
    )


    nodes = []


    for item in tree:

        nodes.append(

            SkillNode(

                skill=item["skill"],

                level=item["level"],

                next_topics=item["next_topics"]

            )

        )



    return SkillTreeResponse(

        target_role=data.target_role,

        current_level=SkillTree.calculate_level(
            data.skills
        ),

        roadmap=nodes

    )