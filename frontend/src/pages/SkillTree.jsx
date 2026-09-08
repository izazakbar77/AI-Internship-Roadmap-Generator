import React, {useState} from "react";
import api from "../api/axios";

import {
    Brain,
    ChevronRight,
    Network,
    Sparkles,
    Loader
} from "lucide-react";



function SkillTree(){


    const [skills,setSkills]=useState(
        "Python, FastAPI, Machine Learning"
    );


    const [tree,setTree]=useState([]);


    const [loading,setLoading]=useState(false);


    const [error,setError]=useState("");




    const generateTree=async()=>{


        try{


            setLoading(true);
            setError("");



            const response = await api.post(
                "/skill-tree/",
                {
                    skills:
                    skills
                    .split(",")
                    .map(skill=>skill.trim())
                }
            );



            console.log(response.data);



            setTree(

                response.data.roadmap ||
                response.data.skill_tree ||
                []

            );



        }

        catch(error){


            console.log(error);


            setError(
                "Unable to generate AI Skill Tree"
            );


        }

        finally{


            setLoading(false);


        }



    };






return (


<div className="min-h-screen bg-slate-100 p-8">





<h1 className="text-4xl font-bold mb-3">

AI Skill Tree Generator 🌳

</h1>


<p className="text-gray-500 mb-8">

AI Powered Dynamic Engineering Skill Roadmap

</p>







<div className="bg-white rounded-3xl shadow-lg p-8 mb-10">



<div className="flex items-center gap-3 mb-5">


<Sparkles className="text-purple-600"/>


<h2 className="text-2xl font-bold">

Enter Current Skills

</h2>


</div>





<input


value={skills}


onChange={(e)=>
setSkills(e.target.value)
}


className="
w-full
border
rounded-xl
p-4
outline-none
"


placeholder="Python, React, Machine Learning"



/>






<button


onClick={generateTree}


disabled={loading}


className="
mt-5
bg-blue-600
hover:bg-blue-700
text-white
px-8
py-3
rounded-xl
flex
items-center
gap-3
"



>


{

loading ?

<>

<Loader className="animate-spin"/>

Generating AI Tree...

</>

:

<>

<Brain/>

Generate Skill Tree

</>

}


</button>






{
error &&

<p className="text-red-600 mt-4">

{error}

</p>

}



</div>









<div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">





{

tree.length > 0 ?



tree.map((item,index)=>(


<div

key={index}

className="
bg-white
rounded-3xl
shadow-lg
p-7
hover:shadow-xl
transition
"



>


<div className="flex items-center gap-4 mb-6">



<div className="
bg-blue-100
text-blue-600
p-3
rounded-xl
">


<Brain/>

</div>




<h2 className="text-xl font-bold">

{item.skill}

</h2>



</div>








<div className="flex items-center gap-2 font-bold">


<Network size={20}/>


Next Learning Topics


</div>







<ul className="mt-5 space-y-3">



{

item.next_topics?.map(

(topic,i)=>(


<li

key={i}

className="
flex
items-center
gap-2
text-gray-700
"


>


<ChevronRight
size={18}
className="text-blue-600"
/>


{topic}



</li>


)


)

}



</ul>





</div>


))





:


<div className="
bg-white
rounded-3xl
shadow
p-10
text-center
col-span-full
">


<Brain
size={50}
className="mx-auto text-blue-600"
/>



<h2 className="text-xl font-bold mt-5">

No Skill Tree Generated

</h2>



<p className="text-gray-500 mt-2">

Enter skills and generate AI learning path.

</p>



</div>



}





</div>





</div>


)


}


export default SkillTree;